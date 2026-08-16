# Bespoke

A portable agent skill that pairs with any writer's actual voice to produce writing that reads as specifically theirs, not generic AI output. It is plain Markdown, so it runs in any harness that supports skill-style instructions, and it has zero external dependencies: no API keys, no build step, no packages to install to use it.

Bespoke goes one step further than a typical AI-tell scrubber. Most tools in this space (including [blader/humanizer](https://github.com/blader/humanizer), which this skill was benchmarked against) remove AI-sounding patterns and hand back generic clean prose. Bespoke removes the same patterns and then rebuilds the draft from a short intake and the writer's own material, so two different people using it get two different-sounding results.

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

Give it 2-3 paragraphs of your own past writing instead of adjectives when you can. A real sample teaches Bespoke your actual sentence rhythm, vocabulary, and habits far better than a description does.

## What it does

- **Intake-first, not voice-fixed.** Confirms Voice, Task, Audience, and Intention before drafting, and only asks for what's actually missing.
- **A durable voice profile**, not a one-shot style match: sentence rhythm, vocabulary register, paragraph-opening habits, punctuation quirks, and recurring phrases, built from a real sample and kept for the rest of the conversation.
- **A 45-plus entry, voice-agnostic tell taxonomy** across content, grammar, structural, and filler/hedging patterns, each with a false-positive guard so a genuinely distinctive voice never gets flattened chasing a pattern match.
- **Platform-specific structure**: Context-Core-Connect for LinkedIn and Substack, hook-plus-white-space for X and Threads, tight distillation for email and Slack.
- **An honest engagement gate.** Rapport techniques that work by being honest (labeling, hypothesis testing) are always available. Techniques that work by deceiving the reader (stating something false to bait a correction) are gated to contexts where that's disclosed and consensual, not applied by default to published, audience-facing content. See `references/engagement-ethics.md`.
- **Verified detection science, not fabricated statistics.** `references/detection-science.md` documents exactly what's checked and sourced versus excluded, including a citation-fabrication finding in one of the documents that originally informed this skill. The short version: current classifier-based detectors are trained specifically to catch surface-level "humanized" rewriting, so this skill optimizes for genuine specificity instead of a target detector score.

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
    ├── voice-capture.md
    ├── tell-taxonomy-general.md
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

- **1.0.0** — Initial public release. Intake-first voice pairing, seven-category tell taxonomy with a false-positive guard, honest-engagement gate, and a sourced-and-corrected detection-science reference.

## License

MIT. See `LICENSE`.

## Credits

Built after a comparative audit against [blader/humanizer](https://github.com/blader/humanizer) (MIT), whose 33-pattern taxonomy and detection-guidance discipline set the bar this skill was built to clear.
