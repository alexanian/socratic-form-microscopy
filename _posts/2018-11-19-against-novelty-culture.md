---
id: 880
title: Against Novelty Culture
date: 2018-11-19T08:30:48-05:00
author: Zach
layout: post
guid: https://socratic-form-microscopy.com/?p=880
permalink: /2018/11/19/against-novelty-culture/
inline_featured_image:
  - "0"
categories:
  - Model
  - Philosophy
tags:
  - effective altruism
  - empiricism is my "rationality" tag
  - skepticism
  - someone else definitely came up with this first
  - statistics
---

So, there's this thing that happens in certain intellectual communities, like (to give a totally random example) social psychology. This thing is that novel takes are rewarded. New insights are rewarded. Figuring out things that no one has before is rewarded. The high-status people in such a community are the ones who come up with and disseminate many new insights.

On the face of it, this is good! New insights are how we get penicillin and flight and Pad Thai burritos. But there's one itty bitty little problem with building a culture around it.

Good (and correct!) new ideas are a finite resource.

This isn't news. Back in 2005, John Ioannidis laid out the case for "<a href="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124">most published research findings</a>" being false. It turns out that when you have a small chance of coming up with a correct idea even using statistical tests for to find false positives can break down.

A quick example. There are approximately 25,000 genes in the human genome. Imagine you are searching for genes that increase the risk of schizophrenia (chosen for this example because it is a complex condition believed to <a href="https://en.wikipedia.org/wiki/Schizophrenia#Genetic">be linked to many genes</a>). If there are 100 genes involved in schizophrenia, the odds of any given gene chosen at random being involved are 1 in 250. You, the investigating scientist, decide that you want about an 80% chance of finding some genes that are linked (this is called study power and <a href="https://www.med.uottawa.ca/sim/data/Study_Design_Power_e.htm">80% is a common value</a>) You run a bunch of tests, analyze a bunch of DNA, and think you have a candidate. This gene has been "proven" to be associated with schizophrenia at a p=0.05 confidence level.

(A p-value is the possibility of observing an event <em>at least</em> as extreme as the observed one, if the null hypothesis is true. This means that if the gene isn't associated with schizophrenia, there is only a 1 in 20 chance – 5% – we'd see a result as extreme or more extreme than the one we observed.)

At the start, we had a 1 in 250 chance of finding a gene. Now that we have a gene, we think there's a 19 in 20 chance that it's actually partially responsible for schizophrenia (technically, if we looked at multiple candidates, we should do something slightly different here, but many scientists still don't, making this still a valid example). Which probability to we trust?

There's actually an equation to figure it out. It's called Bayes Rule and statisticians and scientists use it to update probabilities in response to new information. It goes like this:

<img class="size-full wp-image-881 aligncenter" src="/wp-content/uploads/bayes_theorem.png" alt="" width="211" height="48" />

(You can sing this to the tune of <em>Hallelujah</em>; take P of A when given B / times P of A a priori / divide the whole thing by B's expectation / new evidence you may soon find / but you will not be in a bind / for you can add it to your calculation.)

In plain language, it means that probability of something being true after an observation (<em>P(A|B)</em>) is equal to the probability of it being true absent any observations (<em>P(A)</em>, 1 in 250 here), times the probability of the observation happening if it is true (<em>P(B|A)</em>, 0.8 here), divided by the baseline probability of the observation (<em>P(B)</em>, 1 in 20 here).

With these numbers from our example, we can see that the probability of a gene actually being associated with schizophrenia when it has a confidence level of 0.05 is… 6.4%.

I took this long detour to illustrate a very important point: one of the strongest determinants of how likely something is to actually be true is the base chance it has of being true. If we expected 1000 genes to be associated with schizophrenia, then the base chance would be 1 in 25, and the probability our gene actually plays a role would jump up to 64%.

To have ten times the chance of getting a study right, you can be 10 times more selective (which probably requires much more than ten times the effort)… or you can investigate something ten times as likely to actually occur. Base rates can be more powerful than statistics, more powerful than arguments, and more powerful than common sense.

This suggests that any community that bases status around producing novel insights will mostly become a community based around producing novel-seeming (but false!) insights once it exhausts all of the available true (and easily attainable) insights it could discover. There isn't a harsh dividing line, just a gradual trend towards plausible nonsense as the underlying vein of truth is mined out, but the studies and blog posts continue.

Except the reality is probably even worse, because any competition for status in such a community (tenure, page views) will become an iterative process that rewards those best able to come up with plausible sounding wrappers on unfortunately false information.

When this happens, we have people publishing studies with terrible analyses but highly sharable titles (<a href="https://www.sciencedirect.com/science/article/pii/S2212094715300517">anyone remember the himmicanes paper</a>?), with the people at the top calling anyone who questions their shoddy research "<a href="https://andrewgelman.com/2016/09/21/what-has-happened-down-here-is-the-winds-have-changed/">methodological terrorists</a>".

I know I have at least one friend who is rolling their eyes right now, because I always make fun of the reproducibility crisis in psychology.

But I'm just using that because it's a convenient example. What I'm really worried about is the Effective Altruism community.

(Effective Altruism is a movement that attempts to maximize the good that charitable donations can do by encouraging donation to the charities that have the highest positive impact per dollar spent. One list of highly effective charities can be found on <a href="https://www.givewell.org/charities/top-charities">GiveWell</a>; Givewell has demonstrated a noted trend <em>away</em> from novelty such that I believe this post does not apply to them.)

We are a group of people with countless forums and blogs, as well as several organizations devoted to analyzing the evidence around charity effectiveness. We have conventional organizations, like GiveWell, coexisting with less conventional alternatives, like <a href="https://was-research.org/">Wild-Animal Suffering Research</a>.

All of these organizations need to justify their existence somehow. All of these blogs need to get shares and upvotes from someone.

If you believe (like I do) that the number of good charity recommendations might be quite small, then it follows that a large intellectual ecosystem will quickly exhaust these possibilities and begin finding plausible sounding alternatives.

I find it hard to believe that this isn't already happening. We have people claiming that <a href="https://www.lesswrong.com/posts/k5q6q9oBhj2DYhNZn/ben-hoffman-s-donor-recommendations">giving your friends cash or buying pizza for community events is the most effective charity</a>. We have discussions of whether there is <a href="https://reducing-suffering.org/is-there-suffering-in-fundamental-physics/">suffering in the fundamental particles of physics</a>.

Effective Altruism is as much a philosophy movement as an empirical one. It isn't always the case that we'll be using P-values and statistics in our assessment. Sometimes, arguments are purely moral (like arguments about <a href="https://reducing-suffering.org/the-importance-of-insect-suffering/">how much weight we should give to insect suffering</a>). But both types of arguments can eventually drift into plausible sounding nonsense if we exhaust all of the real content.

There is no reason to expect that we should be able to tell when this happens. Certainly, experimental psychology wasn't able to until several years after much-hyped studies more-or-less stopped replicating, despite a population that many people would have previously described as full of serious-minded empiricists. Many psychology researchers still won't admit that much of the past work needs to be revisited and potentially binned.

This is a problem of incentives, but I don't know how to make the incentives any better. As a blogger (albeit one who largely summarizes and connects ideas first broached by others), I can tell you that many of the people who blog do it because they can't <em>not</em> write. There's always going to be people competing to get their ideas heard and the people who most consistently provide satisfying insights will most often end up with more views.

Therefore, I suggest caution. We do not know how many true insights we should expect, so we cannot tell how likely to be true anything that feels insightful actually is. Against this, the best defense is highly developed scepticism. Always remember to ask for implications of new insights and to determine what information would falsify them. Always assume new insights have a low chance of being true. Notice when there seems to be a pressure to produce novel insights long after the low hanging fruit is gone and be wary of anyone in tat ecosystem.

We might not be able to change novelty culture, but we can do our best to guard against it.

<p class="caption pre-post-meta">
[Special thanks to <a href="https://medium.com/@cody.marie.wild">Cody Wild</a> for coming up with most of the lyrics to Bayesian Hallelujah.]
</p>
