# AGENTS.md

Notes for AI coding agents and human contributors working in this repository.

## What this repo is

A writing-craft skill with no executable core. `SKILL.md` is what an agent reads and follows; everything else here either documents it (`README.md`, this file) or supports distributing it (`.claude-plugin/`, `.github/`, `scripts/validate_package.py`). There's nothing to compile or install to use the skill itself.

## Key files

- `SKILL.md` — the skill. Frontmatter (`name`, `description`, `license`, `compatibility`, `metadata.version`) plus the instructions themselves. If you're changing what the skill does, this is the file to change.
- `README.md` — the human-facing pitch: what it's grounded in, how to install it, how to use it.
- `references/*.md` — supporting depth `SKILL.md` points to on demand. Each file traces back to a specific, named body of research; if you add a new one, it should too.
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` — Claude Code plugin manifests, following Anthropic's published schema for these files.
- `scripts/validate_package.py` — a small, dependency-free (stdlib only) script that checks version numbers and reference-file paths stay consistent across `SKILL.md` and the plugin manifests. It has nothing to do with the skill's writing instructions.

## Keeping things in sync

- Bump `metadata.version` in `SKILL.md`'s frontmatter and `version` in `.claude-plugin/plugin.json` together. `README.md`'s Version History section should get an entry in the same change. `marketplace.json` deliberately has no version field of its own; `plugin.json` is the single source of truth for that number.
- If you add, remove, or rename a file under `references/`, update the "Reference files" list at the bottom of `SKILL.md` in the same change, and check `python3 scripts/validate_package.py` passes before committing.
- Keep `SKILL.md` itself free of anything specific to one agent product (tool names, file paths, product-specific vocabulary). It should read the same way regardless of which harness is loading it.

## A note on sourcing

Every claim in `SKILL.md` and `references/` that names a researcher, a study, or a specific figure should be independently verifiable, not just plausible-sounding. This repository exists partly because an earlier version of it repeated fabricated statistics from a source document without checking them first (see `references/changelog.md` and `references/detection-science.md` for the full account). If you're adding a new claim with a name or number attached, check it against a real source before it goes in.

## Validating a change

```bash
python3 scripts/validate_package.py
```

If you have Claude Code's CLI available, `claude plugin validate .` is a useful additional check for the plugin manifests specifically. CI runs both on every push; see `.github/workflows/validate.yml`.
