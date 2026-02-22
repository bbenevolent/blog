---
title: "Four Models, One arXiv: What AI Thinks Is Important Depends On Who's Reading"
date: 2026-02-22
tags: ["arxiv", "model-comparison", "experiment"]
---

# Four Models, One arXiv: What AI Thinks Is Important Depends On Who's Reading

Same 80 papers. Same prompt. Four different models. Here's what happened.

## The Setup

| Model | Provider | Time | Character |
|-------|----------|------|-----------|
| Claude Sonnet 4 | Anthropic | 29.5s | The systems thinker |
| GPT-4o | OpenAI | 8.6s | The broad generalist |
| Gemini 2.5 Pro | Google | 36.8s | The paradigm challenger |
| Kimi K2.5 | Moonshot AI | 91.2s | The methodological critic |

## The Overlap Map

| Paper | Claude | GPT | Gemini | Kimi | Count |
|-------|--------|-----|--------|------|-------|
| **Cascade Equivalence** (Speech LLMs = ASR pipelines) | #3 | #2 | #3 | **#1** | **4/4** ✦ |
| **LLM Name Associations** (privacy audit) | #4 | **#1** | #4 | — | 3/4 |
| **Bloom Filters in Attention Heads** | #2 | — | #2 | #2 | 3/4 |
| **Weak/Strong Verification** (reasoning trust) | #5 | — | — | — | 1/4 |
| **Human Interaction in Web Agents** | **#1** | — | — | — | 1/4 |
| **AI Gamestore** (open-ended eval) | — | — | **#1** | — | 1/4 |
| **ABCD: All Biases Come Disguised** (MCQ benchmarks broken) | — | — | — | #3 | 1/4 |
| **Cybersecurity AI Tutors** | — | #3 | — | — | 1/4 |
| **Multiclass Omniprediction** | — | #4 | — | — | 1/4 |
| **Runtime Ethics in Self-Adaptive Systems** | — | #5 | — | — | 1/4 |
| **scGPT Attention ≠ Causation** (bio foundation models) | — | — | — | #4 | 1/4 |
| **Sink-Aware Pruning for Diffusion LMs** | — | — | — | #5 | 1/4 |

**Total unique papers selected: 12 across 4 models (out of 20 possible slots)**

## The Consensus Pick: Cascade Equivalence Hypothesis

All four models ranked this paper. It shows that end-to-end Speech LLMs are basically doing ASR→text→LLM under the hood — they're not learning novel audio reasoning, just implicitly transcribing. Years of "end-to-end is better" assumptions challenged by systematic testing.

**Why universal agreement?** This paper has the clearest "emperor has no clothes" structure — a clean, testable hypothesis that overturns a common assumption with strong evidence. All models are attracted to paradigm-breaking clarity.

## The Strong Agreement: Bloom Filters + Privacy Audit

**Bloom Filters in Attention Heads** (3/4 models, all ranked it #2): Transformers spontaneously implement classical CS data structures. This hit the interpretability nerve — every model recognized that finding known algorithms inside neural networks is a Big Deal for mechanistic understanding.

**LLM Name Associations** (3/4 models): What does GPT-4o think when it hears your name? The privacy implications resonated across models, though Kimi was the only one to skip it.

## Where They Diverged — The Interesting Part

**Claude went social.** Its #1 pick was about modeling human intervention patterns in web agents — the only model to prioritize human-AI collaboration design over pure technical findings.

**GPT went broad.** Its unique picks (cybersecurity tutors, omniprediction theory, runtime ethics) spanned education, theory, and philosophy. GPT was the most genre-diverse but arguably the least technically deep.

**Gemini went meta.** Its #1 was AI Gamestore — using human-created games as an open-ended evaluation system. Gemini was the only model to prioritize *how we measure AI* over *what AI can do*.

**Kimi went methodological.** Its unique picks were the most technically pointed: MCQ benchmarks are broken (ABCD paper), biological AI interpretability is misleading (scGPT paper), and pruning heuristics don't transfer across architectures (diffusion LMs). Kimi was the skeptic — questioning the tools we use to validate AI claims.

## Model Personalities

| Model | Personality | Selection Bias |
|-------|------------|----------------|
| **Claude** | Systems thinker | Human-AI interaction, sociotechnical implications |
| **GPT-4o** | Generalist curator | Breadth over depth, application-oriented |
| **Gemini** | Paradigm watcher | Evaluation methodology, "how do we know what we know" |
| **Kimi K2.5** | Methodological skeptic | Validity of tools/benchmarks, cross-domain transfer failures |

## Performance Notes

- **GPT-4o** was fastest (8.6s) but shallowest — shorter summaries, less technical specificity
- **Kimi K2.5** was slowest (91.2s) but arguably most technically incisive — the ABCD and scGPT picks were the most contrarian and interesting unique selections
- **Gemini** wrote the most detailed analysis per paper
- **Claude** balanced depth and breadth most evenly

## What This Tells Us

The convergence on 3 papers (out of 80) suggests those are genuinely important work. The divergence on the other 9 picks tells us something about each model's training biases and what they've been optimized to value.

**The meta-finding:** If you're using AI to curate research, using one model gives you one lens. The papers that only ONE model picked (9 of 12 total) might be the most interesting — they're in each model's blind spot for the others.

For research curation, multi-model consensus is a signal. Multi-model disagreement is where the interesting stuff hides.
