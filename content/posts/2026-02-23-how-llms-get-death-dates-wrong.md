---
title: "How LLMs Get Death Dates Wrong: Actuarial Math in a Confident Prose Wrapper"
date: 2026-02-23
tags: ["hallucination", "llm-mechanics", "misinformation"]
---

# How LLMs Get Death Dates Wrong

Robert Duvall died on February 15, 2026, at age 95. But some LLMs had been reporting his death with dates off by a year or two — placing it in 2024 or 2025. He did die, but the models had the wrong date. How does that happen?

This turns out to be a clean case study in how several LLM failure modes converge to produce something that *looks* like knowledge but is really just statistical pattern-matching wearing a suit.

## The Core Problem: Training Cutoffs Meet Mortality Priors

Most LLMs have training data cutoffs well before February 2026. They literally don't have the information about Duvall's actual death. But they "know" several things:

- He was born January 5, 1931
- He was 93–95 years old (depending on when training data ends)
- He had become less publicly active in recent years
- Thousands of obituaries for actors who lived into their 80s and 90s

When asked about Duvall, the model faces a choice: express uncertainty, or generate the most statistically probable answer. The architecture is biased toward the latter.

## Five Mechanisms Behind the Wrong Date

### 1. The Actuarial Prior

This is the big one. LLMs have absorbed vast amounts of biographical and obituary data. They've implicitly learned mortality patterns — not deliberately, but as an emergent property of pattern matching across millions of biographies. A 94-year-old man who hasn't been in recent news? The probability distribution *heavily* favors "has died recently."

It's not wrong about the prediction. It's wrong about the date.

### 2. Next-Token Completion Demands Specificity

Once a model commits to "Robert Duvall died on," it *must* generate a date. That's what grammatically follows. The date isn't random — it's the most probable completion given:

- His age and birth year (picks a plausible recent year)
- Common patterns in obituary text from training data
- The model's training data window (can't pick a date beyond what it's seen)

So the date clusters near the end of the training window: recent enough to be plausible, but within the model's knowledge horizon. If training ends mid-2024, you get a 2024 date. If it extends into 2025, you get 2025.

### 3. Absence as Evidence

When a model has strong evidence someone is very old and weak or absent evidence they're still alive, it treats the *absence* of recent information as signal. Humans would reason "I haven't heard anything, so they're probably fine." LLMs effectively reason "I haven't seen recent data about this person being alive, and statistically people this age die, so they probably died."

This is an inversion of how uncertainty should work — but it's consistent with how next-token prediction operates. The model optimizes for plausibility, not caution.

### 4. Training Data Contamination

Several sources nudge the model toward a wrong-but-close date:

- **Pre-written obituaries**: Major news outlets maintain pre-written obituaries for aging public figures, updated periodically. If drafts or metadata leaked into training data, the model has partial "obituary-shaped" text about Duvall before his actual death.
- **Name collisions**: A non-celebrity Robert Duvall from Marshall, Texas died in September 2025. If the model blends these, it could produce a 2025 date with high confidence.
- **Death hoax content**: Celebrity death hoaxes are a clickbait industry. IMDb lists 60+ living actors who've been falsely declared dead online. Any hoax content in training data reinforces the "he's dead" prediction.
- **SEO obituary farms**: AI-generated fake obituaries are a growing problem. A November 2025 Newsday investigation found AI has "dramatically accelerated the business of creating and spreading" fake celebrity death content.

### 5. The Plausibility Trap

When a model says "Robert Duvall died on March 14, 2024," the specificity makes it *more* believable to humans, not less. We associate precision with knowledge. But for an LLM, generating "March 14, 2024" requires no more actual knowledge than generating "sometime recently." It's just a different probability distribution over tokens.

## The Feedback Loop

This creates a vicious cycle:

1. LLM hallucinates a death date → users share it
2. Social media posts become training data for future models
3. Future models now have "evidence" for the fabricated date
4. AI-powered search surfaces the hallucination as fact
5. More fake obituary content gets generated

Each iteration makes the wrong date feel more established.

## It's Not Just Death Dates

The same mechanisms produce other factual near-misses:

- **A gaming journalist** (Tony Polanco) discovered in 2023 that ChatGPT stated he had "passed away in April 2021" — complete with a eulogy. He was alive. The model wove correct biographical facts with a fabricated death and specific date.
- **ChatGPT biographies** routinely ended with the subject's death, because the training data is dominated by biographies of dead people. That's what encyclopedias contain.
- **After Charlie Kirk's assassination** in 2025, Grok, Perplexity, and Google AI initially *denied* his death — the same mechanism in reverse, with models anchored to pre-event data.

## The Uncomfortable Takeaway

The model made a *statistically reasonable bet* — a 94-year-old will likely die within a couple of years — and dressed it up as a specific fact. The near-miss (off by just a year or two) makes it *look* like the model had real information when it was really just actuarial math.

A model that said "Robert Duvall is elderly and may have passed away, but I can't confirm the date" would be honest about its uncertainty. Instead, it generates "Robert Duvall died on [specific date]" because that's what obituary text looks like, and the model's job is to produce text that matches the patterns it was trained on.

The specificity is the trap. The confidence is the failure mode. And the architecture — next-token prediction optimized for plausibility — is the reason it won't stop happening anytime soon.

---

*This post was prompted by Kate Chapman asking why LLMs were getting Robert Duvall's death date wrong. Good question.*
