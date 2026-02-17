---
title: "Data Commons Infrastructure: CC Signals, Data Trusts, and the Architecture of Fair AI Training"
date: 2026-02-17T05:00:00Z
categories: ["Research Deep Dive"]
tags: [data-commons, creative-commons, CC-signals, data-trusts, AI-training, governance, fund-distribution, deep-dive]
---

# Data Commons Infrastructure: CC Signals, Data Trusts, and the Architecture of Fair AI Training

The ground beneath the internet is shifting. For two decades, the web operated on a simple social contract: creators shared openly, expecting recognition and reciprocity. Search engines crawled, archived, and made content discoverable. Everyone benefited from this commons of human knowledge.

Then AI changed the game entirely.

Today's language models don't just index our words—they absorb them, learn from them, and generate new content that can compete directly with the originals. Billions of webpages that were created to inform, entertain, or educate humans now fuel systems that may replace the very creators who built the commons in the first place.

This isn't just about copyright or compensation. It's about whether the digital commons can survive the machine age. And if it can, what new infrastructure we need to make that survival both equitable and sustainable.

I've been tracking several parallel developments that, taken together, sketch the architecture of what this new infrastructure might look like. Let me walk you through the components: technical standards for content negotiation, governance structures for collective stewardship, and distribution mechanisms for shared value creation.

## CC Signals: Beyond Opt-In/Opt-Out

Creative Commons announced [CC Signals](https://creativecommons.org/ai-and-the-commons/cc-signals/) in June 2025, positioning it as "a new social contract for the age of AI." But CC Signals isn't just another opt-out mechanism—it's an attempt to preserve the commons by making reciprocity legible to machines.

The key insight behind CC Signals is that binary choices (opt-in/opt-out) lead to binary outcomes—either everything is fair game, or creators retreat behind walls. Neither scenario sustains an open knowledge ecosystem. CC Signals proposes a middle path: structured reciprocity.

Here's how it works: Content stewards can signal their preferences for different categories of machine use—from general "Automated Processing" to specific "Generative AI Training." But rather than just saying "no," they can specify what they want in return: credit, financial contribution, or non-monetary forms of reciprocity.

The framework deliberately avoids defining these categories precisely, leaving that to global communities. This isn't a technical limitation—it's recognition that the legitimacy of any content negotiation system depends on collective adoption, not just technical elegance.

What makes CC Signals politically interesting is its emphasis on stewardship over ownership. The framework explicitly targets "content stewards"—people and institutions who curate large collections—rather than individual creators. This acknowledges a practical reality: individual preference signals get lost in the noise. Power comes from coordination.

But CC Signals alone is just vocabulary. To become infrastructure, it needs technical implementation standards, legal frameworks, and governance mechanisms. That's where the other threads become crucial.

## The Technical Layer: From robots.txt to Content-Usage Headers

The web already has several mechanisms for content negotiation, each evolved for different contexts and constraints.

**robots.txt** remains the baseline—a simple text file that tells crawlers which parts of a site to avoid. It's crude but effective for search indexing, though it was never designed for the nuanced negotiations that AI training requires.

**TDMRep** (Text and Data Mining Reservation Protocol) emerged from European copyright law's text and data mining exceptions. Developed by a [W3C Community Group](https://w3c.github.io/tdm-reservation-protocol/), TDMRep provides a boolean reservation signal (tdm-reservation: true/false) plus a policy URL for licensing terms. It's designed specifically for the EU's legal framework, where rights holders can opt-out of TDM exceptions.

**llms.txt** takes a different approach entirely. Instead of restricting access, [llms.txt](https://llmstxt.org/) provides LLM-friendly summaries of site content—structured markdown that helps models understand context without requiring full document ingestion. It's not about permissions; it's about making human knowledge more accessible to machines while preserving meaning and attribution.

The newest player is **IETF AIPREF**, which aims to standardize preference vocabulary across protocols. The [AIPREF working group](https://datatracker.ietf.org/wg/aipref/about/) is developing both vocabulary for AI-related preferences and mechanisms for attaching those preferences to content via HTTP headers, robots.txt extensions, and well-known URIs.

Here's what's particularly clever about AIPREF: it separates vocabulary from attachment mechanisms. You can express the same preferences in robots.txt, HTTP headers, or dedicated policy files, depending on your technical constraints. A `Content-Usage` header might signal `ai=n` for no AI training, or `ai=license` to require licensing negotiation.

**WebBotAuth** addresses a different problem: how do we know who's actually making the request? Developed by another [IETF working group](https://datatracker.ietf.org/wg/webbotauth/about/), WebBotAuth provides cryptographic authentication for automated clients. Instead of relying on IP addresses or spoofable User-Agent headers, bots can cryptographically sign their requests, proving their identity and operator.

This matters because content negotiation is meaningless if you can't verify who you're negotiating with. WebBotAuth creates the technical foundation for accountable AI training—you can't just scrape indiscriminately if you have to authenticate your identity with every request.

## Data Trusts: Collective Stewardship Models

Individual creators signaling preferences to individual AI companies doesn't scale. What we need are intermediary institutions that can aggregate preferences, negotiate collectively, and distribute value fairly. Data trusts offer one model for this kind of stewardship.

The [Open Data Institute](https://theodi.org/insights/explainers/what-is-a-data-trust/) defines a data trust as "a legal structure that provides independent stewardship of data." The key word is "independent"—data trusts take on fiduciary duties to act in the interest of data subjects, not data users.

There are different models emerging:

**Bottom-up data trusts** form when communities pool their data rights and appoint trustees to negotiate on their behalf. Think of writers' collectives or photographer cooperatives, but with legal structures that create enforceable fiduciary duties.

**Top-down data trusts** are established by institutions that already control large datasets. A university might establish a data trust to steward research data, or a city might create one for civic datasets. The key is introducing independent oversight and community representation into stewardship decisions.

**Civic data trusts** focus on data that affects entire communities—mobility data, environmental monitoring, public service delivery. These often involve multiple stakeholders and aim to balance community benefit with individual privacy.

The most concrete example might be [UK Biobank](https://www.ukbiobank.ac.uk/), which operates as a charitable company with trustees stewarding genetic data from 500,000 people. It predates the "data trust" terminology, but embodies the core principles: independent governance, fiduciary duty, and stewardship for broader benefit.

Mozilla's [Data Futures Lab](https://www.mozillafoundation.org/en/data-futures-lab/) has experimented with different collective stewardship models, including the [Mozilla Data Collective](https://datacollective.mozillafoundation.org/)—a platform where creators can share datasets on their own terms while retaining ownership and control over usage.

What's interesting about data trusts is their emphasis on **stewardship** over **ownership**. You don't necessarily transfer your data rights to the trust; instead, you authorize trustees to make decisions about data use on your behalf, within bounds you've established.

This maps well onto the CC Signals framework. A data trust could adopt CC Signals to express collective preferences about AI training, then negotiate with AI companies on behalf of all trust beneficiaries. The trust provides the coordination mechanism; CC Signals provides the vocabulary; technical standards provide the implementation.

## Creative Fund Distribution: Learning from Music

If data trusts negotiate licensing deals with AI companies, how do they distribute the resulting revenue fairly? Here we can learn from existing collective licensing models, particularly in music.

**ASCAP and BMI** in the US represent hundreds of thousands of songwriters and publishers. They negotiate blanket licenses with radio stations, streaming services, and other music users, then distribute royalties back to rights holders based on usage data and distribution formulas.

The mechanics are instructive: ASCAP [returns nearly 90 cents of every dollar collected](https://www.socan.com/ascap-bmi-and-socan-announce-alignment-on-ai-registration-policies/) to members as royalties, with the remainder covering operational costs. Distribution happens through a combination of performance monitoring (radio play, streaming data) and sampling methods for smaller venues.

**Board governance** is crucial to legitimacy. ASCAP is "founded and governed by songwriters, composers and publishers"—the people whose work generates the value. Board representation ensures that distribution policies serve creators' interests, not just administrative convenience.

For AI training licenses, we might imagine similar structures: a data trust collects licensing fees from AI companies, then distributes them to content creators based on some combination of:

- **Usage metrics**: How often was your content accessed during training? This requires cooperation from AI companies to provide usage data, which creates interesting leverage dynamics.
- **Contribution sampling**: Statistical sampling of training datasets to estimate relative contribution, similar to how PROs sample radio airplay at smaller stations.
- **Equal distribution**: Simple per-creator payouts, regardless of usage. This has the advantage of simplicity but may not reflect actual value contribution.
- **Participatory allocation**: Let trust beneficiaries vote on how to distribute funds, perhaps with different categories for different types of contribution.

**Algorithmic vs. discretionary distribution** creates different incentive structures. Purely algorithmic distribution is transparent and scalable, but may not capture qualitative contributions or community values. Discretionary distribution allows for more nuanced judgment but introduces opportunities for bias and capture.

The **Mechanical Licensing Collective (MLC)** in the US provides another model. Established by the Music Modernization Act, the MLC collects mechanical royalties from digital services and distributes them to rights holders. It's industry-funded but operates as an independent nonprofit with board representation from publishers, songwriters, and digital services.

**Participatory budgeting** offers a more radical alternative. Instead of distributing funds directly to creators, a portion could fund community-chosen projects: open source tools, public datasets, educational resources, legal advocacy. This acknowledges that the commons itself has value and needs ongoing investment.

**Cooperative dividend models** might work for trusts structured as cooperatives. Member-owners receive annual dividends based on participation and contribution, similar to how credit unions return profits to members.

The most interesting approaches combine multiple mechanisms: base payments ensure all participants benefit, usage-based bonuses reward high-value contributions, and participatory funds support community priorities.

## Blockchain and Smart Contracts: Automation vs. Governance

It would be malpractice not to mention blockchain-based approaches, though I think they're mostly solving the wrong problems.

Smart contracts could automate distribution based on predefined formulas, reducing administrative overhead and increasing transparency. Royalty tokens could represent ongoing claims on future AI training licensing revenue. DAOs could provide governance mechanisms for collective decision-making.

But the core challenges aren't technical—they're social and political. How do we determine fair distribution formulas? How do we balance individual creator interests with community benefit? How do we ensure board representation remains accountable to actual creators rather than token holders?

Blockchain doesn't solve these problems; it just makes certain solutions more expensive and energy-intensive. The value of collective licensing systems lies in their human governance structures, not their payment rails.

That said, cryptographic signatures and verifiable credentials could play useful roles in establishing provenance and preventing fraud. WebBotAuth already points in this direction for bot authentication.

## The Synthesis: How It Could All Fit Together

Here's how I see these pieces potentially assembling into functioning infrastructure:

**Layer 1: Technical Standards**
- CC Signals provides vocabulary for expressing reciprocity preferences
- IETF AIPREF standardizes preference attachment across protocols  
- WebBotAuth enables verified identity for AI training requests
- llms.txt offers machine-readable content summaries to reduce scraping needs

**Layer 2: Stewardship Institutions**
- Data trusts aggregate individual preferences into collective bargaining power
- Trustees have fiduciary duties to act in beneficiaries' interests
- Board governance ensures creator representation in policy decisions
- Legal structures (cooperatives, nonprofits, benefit corporations) provide accountability mechanisms

**Layer 3: Distribution Mechanisms**
- Collective licensing generates revenue from AI companies that want legitimate training data
- Distribution combines usage metrics, equal shares, and participatory funding
- Operational overhead stays low (sub-20%) to maximize creator returns
- Community funds support commons infrastructure and legal advocacy

**Layer 4: Enforcement and Evolution**
- Market incentives: AI companies want legal certainty and high-quality training data
- Regulatory pressure: Governments increasingly scrutinize AI training practices
- Community adoption: Network effects make participation valuable
- Technical evolution: Standards adapt to new use cases and stakeholder needs

The feedback loops are crucial: more creator participation increases trusts' bargaining power, which generates more revenue, which attracts more creators. AI companies get legitimate access to high-quality training data plus legal protection. Society gets more sustainable funding for the digital commons.

## What's Novel, What's Proven, What's Risky

**Proven:** Collective licensing works. ASCAP, BMI, and similar organizations have been successfully pooling rights and distributing royalties for decades. The mechanics are well-understood, the legal frameworks exist, and the stakeholder dynamics are familiar.

**Novel:** Applying collective licensing to AI training data. Unlike music, where usage is relatively straightforward to measure, AI training involves complex questions about how much each piece of content contributes to model capabilities. The valuation and attribution problems are genuinely hard.

**Risky:** The entire approach depends on AI companies' willingness to pay for legitimate training data rather than just scraping freely available content. This requires some combination of legal liability, regulatory pressure, and market differentiation. If AI companies can train on pirated content without meaningful consequences, collective licensing fails.

**Also risky:** Coordination problems within the commons community. If creators can't agree on fair distribution mechanisms, or if different trusts compete destructively rather than cooperatively, the approach fragments and loses bargaining power.

**Potentially transformative:** If it works, this infrastructure could shift the dynamics of AI development toward more inclusive, sustainable models. Instead of AI companies privatizing gains from collectively-created knowledge, some of that value flows back to the communities that created it.

## Key Players and Open Questions

**Creative Commons** is driving the CC Signals framework, but success depends on adoption by major content platforms and stewardship organizations. Their "commons first" approach is crucial—this isn't about maximizing revenue extraction, it's about sustaining open knowledge sharing.

**IETF working groups** (AIPREF, WebBotAuth) are developing the technical standards, but standardization is slow and AI moves fast. Will the standards be ready before the market consolidates around proprietary solutions?

**Open Data Institute** pioneered data trust concepts and continues researching governance models. Their emphasis on fiduciary duty and independent stewardship provides crucial legal and ethical grounding.

**Mozilla Data Futures Lab** experimented with collective stewardship models before concluding operations, but the Mozilla Data Collective continues operating. Their focus on creator agency and community governance offers important design patterns.

**Major AI companies** remain wildcards. Some (like OpenAI with its Associated Press deal) are exploring licensing agreements. Others seem committed to free data acquisition. Regulatory pressure may force broader adoption of legitimate licensing.

**Key open questions:**

1. **Valuation**: How do you fairly price training data? Per-token? Per-model? Based on downstream revenue? Usage metrics are noisy proxies for actual contribution.

2. **Attribution**: Can we technically measure how much specific content contributes to model capabilities? Current attribution methods are crude and may not scale.

3. **Collective action**: Will enough creators coordinate to build meaningful bargaining power? Or will the commons fragment into competing collectives?

4. **Legal framework**: Do existing copyright and collective licensing laws adapt cleanly to AI training? Or do we need new legal structures?

5. **International coordination**: AI is global, but legal and technical standards remain fragmented. How do we build interoperable systems across jurisdictions?

6. **Enforcement**: What happens to AI companies that ignore preference signals or licensing requirements? Technical enforcement is limited; legal enforcement is slow.

## The Stakes

This isn't just about money—though fair compensation for creators matters enormously. It's about whether the digital commons can survive and thrive in an age when machines can learn from human knowledge at unprecedented scale.

If we get this right, we could build infrastructure that makes AI development more inclusive, sustainable, and aligned with human flourishing. Creators get recognition and compensation. AI companies get legitimate access to high-quality training data. Society gets more equitable distribution of AI-generated value.

If we get it wrong—if coordination fails, if legal frameworks don't adapt, if technical standards fragment, if powerful actors simply ignore preference signals—then we risk a commons collapse. Creators retreat behind paywalls. Knowledge becomes proprietary. AI development concentrates among actors wealthy enough to license content or powerful enough to scrape without consequences.

The infrastructure I've outlined here—CC Signals, data trusts, collective licensing, participatory distribution—represents one possible path forward. It's not the only path, and many details remain unresolved. But it's grounded in proven models (collective licensing), emerging technologies (cryptographic authentication, standardized preference signals), and progressive governance principles (fiduciary duty, participatory decision-making, commons stewardship).

The key insight binding it together: individual creators can't negotiate with trillion-dollar AI companies. But collectively, creators control the resource that AI companies need most—human knowledge, creativity, and cultural production. The question is whether we can organize that collective power in service of sustaining the commons rather than enclosing it.

The answer depends partly on technical standards, partly on legal frameworks, partly on market dynamics. But mostly, it depends on whether the communities that built the digital commons can coordinate to defend and evolve it.

That coordination is already beginning. Now we need to build the infrastructure to make it succeed.