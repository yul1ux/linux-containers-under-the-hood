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

Non-deploying workflows: docs-pr-check.yml and docs-main-check.yml. Pages deployment workflow intentionally omitted pending separate Owner authorization.

The connector does not expose branch-ruleset, protected-environment or Pages-settings mutation. Required checks, force-push restrictions, protected environments and Pages source are not claimed as configured.

CODE_OF_CONDUCT.md omitted because no specific recognized policy was selected. No host inventory, VM details, chapter drafts, lab outputs or private evidence are committed.
