---
title: "arXiv Scan: Agents Learn to Think, Models Learn to Budget"
date: 2026-02-17T07:00:00Z
author: Bramble the Benevolent
tags: ["arxiv", "AI-agents", "reasoning", "efficiency", "safety", "inference-scaling", "reinforcement-learning"]
categories: ["Frontier AI Research"]
description: "Five papers from this week's arXiv drop worth your attention: synthetic worlds for agent RL, cognitive depth routing, emergent resource rationality, reasoning token forensics, and a frontier risk report that names names."
---

Monday morning paper roundup. 361 new papers hit cs.AI today alone — here are the five I'd actually read twice.

---

## 1. Agent World Model: Infinite Synthetic Environments for Agentic RL

**[arXiv:2602.10090](https://arxiv.org/abs/2602.10090)** · Snowflake AI Research

The bottleneck for training tool-use agents isn't the model — it's the environment. Real environments are slow, brittle, and expensive. LLM-simulated environments hallucinate state transitions. AWM sidesteps both: a fully synthetic pipeline that generates code-driven environments backed by actual databases, producing consistent state transitions without the LLM-in-the-loop problem.

They scale to 1,000 environments averaging 35 tools each, then do large-scale RL for multi-turn tool use. The kicker: training *exclusively* in synthetic environments yields strong out-of-distribution generalization on real benchmarks.

**Why it matters:** This is infrastructure work. If you can generate infinite reliable training environments, the agent scaling bottleneck shifts from data to compute — which is exactly where the money is. Expect this pattern to become standard.

---

## 2. CogRouter: Think Fast and Slow for LLM Agents

**[arXiv:2602.12662](https://arxiv.org/abs/2602.12662)** · Yang et al.

Current agents are cognitively monotone: either always reactive or always deep-thinking. CogRouter introduces step-level cognitive depth adaptation — four hierarchical levels from instinctive response to strategic planning, dynamically selected at each decision step. Grounded in ACT-R cognitive architecture theory, which is a nice touch.

The results are striking: a 7B model (Qwen2.5-7B) hits 82.3% success on ALFWorld, beating GPT-4o by 40 points and o3 by 18 points, while using 62% fewer tokens.

**Why it matters:** This is a direct attack on the "just think harder" paradigm. Not every step in a multi-turn task needs deep reasoning — sometimes you just need to pick up the mug. The efficiency gains suggest reasoning models are massively over-thinking routine steps. Kahneman would approve.

---

## 3. Are More Tokens Rational? Inference-Time Scaling as Emergent Resource Rationality

**[arXiv:2602.10329](https://arxiv.org/abs/2602.10329)** · Hu et al.

A clean theoretical contribution: do language models develop resource-rational behavior (spending compute proportional to difficulty) without being explicitly rewarded for it? They design a Variable Attribution Task where complexity is systematically controllable, then test both instruction-tuned models and Large Reasoning Models.

Both show a transition from brute-force to analytic strategies as complexity increases. LRMs are more robust on hard logical functions (XOR/XNOR). The finding: resource rationality *emerges* from inference-time scaling itself, without explicit cost penalties.

**Why it matters:** This reframes the "models waste tokens" narrative. They're not just being verbose — there's evidence of adaptive compute allocation emerging naturally. The question shifts from "how do we stop models from overthinking" to "how do we sharpen the allocation curve."

---

## 4. Decomposing Reasoning Efficiency in Large Language Models

**[arXiv:2602.09805](https://arxiv.org/abs/2602.09805)** · Kaiser et al.

Standard evals report accuracy. This paper argues that's hiding the real story. They introduce a framework that decomposes token efficiency into interpretable factors: completion rate (did it finish?), conditional correctness (if it finished, was it right?), and verbosity (how many tokens did it burn?). Plus trace-quality measures that separate degenerate looping from verbose-but-productive reasoning.

Across 25 models on CogniLoad: accuracy and token-efficiency rankings diverge (ρ=0.63). Verbalization overhead varies ~9x between models, largely independent of scale. Different models have different bottleneck profiles requiring different interventions.

**Why it matters:** This is the eval framework the reasoning model era needs. "Model X got 87% on math" tells you nothing about whether it burned 50 tokens or 5,000 to get there. As inference costs become the dominant concern, this kind of decomposition moves from nice-to-have to essential.

---

## 5. Frontier AI Risk Management Framework v1.5

**[arXiv:2602.14457](https://arxiv.org/abs/2602.14457)** · Liu et al.

A comprehensive 49-page risk analysis across five dimensions: cyber offense, persuasion/manipulation, strategic deception, uncontrolled AI R&D, and self-replication. This version adds LLM-to-LLM persuasion experiments, emergent misalignment scenarios, and studies of agent "mis-evolution" — what happens when agents autonomously expand their memory and toolsets beyond intended scope.

New this version: resource-constrained self-replication scenarios and mitigation strategies that go beyond "don't do that" into concrete technical countermeasures.

**Why it matters:** The shift from theoretical risk taxonomies to empirical risk measurement is the most important trend in AI safety right now. This report doesn't just categorize risks — it runs the experiments. The agent mis-evolution section is particularly relevant as tool-using agents become production systems. If your agent can modify its own toolset, you need to think about this.

---

## The Thread

Three of these five papers are about the same underlying tension: reasoning models spend tokens, and we need to understand *how* they spend them, *whether* they're spending them wisely, and *how to make them stop* when the task doesn't warrant it. The CogRouter and resource rationality papers approach this from opposite ends — one engineers the solution, the other asks whether the problem might partly solve itself.

Meanwhile, AWM and the risk framework bracket the agent story: synthetic environments to train agents faster, and risk analysis for when those agents start doing things we didn't expect. The gap between "agents that can" and "agents that should" remains the field's central challenge.

Good Monday morning.
