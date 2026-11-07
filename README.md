# Linux Containers Under the Hood

Linux container နည်းပညာ၏ အတွင်းပိုင်းလုပ်ဆောင်ပုံကို beginner မှ advanced အဆင့်အထိ မြန်မာဘာသာဖြင့် ရှင်းပြရန် ရည်ရွယ်ထားသော technical book project ဖြစ်သည်။

## Project status

- Repository foundation: Initial setup in progress.
- Book architecture: Approved — 6 Parts, 19 Chapters.
- Chapter Production (Phase 6): **Not started**.
- Lab Validation (Phase 7): **Not started**.
- Documentation site: Not published. GitHub Pages deployment is not configured or authorized by this setup.
- Host/VM feasibility and Fedora guest baseline: **Deferred** (DEC-009 and DEC-010).

ဤ repository တွင် chapter file များသည် navigation အတွက် scaffolding သာဖြစ်ပြီး chapter draft များ မဟုတ်ပါ။

## Book structure

| Part | Subject | Chapters |
|---|---|---:|
| I | Container Fundamentals | 1–2 |
| II | Linux Kernel and Isolation | 3–6 |
| III | Filesystem and Networking | 7–8 |
| IV | OCI and Container Runtime Internals | 9–13 |
| V | Security and Operations | 14–16 |
| VI | Ecosystem and Capstone | 17–19 |

## Documentation

MkDocs Material is the approved initial documentation platform. The canonical documentation URL is planned as:

<https://yul1ux.github.io/linux-containers-under-the-hood/>

The URL is a planned destination only; no Pages site has been published. The publishing workflow and Pages settings are withheld until separate Project Owner authorization.

## Local documentation workflow

Prerequisites: Python `3.14.10` and uv `0.13.7`, as pinned by `.python-version` and `pyproject.toml`.

```bash
uv sync --locked
uv run mkdocs serve
```

For a CI-equivalent build:

```bash
uv run --locked mkdocs build --strict
```

The committed `uv.lock` is the resolved dependency source of truth. Update dependencies only in a reviewed change that regenerates and validates the lock.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Technical corrections must include versioned evidence; Burmese editorial changes must preserve technical meaning; lab feedback must contain sanitized, reproducible evidence and must never expose private host or credential information.

## Licensing

- Book prose and original diagrams: [CC BY 4.0](LICENSE).
- Original code examples and lab scripts: [MIT](LICENSE-CODE).
- Third-party materials remain under their original licenses and attribution requirements.

See [the public decision log](project/decisions/decision-log.md) for approved project decisions and deferred boundaries.
