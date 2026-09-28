# GRE revision mountains

A Gregmat-style revision *mountain* for my own GRE notes, built from
`data/GRE_Prep.xlsx`. Two boards:

| Page      | Source                | Content                                          |
| --------- | --------------------- | ------------------------------------------------ |
| **Vocab** | `New Words` sheet     | 454 words → 6 shuffled groups of 75–76            |
| **Quant** | `content/quant/*.md`  | 148 concepts → 6 topic-coherent groups of 16–31   |

Both decks work the same way: the board shows a **prompt** — a word, or a question
like *"Compound interest formula?"* — you try to recall the answer, then press `D`
to check. Quant entries open with the formula or rule, then explain it and work an
example.

The **day slider (1–6)** is the mountain: day 1 shows group 1, day 4 shows
groups 1–4, day 6 shows everything. Each new day adds a column on the right and
you re-climb every column to its left.

## Running it

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Progress is saved automatically. Out of the box it goes to `.gre_progress/` on
the machine you are running on — see [Syncing between devices](#syncing-between-devices)
to have your phone and your laptop share one climb.

## Using the board

| Key         | Action                                                      |
| ----------- | ----------------------------------------------------------- |
| `←` `↑` `↓` `→` | Move between items (`h` `j` `k` `l` work too). Up/down walks into the next column at the end of one. |
| `D` / `Space` | Reveal the answer — definition (vocab), or formula + explanation + example (quant) |
| `G`         | I knew this → green                                          |
| `R`         | I forgot this → red                                          |
| `W`         | Clear the mark (back to white)                               |

Click the board once after the page loads so the keyboard reaches it — the blue
chip under the board says so until you do. On a phone, tap an item and then tap
the on-screen `D` / `G` / `R` / `W` keys.

**Marks belong to a day.** `G` on day 5 records *"I knew this on day 5"*; move the
slider to day 6 and everything starts unmarked again, so each climb is scored on
its own. `↺ Reset` clears the current day only; the sidebar can reset a whole deck.

**Order** (dropdown above the board):

- *Default order* — a fixed shuffle for vocab (so synonyms are not adjacent), the
  curated topic order for quant.
- *Shuffle within groups* — each column is scrambled, group membership unchanged.
- *Shuffle all* — the items of the groups revealed so far are dealt back across
  those same columns. On day 2 that is groups 1 and 2 mixed into columns 1 and 2;
  nothing from a later group ever appears early. The detail panel names the group
  each item actually came from.

Shuffles are stable (the same order every rerun) until you press `🔀 Reshuffle`.

**Filter** (under the board) narrows the climb:

- *Adaptive* hides anything you have marked green **three days running** — once a
  word has been known on three consecutive days it is retired and stops competing
  for your attention. It disappears the moment the third green lands, and the tally
  counts how many are retired. Switch back to *Show all* to see them again.
- *Not marked yet*, *green only*, *red only*, *red + not marked* do what they say.

The search box next to it filters by text.

## Syncing between devices

The app writes one small JSON document per profile through a pluggable backend,
chosen in `.streamlit/secrets.toml` (copy `.streamlit/secrets.toml.example`):

### GitHub Gist (recommended — one token, nothing to host)

1. Create a token with the **gist** scope at <https://github.com/settings/tokens>.
2. Put it in secrets:

   ```toml
   [storage]
   backend = "gist"
   profile = "default"

   [storage.gist]
   token = "ghp_..."
   ```

The app looks for a secret gist containing `gre-mountain-<profile>.json`, creates
one the first time you mark something, and reuses it everywhere after that.

### Supabase (if you would rather have a database)

```sql
create table gre_progress (
  id text primary key,
  document jsonb not null,
  updated_at timestamptz default now()
);
alter table gre_progress enable row level security;
create policy "anon can read/write" on gre_progress
  for all using (true) with check (true);
```

```toml
[storage]
backend = "supabase"

[storage.supabase]
url = "https://xxxx.supabase.co"
key = "eyJhbGciOi..."
table = "gre_progress"
```

That policy lets anyone with the anon key read and write the table, which is fine
for a private study app on a URL nobody else has — tighten it if that is not true
for you.

### When it writes, and how it merges

**Marking never touches the network.** Changes are queued in the session and
pushed when you press **💾 Save**, when the autosave timer expires (2 minutes by
default; set it to 0 in the sidebar for save-only), or when you move to another
day. Writing on every keypress is what tripped GitHub's *secondary* rate limit,
which throttles bursts of writes to the same endpoint regardless of how much of
your hourly quota is left.

Each push re-reads the stored document and replays only the queued changes onto
it, so the phone and the laptop merge instead of overwriting each other. A fresh
page load pulls the latest; ⟳ Pull forces it, and is disabled while you have
unsaved work so it cannot clobber it. If the push fails, the changes stay queued
and the app says so — press Save again.

The one thing to know: unsaved marks live in the browser session, so pressing Save
before you close the tab is what makes them permanent.

## Deploying to Streamlit Community Cloud

1. Push this repo to GitHub.
2. <https://share.streamlit.io> → **Create app** → pick the repo/branch, main file
   `streamlit_app.py`.
3. **Advanced settings → Secrets**: paste the `[storage]` block from above (without
   it, progress resets whenever the app reboots).
4. Deploy, then open the URL on your phone and add it to the home screen.

The app is a plain Streamlit app plus one dependency-free JS component, so any
host that runs `streamlit run streamlit_app.py` (Anaconda Cloud, a small VM,
Hugging Face Spaces) works the same way.

## Changing the notes

`data/*.json` is generated. Edit the sources, then rebuild:

```bash
python scripts/build_data.py          # rebuild both decks, print the group sizes
python scripts/build_data.py --check  # non-zero exit if anything looks off
```

### Vocab

Comes from the `New Words` sheet of `data/GRE_Prep.xlsx`: one row is one word
(`Word`, `Definition`, `Synonyms`, `Example`). Words listed in
`content/vocab/memorized.txt` are dropped — that file is a plain list, one word per
line, and near-misses are matched and reported so a typo does not silently keep a
word on the board. What is left is shuffled with a fixed seed and split into 6 even
groups. The shuffle matters: the sheet keeps synonyms next to each other, which
makes them far too easy to guess in order. The seed is fixed so a word never
wanders into another group and loses its progress.

### Quant

The quant notes were rewritten from the original `Quant Notes` sheet into
`content/quant/`, one markdown file per day, because long explanations and worked
examples do not fit comfortably in a spreadsheet cell. Each entry is a flashcard:
the `##` heading is the prompt you see on the board, and the first block is the
answer you were trying to recall.

```markdown
## How many factors does a number have?
covers: 25

### Answer
Prime factorize, **add 1 to every exponent, and multiply**. For
`60 = 2^2 x 3^1 x 5^1` that is `3 x 2 x 2 = 12`.

### Explanation
Building a factor means choosing how many copies of each prime to take...

### Example
60's twelve factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.

### Watch out
The count includes 1 and the number itself.
```

- The `# heading` on line 1 is the day's name; the file's numeric prefix is its day.
- `## ` starts a concept — write it as a question that does **not** give the answer
  away. `### ` starts a labelled block; the first one must be `Answer` (or
  `In short` for the few entries that are not worth quizzing). `**bold**`,
  `*italic*`, `` `code` `` and `- ` bullet lists all render in the app.
- `covers:` lists audit ids from `content/quant/_source_concepts.json`, the frozen
  list of the 162 concepts in the original sheet. Every id must be claimed by some
  entry — or be listed in `content/quant/_retired_concepts.json`, which records the
  26 concepts deliberately dropped as already memorized. Nothing can be lost by
  accident. Use `covers: new` for a concept that was not in the original, and
  `covers: 23 (split)` when one original concept is deliberately taught across two
  entries.
- The build prints a warning for any uncovered id, and `tests/test_mountain.py`
  fails on one.

The six days run number properties and factors → ranges, series, percents and
rates → exponents, algebra and functions → coordinate geometry and angles →
triangles, area and solids → statistics, counting and probability.

To read the same notes in a spreadsheet, `python scripts/export_quant_xlsx.py`
writes `data/GRE_Quant_Notes_rewritten.xlsx` (one row per concept). That export is
one-way — the markdown stays the source of truth.

## Tests

```bash
python -m pytest tests -q
```

They cover the deck build (all 162 original concepts still covered, every entry a
prompt with an answer and an example), the three shuffle modes, and the day-scoped
merge logic behind cross-device sync.

## Layout

```
streamlit_app.py          entry point + page navigation
views/                    home, vocab and quant pages
gre_mountain/
  decks.py                loading decks, building a day's board, shuffles
  progress.py             session state, deltas, merge-on-write
  storage.py              local / gist / supabase backends
  ui.py                   page chrome shared by both mountains
  component/static/       the board itself (vanilla JS, no build step)
content/quant/            the rewritten quant notes, one file per day
content/vocab/memorized.txt  words to leave off the vocab board
scripts/build_data.py     workbook + markdown -> data/*.json
scripts/export_quant_xlsx.py  the quant notes as a spreadsheet
data/GRE_Prep.xlsx        the vocab source of truth
```
