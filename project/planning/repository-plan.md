# Repository plan — Initial setup

- Repository: yul1ux/linux-containers-under-the-hood (Public)
- Default branch: main
- Planned canonical Pages URL: https://yul1ux.github.io/linux-containers-under-the-hood/
- MkDocs source: docs/; generated output: site/
- Public-safe planning/decision summaries: project/
- Published assets: docs/assets/diagrams/
- Editable source assets: assets/diagrams/source/
- Python: .python-version; direct deps: pyproject.toml; full resolution: uv.lock
- Initial platform: MkDocs Material. No Zensical pilot.

Validation workflows: docs-pr-check.yml and docs-main-check.yml are non-deploying. The Pages workflow (`.github/workflows/pages-deploy.yml`) is manually triggered from `main` via `workflow_dispatch`; it does not deploy on PR merge or ordinary pushes. This Chapter 01 request authorizes one manual deployment after merge and successful checks.

The connector does not expose branch-ruleset, protected-environment or Pages-settings mutation. Required checks, force-push restrictions, protected environments and Pages source are not claimed as configured.

CODE_OF_CONDUCT.md omitted because no specific recognized policy was selected. Chapter 01's initial manuscript is stored at `docs/part-01-fundamentals/chapter-01-understanding-containers.md`. No host inventory, VM details, unvalidated lab outputs or private evidence are committed.
