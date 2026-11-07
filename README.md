# Linux Containers Under the Hood

Linux container နည်းပညာ၏ အတွင်းပိုင်းလုပ်ဆောင်ပုံကို beginner မှ advanced အဆင့်အထိ မြန်မာဘာသာဖြင့် ရှင်းပြရန် ရည်ရွယ်ထားသော technical book project ဖြစ်သည်။

## Project status

- Repository: `yul1ux/linux-containers-under-the-hood` (Public).
- Default branch: `main`.
- Repository foundation: initial structure and documentation toolchain are committed.
- Book architecture: Approved — 6 Parts, 19 Chapters.
- Chapter Production (Phase 6): **Not started**.
- Lab Validation (Phase 7): **Not started**.
- Documentation site: Not published. Pages deployment workflow/settings are not configured by this setup; publishing requires separate Owner authorization.
- Host feasibility and Fedora guest/VM profile: **Deferred** (DEC-009 and DEC-010).

Chapter files currently contain navigation scaffolding only; they are not chapter drafts, verified technical content, or lab instructions.

## Book structure

| Part | Subject | Chapters |
|---|---|---:|
| I | Container Fundamentals | 1–2 |
| II | Linux Kernel and Isolation | 3–6 |
| III | Filesystem and Networking | 7–8 |
| IV | OCI and Container Runtime Internals | 9–13 |
| V | Security and Operations | 14–16 |
| VI | Ecosystem and Capstone | 17–19 |

## Documentation platform

MkDocs Material is the approved initial documentation platform (DEC-003). The platform decision record notes upstream maintenance is scheduled to end on **5 May 2027**; the project must reassess the platform before that date. Zensical work, pilot, and migration remain deferred under DEC-004.

The canonical documentation URL is planned as:

<https://yul1ux.github.io/linux-containers-under-the-hood/>

This is a planned destination only. No Pages site has been published, and deployment requires separate Owner authorization.

## Toolchain and local workflow

Pinned toolchain:

- Python: `3.14.10` (`.python-version`)
- uv: `0.13.7` (`tool.uv.required-version`)
- MkDocs Material: `9.8.0` (`pyproject.toml`)
- Fully resolved dependencies: `uv.lock`

From the repository root:

```bash
uv sync --locked
uv run --no-sync mkdocs serve
uv run --no-sync mkdocs build --strict
```

CI verifies the committed lock with `uv lock --check`, installs only the locked dependencies with `uv sync --locked`, runs a strict MkDocs build, and checks the approved 6-Part / 19-Chapter navigation and public-site boundary.

Dependency updates must change the direct dependency declaration as needed, regenerate `uv.lock` with the pinned uv version, and be reviewed together. CI intentionally fails if the committed lock is missing or out of date; it does not generate or upload a replacement lockfile.

## CI status

Latest verified default-branch run at the time of this update:

- Commit: [`bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4`](https://github.com/yul1ux/linux-containers-under-the-hood/commit/bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4) — `ci: enforce committed uv lock and pin artifact release`.
- Workflow: [Documentation main check — Run #11](https://github.com/yul1ux/linux-containers-under-the-hood/actions/runs/42388845338).
- Result: **Success** — lock verification, locked dependency sync, strict documentation build, structure/public-site-boundary check, and non-published build-artifact upload passed.

The PR workflow is configured but has not yet been verified with a real pull request. Repository-level branch protection, rulesets, default Actions permissions, and protected environment settings have not been independently confirmed. See `project/planning/version-matrix.md` for the detailed evidence/status snapshot.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Technical corrections require versioned evidence; Burmese editorial changes must preserve technical meaning; lab feedback must come from separately authorized work and contain sanitized evidence only.

## Licensing

- Book prose and original diagrams: [CC BY 4.0](LICENSE).
- Original code examples and lab scripts: [MIT](LICENSE-CODE).
- Third-party materials retain their original licenses and attribution requirements.

See [the public decision log](project/decisions/decision-log.md) for the current public-safe summary of approved decisions and deferred boundaries.
