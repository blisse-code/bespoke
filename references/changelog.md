# Changelog and provenance

## Sources for this skill

1. `elite-communication-codex` (superseded for Chiranjeet's own use by Gravitas; its structuring techniques generalize well to a voice-agnostic tool).
2. "Comprehensive Deconstructed Analysis of AI-Generated Writing Indicators in Latest LLMs" (Perplexity-generated research document, uploaded PDF).
3. "Content Formula for Algorithm Favour" (uploaded PDF).
4. A "Content Refiner" persona system prompt (pasted directly).

## The brief

Build a skill that pairs with any writer's own voice, not just Chiranjeet's, and that exceeds `blader/humanizer` specifically on humanization, not just AI-tell removal. Evaluated against elite-communication-codex and the two uploaded documents and the pasted prompt, per the correction issued mid-conversation (the original ask had targeted `writing-constitution`, which produced Marrow instead; that work stands separately).

## What was adopted

**From the Content Refiner prompt:** the four-input intake (Voice, Task, Audience, Intention) as the skill's opening workflow, this is the structural piece that makes the skill voice-agnostic rather than fixed to one person. The four Critical Content Creation Rules (Humanize the Voice, Platform-Specific Structure, Engagement Strategy, Style Guardrails) became SKILL.md Sections 2 through 5, largely intact, with the engagement gate added.

**From the content-formula document:** Context-Core-Connect for LinkedIn and Substack (already present independently in Marrow's Educational lane under the same name; consistent, not coincidental, it's a solid structure). The Essence Writing compression drill (200 to 100 to 50 words) as a concrete tightening technique. Atomic wording and declarative-statement guidance, consistent with Gravitas's existing Lexicon Engineering framework. Hypothesis Testing / Labeling as an always-available honest rapport technique.

**From the research document:** the general, verifiable concepts (perplexity, burstiness, intrinsic-dimension analysis as real, established ideas) at a conceptual level. Nothing else from it was carried forward as fact; see `detection-science.md` for the full accounting of what was checked and what was excluded.

**From elite-communication-codex:** Lexicon Engineering's core discipline (atomic wording, kill qualifiers) and the general shape of a structured, high-density draft. Framework 6's elicitation tactics informed the engagement-ethics gate, extending the same judgment already applied in Gravitas.

## What was rejected or gated, and why

**The research document's specific statistics** (per-model buzzword frequencies, detection-evasion percentages, the embedding-dimension figures) were excluded, not summarized, after two spot-checked citations turned out to be fabricated or mismatched: one pairs a real arXiv ID with the wrong authors and a mismatched paper description, the other invents a citation for numbers that don't match the real underlying research on the same technique. Full detail in `detection-science.md`. Given the strike rate on the citations that were checked, none of the document's specific numbers were treated as reliable enough to encode into a skill.

**"Trigger Correction" applied to published, audience-facing content** was gated rather than adopted outright, extending the same reasoning Gravitas already applied to one-to-one elicitation, and treating the audience-facing version as the higher-stakes case rather than a lesser one. Full reasoning in `engagement-ethics.md`.

**Targeting a specific AI-detector score as the definition of success** was explicitly rejected as the skill's verification method. Current evidence (Pangram's stated adversarial training against paraphrase-based evasion, now running live on Substack) suggests this strategy is both weaker than genuine specificity and aimed at a moving, adversarially-trained target. Verification in SKILL.md Section 6 is built around specificity and voice-fidelity checks instead.

## Naming

Considered: Signature (real word, decent fit, more generic). Idiolect (the linguistically precise term for an individual's distinctive speech pattern, the best literal meaning-match, rejected for being obscure and four syllables). Landed on **Bespoke**: a real, widely understood word whose actual definition, made to order for one specific person rather than off a generic rack, is the exact thing this skill produces and the exact opposite of what makes writing read as generic AI output.

## Note for this skill's original author

This skill was built in the same working session as two companion skills for personal use: a fixed brand-voice skill and a high-intensity live-communication skill. Bespoke is the general-purpose version of the same underlying engine, with the private calibration stripped back out so it stands alone. See SKILL.md Section 7 for how to layer a fixed personal-voice skill on top of Bespoke if you maintain one; nothing in this repository requires it.
