# Bespoke

A portable agent skill that builds writing from a specific person's real voice, grounded in four established, independent bodies of research rather than a fixed list of banned phrases:

- **Stylometry and authorship attribution** for what an individual's actual linguistic fingerprint consists of (function words, sentence-length variance, recurring phrase patterns), the same class of evidence used in forensic authorship analysis since the statistical study of the disputed Federalist Papers.
- **Orwell's plain-style diagnostics**, from "Politics and the English Language" (1946), for a principled account of why prefabricated phrasing reads as hollow, eight decades before anything resembling AI-generated text existed.
- **Formulaic-language psycholinguistics**, for why the goal is swapping shared, generic phrasing for a writer's own recurring language, not eliminating pre-formed phrasing altogether.
- **Forensic content-analysis criteria** (Criteria-Based Content Analysis and Reality Monitoring) for what distinguishes genuine, specific, lived detail from plausible-sounding invention.

It is plain Markdown with zero external dependencies: no API keys, no build step, nothing to install to use it. Full sourcing for all four is in `references/`.

## Installation

### Skills CLI

Install with the cross-agent [skills CLI](https://www.npmjs.com/package/skills):

```bash
npx skills add <your-username>/bespoke --global
```

Update an existing install:

```bash
npx skills update bespoke --global
```

To install into every supported agent harness on your machine:

```bash
npx skills add <your-username>/bespoke --global --agent '*'
```

Omit `--global` for a project-local install that can be committed and shared with collaborators.

### Claude Code plugin

```
/plugin marketplace add <your-username>/bespoke
/plugin install bespoke@bespoke
```

The skill is then invoked as `/bespoke:bespoke`.

### Manual

Any agent harness can use the skill directly because the runtime artifact is `SKILL.md`. Copy it, and the `references/` folder alongside it, into wherever your harness expects skill directories:

```bash
git clone https://github.com/<your-username>/bespoke.git /path/to/your/skills/bespoke
```

Or, if you already have this repo cloned:

```bash
mkdir -p /path/to/your/skills/bespoke
cp -r SKILL.md references /path/to/your/skills/bespoke/
```

### Claude.ai

Upload `SKILL.md` and the `references/` folder as a `.skill` file (zip the repo, excluding `.git`, `.github`, and `.claude-plugin`) through Settings → Capabilities → Skills.

## Usage

Invoke however your harness exposes installed skills. Common forms:

```
/bespoke

Write in my voice: [paste a LinkedIn post topic]
```

```
Humanize this: [paste AI-sounding text]
```

The skill opens with a short intake if it doesn't already know your voice, platform, audience, and intention for the piece:

```
My Personal Voice: direct, a little dry, no corporate hedging
Task: LinkedIn post about a product launch delay
Audience: my team and a few clients who are already annoyed
Intention: own the delay without sounding defensive
```

Give it 2-3 paragraphs of your own past writing instead of adjectives when you can. A real sample gives the stylometric layer (below) something to actually measure.

## What it does

- **A stylometric voice fingerprint**, not a one-shot style match: function-word habits, sentence-length variance, opening patterns, and the writer's own recurring bigrams and trigrams, read from a real sample and kept for the rest of the conversation.
- **Orwell's plain-style check**, applied as a live diagnostic: dying metaphors, verbal false limbs, pretentious diction, and meaningless words, the same four faults named in 1946, with current examples.
- **A formulaic-language swap, not a ban.** Pre-formed phrasing is normal and necessary for fluent writing; the skill directs it toward the writer's own recurring phrases instead of shared clichés.
- **A specificity test drawn from forensic content analysis**: contextual embedding, unexpected complications, reproduced (not summarized) conversation, and admitted gaps, the actual criteria used to distinguish genuine accounts from fabricated ones, repurposed as a construction checklist.
- **Platform-specific structure**: Context-Core-Connect for LinkedIn and Substack, hook-plus-white-space for X and Threads, tight distillation for email and Slack.
- **An honest engagement gate.** Rapport techniques that work by being honest are always available. Techniques that work by deceiving the reader are gated to disclosed, consensual contexts, not applied by default to published, audience-facing content. See `references/engagement-ethics.md`.
- **Verified detection science, not fabricated statistics.** `references/detection-science.md` documents a citation-fabrication finding caught and excluded during research, and why current classifier-based detectors make surface-level evasion a weaker strategy than genuine specificity.

## Repository structure

```
bespoke/
├── SKILL.md                        # the skill itself; source of truth
├── README.md                       # this file
├── AGENTS.md                       # guidance for agents/contributors editing this repo
├── LICENSE                         # MIT
├── .claude-plugin/
│   ├── plugin.json                 # Claude Code plugin manifest
│   └── marketplace.json            # single-repo marketplace entry
├── .github/workflows/validate.yml  # CI: runs the same checks below on every push
├── scripts/
│   └── validate_package.py         # dependency-free sync checks (stdlib only)
└── references/
    ├── plain-style-diagnostics.md
    ├── detection-science.md
    ├── engagement-ethics.md
    └── changelog.md
```

## Validating a local copy

```bash
python3 scripts/validate_package.py
```

Stdlib only, no `pip install` required. Checks that `SKILL.md`'s name and version match `.claude-plugin/plugin.json`, that every file `SKILL.md` points to under `references/` actually exists, and that the marketplace entry resolves.

## Version history

- **2.0.0** — Rebuilt around independent research (stylometry, Orwell's plain-style diagnostics, formulaic-language psycholinguistics, forensic content-analysis criteria) rather than a comparative audit of an existing tool. See `references/changelog.md` for the full account of what changed and why.
- **1.0.0** — Initial release, built after benchmarking against an existing AI-tell removal tool. Superseded by 2.0.0's independent research base.

## License

MIT. See `LICENSE`.

## Credits

Early development benchmarked against [blader/humanizer](https://github.com/blader/humanizer) (MIT). Bespoke's current structure is built from independent research (see `references/changelog.md`); this credit reflects where the project started, not its present design.
