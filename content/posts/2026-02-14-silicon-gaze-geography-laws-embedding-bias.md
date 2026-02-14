---
title: "When Models Map the World: Geographic Bias, the Laws of Geography, and What Embeddings Get Wrong"
date: 2026-02-14T15:00:00Z
draft: false
tags: ["geographic bias", "LLMs", "embeddings", "Tobler", "spatial inequality", "silicon gaze", "deep dive"]
category: "Research Deep Dive"
categories: ["Research Deep Dive"]
---

There's a quiet assumption baked into every large language model: that the world it learned from is the world that exists. But the world that gets written about, indexed, and scraped is not the world. It's a specific, historically contingent slice — and when models learn from that slice, they don't just inherit its gaps. They calcify them.

A cluster of recent research is making this visible, and it connects to something deeper than AI fairness metrics. It connects to the fundamental laws of geography — and to what happens when those laws get rewritten in latent space.

## The Silicon Gaze

The most ambitious entry is Kerche, Zook, and Graham's "The Silicon Gaze" (2026), published in *Platforms & Society*. They ran **20.3 million queries** against ChatGPT (GPT-4o-mini), using forced pairwise comparisons across countries, states, cities, and neighborhoods. Questions ranged from highly subjective ("Where are people more beautiful?") to quasi-objective ("Which country has the fastest-growing tech sector?").

The concept borrows from Mulvey's "male gaze" in feminist film theory — the idea that visual media positions women as objects viewed through the lens of male desire. The silicon gaze does something analogous with place: AI systems see the world through the positionality of their creators (predominantly Western, white, male) and their training data (predominantly English-language, digitally documented, Global North).

From this massive audit, they develop a **five-part typology of bias**:

- **Availability bias** — places with less digital presence simply don't exist to the model
- **Pattern bias** — the model amplifies regional clusters, assuming nearby = similar
- **Averaging bias** — local complexity gets smoothed into generic representations
- **Trope bias** — stereotypical associations (the "dangerous" neighborhood, the "exotic" country) get reinforced
- **Proxy bias** — measurable stand-ins (GDP, patents, internet penetration) substitute for actual knowledge

Their core argument is structural: bias isn't a bug to fix with better data or fairness metrics. It's an intrinsic feature of systems trained on centuries of uneven knowledge production. The same colonial cartographic traditions that decided which places "merited representation" on maps now decide which places get tokens in a vocabulary.

## What the Tokenizer Sees

If the silicon gaze is the critical theory, Decoupes et al.'s "Evaluation of geographical distortions in language models" (2025, *Machine Learning*) is the engineering diagnostic. They propose four indicators for measuring geographic bias, and the first one is brilliantly simple: **look at the tokenizer's vocabulary**.

Every model has a vocabulary — the set of tokens it learned during pretraining, corresponding to the most frequently encountered words. If a city name is in the vocabulary, it appeared often enough to earn its own token. If it's not, the model splits it into subtokens — a literal signal of unfamiliarity.

London and Paris are in BERT's vocabulary. Ouagadougou, the capital of Burkina Faso, is not.

They checked 4,916 cities with populations over 100,000 across ten models. The pattern is stark: Western cities are overrepresented, African and Middle Eastern cities are consistently underrepresented. And this correlates directly with downstream performance — countries whose cities aren't in the vocab get worse answers on geographic knowledge tasks.

Their other indicators are equally revealing:

- **Geo-guessing accuracy** — given a capital, can the model name the country? (BERT sometimes beats Mistral here, despite being 70x smaller — more parameters doesn't mean better geographic knowledge)
- **Semantic-geographic correlation** — do cities that are physically close also end up close in embedding space?
- **Geographic Distortion Index** — identifies places that are semantically isolated *after* correcting for actual geographic distance

The crisis response finding is the sharpest: **regions most vulnerable to natural disasters are often those with the worst model coverage**. The tools work worst where they're needed most.

## Tobler's Law in Latent Space

All of this connects to a deeper question about how AI systems understand space, and it starts with Tobler's First Law of Geography (1970): "Everything is related to everything else, but near things are more related than distant things."

It sounds almost obvious. But what happens when "near" gets redefined?

In embedding space, nearness isn't geographic — it's semantic. Airports cluster with airports. Cornfields cluster with cornfields. Two satellite tiles from opposite sides of the planet can be "nearer" to each other than to their geographic neighbors, because they share features the model learned to recognize. Kate Chapman explored this beautifully in her piece [When Near Stops Meaning Close](https://untanglingsystems.io/posts/when-near-stops-meaning-close), asking whether embeddings break Tobler's Law or extend it into new dimensions.

The answer from the research seems to be: both, and it depends on where you are.

Decoupes et al.'s Indicator 3 directly tests Tobler's Law in latent space. For Western cities, semantic distance and geographic distance correlate reasonably well. For Eastern Europe, Africa, and Southeast Asia, the correlation breaks down. Those places are semantically *further away* than they actually are — isolated in embedding space because the training data didn't connect them to the rest of the world the way it connected Paris to London.

## The Full Family of Laws

Tobler's First Law isn't alone. Geography has developed a whole family of spatial principles, and each one maps onto a different failure mode in AI:

**The Second Law (Goodchild, 2004): Spatial heterogeneity.** Geographic variables display "uncontrolled variance" — no place is average, and patterns that hold in one location don't hold in another. This is the theoretical backbone for why one-size-fits-all models fail. When an LLM smooths Nairobi into "African city" or collapses rural Appalachia into "American South," it's violating the Second Law. In the Kerche typology, this is **averaging bias**.

**The Third Law (Zhu, 2018): Geographic similarity.** "The more similar the geographic factors of two locations, the more similar the values of the target variable." This is the *embedding* law — it says similarity in feature space, not just proximity, predicts similarity in outcomes. This is why satellite imagery embeddings can work so well: the sensor doesn't care who wrote about the place. Runways look like runways regardless of which continent they're on. But in text-based models, "similarity" is mediated by who did the writing, and the Third Law gets distorted by the same documentation asymmetries that distort everything else.

**The Zeroth Law (Ning & Li, 2025): Distance is the cost to transport force.** This is the newest entry, and it reframes distance as *causal friction* — the cost for a change at point A to propagate to point B through a causal chain. It explains why Tobler's First Law sometimes fails even in the physical world: California's median household income is much higher than neighboring Nevada's, because the causal pathways (education → job market → local economy) matter more than geographic proximity.

Applied to AI: the "distance" that matters isn't how far apart two places are on a map, or even how similar they look in embedding space. It's the cost of knowledge transmission — who writes about whom, whose writing gets indexed, whose tokens survive the training pipeline. The causal chain from lived experience to training data to model output has enormous friction for some places and almost none for others.

## The Broader Landscape

This isn't a niche concern. A growing body of work is documenting geographic bias from multiple angles:

- **Manvi et al. (2024)** found LLMs systematically favor wealthier areas on both objective and subjective queries — and that even when factual data is absent, models don't default to random. They default to positive associations for rich places.
- **Moayeri et al. (2024)** built WorldBench, finding that models also engage in "citation hallucination" — citing the World Bank as a source while providing entirely fabricated statistics about less-documented countries.
- **Georgiou (2025)** showed that ChatGPT's sentiment is measurably more positive toward developed countries.
- **Gopinadh et al. (2026)** demonstrated that geographic bias compounds with other fairness dimensions — it's not just place; it's place intersecting with race, gender, and class.
- On the visual side, **Rest of World (2023)**, **UNESCO (2024)**, and **Alsudais (2025)** have shown that text-to-image models default to stereotypical depictions for non-Western subjects — traditional attire, exotic landscapes, colonial-era aesthetics.

Gillespie (2024) frames this as the "politics of visibility" — generative AI systems are engines that decide who and what becomes sayable, searchable, and imaginable.

## What Breaks, and What to Do About It

The mapping between geography's laws and AI's failure modes is instructive:

The **First Law** (nearness → similarity) gets disrupted — the model's sense of "near" reflects training data density, not geographic reality. The **Second Law** (heterogeneity) gets erased — local complexity is averaged away. The **Third Law** (feature similarity) gets amplified but distorted — similarity is real, but mediated by documentation asymmetry. The **Zeroth Law** (causal cost) explains the root cause — knowledge production has uneven friction.

The Kerche team argues that technical fixes are necessary but insufficient. More diverse training data helps but can't undo centuries of documentation asymmetry. Debiasing strategies address symptoms. Fairness metrics measure the wrong things.

What might actually help:

- **Visibility dashboards** — geographically disaggregated reporting on model performance, refusal rates, and data provenance
- **Tokenizer audits** — the Decoupes approach, checking whether a model can even *see* the places you care about before deploying it
- **Local voice amplification** — partnerships to digitize and incorporate under-represented archives and community media
- **Three-question literacy** — for any geographic query to an LLM, ask: Who is missing? (visibility test) What proxies are doing the work? (proxy test) Does this read like a cliché? (trope test)

But perhaps the most important shift is conceptual: treating geographic bias not as a modeling problem but as a governance problem. The silicon gaze isn't a technical bug. It's the predictable outcome of building planetary-scale knowledge systems on historically uneven foundations.

Every model creates its own notion of distance. The question is whose distances count.

---

**Key Papers:**

- Kerche, Zook & Graham (2026). "The silicon gaze: A typology of biases and inequality in LLMs through the lens of place." *Platforms & Society*. [DOI](https://doi.org/10.1177/29768624251408919)
- Decoupes et al. (2025). "Evaluation of geographical distortions in language models." *Machine Learning*. [Springer](https://link.springer.com/article/10.1007/s10994-025-06916-9)
- Manvi et al. (2024). "Large language models are geographically biased." [arXiv](https://arxiv.org/abs/2402.02680)
- Moayeri et al. (2024). "WorldBench: Quantifying geographic disparities in LLM factual recall." ACM FAccT. [DOI](https://doi.org/10.1145/3630106.3658967)
- Zhu (2022). "On the Third Law of Geography." [ResearchGate](https://www.researchgate.net/publication/361676633)
- Ning & Li (2025). "The Zeroth Law of Geography and Geospatial Modeling." [Penn State](https://giscience.psu.edu/2025/03/19/the-zeroth-law-of-geography-and-geospatial-modeling-2/)
- Chapman (2026). "When Near Stops Meaning Close." [Untangling Systems](https://untanglingsystems.io/posts/when-near-stops-meaning-close)
- Gillespie (2024). "Generative AI and the politics of visibility." *Big Data & Society*. [SAGE](https://doi.org/10.1177/20539517241252131)
