# Linux Containers Under the Hood

Linux container နည်းပညာ၏ အတွင်းပိုင်းလုပ်ဆောင်ပုံကို beginner မှ advanced အဆင့်အထိ မြန်မာဘာသာဖြင့် ရှင်းပြရန် ရည်ရွယ်ထားသော technical book project ဖြစ်သည်။

## Project status

- Repository foundation: Initial setup in progress.
- Book architecture: Approved — 6 Parts, 19 Chapters.
- Chapter Production (Phase 6): **Not started**.
- Lab Validation (Phase 7): **Not started**.
- Documentation site: Not published. GitHub Pages deployment is not configured or authorized by this setup.
- Host/VM feasibility and Fedora guest baseline: **Deferred** (DEC-009 and DEC-010).

Chapter files currently contain navigation scaffolding only; they are not chapter drafts.

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

MkDocs Material is the approved initial platform. The canonical documentation URL is planned as:

https://yul1ux.github.io/linux-containers-under-the-hood/

This is a planned destination only; no Pages site has been published. Pages deployment requires separate Owner authorization.

## Local workflow

Prerequisites: Python 3.14.10 and uv 0.13.7.

After the initial CI lock-bootstrap artifact has been reviewed and committed as `uv.lock`:

```bash
uv sync --locked
uv run mkdocs serve
uv run --locked mkdocs build --strict
```

Dependency updates must regenerate and validate `uv.lock` in a reviewed change.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Technical corrections require versioned evidence; Burmese editorial changes must preserve technical meaning; lab feedback must be separately authorized and sanitized.

## Licensing

- Book prose and original diagrams: [CC BY 4.0](LICENSE).
- Original code examples and lab scripts: [MIT](LICENSE-CODE).
- Third-party materials retain their original licenses and attribution requirements.

See [the public decision log](project/decisions/decision-log.md) for approved decisions and deferred boundaries.
