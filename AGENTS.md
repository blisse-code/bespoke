# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, OpenCode, Warp, and others) working in this repository, and for anyone editing it by hand.

## What this repo is

A portable agent skill implemented entirely as Markdown. The runtime artifact is `SKILL.md`: the agent reads its YAML frontmatter and the instructions below it. There is no build step and no code to run to use the skill. The only code in this repo (`scripts/validate_package.py`) is a packaging check, not part of the skill's runtime behavior. The repo should avoid wording that limits support to one or two harnesses; it's meant to work anywhere Markdown skill instructions are supported.

## Key files

- `SKILL.md` — the skill itself. Portable YAML frontmatter (`name`, `description`, `license`, `compatibility`, `metadata.version`) followed by the instructions. **This is the source of truth.**
- `README.md` — for humans: installation across multiple methods, usage, a feature summary, and a version history.
- `.claude-plugin/plugin.json` — optional Claude Code plugin manifest.
- `.claude-plugin/marketplace.json` — optional single-repo marketplace entry so `/plugin marketplace add <owner>/bespoke` works.
- `scripts/validate_package.py` — dependency-free (Python stdlib only) package and synchronization checks, used locally and in CI.
- `references/` — supporting detail `SKILL.md` points to as needed: voice capture, the tell taxonomy, the detection-science sourcing, the engagement-ethics gate, and the changelog. `SKILL.md` stays the entry point; these are loaded on demand, not required reading up front.

## The maintenance contract

`SKILL.md`, `README.md`, and `.claude-plugin/plugin.json` must stay in sync:

- **Version:** `SKILL.md` frontmatter stores the version under `metadata.version`. `.claude-plugin/plugin.json` has a top-level `version` field. `README.md` has a "Version History" section. Bump all three together. Keep the skill version under `metadata` in `SKILL.md`; a top-level `version` key is not portable across Agent Skills hosts. `marketplace.json` intentionally omits a version so `plugin.json` stays the single source of truth for it.
- **Reference files:** if you add, remove, or rename a file under `references/`, update the "Reference files" list at the bottom of `SKILL.md` in the same change. `scripts/validate_package.py` checks that every reference `SKILL.md` names actually exists on disk, but it can't check the reverse, so don't leave an orphaned file `SKILL.md` never mentions.
- **Compatibility:** keep install and usage language harness-neutral. The skill should work in any agent harness that can load Markdown skill instructions; Claude Code, OpenCode, Codex, and others are examples, not limits.
- **Validation:** run `python3 scripts/validate_package.py` before publishing a change. If you have the Claude Code CLI available, `claude plugin validate .` and `npx skills add . --list` are good additional checks; CI runs equivalents of these on every push (see `.github/workflows/validate.yml`).
- **No fabricated specifics:** if you're tempted to add a specific statistic, benchmark number, or citation to `SKILL.md` or `references/detection-science.md`, verify it against the actual source first. This skill exists partly because an earlier draft of it almost shipped fabricated citations; `references/detection-science.md` documents exactly what happened and why the standard is strict here specifically.

## Editing SKILL.md

- Preserve valid YAML frontmatter (formatting and indentation matter for cross-host parsing).
- The prompt below the frontmatter is the product. Edit it like a careful instruction document, not code. Keep it harness-neutral: no tool calls, file paths, or vocabulary specific to one agent product.
- If a change alters what the skill actually does (not just wording), add a line to `README.md`'s Version History explaining what changed and why, and bump the version per the maintenance contract above.
