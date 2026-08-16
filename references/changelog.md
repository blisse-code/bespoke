# Changelog and provenance

## v2.1.0 (current)

**Trigger:** a direct, critical comparison against `blader/humanizer` v2.9.1, requested after v2.0.0 shipped, turned up a real regression rather than a purely stylistic trade-off. Rebuilding away from humanizer's category structure to fix v1's architectural over-dependence (see v2.0.0 below) had also cut real coverage: roughly a third of humanizer's 33 named patterns, including em dashes, arguably the single most recognizable AI-writing tell, had no equivalent anywhere in v2.0.0.

**What was added, and where it lives:**

- **Typography and formatting** (em dashes, curly quotes, Title Case headings, boldface density, inline-header lists, hyphenated-compound overuse, emoji): new file `typographic-markers.md`, framed through Section 1's voice-fingerprint concept rather than as a flat ban list. The default (rare em dashes, sentence-case headings, and so on) is explicitly a calibration absent a sample, not a permanent rule; a real sample that contradicts the default wins.
- **Vague attribution, notability namedropping, persuasive authority tropes** ("borrowed authority," Cluster A in `plain-style-diagnostics.md`): grouped as ways a sentence implies credibility it hasn't earned, tied to both Orwell's pretentious diction and the specificity test in `SKILL.md` Section 4.
- **Synonym cycling, false ranges, negative parallelisms/tailing negations, fragmented headers, manufactured punchline runs, aphorism formulas** ("decorative structure," Cluster B): folded in alongside the patterns already present (rule-of-three, metaphor stacking, thesis repetition, copula avoidance, signposting).
- **Chatbot artifacts, sycophantic tone, conversational rhetorical openers** ("borrowed register," Cluster C): framed as correspondence-shaped or performed language leaking into content that isn't correspondence, cross-referenced from `SKILL.md` Section 5.
- **Cutoff disclaimers and speculative gap-filling**: not placed in the pattern-list file at all. Folded directly into `SKILL.md` Section 4 as a concrete example of what fails the specificity test, since dressing an unknown as narrative is a fabrication mechanism, not a phrasing tell, and belongs with the CBCA-based construction checklist rather than a word list.
- **The despite-challenges formula, diff-anchored writing, superficial "-ing" tack-ons**: added as paragraph-level instances of Orwell's verbal-false-limb pattern (Fault 2), since each pads a paragraph the way a verbal false limb pads a sentence.

**What this doesn't do:** revert to humanizer's own category names or numbering. Every addition above sits inside one of Bespoke's existing frames (the voice fingerprint, Orwell's four faults, the specificity test, borrowed authority/structure/register) rather than being appended as a flat, renumbered list. The goal was closing a real functional gap without reintroducing the structural mimicry v2.0.0 was built to fix.

**Also fixed:** a stale internal cross-reference in `SKILL.md`'s intro, which pointed to Section 5 for the AI-detector note when the actual content is in Section 7.

---

## v2.0.0

**Trigger for this rewrite:** v1.0.0 (below) was built after benchmarking against `blader/humanizer`, an existing open-source AI-tell removal skill. v1 organized its tell taxonomy under the same category scheme humanizer uses (content-level, grammar-level, structural, filler/hedging), and its packaging (`AGENTS.md`, `.claude-plugin/`, CI workflow) closely mirrored humanizer's actual repository structure, which had been fetched directly during development. The content was original, the wording was original, but the shape of the thing was a close structural echo of the tool it was benchmarked against.

**What changed and why:** rebuilt from independent research instead of from a comparative audit. The previous version's core weakness wasn't plagiarism, the words were original, it was architectural dependence: reasoning that starts from "here's what humanizer does, now do it better" produces something shaped like humanizer even when every sentence is new. v2 starts instead from four independent, established, verifiable bodies of research that have nothing to do with AI-tell removal as a category:

- **Stylometry and authorship attribution** (Mosteller and Wallace, 1964; Stamatatos, 2009) for what a real voice fingerprint actually consists of.
- **Orwell's "Politics and the English Language"** (1946) for a principled, pre-AI account of why prefabricated language reads as hollow, with a diagnosis ("gone some distance toward turning himself into a machine") more precise than any list of buzzwords.
- **Formulaic language psycholinguistics** (Alison Wray) for why eliminating all pre-formed phrasing is the wrong goal, and what the right one is instead.
- **Criteria-Based Content Analysis and Reality Monitoring** (Undeutsch; Steller and Köhnken, 1989), forensic-psychology research on what separates genuine, experience-based accounts from fabricated ones, repurposed here as a construction checklist rather than a detection tool.

Humanizer's 33-pattern taxonomy is real, useful, and covers ground worth covering. It's now one smaller supporting file (`plain-style-diagnostics.md`'s second section) folded under Orwell's four-fault framework rather than the organizing structure of the whole skill. The packaging (`AGENTS.md`, plugin manifests, CI) still follows the correct external schemas for Claude Code plugins and GitHub Actions, those are platform requirements, not humanizer's invention, but the wording was rewritten independently rather than adapted from humanizer's actual files.

**What this means concretely:** `SKILL.md`'s operational instructions no longer compare themselves to humanizer anywhere. The comparison lives in exactly one place, this file, as attribution for where the benchmarking started, not as the skill's ongoing frame of reference.

---

## v1.0.0

Initial build. See the v2.0.0 entry above for what was wrong with its approach and why it was rebuilt.

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
