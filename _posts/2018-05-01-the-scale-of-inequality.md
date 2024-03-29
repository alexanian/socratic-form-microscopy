---
id: 746
title: The Scale of Inequality
date: 2018-05-01T01:17:17-04:00
author: Zach Jacobi
author_link: https://socratic-form-microscopy.com/about-me
layout: post
guid: https://socratic-form-microscopy.com/?p=746
permalink: /2018/05/01/the-scale-of-inequality/
inline_featured_image:
  - "0"
categories:
  - Data Science
  - Economics
  - Falsifiable
tags:
  - inequality
  - overview
  - zach does analysis
---

When dealing with questions of inequality, I often get boggled by the sheer size of the numbers. People aren't very good at intuitively parsing the difference between a million and a billion. Our brains round both to "very large". I'm actually in a position where I get reminded of this fairly often, as the difference can become stark when programming. Running a program on a million points of data takes scant seconds. Running the same set of operations on a billion data points can take more than an hour. A million seconds is eleven and a half days. A billion seconds 31 years.

Here I would like to try to give a sense of the relative scale of various concepts in inequality. Just how much wealth do the wealthiest people in the world possess compared to the rest? How much of the world's middle class is concentrated in just a few wealthy nations? How long might it take developing nations to catch up with developed nations? How long before there exists enough wealth in the world that everyone could be rich if we just distributed it more fairly?

According to the <a href="https://en.wikipedia.org/wiki/The_World's_Billionaires#2018">Forbes billionaire list</a>, there are (as of the time of writing) 2,208 billionaires in the world, who collectively control $9.1 trillion in wealth (1 trillion seconds ago was the year 29691 BCE, contemporaneous with the oldest cave paintings in Europe). This is 3.25% of the total global wealth of <a href="https://www.cnbc.com/2017/11/14/richest-1-percent-now-own-half-the-worlds-wealth.html">$280 trillion</a>.

The US Federal Budget for 2019 is <a href="https://www.thebalance.com/u-s-federal-budget-breakdown-3305789">$4.4 trillion</a>. State governments and local governments each spend another <a href="https://www.usgovernmentspending.com/total">$1.9 trillion</a>. Some $700 billion dollars is given to those governments by the Federal government. With that subtracted, total US government spending is projected to be $7.5 trillion next year.

Therefore, the whole world population of billionaires holds assets equivalent to 1.2 years of US government outlays. Note that US government outlays aren't equivalent to that money being destroyed. It goes to pay salaries or buy equipment. The comparison here is simply to illustrate how private wealth stacks up against the budgets that governments control.

If we go down by a factor of 1000, there are about 15 million millionaires in the world (according to <a href="https://en.wikipedia.org/wiki/Millionaire#HNWI_population">Wikipedia</a>). Millionaires collectively hold $37.1 trillion (13.25% of all global wealth). All of the wealth that millionaires hold would be enough to fund US government spending for five years.

When we see sensational headlines, like "<a href="https://www.cnbc.com/2017/11/14/richest-1-percent-now-own-half-the-worlds-wealth.html">Richest 1% now owns half the world's wealth</a>", we tend to think that we're talking about millionaires and billionaires. In fact, millionaires and billionaires only own about 16.5% of the world's wealth (which is still a lot for 0.2% of the world's population to hold). The rest is owned by less wealthy individuals. The global 1% makes <a href="https://www.investopedia.com/articles/personal-finance/050615/are-you-top-one-percent-world.asp">$32,400</a> a year or more. This is virtually identical to the <a href="https://fred.stlouisfed.org/series/MEPAINUSA672N">median American yearly salary</a>. This means that almost fully half of Americans are in the global 1%. Canadians now have a <a href="http://www.statcan.gc.ca/tables-tableaux/sum-som/l01/cst01/famil105a-eng.htm">similar median wage</a>, which means a similar number are in the global 1%.

To give a sense of how this distorts the global middle class, I used <a href="http://iresearch.worldbank.org/PovcalNet/povOnDemand.aspx">Povcal.net</a>, the World Bank's online tool for poverty measurement. I looked for the percentage of a country's population making between 75% and 125% of the median US income (at <a href="https://www.investopedia.com/updates/purchasing-power-parity-ppp/">purchasing power parity,</a> which takes into account cheaper goods and services in developing countries), equivalent to $64-$107US per day (which is what you get when you divide 75% and 125% of the median US wage by 365 – as far as I can tell, this is the procedure that gives us numbers like $1.25 per day income as the threshold for absolute poverty).

I grabbed what I thought would be an interesting set of countries: The <a href="https://en.wikipedia.org/wiki/Group_of_Eight">G8</a>, <a href="https://en.wikipedia.org/wiki/BRICS">BRICS</a>, <a href="https://en.wikipedia.org/wiki/Next_Eleven">The Next 11</a>, Australia, Botswana, Chile, Spain, and Ukraine. These 28 countries had – in the years surveyed – a combined population of 5.3 billion people and had among them the 17 largest economies in the world (in nominal terms). You can see my spreadsheet collecting this data <a href="https://docs.google.com/spreadsheets/d/1b6dSdhZDGc4rNsxTtDTnyrd8SOsqOkBWdumgm1WXwL8/edit?usp=sharing">here</a>.

The United States had by far the largest estimated middle class (73 million people), followed by Germany (17 million), Japan (12 million), France (12 million), and the United Kingdom (10 million). Canada came next with 8 million, beating most larger countries, including Brazil, Italy, Korea, Spain, Russia, China, and India. Iran and Mexico have largely similar middle-class sizes, despite Mexico being substantially larger. Botswana ended up having a larger middle class than the Ukraine.

This speaks to a couple of problems when looking at inequality. First, living standards (and therefore class distinctions) are incredibly variable from country to country. A standard of living that is considered middle class in North America might not be the same in Europe or <a href="http://www.themoneyillusion.com/japan-is-in-the-details/">Japan</a>. In fact, I've frequently heard it said that the North American middle class (particularly Americans and Canadians) consume more than their equivalents in Europe. Therefore, this should be looked at as a comparison of <em>North American </em>equivalent middle class – who, as I've already said, are about 50% encompassed in the global 1%.

Second, we tend to think of countries in Europe as generally wealthier than countries in Africa. This isn't necessarily true. Botswana's GDP per capita is actually three times larger than Ukraine's when unadjusted and more than twice as large at purchasing power parity (which takes into account price differences between countries). It also has a higher GDP per capita than Serbia, Albania, and Moldova (even at purchasing power parity). Botswana, Seychelles, and Gabon have per capita GDPs at purchasing power parity that aren't dissimilar from those possessed by some less developed European countries.

Botswana, Gabon, and Seychelles have all been distinguished by relatively high rates of growth since decolonization, which has by now made them "middle income" countries. Botswana's growth has been so powerful and sustained that in my spreadsheet, it has a marginally larger North American equivalent middle class than Nigeria, a country approximately 80 times larger than it.

Of all the listed countries, Canada had the largest middle class as a percent of its population. This no doubt comes partially from using North American middle-class standards (and perhaps also because of the omission of the small, homogenous Nordic countries), although it is also notable that Canada <a href="https://www.nytimes.com/2014/04/23/upshot/the-american-middle-class-is-no-longer-the-worlds-richest.html">has the highest median income of major countries</a> (although this might be tied with the United States) and the highest 40<sup>th</sup> percentile income. America dominates income for people in the 60<sup>th</sup> percentile and above, while Norway comes out ahead for people in the 30<sup>th</sup> percentile or below.

The total population of the (North American equivalent) middle class in these 28 countries was 170 million, which represents about 3% of their combined population.

There is a staggering difference in consumption between wealthy countries and poor countries, in part driven by the staggering difference in the size of middle (and higher classes) – people with income to spend on things beyond immediate survival. According to Trading Economics, the total <a href="https://tradingeconomics.com/china/disposable-personal-income">disposable income of China</a> is $7.84 trillion (dollars are US). <a href="https://tradingeconomics.com/india/disposable-personal-income">India</a> has $2.53 trillion. <a href="https://tradingeconomics.com/canada/disposable-personal-income">Canada</a>, with a population almost 40 times smaller than either, has a total disposable income of $0.96 trillion, while <a href="https://tradingeconomics.com/united-states/disposable-personal-income">America</a>, with a population about four times smaller than either China or India has a disposable income of $14.79 trillion, larger than China and India put together. If China was as wealthy as Canada, its yearly disposable income would be almost $300 trillion, approximately equivalent to the total amount of wealth <em>in the world</em>.

According to Wikipedia, The Central African Republic has the world's lowest GDP per capita at purchasing power parity, making it a good candidate for the title of "world's poorest country". Using Povcal, I was able to estimate the median wage at $1.33 per day (or $485 US per year). If the Central African Republic grew at the same rate as Botswana did post-independence (approximately 8% year on year) starting in 2008 (the last year for which I had data) and these gains were seen in the median wage, it would take until 2139 for it to attain the same median wage as the US currently enjoys. This of course ignores development aid, which could speed up the process.

All of the wealth currently in the world is equivalent to $36,000 per person (although this is misleading, because much of the world's wealth is illiquid – it's in houses and factories and cars). All of the wealth currently on the <a href="https://en.wikipedia.org/wiki/Toronto_Stock_Exchange">TSX</a> is equivalent to about $60,000 per Canadian. All of the wealth currently on the <a href="https://en.wikipedia.org/wiki/New_York_Stock_Exchange">NYSE</a> is equivalent to about $65,000 per American. In just corporate shares alone, Canada and the US are almost twice as wealthy as the global average. This doesn't even get into the cars, houses, and other resources that people own in those countries.

If total global wealth were to grow at the same rate as the <a href="http://www.simplestockinvesting.com/SP500-historical-real-total-returns.htm">market</a>, we might expect to have approximately $1,000,000 per person (not inflation adjusted) sometime between 2066 and 2072, depending on population growth. If we factor in inflation and want there to be approximately $1,000,000 per person in present dollars, it will instead take until sometime between 2102 and 2111.

This assumes too much, of course. But it gives you a sense of how much we have right now and how long it will take to have – as some people incorrectly believe we already do – enough that everyone could (in a fair world) have so much they might never need to work.

This is not of course, to say, that things are fair today. It remains true that the median Canadian or American makes more money every year than 99% of the world, and that the wealth possessed by those median Canadians or Americans and those above them is equivalent to that held by the bottom 50% of the world. Many of us, very many of those reading this perhaps, are the 1%.

That's the reality of inequality.
