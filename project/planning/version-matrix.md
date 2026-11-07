# Toolchain and workflow version matrix

**Evidence snapshot:** 7 November 2026
**Repository:** `yul1ux/linux-containers-under-the-hood`
**Branch:** `main`
**Latest reviewed commit:** `bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4`

This matrix records selected versions and observed CI evidence. A version pin is not, by itself, proof of compatibility; runtime verification is recorded separately.

## Documentation toolchain

| Component | Selected version / source | Evidence and status |
|---|---|---|
| Python | `3.14.10`; `.python-version` | Pinned; installed successfully in Documentation main check Run #11. |
| uv | `0.13.7`; `tool.uv.required-version` | Pinned; setup succeeded in Run #11. |
| MkDocs Material | `9.8.0`; `pyproject.toml` | Direct dependency pinned; locked install and `mkdocs build --strict` passed in Run #11. |
| Full dependency resolution | `uv.lock` | Committed; `uv lock --check` and `uv sync --locked` passed in Run #11. |
| GitHub-hosted runner | `ubuntu-24.04` | Declared by both current validation workflows; actual main workflow job passed. Runner image contents remain GitHub-managed. |

## GitHub Actions pins

All external actions in the two current workflows are pinned to full 40-character commit SHAs.

| Action | Release | Pinned commit SHA | Verification |
|---|---|---|---|
| `actions/checkout` | `v7.0.1` | `3d3c42e5aac5ba805825da76410c181273ba90b1` | Full SHA; verified to match the `v7.0.1` release tag. |
| `astral-sh/setup-uv` | `v10.3.2` | `07a047e608db84b3d8c06cd9a7c7dcc9c355c18e` | Full SHA; verified to match the `v10.3.2` release tag. |
| `actions/upload-artifact` | `v7.0.2` | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` | Full SHA; exact `v7.0.2` release commit. Used by `docs-main-check.yml`. |

## Workflow verification evidence

| Workflow | Current role | Evidence status |
|---|---|---|
| `.github/workflows/docs-pr-check.yml` | Untrusted PR validation using `pull_request`, read-only `contents`, no secrets, no persistent checkout credentials, and locked dependencies | Static source review passed. Real PR runtime smoke test remains pending. |
| `.github/workflows/docs-main-check.yml` | Non-deploying default-branch validation and short-lived build artifact upload | Run #11 passed on commit `bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4`. |
| `.github/workflows/pages-deploy.yml` | Separate protected Pages deployment workflow from DEC-007 design | Not present; intentionally not implemented because deployment/Pages publishing has not been authorized. |

### Latest main CI evidence

- Commit: [`bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4`](https://github.com/yul1ux/linux-containers-under-the-hood/commit/bb9f7b40ceace4ad3bb8cc004ad147a993bb80c4)
- Run: [Documentation main check — #11](https://github.com/yul1ux/linux-containers-under-the-hood/actions/runs/42388845338)
- Conclusion: **success**
- Successful steps: pinned uv setup; Python installation; `uv lock --check`; `uv sync --locked`; `mkdocs build --strict`; `scripts/check_docs_structure.py`; upload of `docs-main-build`.
- The initial `uv-lock-bootstrap` artifact step no longer exists. A missing or stale lockfile now fails the workflow rather than being regenerated in CI.

## Platform lifecycle

| Item | Current decision / status |
|---|---|
| MkDocs Material | DEC-003: approved as the initial platform. The repository currently pins Material `9.8.0`. |
| Material maintenance horizon | The public platform decision note records 5 May 2027 as the announced end of upstream maintenance. Re-check the upstream notice before that date and before any platform change. |
| Zensical | DEC-004: Deferred. No pilot, migration, or production switch is authorized. |

## Evidence gaps and limits

- The main-branch build has passed; this is not a test of every developer workstation or operating system.
- The PR workflow has not yet been exercised by a real pull request.
- Repository-level `main` branch rules/protection, required checks, default Actions `GITHUB_TOKEN` permissions, and protected-environment settings have not been independently confirmed. The GitHub integration used for this review could not read the branch-protection endpoint.
- No browser/mobile rendering, Burmese search-quality, host/VM, kernel feature, container runtime, or lab validation is claimed by this matrix.
- No Pages deployment workflow or published site is present.

## Dependency update rule

Update direct dependencies in `pyproject.toml`, regenerate and review `uv.lock` with the pinned uv version, run `uv lock --check`, `uv sync --locked`, and the strict documentation build, then submit both dependency files together for review. Do not rely on CI to create or amend lockfiles.
