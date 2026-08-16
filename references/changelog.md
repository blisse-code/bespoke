# Changelog and provenance

## v1.0.0

Built after benchmarking against `blader/humanizer`, an existing open-source AI-tell removal skill. v1 organized its tell taxonomy under the same category scheme humanizer uses (content-level, grammar-level, structural, filler/hedging), and its packaging (`AGENTS.md`, `.claude-plugin/`, CI workflow) closely mirrored humanizer's actual repository structure, which had been fetched directly during development. The content was original, the wording was original, but the shape of the thing was a close structural echo of the tool it was benchmarked against.

## v2.0.0 (current)

**What changed and why:** rebuilt from independent research instead of from a comparative audit. The previous version's core weakness wasn't plagiarism, the words were original, it was architectural dependence: reasoning that starts from "here's what humanizer does, now do it better" produces something shaped like humanizer even when every sentence is new. v2 starts instead from four independent, established, verifiable bodies of research that have nothing to do with AI-tell removal as a category:

- **Stylometry and authorship attribution** (Mosteller and Wallace, 1964; Stamatatos, 2009) for what a real voice fingerprint actually consists of.
- **Orwell's "Politics and the English Language"** (1946) for a principled, pre-AI account of why prefabricated language reads as hollow, with a diagnosis ("gone some distance toward turning himself into a machine") more precise than any list of buzzwords.
- **Formulaic language psycholinguistics** (Alison Wray) for why eliminating all pre-formed phrasing is the wrong goal, and what the right one is instead.
- **Criteria-Based Content Analysis and Reality Monitoring** (Undeutsch; Steller and Köhnken, 1989), forensic-psychology research on what separates genuine, experience-based accounts from fabricated ones, repurposed here as a construction checklist rather than a detection tool.

Humanizer's 33-pattern taxonomy is real, useful, and covers ground worth covering. It's now one smaller supporting file (`plain-style-diagnostics.md`'s second section) folded under Orwell's four-fault framework rather than the organizing structure of the whole skill. The packaging (`AGENTS.md`, plugin manifests, CI) still follows the correct external schemas for Claude Code plugins and GitHub Actions, those are platform requirements, not humanizer's invention, but the wording was rewritten independently rather than adapted from humanizer's actual files.

**What this means concretely:** `SKILL.md`'s operational instructions no longer compare themselves to humanizer anywhere. The comparison lives in exactly one place, this file, as attribution for where the benchmarking started, not as the skill's ongoing frame of reference.

## Sources that shaped the original brief

1. `elite-communication-codex`, a prior skill whose structuring techniques informed early drafts.
2. A research document on AI-detection science (see `detection-science.md` for a citation-fabrication correction found in it).
3. A content-formula document on platform-favored writing patterns.
4. A "Content Refiner" persona prompt, the source of the four-input intake (Voice, Task, Audience, Intention) that still structures `SKILL.md`'s opening workflow.

## What was rejected or gated, and why

**The research document's specific statistics** (per-model buzzword frequencies, detection-evasion percentages, embedding-dimension figures) were excluded after two spot-checked citations turned out to be fabricated or mismatched. Full detail in `detection-science.md`.

**Deliberate-inaccuracy engagement tactics applied to published, audience-facing content** were gated rather than adopted by default. Full reasoning in `engagement-ethics.md`.

**Targeting a specific AI-detector score as the definition of success** was rejected as the skill's verification method, in favor of the specificity and voice-fidelity checks in `SKILL.md` Sections 1 through 4.

## Naming

Considered: Signature (fine, more generic). Idiolect (the linguistically precise term, and now a genuinely apt one given Section 1's grounding, but rejected again for being obscure and four syllables). Kept **Bespoke**: made to order for one specific person, not off a generic rack, which is the actual mechanism this skill now implements at every layer, not just a tagline.

## Note for this skill's original author

This skill was built in the same working session as two companion skills for personal use: a fixed brand-voice skill and a high-intensity live-communication skill. Bespoke is the general-purpose version of the underlying engine, with the private calibration stripped back out so it stands alone. See `SKILL.md` Section 8 for how to layer a fixed personal-voice skill on top of Bespoke if you maintain one; nothing in this repository requires it.
