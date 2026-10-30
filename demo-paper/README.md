# demo-paper · *Questions Before Priors* as a round-1 submission, its reports, and its resubmission

Source material for the Mark 1 demonstration, taken from Ryall's paper repository (`2026_TBV_Paper-1`) on
2026-10-24 and frozen here so that the working repository stays out of this project. Everything in this folder
is Ryall's own work or machine output on it; nothing is licensed from anyone else.

## What is here

| Folder | Contents | Taken from |
|---|---|---|
| `round-1/` | `tbv_mdr_Paper01-v02.tex`, its bibliography `tbv_mdr_Paper01-v01.bib`, and the compiled PDF | commit `18b3ebd`, 2026-07-23 |
| `reports/` | the two machine reviews of that draft, as PDFs and as text extracts (`.md`) | commit `18b3ebd`, 2026-07-23 |
| `round-2/` | `tbv_mdr_GPTedit-10.tex`, its bibliography `MDR_TBV_Paper01.bib`, and the compiled PDF | commit `0a18f80`, 2026-08-15 |
| `history/commits.md` | every commit from `18b3ebd` through `0a18f80`, oldest first, full message and file statistics | 29 commits |
| `history/patches/` | the same commits as patches, restricted to the paper's `.tex` and `.bib` files and the reviews, compiled PDFs excluded; `git am` replays them | 27 patches (the other commits touched none of these) |

## The round structure

- **Round 1** is `round-1/tbv_mdr_Paper01-v02.tex`. The second review names it as the file it read
  (`TRUTH VERSION: tbv_mdr_Paper01-v02.tex`); the first review's verdict and description match the same
  1,786-line file. Both verdicts are REVISE.
- **The reports** are the two machine reviews, filed as the round-1 reviewer reports. The editor signs revise
  and resubmit on them.
- **The working history** is `history/`. The response began in the same commit that filed the reviews (the v03
  repair pass) and runs through the single-clock overhaul, the audit fixes, the formal-core phases, and the
  GPTedit series with its B1–B8 audits. The round-2 AI-use declaration is written from `commits.md`; the commit
  messages name each pass.
- **Round 2** is `round-2/tbv_mdr_GPTedit-10.tex`, the resubmission. It is the draft Mark 1 already holds as
  the record `2-author/questions-before-priors/`, so that record becomes round 2 and a new record is made from
  round 1.

## What is not here, and why

- Nothing after 2026-08-15. The later work (the v10 sessions, the two-track format, FormalCore 12–14, the
  September integration) re-architects the paper past the reviews and is still in motion.
- `notes/`, `talks/`, `agenda/`, and the rest of the working repository. The patches carry only the paper and the
  reviews.
- The working repository itself. It is private and stays so; this folder is the only copy the project uses.

## The test this supports

Run the checks on round 1 and file its findings report. File the two reports as the round's reviewer reports
and sign revise and resubmit. Submit round 2, run the checks on it, and write the diff between rounds with each
changed file attributed to author or AI as the declaration states. The demonstration stops at round 2's intake;
"new", interest and issue are what this history cannot reach, and the tests take a copy of the record through them.
