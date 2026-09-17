/* The mountain board: renders the group columns, owns selection + marking,
   and reports marks and UI preferences back to Streamlit (debounced). */

const state = {
  payload: null,
  boardKey: null,
  marks: {},
  ui: { filter: "all", alwaysDef: false, autoAdvance: true },
  query: "",
  selectedId: null,
  revealed: false,
  nonce: 0,
  flushTimer: null,
  pendingSince: null,
  elements: new Map(),
};

const dom = {
  app: document.getElementById("app"),
  board: document.getElementById("board"),
  detail: document.getElementById("detail"),
  filter: document.getElementById("filter"),
  search: document.getElementById("search"),
  alwaysDef: document.getElementById("always-def"),
  autoAdvance: document.getElementById("auto-advance"),
  tally: document.getElementById("tally"),
  hint: document.getElementById("focus-hint"),
};

/* ----------------------------------------------------------------- helpers */

function allItems() {
  const out = [];
  (state.payload.columns || []).forEach((column, ci) =>
    column.items.forEach((item) => out.push({ item, ci }))
  );
  return out;
}

function matchesFilter(id) {
  const status = state.marks[id] || "";
  switch (state.ui.filter) {
    case "green":
      return status === "green";
    case "red":
      return status === "red";
    case "unmarked":
      return status === "";
    case "red_unmarked":
      return status !== "green";
    default:
      return true;
  }
}

function matchesQuery(item) {
  if (!state.query) return true;
  return item.label.toLowerCase().includes(state.query);
}

/** Items per column that survive the filter + search box. */
function visibleColumns() {
  return (state.payload.columns || []).map((column) =>
    column.items.filter((item) => matchesFilter(item.id) && matchesQuery(item))
  );
}

function findSelection(columns) {
  for (let ci = 0; ci < columns.length; ci += 1) {
    const ri = columns[ci].findIndex((item) => item.id === state.selectedId);
    if (ri >= 0) return { ci, ri };
  }
  return null;
}

function firstVisibleId(columns) {
  for (const column of columns) {
    if (column.length) return column[0].id;
  }
  return null;
}

/* ------------------------------------------------------------------ render */

function render() {
  const columns = visibleColumns();
  state.elements.clear();
  dom.board.replaceChildren();

  (state.payload.columns || []).forEach((column, ci) => {
    const items = columns[ci];
    const wrapper = document.createElement("div");
    wrapper.className = "column";

    const head = document.createElement("div");
    head.className = "col-head";
    const title = document.createElement("div");
    title.className = "col-title";
    title.textContent = column.title;
    title.title = column.title;
    head.appendChild(title);

    const total = column.items.length;
    let green = 0;
    let red = 0;
    column.items.forEach((item) => {
      const status = state.marks[item.id];
      if (status === "green") green += 1;
      else if (status === "red") red += 1;
    });

    const sub = document.createElement("div");
    sub.className = "col-sub";
    const counts = document.createElement("span");
    counts.textContent = `${green}/${total}`;
    const bar = document.createElement("span");
    bar.className = "col-bar";
    const gbar = document.createElement("i");
    gbar.className = "b-green";
    gbar.style.width = total ? `${(green / total) * 100}%` : "0";
    const rbar = document.createElement("i");
    rbar.className = "b-red";
    rbar.style.width = total ? `${(red / total) * 100}%` : "0";
    bar.append(gbar, rbar);
    sub.append(counts, bar);
    head.appendChild(sub);
    wrapper.appendChild(head);

    const list = document.createElement("div");
    list.className = "items";
    if (!items.length) {
      const empty = document.createElement("div");
      empty.className = "empty-col";
      empty.textContent = total ? "nothing matches the filter" : "empty";
      list.appendChild(empty);
    }
    items.forEach((item) => {
      const el = document.createElement("div");
      el.className = "item";
      el.dataset.id = item.id;
      el.setAttribute("role", "gridcell");
      const label = document.createElement("span");
      label.textContent = item.label;
      el.appendChild(label);
      el.title = item.label;
      el.addEventListener("click", () => {
        state.selectedId = item.id;
        state.revealed = state.ui.alwaysDef;
        paintSelection();
        renderDetail();
      });
      el.addEventListener("dblclick", () => {
        state.revealed = !state.revealed;
        renderDetail();
      });
      list.appendChild(el);
      state.elements.set(item.id, el);
    });
    wrapper.appendChild(list);
    dom.board.appendChild(wrapper);
  });

  if (!findSelection(columns)) {
    state.selectedId = firstVisibleId(columns);
    state.revealed = state.ui.alwaysDef;
  }
  paintSelection();
  renderDetail();
  renderTally();
  fitHeight();
}

function paintSelection(scroll = false) {
  state.elements.forEach((el, id) => {
    const status = state.marks[id] || "";
    el.className = `item${status ? ` ${status}` : ""}${id === state.selectedId ? " selected" : ""}`;
  });
  if (scroll && state.selectedId && state.elements.has(state.selectedId)) {
    state.elements.get(state.selectedId).scrollIntoView({ block: "nearest", inline: "nearest" });
  }
}

/** Inline `code`, **bold** and *italic*, built as DOM nodes (never innerHTML). */
function applyInline(element, text) {
  const pattern = /(`[^`]+`|\*\*[^*]+\*\*|\*[^*\n]+\*)/g;
  let last = 0;
  let match;
  while ((match = pattern.exec(text)) !== null) {
    if (match.index > last) {
      element.appendChild(document.createTextNode(text.slice(last, match.index)));
    }
    const token = match[0];
    let node;
    if (token.startsWith("`")) {
      node = document.createElement("code");
      node.textContent = token.slice(1, -1);
    } else if (token.startsWith("**")) {
      node = document.createElement("strong");
      node.textContent = token.slice(2, -2);
    } else {
      node = document.createElement("em");
      node.textContent = token.slice(1, -1);
    }
    element.appendChild(node);
    last = match.index + token.length;
  }
  element.appendChild(document.createTextNode(text.slice(last)));
}

/** Blank lines separate paragraphs; a run of "- " lines becomes a list. */
function renderRichText(container, text) {
  text
    .split(/\n\s*\n/)
    .map((chunk) => chunk.trim())
    .filter(Boolean)
    .forEach((chunk) => {
      const lines = chunk.split("\n").map((line) => line.trim());
      if (lines.every((line) => line.startsWith("- "))) {
        const list = document.createElement("ul");
        lines.forEach((line) => {
          const item = document.createElement("li");
          applyInline(item, line.slice(2));
          list.appendChild(item);
        });
        container.appendChild(list);
      } else {
        const paragraph = document.createElement("p");
        applyInline(paragraph, lines.join(" "));
        container.appendChild(paragraph);
      }
    });
}

function renderDetail() {
  const details = state.payload.details || {};
  const id = state.selectedId;
  dom.detail.replaceChildren();
  if (!id || !details[id]) {
    const card = document.createElement("div");
    card.className = "detail-hidden";
    card.textContent = "Nothing selected.";
    dom.detail.appendChild(card);
    return;
  }
  const detail = details[id];
  const card = document.createElement("div");
  card.className = "detail-card";

  if (detail.group) {
    const kicker = document.createElement("div");
    kicker.className = "detail-kicker";
    kicker.textContent = detail.group;
    card.appendChild(kicker);
  }
  const title = document.createElement("div");
  title.className = "detail-title";
  title.textContent = detail.title;
  card.appendChild(title);

  const status = state.marks[id] || "none";
  const badge = document.createElement("div");
  badge.className = `detail-status ${status}`;
  badge.textContent =
    status === "green" ? "I knew this" : status === "red" ? "I forgot this" : "not marked yet";
  card.appendChild(badge);

  if (!state.revealed && !state.ui.alwaysDef) {
    const hidden = document.createElement("div");
    hidden.className = "detail-hidden";
    hidden.innerHTML = "Press <b>D</b> to reveal";
    card.appendChild(hidden);
  } else if (!(detail.blocks || []).length) {
    const hidden = document.createElement("div");
    hidden.className = "detail-hidden";
    hidden.textContent = "No explanation in the spreadsheet for this one.";
    card.appendChild(hidden);
  } else {
    detail.blocks.forEach((block) => {
      const wrap = document.createElement("div");
      wrap.className = "block";
      const label = document.createElement("div");
      label.className = "block-label";
      label.textContent = block.label;
      const text = document.createElement("div");
      text.className = "block-text";
      renderRichText(text, block.text);
      wrap.append(label, text);
      card.appendChild(wrap);
    });
  }
  dom.detail.appendChild(card);
  fitHeight();
}

function renderTally() {
  const items = allItems();
  let green = 0;
  let red = 0;
  items.forEach(({ item }) => {
    const status = state.marks[item.id];
    if (status === "green") green += 1;
    else if (status === "red") red += 1;
  });
  const left = items.length - green - red;
  dom.tally.innerHTML = `<b class="g">${green}</b> known &middot; <b class="r">${red}</b> forgot &middot; ${left} left of ${items.length}`;
}

/** Shrink the iframe to the content on short days, scroll inside it on long ones. */
function fitHeight() {
  const desired = (state.payload && state.payload.height) || 760;
  const controls = document.querySelector(".controls");
  const chrome = (controls ? controls.offsetHeight : 90) + 26;
  // Measure the natural height of the tallest column: a scroll container's
  // scrollHeight can never drop below its own clientHeight, so it cannot shrink us.
  let tallest = 0;
  dom.board.querySelectorAll(".column").forEach((column) => {
    tallest = Math.max(tallest, column.offsetHeight);
  });
  const card = dom.detail.firstElementChild;
  const content = Math.max(tallest + 16, card ? card.offsetHeight + 16 : 0) + chrome;
  Streamlit.setFrameHeight(Math.max(340, Math.min(desired, content)));
}

/* -------------------------------------------------------------- interaction */

function move(dCol, dRow) {
  const columns = visibleColumns();
  let position = findSelection(columns);
  if (!position) {
    state.selectedId = firstVisibleId(columns);
    state.revealed = state.ui.alwaysDef;
    paintSelection(true);
    renderDetail();
    return;
  }
  let { ci, ri } = position;
  if (dRow) {
    ri += dRow;
    while (ci >= 0 && ci < columns.length && (ri < 0 || ri >= columns[ci].length)) {
      // Walk into the neighbouring column so up/down never dead-ends.
      ci += dRow > 0 ? 1 : -1;
      if (ci < 0 || ci >= columns.length) break;
      ri = dRow > 0 ? 0 : columns[ci].length - 1;
    }
  }
  if (dCol) {
    let next = ci + dCol;
    while (next >= 0 && next < columns.length && !columns[next].length) next += dCol;
    if (next >= 0 && next < columns.length) {
      ci = next;
      ri = Math.min(ri, columns[ci].length - 1);
    }
  }
  if (ci < 0 || ci >= columns.length) return;
  const target = columns[ci][Math.max(0, Math.min(ri, columns[ci].length - 1))];
  if (!target) return;
  state.selectedId = target.id;
  state.revealed = state.ui.alwaysDef;
  paintSelection(true);
  renderDetail();
}

function advance() {
  const columns = visibleColumns();
  const position = findSelection(columns);
  if (!position) return;
  move(0, 1);
  const after = findSelection(visibleColumns());
  if (after && after.ci === position.ci && after.ri === position.ri) {
    // Last item of the last column: stay put.
    paintSelection(true);
  }
}

function mark(status) {
  const id = state.selectedId;
  if (!id) return;
  const hideIfFiltered = state.ui.filter !== "all";
  if (status === null) delete state.marks[id];
  else state.marks[id] = status;

  if (hideIfFiltered && !matchesFilter(id)) {
    // The item just fell out of the active filter: rebuild so the board matches.
    const columns = visibleColumns();
    const next = findSelection(columns);
    if (!next) state.selectedId = null;
    render();
  } else {
    paintSelection();
    renderDetail();
    renderTally();
    if (status !== null && state.ui.autoAdvance) advance();
    else if (status === null) paintSelection(true);
    updateColumnHeads();
  }
  scheduleFlush();
}

function updateColumnHeads() {
  const wrappers = dom.board.querySelectorAll(".column");
  (state.payload.columns || []).forEach((column, ci) => {
    const wrapper = wrappers[ci];
    if (!wrapper) return;
    const total = column.items.length;
    let green = 0;
    let red = 0;
    column.items.forEach((item) => {
      const status = state.marks[item.id];
      if (status === "green") green += 1;
      else if (status === "red") red += 1;
    });
    const counts = wrapper.querySelector(".col-sub span");
    if (counts) counts.textContent = `${green}/${total}`;
    const gbar = wrapper.querySelector(".b-green");
    const rbar = wrapper.querySelector(".b-red");
    if (gbar) gbar.style.width = total ? `${(green / total) * 100}%` : "0";
    if (rbar) rbar.style.width = total ? `${(red / total) * 100}%` : "0";
  });
}

function scheduleFlush() {
  // Save ~0.6s after you stop marking, but never let an unbroken streak of
  // keypresses hold changes back for more than 4s.
  if (!state.pendingSince) state.pendingSince = Date.now();
  if (state.flushTimer) clearTimeout(state.flushTimer);
  const wait = Math.max(0, Math.min(600, 4000 - (Date.now() - state.pendingSince)));
  state.flushTimer = setTimeout(flush, wait);
}

function flush() {
  if (state.flushTimer) clearTimeout(state.flushTimer);
  state.flushTimer = null;
  state.pendingSince = null;
  state.nonce += 1;
  Streamlit.setComponentValue({
    nonce: state.nonce,
    board_key: state.boardKey,
    marks: state.marks,
    ui: state.ui,
  });
}

/* ------------------------------------------------------------------ events */

function onKeyDown(event) {
  const target = event.target;
  if (target && (target.tagName === "INPUT" || target.tagName === "SELECT")) {
    if (event.key === "Escape") {
      target.blur();
      dom.app.focus();
    }
    return;
  }
  const key = event.key.toLowerCase();
  const map = {
    arrowup: () => move(0, -1),
    arrowdown: () => move(0, 1),
    arrowleft: () => move(-1, 0),
    arrowright: () => move(1, 0),
    k: () => move(0, -1),
    j: () => move(0, 1),
    h: () => move(-1, 0),
    l: () => move(1, 0),
    d: () => {
      state.revealed = !state.revealed;
      renderDetail();
    },
    " ": () => {
      state.revealed = !state.revealed;
      renderDetail();
    },
    g: () => mark("green"),
    r: () => mark("red"),
    w: () => mark(null),
  };
  const handler = map[key];
  if (!handler) return;
  event.preventDefault();
  handler();
}

function wireControls() {
  dom.filter.addEventListener("change", () => {
    state.ui.filter = dom.filter.value;
    render();
    scheduleFlush();
  });
  dom.search.addEventListener("input", () => {
    state.query = dom.search.value.trim().toLowerCase();
    render();
  });
  dom.alwaysDef.addEventListener("change", () => {
    state.ui.alwaysDef = dom.alwaysDef.checked;
    state.revealed = state.ui.alwaysDef;
    renderDetail();
    scheduleFlush();
  });
  dom.autoAdvance.addEventListener("change", () => {
    state.ui.autoAdvance = dom.autoAdvance.checked;
    scheduleFlush();
  });

  // The on-screen key legend doubles as buttons (phones have no keyboard).
  const actions = {
    "←": () => move(-1, 0),
    "↑": () => move(0, -1),
    "↓": () => move(0, 1),
    "→": () => move(1, 0),
    D: () => {
      state.revealed = !state.revealed;
      renderDetail();
    },
    G: () => mark("green"),
    R: () => mark("red"),
    W: () => mark(null),
  };
  document.querySelectorAll(".key").forEach((key) => {
    const action = actions[key.textContent.trim()];
    if (action) key.addEventListener("click", action);
  });

  document.addEventListener("keydown", onKeyDown);
  window.addEventListener("resize", () => {
    if (state.payload) fitHeight();
  });
  window.addEventListener("pagehide", () => {
    if (state.flushTimer) flush();
  });
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden" && state.flushTimer) flush();
  });
  ["mousedown", "touchstart", "focus"].forEach((type) =>
    document.addEventListener(type, () => dom.hint.classList.add("hidden"), { passive: true })
  );
}

/* ------------------------------------------------------------------ render */

function applyTheme(theme) {
  if (!theme) return;
  const root = document.documentElement.style;
  const dark = (theme.base || "light") === "dark";
  root.setProperty("--bg", theme.backgroundColor || (dark ? "#0e1117" : "#ffffff"));
  root.setProperty("--fg", theme.textColor || (dark ? "#e6e9ef" : "#26324a"));
  root.setProperty("--accent", theme.primaryColor || "#1f6feb");
  if (theme.font) root.setProperty("--font", theme.font);
  if (dark) {
    root.setProperty("--muted", "#9aa6bd");
    root.setProperty("--line", "#2b3245");
    root.setProperty("--card", "#161b26");
    root.setProperty("--item", "#12161f");
    root.setProperty("--item-hover", "#1b2231");
    root.setProperty("--code-bg", "#1e2534");
    root.setProperty("--mint", "#1d3b2c");
    root.setProperty("--mint-line", "#255139");
    root.setProperty("--green-bg", "#2c8f57");
    root.setProperty("--red-bg", "#b8393e");
  }
}

function onRender(event) {
  const detail = event.data;
  const args = detail.args || {};
  const payload = args.payload || { columns: [], details: {}, marks: {}, ui: {} };
  applyTheme(detail.theme);

  if (payload.board_key === state.boardKey) {
    // Same board (Streamlit just re-ran after saving): keep local state as-is.
    state.payload.height = payload.height;
    fitHeight();
    return;
  }

  state.payload = payload;
  state.boardKey = payload.board_key;
  state.marks = Object.assign({}, payload.marks || {});
  state.ui = Object.assign({ filter: "all", alwaysDef: false, autoAdvance: true }, payload.ui || {});
  state.selectedId = null;
  state.revealed = state.ui.alwaysDef;

  dom.filter.value = state.ui.filter;
  dom.alwaysDef.checked = !!state.ui.alwaysDef;
  dom.autoAdvance.checked = !!state.ui.autoAdvance;
  document.documentElement.style.setProperty("--col-w", `${payload.column_width || 260}px`);

  render();
  dom.app.focus({ preventScroll: true });
}

wireControls();
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
Streamlit.setFrameHeight(760);
