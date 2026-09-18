# GRE revision mountains

A Gregmat-style revision *mountain* for my own GRE notes, built from
`data/GRE_Prep.xlsx`. Two boards:

| Page      | Source                | Content                                           |
| --------- | --------------------- | ------------------------------------------------- |
| **Vocab** | `New Words` sheet     | 733 words → 16 groups of 45–46                     |
| **Quant** | `content/quant/*.md`  | 188 concepts → 16 topic-coherent groups of 10–13   |

Both decks work the same way: the board shows a **prompt** — a word, or a question
like *"Compound interest formula?"* — you try to recall the answer, then press `D`
to check. Quant entries open with the formula or rule, then explain it and work an
example.

The **day slider (1–16)** is the mountain: day 1 shows group 1, day 5 shows
groups 1–5, day 16 shows everything. Each new day adds a column on the right and
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

- *Default order* — the spreadsheet order for vocab, the curated topic order for quant.
- *Shuffle within groups* — each column is scrambled, group membership unchanged.
- *Shuffle all* — the items of the groups revealed so far are dealt back across
  those same columns. On day 2 that is groups 1 and 2 mixed into columns 1 and 2;
  nothing from a later group ever appears early. The detail panel names the group
  each item actually came from.

Shuffles are stable (the same order every rerun) until you press `🔀 Reshuffle`.

**Filter** (under the board) narrows the climb to *not marked yet*, *green only*,
*red only* or *red + not marked* — the one that matters once day 14 has 640 words
on screen. The search box next to it filters by text.

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

### How merging works

Marks are flushed ~0.6s after you stop pressing keys (and at least every 4s while
you keep going). Each flush re-reads the remote document and applies only the
marks that changed, so the phone and the laptop merge instead of overwriting each
other. A fresh page load pulls the latest, and an open tab re-reads it at most
every two minutes; `⟳ Sync` forces it. If the network is down the app keeps the
changes queued, tells you, and retries.

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
(`Word`, `Definition`, `Synonyms`, `Example`). Rows keep their sheet order and are
split into 16 even groups. Repeated words are dropped with a warning.

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
  entry, so nothing can be silently dropped in a rewrite. Use `covers: new` for a
  concept that was not in the original, and `covers: 23 (split)` when one original
  concept is deliberately taught across two entries.
- The build prints a warning for any uncovered id, and `tests/test_mountain.py`
  fails on one.

The days run number sense → divisibility → primes and factors → GCF/LCM and
factorials → series → fractions and percents → exponents → algebra → coordinate
geometry → plane geometry → area and volume → statistics → counting → probability,
so each day continues where the previous one stopped.

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
scripts/build_data.py     workbook + markdown -> data/*.json
scripts/export_quant_xlsx.py  the quant notes as a spreadsheet
data/GRE_Prep.xlsx        the vocab source of truth
```
