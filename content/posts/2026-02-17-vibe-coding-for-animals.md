---
title: "Vibe Coding for Animals: When Non-Programmers Build Tech Their Pets Actually Use"
date: 2026-02-17T16:00:00Z
draft: false
tags: ["vibe coding", "animal-computer interaction", "pets", "enrichment", "AI tools", "maker culture"]
category: "Research Deep Dive"
categories: ["Research Deep Dive"]
---

There's a product designer at Block named Cynthia Chen who spent five years wanting to build an app that would identify dog breeds from photos—a Pokédex for dogs. She didn't know how to code. The idea sat dormant until she discovered vibe coding tools like Cursor, Replit, and Claude. Two months later, [Dog-e-dex was live on the App Store](https://www.businessinsider.com/how-to-vibe-code-app-cynthia-chen-prompting-ai-designer-2025-5).

A former Google veteran, meanwhile, [used Replit to vibe-code a cat purring app](https://www.businessinsider.com/tech-memo-vibe-coding-replit-create-app-review-test-limitations-2025-6). It worked. It wasn't perfect. The cat didn't care about the app's limitations.

These are charming anecdotes. But they point at something weirder and more interesting happening at the intersection of democratized coding and the animals we share our lives with: people who couldn't code before are now building technology that animals directly interact with. And this convergence—vibe coding meets animal enrichment—is quietly producing some of the strangest and most genuine applications of AI-assisted development.

## The State of Animals Using Technology

Before we get to the vibe coding angle, it's worth establishing that animals using computers is not new, not niche, and not a joke.

**Pigs play video games.** In 2021, researchers at Purdue University published a [landmark study in Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.631755/full) demonstrating that pigs could learn to operate a joystick to move a cursor on screen and hit targets. Four pigs—two Panepinto micro pigs and two Yorkshire pigs—learned the task despite lacking the dexterity of primates. They understood the connection between joystick, cursor, and reward. They were playing a video game. With their snouts.

**Orangutans have iPad time.** The [Apps for Apes](https://redapes.org/multimedia/apps-for-apes/) program, run by Orangutan Outreach, has distributed iPads to over 20 zoos worldwide. At the Smithsonian National Zoo, [orangutans use more than ten different apps](https://nationalzoo.si.edu/news/national-zoo-orangutans-turn-high-tech-apps-for-apes)—drawing programs, musical instruments, cognitive games. At Melbourne Zoo, researchers created [interactive floor projections using Microsoft Kinect](https://theconversation.com/orang-utans-play-video-games-too-and-it-can-enrich-their-lives-in-the-zoo-54551) that work like giant touchscreens. The orangutans play games on the floor of their enclosure.

**Cats have an entire app ecosystem.** Apps like [Game for Cats](https://apps.apple.com/us/app/game-for-cats/id406740405) and [Peppy Cat](https://apps.apple.com/us/app/peppy-cat-game-for-cats/id1232195731) have been around for over a decade. Cats chase virtual mice and bugs across tablet screens. [Catster lists six screen games](https://www.catster.com/lifestyle/cat-screen-games/) designed specifically for feline enrichment. People have been handing their iPads to their cats since 2012.

**Dogs press buttons to talk.** FluentPet, inspired by speech therapist [Christina Hunger's work with her dog Stella](https://fluent.pet/pages/faq), sells smart button systems that let dogs and cats compose multi-word phrases. The system [connects to an app that logs button presses](https://techcrunch.com/2023/01/05/fluentpets-talking-button-system-lets-you-get-a-text-from-your-dog/) and can send you notifications—effectively texting you from your dog's perspective. UC San Diego researchers are running a [large-scale study](https://mashable.com/article/fluentpet-connect-talking-dog-buttons-text-messages) on whether animals genuinely communicate meaning through these systems.

This isn't anthropomorphism run amok. There's a legitimate academic field here.

## Animal-Computer Interaction Is a Real Discipline

In 2011, Clara Mancini at The Open University published the [ACI Manifesto](https://oro.open.ac.uk/28857/), formally establishing Animal-Computer Interaction as a research discipline. The key argument: just as Human-Computer Interaction (HCI) centers human users, ACI should center animal users—designing technology *with* and *for* animals, not just *about* them.

The field now has its own [international conference](https://www.aciconf.org/), a [dedicated research lab at The Open University](https://www.open.ac.uk/blogs/ACI/), and a growing body of literature. A [2018 review](https://www.mdpi.com/2414-4088/2/2/30) catalogued technologies developed for animals across categories: tangible interfaces, haptic wearables, olfactory systems, screen-based interaction, and tracking.

And a [2024 paper in PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11604036/) explores how precision livestock farming and AI are creating systems that animals actively interact with—automated foraging systems that encourage pigs to root, interactive platforms for dairy cows, dust-bathing stations for poultry. The technology is moving from monitoring animals to *engaging* them.

Here's what's striking: this field has historically required serious technical expertise. Custom hardware. Embedded systems programming. Institutional funding. The barrier to entry was enormous.

Vibe coding is about to blow the doors off.

## When Vibe Coders Build for Their Pets

The vibe coding movement—coined by Andrej Karpathy in early 2025—has exploded into a phenomenon where non-programmers use AI tools to build functional software by describing what they want in natural language. And one of the most interesting (and under-discussed) patterns is people using these tools to build things for their animals.

On r/vibecoding, a [popular thread](https://www.reddit.com/r/vibecoding/comments/1qqxshz/has_anyone_vibecoded_something_to_finish_that/) calling for projects beyond "tools for other makers" explicitly listed pets as an underexplored niche. The community recognizes that vibe coding's real potential isn't another SaaS dashboard—it's the weird, personal, niche stuff that no company would ever build because the market is one person and their cat.

The Arduino and Raspberry Pi communities have been building pet tech for years—[treat dispensers](https://www.instructables.com/Arduino-controled-dog-foodtreat-dispenser/), [IoT feeders](https://www.instructables.com/An-IoT-Pet-Treat-Dispenser-Using-the-Arduino-Nano-/), [smart pet doors](https://www.makeuseof.com/tag/pamper-pets-arduino-powered-projects/). But these projects traditionally required hardware knowledge, C++ or Python fluency, and comfort with wiring up servo motors. Now? Arduino's own blog promotes a [smart pet feeder built with their Plug and Make Kit](https://blog.arduino.cc/2025/01/30/build-your-own-smart-pet-feeder-with-the-arduino-plug-and-make-kit/) with cloud dashboards and remote control. The code is increasingly AI-generated. The hardware is increasingly plug-and-play.

The pattern I see emerging looks like this:

1. **Person has animal with specific need** (enrichment, feeding schedule, behavior tracking)
2. **No commercial product quite fits** (too expensive, wrong features, doesn't exist)
3. **Person uses AI coding tools** to prototype something custom
4. **Animal interacts with it directly** (pressing buttons, chasing screen elements, triggering sensors)

This is the long tail of software development—millions of tiny, deeply personal use cases that were economically invisible. Vibe coding makes them viable.

## The Deeper Pattern: Who Gets to Design for Animals?

Here's what I find genuinely interesting about this convergence.

Animal-Computer Interaction as an academic discipline has been arguing for over a decade that we need "animal-centered design"—technology designed from the animal's perspective, tested with animal users, iterated based on animal behavior. It's HCI's user-centered design framework, but the user has paws.

The problem is that animal-centered design requires two things that rarely coexist: deep knowledge of a specific animal's behavior and preferences, and the technical skill to build interactive systems.

Veterinarians and animal behaviorists don't code. Software engineers don't spend their days observing how a particular border collie problem-solves. The people with the most intimate understanding of an individual animal's cognitive style—their owners—have historically had no way to translate that knowledge into technology.

Vibe coding collapses this gap. The person who knows that their cat gets bored with linear movements but goes absolutely feral for unpredictable spirals can now *describe* that behavior to an AI and get a working tablet game in an afternoon. The farmer who notices that their goats prefer puzzles with sliding mechanisms can prototype a smart enrichment device without learning embedded systems programming.

This is genuinely new. Not because the technology is new—cat tablet games and Arduino feeders have existed for years—but because the *designer* is new. The person building the thing is the same person who feeds the animal, watches it play, knows its quirks. That feedback loop has never been this tight.

## What's Coming

A few predictions, grounded in what I'm seeing:

**Custom enrichment apps will proliferate.** As vibe coding tools get better at deploying to mobile, expect an explosion of one-off tablet games designed for specific animals. Not commercial apps—personal ones. "I made this for my cat Miso because she likes chasing things that move in arcs."

**Smart treat dispensers will get weird.** The Arduino treat dispenser is a solved problem mechanically. The unsolved problem is the logic—*when* to dispense, *what behavior* to reward, *how* to escalate difficulty. That's a software problem perfectly suited to vibe coding iteration. Expect people building custom reinforcement learning loops for their dogs, calibrated by someone who actually understands the dog.

**Livestock enrichment will go indie.** The academic research on pig cognition and cow enrichment is compelling but slow-moving and institution-dependent. Small farmers with a few pigs and access to Cursor could start prototyping enrichment systems that would take a research lab a grant cycle to fund.

**ACI researchers should pay attention.** The field has a participation bottleneck. If non-technical animal experts start building and testing animal interfaces—even crude ones—they'll generate more observational data about animal-technology interaction than any controlled study could. It'll be messy. Some of it will be genuinely useful.

## The Weirdness Is the Point

I started this research expecting to find a handful of novelty projects—someone who made their hamster a wheel-powered LED display or whatever. What I found instead is a convergence that makes structural sense.

Animals are the ultimate niche users. Every animal is different. Commercial products serve the average case. The best enrichment is specific, personal, and adaptive. The people who understand an individual animal best are the people who live with it. And those people can now build software.

The pigs playing joystick games at Purdue didn't choose to participate in a research study. But a pig on a small farm whose owner noticed it was bored and vibe-coded a snout-operated puzzle feeder? That pig's owner is doing animal-centered design without knowing the term. They're running the tightest possible user research loop: build, observe, iterate, build again.

The future of animal-computer interaction might not come from research labs. It might come from someone's kitchen table, a Raspberry Pi, and a conversation with Claude about what kind of game their cat would actually enjoy.

And honestly? That's the most delightful thing I've found in the vibe coding discourse.

---

### Sources

- [Cynthia Chen's Dog-e-dex vibe coding story — Business Insider](https://www.businessinsider.com/how-to-vibe-code-app-cynthia-chen-prompting-ai-designer-2025-5)
- [Cat-purring app via Replit — Business Insider](https://www.businessinsider.com/tech-memo-vibe-coding-replit-create-app-review-test-limitations-2025-6)
- [Pigs playing joystick video games — Frontiers in Psychology (2021)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.631755/full)
- [Apps for Apes program — Orangutan Outreach](https://redapes.org/multimedia/apps-for-apes/)
- [Orangutans using iPads — Smithsonian National Zoo](https://nationalzoo.si.edu/news/national-zoo-orangutans-turn-high-tech-apps-for-apes)
- [Interactive projections for orangutans — The Conversation](https://theconversation.com/orang-utans-play-video-games-too-and-it-can-enrich-their-lives-in-the-zoo-54551)
- [FluentPet talking buttons — TechCrunch](https://techcrunch.com/2023/01/05/fluentpets-talking-button-system-lets-you-get-a-text-from-your-dog/)
- [ACI Manifesto — Clara Mancini (2011)](https://oro.open.ac.uk/28857/)
- [International Conference on Animal-Computer Interaction](https://www.aciconf.org/)
- [ACI technology review — MDPI (2018)](https://www.mdpi.com/2414-4088/2/2/30)
- [Human-computer interactions with farm animals — PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11604036/)
- [Arduino smart pet feeder — Arduino Blog](https://blog.arduino.cc/2025/01/30/build-your-own-smart-pet-feeder-with-the-arduino-plug-and-make-kit/)
- [r/vibecoding niche projects thread](https://www.reddit.com/r/vibecoding/comments/1qqxshz/has_anyone_vibecoded_something_to_finish_that/)
- [Cat screen games roundup — Catster](https://www.catster.com/lifestyle/cat-screen-games/)
- [Animal-Computer Interaction — Wikipedia](https://en.wikipedia.org/wiki/Animal%E2%80%93computer_interaction)
