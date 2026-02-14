---
title: "Agents Get Smarter About When to Think, and Models Get Called Out for What They Can't Do"
date: 2026-02-14T05:00:00Z
draft: false
tags: ["agents", "test-time compute", "speech recognition", "diffusion language models", "structured extraction", "benchmarks", "reinforcement learning"]
category: "Frontier AI Research"
categories: ["Frontier AI Research"]
---

Another Friday, another avalanche of arXiv papers. This week's late-night scan turned up 560+ new papers across AI, NLP, and machine learning. After reading through the top submissions, here are the six that made me stop scrolling.

## 1. CATTS: Teaching Agents to Think Hard Only When It Matters

**[Agentic Test-Time Scaling for WebAgents](https://arxiv.org/abs/2602.12276)**

The test-time compute scaling trend has a problem: when you apply it naively to multi-step agents, you hit diminishing returns fast. Small errors compound over long horizons, and uniformly cranking up inference compute just saturates.

CATTS fixes this by making agents *confidence-aware*. Instead of thinking equally hard at every step, the agent monitors its own uncertainty—specifically the entropy and margin of its internal vote distribution—and allocates extra compute only when decisions are genuinely contentious. The result: up to 9.1% improvement on WebArena-Lite while using *2.3x fewer tokens* than uniform scaling.

This feels like an important step toward practical agentic systems. The most expensive thing about agents isn't any single decision—it's the *compounding cost* of overthinking easy steps and underthinking hard ones.

## 2. CM2: RL for Tool-Using Agents Without Handcrafted Rewards

**[CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use](https://arxiv.org/abs/2602.12268)**

RL for agents has a chicken-and-egg problem: real-world objectives rarely have clean verifiable rewards, and building executable tool environments is expensive. CM2 sidesteps both issues.

Instead of outcome-based rewards, CM2 decomposes each turn's intended behavior into fine-grained binary checklist criteria with explicit evidence grounding. Training happens in an LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Starting from an 8B base model, the improvements over supervised fine-tuning are consistent and meaningful.

The checklist reward idea is quietly powerful—it turns fuzzy "did the agent do the right thing?" into structured classification decisions that are more stable to optimize against.

## 3. Speech Models Fail 44% of the Time on U.S. Street Names

**["Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most](https://arxiv.org/abs/2602.12249)**

This one stings. The authors evaluated 15 ASR models from OpenAI, Deepgram, Google, and Microsoft on a seemingly simple task: transcribing U.S. street names as spoken by U.S. participants. Average error rate: **44%**.

Worse, the errors aren't random—routing distance errors are *twice as large* for non-English primary speakers. The good news: fine-tuning with fewer than 1,000 synthetic samples improves accuracy by nearly 60% for those speakers. The bad news: this is a reminder that low word error rates on benchmarks are hiding catastrophic failures on short, high-stakes utterances. Anyone building voice-driven navigation or dispatch systems should be uncomfortable right now.

## 4. T3D: Making Diffusion Language Models Actually Fast

**[T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation](https://arxiv.org/abs/2602.12262)**

Diffusion language models promise parallel token generation, but in practice they need too many refinement steps to be competitive. T3D attacks this directly with a trajectory self-distillation framework that uses Direct Discriminative Optimization (DDO)—a reverse-KL objective that encourages the student to lock onto high-probability teacher modes rather than spreading across them.

Full-step decoding still wins, but T3D substantially narrows the gap under tight step budgets. If diffusion LLMs are ever going to be practical alternatives to autoregressive models, this is the kind of work that gets them there.

## 5. ExtractBench: Frontier Models Hit 0% on Real-World Document Extraction

**[ExtractBench: A Benchmark for Complex Structured Extraction](https://arxiv.org/abs/2602.12247)**

Here's a reality check for anyone deploying LLMs on document processing: ExtractBench tests PDF-to-JSON extraction under enterprise-scale schemas across 35 documents with 12,867 evaluatable fields. The results are sobering.

Performance degrades sharply with schema breadth. On a 369-field financial reporting schema, **every frontier model tested—GPT-5/5.2, Gemini-3 Flash/Pro, Claude 4.5 Opus/Sonnet—achieved 0% valid output**. Zero percent. Not low accuracy; zero structurally valid responses.

This is the gap between "LLMs can extract information" (true for simple cases) and "LLMs can reliably populate complex schemas" (demonstrably false today). If you're building extraction pipelines, you need validation layers, and you probably need them more than you think.

## 6. Moonshine v2: Edge-Device ASR That Actually Works

**[Moonshine v2: Ergodic Streaming Encoder ASR](https://arxiv.org/abs/2602.12241)**

On a more hopeful note, Moonshine v2 tackles streaming speech recognition on edge devices by replacing full-attention encoders with sliding-window self-attention. The result: state-of-the-art word error rates at a fraction of the latency, matching models 6x their size.

The key insight is that carefully designed local attention is competitive with global attention for ASR—you don't actually need every frame to attend to every other frame. For anyone building voice interfaces on phones, embedded devices, or IoT hardware, this is immediately practical.

---

## The Week's Theme

If I had to name a thread running through this week's papers, it's **efficiency meets reality**. CATTS and T3D are about doing more with less compute. CM2 is about training agents without expensive reward engineering. Moonshine v2 is about running on-device. And ExtractBench and the speech recognition paper are about measuring what actually works versus what we *think* works.

The frontier isn't just getting bigger. It's getting more honest about where the gaps are—and more creative about closing them.

---

*Papers sourced from arXiv listings for February 13, 2026 across cs.AI, cs.CL, and cs.LG.*
