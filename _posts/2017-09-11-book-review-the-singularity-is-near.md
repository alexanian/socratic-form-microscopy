---
id: 496
title: "Book Review: The Singularity is Near"
date: 2017-09-11T22:23:02-04:00
author: Zach
layout: post
guid: https://socratic-form-microscopy.com/?p=496
permalink: /2017/09/11/book-review-the-singularity-is-near/
inline_featured_image:
  - "0"
categories:
  - Literature
  - Science
tags:
  - book review
  - futurism
  - nuclear weapons
  - reading
  - x-risk
---

I recently read <em>The Singularity is Near</em> as part of a book club and figured a few other people might benefit from hearing what I got out of it.

First – it was a useful book. I shed a lot of my skepticism of the singularity as I read it. My mindset has shifted from "a lot of this seems impossible" to "some of this seems impossible, but a lot of it is just incredibly hard engineering". But that's because I stuck with it – something that probably wouldn't have happened without the structure of a book club.

I'm not sure Kurzweil is actually the right author for this message. <em>Accelerando</em> (by Charles Stross) covered much of the same material as <em>Singularity</em>, while being incredibly engaging. Kurzweil's writing is technically fine – he can string a sentence together and he's clear – but incredibly repetitious. If you read the introduction, the introduction of each chapter, all of Chapter 4 (in my opinion, the only consistently good part of the book proper), and his included responses to critics (the only other interesting part of the whole tome) you'll get all the worthwhile content, while saving yourself a good ten hours of hearing the same thing over and over and over again. Control-C/Control-V may have been a cheap way for Kurzweil to pad his word count, but it's expensive to the reader.

I have three other worries about Kurzweil as a futurist. One deals with his understanding of some of the more technical aspects of what he's talking about, especially physics. Here's a verbatim quote from <em>Singularity</em> about nuclear weapons:

<blockquote>Alfred Nobel discovered dynamite by probing chemical interactions of molecules. The atomic bomb, which is tens of thousands of times more powerful than dynamite, is based on nuclear interactions involving large atoms, which are much smaller scales of matter than large molecules. The hydrogen bomb, which is thousands of times more powerful than an atomic bomb, is based on interactions involving an even smaller scale: small atoms. Although this insight does not necessarily imply the existence of yet more powerful destructive chain reactions by manipulating subatomic particles, it does make the conjecture [that we can make more powerful weapons using sub-atomics physics] plausible.</blockquote>
This is false on several levels. First, uranium and plutonium (the fissile isotopes used in atomic bombs) are both more massive (in the sense that they contain more matter) than the nitroglycerine in dynamite. Even if fissile isotopes are smaller in one dimension, they are on the same scale as the molecules that make up high explosives. Second, the larger energy output from hydrogen bombs has nothing to do with the relative size of hydrogen vs. uranium. Long time readers will know that the <a href="{{ site.baseurl }}/2017/01/25/nuclear-weapons-4-0-weapon-design/#tu">majority of the destructive output of a hydrogen bomb actually comes from fission of the uranium outer shell</a>. Hydrogen bombs (more accurately thermonuclear weapons) derive their immense power from a complicated multi-step process that liberates a lot of energy from the nuclei of atoms.

Kurzweil falling for this plausible (but entirely incorrect) explanation doesn't speak well of his ability to correctly pick apart the plausible and true from the plausible and false in fields he is unfamiliar with. But it's this very picking apart that is so critical for someone who wants to undertake such a general survey of science.

My second qualm emerges when Kurzweil talks about AI safety. Or rather, it arises from the lack of any substantive discussion of AI safety in a book about the singularity. As near as I can tell, Kurzweil believes that AI will emerge naturally from attempts to functionally reverse engineer the human brain. Kurzweil believes that because this AI will be essentially human, there will be no problems with value alignment.

This seems very different from the <a href="https://en.wikipedia.org/wiki/Superintelligence:_Paths,_Dangers,_Strategies">Bostromian paradigm</a> of dangerously misaligned AI: AI with ostensibly benign goals that turn out to be inimical to human life when taken to their logical conclusion. The most common example I've heard for this paradigm is an industrial AI tasked with maximizing paper clip production that tiles the entire solar system with paper clips.

Kurzweil is so convinced that the first AI will be based on reverse engineering the brain that he doesn't adequately grapple with the orthogonality thesis:<a href="https://wiki.lesswrong.com/wiki/Orthogonality_thesis"> the observation that intelligence and comprehensible (to humans) goals don't need to be correlated</a>. I see no reason to believe Kurzweil that the first super-intelligence will be based off a human. I think to believe that it would be based on a human, you'd have to assume that various university research projects will beat Google and Facebook (who aren't trying to recreate functional human brains <em>in silica</em>) in the race to develop a general AI. I think that is somewhat unrealistic, especially if there are paths to general intelligence that look quite different from our brains.

Finally, I'm unhappy with how Kurzweil's predictions are sprinkled throughout the book, vague, and don't include confidence intervals. The only clear prediction I was able to find was Kurzweil's infamously false assertion that by ~2010, our computers would be split up and worn with our clothing.

It would be much easier to assess Kurzweil's accuracy as a predictor if he listed all of his predictions together in a single section, applied to them clear target dates (e.g. less vague than: "in the late 2020s"), and gave his credence (as it stands, it is hard to distinguish between things Kurzweil believes are very likely and things he views as only somewhat likely). Currently any attempts to assess Kurzweil's accuracy are very sensitive to what you choose to view as "a prediction" and how you interpret his timing. More clarity would make this unambiguous.

Outside of Kurzweil's personal suitability as an author and advocate (and his sagacity), I have one beef with singulatarian thought in general. <a href="https://www.technologyreview.com/s/601441/moores-law-is-dead-now-what/">It's becoming increasingly clear that the silicon paradigm of computing will soon come to the end of its exponential growth</a>. Switching to something like <a href="https://arstechnica.co.uk/gadgets/2015/02/intel-forges-ahead-to-10nm-will-move-away-from-silicon-at-7nm/">indium gallium arsenide</a> and moving key processes to more optimized chips will buy a bit more time, but doesn't represent a fundamental paradigm shift of the sort that gets us around the tunneling problem.

Furthermore, we've already began to bump up against the limit on clock speed in silicon; <a href="https://cartesianproduct.wordpress.com/2013/04/15/the-end-of-dennard-scaling/">we can't really run silicon chips at higher clock rates without melting them</a>. This is unfortunate, because speed ups in clock time are much nicer than increased parallelism. Almost all programs benefit from quicker processing, while only certain programs benefit from increased parallelism. This isn't an insurmountable obstacle when it comes to things like artificial intelligence (the human brain has a very slow clock speed and massive parallelism and it's obviously good enough to get lots done), but it does mean that some things that Kurzweil were counting on to get quicker and quicker have stalled out (the book was written just as the <a href="https://en.wikipedia.org/wiki/Dennard_scaling">Dennard Scaling</a> began to break down).

All this means that the exponential growth that is supposed to drive the singularity is about to fizzle out… maybe. Kurzweil is convinced that the slowdown in silicon will necessarily lead to a paradigm shift to something else. But I'm not sure what it will be. He talks a bit about graphene, but when I was doing my degree in nanotechnology engineering, the joke among the professors was that graphene could do anything… except make it out of the lab.

Kurzweil has an almost religious faith that there will be another paradigm shift, keeping his exponential trend going strong. And I want to be really clear that I'm not saying there <em>won't</em> be. I'm just saying there <em>might not</em> be. There is no law of the universe that says that we have to have convenient paradigm shifts. We could get stuck with linear (or even logarithmic) incremental improvements for years, decades, or even centuries before we resume exponential growth in computing power.

It does seem like ardent belief in the singularity might attract more religiously minded atheists. Kurzweil himself believes that it is our natural destiny to turn the whole universe into computational substrate. Identifying god with the most holy and perfect (in fine medieval tradition; there's something <a href="https://en.wikipedia.org/wiki/Ontological_argument#Anselm">reminiscent of Anselm</a> in Kurzweil's arguments), Kurzweil believes that once every atom in the universe sings with computation, we will have created god.

I don't believe that humanity has any grand destiny, or that the arc of history bends towards anything at all in particular. And I by no means believe that the singularity is assured, technologically or socially. But it is a beautiful vision. Human flourishing, out to the very edges of the cosmos…

Yeah, I want that too. I'm a religiously minded atheist, after all.

In both disposition and beliefs, I'm far closer to Kurzweil than his many detractors. I think "<a href="https://en.wikipedia.org/wiki/Degrowth">degrowth</a>" is an insane policy that if followed, would create scores of populist demagogues. I think that the <a href="https://en.wikipedia.org/wiki/Chinese_room">Chinese room argument</a> is good only for identifying people who don’t think systemically. I'm also more or less in agreement that government regulations won't be able to stop a singularity (if one is going to occur because of continuing smooth acceleration in the price performance of information technology; regulation could catch up if a slowdown between paradigm shifts gives it enough time).

I think the singularity very well <em>might</em> happen. And at the end of the day, the only real difference between me and Kurzweil is that "might".

Also: I repeat myself less.

<hr class="post-end" />
