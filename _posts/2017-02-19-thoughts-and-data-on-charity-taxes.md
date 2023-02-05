---
id: 285
title: "Thoughts (and Data) on Charity &#038; Taxes"
date: 2017-02-19T22:52:17-05:00
author: Zach Jacobi
author_link: https://socratic-form-microscopy.com/about-me
layout: post
guid: http://socratic-form-microscopy.com/?p=285
permalink: /2017/02/19/thoughts-and-data-on-charity-taxes/
inline_featured_image:
  - "0"
categories:
  - Data Science
  - Politics
tags:
  - charity
  - tax policy zzz
---

The other day, I posed a question to my friends on Facebook:

<blockquote>Do you think countries with higher taxes see more charitable donations or fewer charitable donations? What sort of correlation would you expect between the two (weak positive? weak negative? strong positive? strong negative?).

I just crunched some numbers and I'll post them later. First I want to give people a chance to guess and test their calibration.</blockquote>
I was doing research for a future blog post on libertarianism and wanted to check one of the fundamental assumptions that many libertarians make: in the absence of a government, private charity would provide many of the same social services that are currently provided by the government.

<!--more-->

I honestly wasn't sure what I'd find. But I was curious to see what people would suggest.

Answers fell into four main camps:

<ol>
 	<li>Charitable giving and support for a welfare state might be caused by the same thing, so there will be a weak positive correlation.</li>
 	<li>Tax incentives for charitable donations shift the utility of donating, such that people in higher tax countries will donate more, as they get more utility per dollar spent (they get the same good feelings from charity, but also receive a bigger rebate come tax time). People who thought up this mechanism predicted a weak positive correlation.</li>
 	<li>This whole thing will be hopeless confounded by other variables and no conclusion would survive proper controls.</li>
 	<li>Libertarians are right. Taxes drain money that would go to private charity, so we should see a strong(ish) negative correlation.</li>
</ol>
I was surprised (but probably shouldn't have been) to find that these tracked people's political views. The more libertarian I thought someone was, the more likely they were to believe in a negative correlation. Meanwhile, people who were really into the welfare state tended to assume that charitable donations and taxes would be correlated.

In order to figure out who was right, I grabbed the most recent <a href="https://www.cafonline.org/docs/default-source/about-us-publications/1950a_wgi_2016_report_web_v2_241016.pdf?sfvrsn=4">World Giving Index</a> and correlated it with data about <a href="http://www.tradingeconomics.com/country-list/sales-tax-rate">personal income tax levels</a> (and <a href="http://www.tradingeconomics.com/country-list/sales-tax-rate">sales tax levels</a>, just to see what happened).

There are a number of flaws with this analysis. I'm not looking for confounding variables. Like at all. When it comes to things as tied to national character as charity and taxes (and how they interact!), this is a serious error in the analysis. I'm also using pretty poor metrics. It would be best to compare something like average tax rate with charitable donation amount per capita. Unfortunately, I couldn't find any good repositories of this data and didn't want to spend the hours it would take to build a really solid database of my own.

I decided to restrict my analysis to OECD countries (minus Turkey, which I was missing data on). You'll have to take my word that I made this decision before I saw any of the data (it turns out that there is essentially no correlation between income tax rate and percent of people who donate to charity when looking at all countries where I have data for both).

Caveats aside, what did I see?

There was a weak correlation (I'm using a simple Pearson correlation, as implemented by Google sheets here, nothing fancy) between the percentage of a population that engaged in charitable giving and the highest income tax bracket in a country. There was a weaker, negative correlation between sales tax and the percent of a population that engaged in charitable giving, but more than 60% of this came from the anchoring effect of the USA, with its relatively high charitable giving and lack of Federal sales tax. The correlation with income tax rates wasn't similarly vulnerable to removing the United States (in fact, it jumped up by about 12% when they were removed).

Here's the graphs. I've deliberately omitted trend lines because I'm a strong believer in <a href="https://xkcd.com/1725/">the constellation test</a>.

<img class="alignnone size-full wp-image-287" src="{{ site.baseurl }}/wp-content/uploads/income-tax.png" alt="" width="600" height="371" />

&nbsp;

<img class="alignnone size-full wp-image-286" src="{{ site.baseurl }}/wp-content/uploads/sales-tax-and-charity.png" alt="" width="600" height="371" />

All the data available is in a <a href="https://docs.google.com/spreadsheets/d/16bouNaKvdREBWpNXoVSonBnpAdguuGT1oFqMjN_KKgw/edit?usp=sharing">publicly viewable Google Sheet</a>.

I don't think these data give a particularly clear answer about the likelihood of private charity replacing government sponsored welfare programs in a hypothetical libertarian state. But they do suggest to me that the burden of proof should probably rest on libertarians. These results should make you view any claims that charitable giving is held back by the government with skepticism, but it should by no means prevent you from being convinced by good evidence.

I am happy to see that my results largely line up with better academic studies (as reported by the <a href="https://www.wsj.com/articles/the-surprising-relationship-between-taxes-and-charitable-giving-1450062191">WSJ</a>). It seems that if we look at the past few decades, decreasing the tax rates in the highest income brackets have been associated with decreasing charitable giving, at least in the United States. Whether this represents a correlated increase in selfishness, or fewer individuals donating as the utility of donating decreases is difficult to know.

The WSJ article also mentions that government grants to a charity reduce private donation by about 75% of the grant amount. I don't know if this represents donations that are lost entirely, or merely substituted for other (presumably needier) charities. If it's the first, then this would be strong evidence for the libertarian perspective. If it's the latter, then it means that many people intuitively understand and accept the key effective altruism concept of "<a href="https://en.wikipedia.org/wiki/Room_for_more_funding">room for more funding</a>", at least as far as the government is concerned.

<h5>Conclusions</h5>
Finding good answers to the question of whether private charity would replace government welfare turned out to be harder than I thought. The main problem was the quality of data that is easily available. While it was easy to find statistics good enough for a simple, limited analysis, I wasn't able to find a convenient table with all of the data I needed. This is where actual researchers have a huge advantage over random people on the internet. They have access to cheap labour in the volumes necessary to find and tabulate high quality data.

I'm very glad I posed the question to my friends before figuring out the answer. It never occurred to me to consider the effect of tax incentives on charitable giving. I'm now of the weakly held opinion that the main way taxes affect charitable donations is by offsetting the costs with rebates. I'm also fascinated by the extent to which people's guesses tracked their political leanings. This shows that (on my Facebook wall, at least) people hold opinions that are motivated by a genuine desire to see the most effective possible government. Differing axioms and exposure to different data lead to differing conceptions of what this would be, but everyone is ultimately on the same team.

I will try and remember this next time I think someone's preferred government policy is a terrible idea. It's probably much more productive to try and figure out why they believe their policy objectives will lead to the best outcomes and arguing about that, rather than slipping into clichéd insults.

I was also reminded that it's fun and rewarding to spend a few hours doing data analysis (especially when you get the same results as studies that get reported on in the WSJ).

<hr class="post-end" />
