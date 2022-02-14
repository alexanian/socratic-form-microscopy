---
id: 596
title: "Two Fallacies From &#8216;Weapons of Math Destruction&#8217;"
date: 2017-11-19T11:26:09-05:00
author: Zach
layout: post
guid: https://socratic-form-microscopy.com/?p=596
permalink: /2017/11/19/two-fallacies-from-weapons-of-math-destruction/
inline_featured_image:
  - "0"
categories:
  - Data Science
  - Literature
  - Model
tags:
  - book review
---

<em>Much thanks to <a href="http://decodyng.com/">Cody Wild</a> for providing editing and feedback. That said, I would like to remind my readers that I deserve full credit for all errors and that all opinions expressed here are only guaranteed to be mine.</em>

<em>[12 minute read]</em>

I recently read <a href="https://www.goodreads.com/book/show/28186015-weapons-of-math-destruction">Weapons of Math Destruction by Dr. Cathy O'Neil</a> and found it an enormously frustrating book. It's not that whole book was rubbish ­– that would have made things easy. No, the real problem with this book is that the crap and the pearls were so closely mixed that I had to stare at every sentence very, <em>very</em> carefully in hopes of figuring out which one each was. There's some good stuff in here. But much of Dr. O'Neil's argumentation relies on two new (to me) fallacies. It's these fallacies (which I've dubbed the Ought-Is Fallacy and the Availability Bait-and-Switch) that I want to explore today.

<h1 id="ought-is">Ought-Is Fallacy</h1>
It's a commonly repeated truism that "correlation doesn't imply causation". People who've been around the statistics block a bit longer might <a href="https://xkcd.com/552/">echo Randall Monroe</a> and retort that "correlation doesn't imply causation, but it does waggle its eyebrows suggestively and gesture furtively while mouthing 'look over there'". Understanding why a graph like this:

[caption id="attachment_602" align="alignnone" width="768"]<img class="wp-image-602 size-medium_large" src="https://socratic-form-microscopy.com/wp-content/uploads/obviously_anchoring_OMFG-768x580.png" alt="In addition to this graph obviously being anchored, using it is obviously fair use." width="768" height="580" /> Image Copyright <a href="https://www.nytimes.com/2017/11/07/world/americas/mass-shootings-us-international.html">The New York Times, 2017</a>. Used here for purposes of commentary and criticism.[/caption]

Is utter horsecrap <a id="wtf-top-1" href="#wtf-bot-1">[1]</a>, despite how suggestive it looks is the work of a decent education in statistics. Here correlation doesn't imply causation. On the other hand, it's not hard to find excellent examples where correlation really does mean causation:

[caption id="attachment_601" align="alignnone" width="768"]<img class="wp-image-601 size-medium_large" src="https://socratic-form-microscopy.com/wp-content/uploads/global-temp-and-co2-us-gov-768x582.gif" alt="This would be a risky graph to use if echo chambers didn't mean that I know literally no one who doesn't believe in global warming" width="768" height="582" /> Source: <a href="https://www.ncdc.noaa.gov/monitoring-references/faq/indicators.php">The National Centers for Environmental Administration</a>. Having to spell "centre" wrong and use inferior units is a small price to pay for the fact that the American government immediately releases everything it creates into the public domain.[/caption]

When trying to understand the ground truth, it's important that you don't confuse correlation with causation. But not every human endeavour is aimed at determining the ground truth. Some endeavours really do just need to understand which activities and results are correlated. Principal among these is insurance.

Let's say I wanted to sell you "punched in the face" insurance. You'd pay a small premium every month and if you were ever punched in the face hard enough to require dental work, I'd pay you enough to cover it <a id="wtf-top-2" href="#wtf-bot-2">[2]</a>. I'd probably charge you more if you were male, because men are much, much <a href="http://www.statcan.gc.ca/pub/85f0033m/2010024/part-partie1-eng.htm#h2_8">more likely to be seriously injured in an assault than women are</a>.

I'm just interested in pricing my product. It doesn't actually matter if being a man is causal of more assaults or just correlated with it. It doesn't matter if men aren't inherently more likely to assault and be assaulted compared to women (for a biological definition of "inherently"). It doesn't matter what assault rates would be like in a society without toxic masculinity. One thing and one thing alone matters: on average, I will have to pay out more often for men. Therefore, I charge men more.

If you were to claim that because there may be nothing inherent in maleness that causes assault and being assaulted, therefore men shouldn't have to pay more, you are making a <em>moral</em> argument, not an empirical one. You are also committing the <em>ought-is fallacy</em>. Just because your beliefs tell you that some aspect of the world <em>should</em> be a certain way, or that it would be <em>more moral</em> for the world to be a certain way, does not mean the world <em>actually is</em> that way or that everyone must agree to order the world as if that were true.

This doesn't prevent you from making a moral argument that we should ignore certain correlates in certain cases in the interest of fairness, merely that you should not be making an empirical argument about what is ultimately values.

The ought-is fallacy came up literally whenever Weapons of Math Destruction talked about insurance, as well as when it talked about sentencing disparities. Here's one example:

<blockquote>But as the questions continue, delving deeper into the person’s life, it’s easy to imagine how inmates from a privileged background would answer one way and those from tough inner-city streets another. Ask a criminal who grew up in comfortable suburbs about “the first time you were ever involved with the police,” and he might not have a single incident to report other than the one that brought him to prison. Young black males, by contrast, are likely to have been stopped by police dozens of times, even when they’ve done nothing wrong. A 2013 study by the New York Civil Liberties Union found that while black and Latino males between the ages of fourteen and twenty-four made up only 4.7 percent of the city’s population, they accounted for 40.6 percent of the stop-and-frisk checks by police. More than 90 percent of those stopped were innocent. Some of the others might have been drinking underage or carrying a joint. And unlike most rich kids, they got in trouble for it. So if early “involvement” with the police signals recidivism, poor people and racial minorities look far riskier.</blockquote>
Now I happen to agree with Dr. O'Neil that we should not allow race to end up playing a role in prison sentence length. There are plenty of good things to include in a sentence length: seriousness of crime, remorse, etc. I don't think race should be one of these criteria and since the sequence of events that Dr. O'Neil mentions make this far from the default in the criminal justice system, I think doing more to ensure race stays out of sentencing is an important <em>moral</em> responsibility we have as a society.

But Dr. O'Neil's empirical criticism of recidivism models is entirely off base. In this specific example, she is claiming that some characteristics that correlate with recidivism should not be used in recidivism models <em>even though they improve the accuracy</em>, because they are not per se causative of crime.

Because of systematic racism and discrimination in policing <a id="wtf-top-3" href="#wtf-bot-3">[3]</a>, the recidivism rate among black Americans <em><a href="https://en.wikipedia.org/wiki/Recidivism#African_Americans_and_recidivism">is higher</a></em>. If <em>the only thing you care about</em> is maximizing the prison sentence of people who are most likely to re-offend, then your model <em>will</em> tag black people for longer sentences. <em>It does not matter what the "cause" of this is! Your accuracy will still be higher if you take race into account.</em>

To say "black Americans seem to have a higher rate of recidivism, therefore we should punish them more heavily" is almost to commit the opposite fallacy, the is-ought. Instead, we should say "yes, empirically there's a high rate of recidivism among black Americans, but this is probably caused by social factors and regardless, if we don't want to create a population of permanently incarcerated people, with all of the vicious cycle of discrimination that this creates, we should aim for racial parity in sentencing". This is a very strong (and I think persuasive) moral claim <a id="wtf-top-4" href="#wtf-bot-4">[4]</a>.

It certainly is more work to make a complicated moral claim that mentions the trade-offs we must make between punishment and fairness (or between what is morally right and what is expedient) than it is to make a claim that makes no reference to these subtleties. When we admit that we are sacrificing accuracy in the name of fairness, we do open up an avenue for people to attack us.

Despite this disadvantage, I think keeping our moral and empirical claims separate is very important. When you make the empirical claim that "being black isn't causative of higher rates of recidivism, therefore the models are wrong when they rank black Americans as more likely to reoffend", instead of the corresponding ethical claim, then you are making two mistakes. First, there's lots of room to quibble about what "causative" even means, beyond simple genetic causation. Because you took an empirical and not ethical position, you may have to fight any future evidence to the contrary of your empirical position, even if the evidence is true; in essence, you risk becoming an enemy of the truth. If the truth becomes particularly obvious (and contrary to your claims) you risk looking risible and any gains you achieved will be at risk of reversal.

Second, I would argue that it is ridiculous to claim that universal human rights must rest on claims of genetic identicalness between all groups of people (and trying to make the empirical claim above, rather than a moral claim implicitly embraces this premise). Ashkenazi Jews are (on average) <a href="http://web.mit.edu/fustflum/documents/papers/AshkenaziIQ.jbiosocsci.pdf">about 15 IQ points ahead of other groups</a>. Should we give them any different moral worth because of this? I would argue no <a id="wtf-top-5" href="#wtf-bot-5">[5]</a>. The only criteria for full moral worth as a human and all universal rights that all humans are entitled to is <em>being human</em>.

As genetic engineering becomes possible, it will be especially problematic to have a norm that moral worth of humans can be modified by their genetic predisposition to pro-social behaviour. Everyone, but most especially the left, which views diversity and flourishing as some of its most important projects should push back against both the is-ought and ought-is fallacies and fight for an expansive definition of universal human rights.

<h1>Availability Bait-and-Switch</h1>
Imagine someone told you the following story:
<blockquote>The <a href="https://en.wikipedia.org/wiki/Fair_Housing_Act">Fair Housing Act</a> has been an absolute disaster for my family! My brother was trying to sublet his apartment to a friend for the summer. Unfortunately, one of the fair housing inspectors caught wind of this and forced him to put up notices that it was for rent. He had to spend a week showing random people around it and some snot-nosed five-year-old broke one of his vases while he was showing that kid's mother around. I know there were problems before, but is the Fair Housing Act really worth it if it can cause this?</blockquote>
Most people would say the answer to the above is "yes, it <em>really was</em> worth it, oh my God, what is wrong with you?"

But it's actually hard to think that. Because you just read a long, vivid, easily imaginable example of what exactly was wrong with the current regime and a quick throw away reference to there being problems with the old way things were done. Some people might say that it's better to at least mention that the other way of doing things had its problems too. I disagree strenuously.

When you make a throw-away reference to problems with another way of doing things, while focusing all of your descriptive effort on the problems of the current way (or vice-versa), you are committing the <em>Availability Bait-and-Switch</em>. And you are giving a very false illusion of balance; people will remember that you mentioned both had problems, but <em>they will not take this away as their impression</em>. You will have tricked your readers into thinking you gave a balanced treatment (or at least paved the way for a defence against claims that you didn't give a balanced treatment) while doing nothing of the sort!

We are all running <a href="https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow">corrupted hardware</a>. One of the most notable cognitive biases we have is the <a href="https://en.wikipedia.org/wiki/Availability_heuristic">availability heuristic</a>. We judge probabilities based on what we can easily recall, not on any empirical basis. If you were asked "are there more words in the average English language book that start with k, or have k as the third letter?", you'd probably say "start with k!" <a id="wtf-top-6" href="#wtf-bot-6">[6]</a>. In fact, words with "k" as the third letter show up more often. But these words are harder to recall and therefore much less <em>available</em> to your brain.

If I were to give you a bunch of very vivid examples of how algorithms can ruin your life (as Dr. O'Neil repeatedly does, most egregiously in chapters 1, 5, and 8) and then mention off-hand that human decision making also used to ruin a lot of people's lives, you'd probably come out of our talk much more concerned with algorithms than with human decision making. This was a thing I had to deliberately fight against while reading Weapons of Math Destruction.

Because for a book about how algorithms are destroying everything, there was a remarkable paucity of <em>data</em> on this destruction. I cannot recall seeing any comparative analysis (backed up by statistics, not <em>anecdotes</em>) of the costs and benefits of human decision making and algorithmic decision making, as it applied to Dr. O'Neil's areas of focus. The book was all the costs of one and a vague allusion to the potential costs of the other.

If you want to give your readers an accurate snapshot of the ground truth, your examples must be representative of the ground truth. If algorithms cause twice as much damage as human decision making in certain circumstances (and again, I've seen <em>zero</em> proof that this is the case) then you should interleave every two examples of algorithmic destruction with one of human pettiness. As long as you aren't doing this, you are lying to your readers. If you're committed to lying, perhaps for reasons of pithiness or flow, then drop the vague allusions to the costs of the other way of doing things. Make it clear you're writing a hatchet job, instead of trying to claim epistemic virtue points for "telling both sides of the story". At least doing things that way is honest <a id="wtf-top-7" href="#wtf-bot-7">[7]</a>.

<h3>Footnotes:</h3>

<strong id="wtf-bot-1">[1]</strong> This is a classic example of "anchoring", a phenomenon where you appear to have a strong correlation in a certain direction because of a single extreme point. When you have anchoring, it's unclear how generalizable your conclusion is – as the whole direction of the fit could be the result of the single extreme point.

Here's a toy example:

<img class="alignnone wp-image-600 size-medium" src="https://socratic-form-microscopy.com/wp-content/uploads/anchored-300x288.png" alt="" width="300" height="288" /> <img class="alignnone wp-image-599 size-medium" src="https://socratic-form-microscopy.com/wp-content/uploads/not-anchored-300x288.png" alt="" width="300" height="288" />

Note that the thing that makes me suspicious of anchoring here is that we have a big hole with no data and no way of knowing what sort of data goes there (it's not likely we can randomly generate a bunch of new countries and plot their gun ownership and rate of mass shootings). If we did some more readings (ignoring the fact that in this case <em>we can't</em>) and got something like this:

<img class="alignnone wp-image-598 size-medium" src="https://socratic-form-microscopy.com/wp-content/uploads/also-not-anchored-300x288.png" alt="" width="300" height="288" />

I would no longer be worried about anchoring. It really isn't enough just to look at the correlation coefficient either. The image labelled "Also Not Anchored" has a marginally lower correlation coefficient than the anchored image, even though (I would argue) it is FAR more likely to represent a true positive correlation. Note also we have no way to tell that more data will necessarily give us a graph like the third. We could also get something like this:

<img class="alignnone wp-image-597 size-medium" src="https://socratic-form-microscopy.com/wp-content/uploads/outlier-300x288.png" alt="" width="300" height="288" />

In which we have a fairly clear trend of noisy data with an average of 2.5 irrespective of our x-value and a pair of outliers driving a slight positive correlation.

Also, the NYT graph isn't normalized to population, which is kind of a WTF level mistake. They include another graph that is normalized later on, but the graph I show is the preview image on Facebook. I was very annoyed with the smug liberals in the comments of the NYT article, crowing about how conservatives are too stupid to understand statistics. But that's a rant for another day…  <a href="#wtf-top-1">^</a>

<strong id="wtf-bot-2">[2]</strong> I'd very quickly go out of business because of the <a href="https://en.wikipedia.org/wiki/Moral_hazard">moral hazard</a> and <a href="https://www.investopedia.com/terms/a/adverseselection.asp">adverse selection</a> built into this product, but that isn't germane to the example. <a href="#wtf-top-2">^</a>

<strong id="wtf-bot-3">[3]</strong> Or at least, this is my guess as to the most plausible factors in the recidivism rate discrepancy. I think social factors ­– especially when social gaps are so clear and pervasive – seem much more likely than biological ones. The simplest example of the disparity in policing – and its effects – is the relative rates of being stopped by police during <em>Stop and Frisk</em> given above by Dr. O'Neil. <a href="#wtf-top-3">^</a>

<strong id="wtf-bot-4">[4]</strong> It's possible that variations in <a href="https://en.wikipedia.org/wiki/Monoamine_oxidase_A">Monoamine oxidase A</a> or some other gene amongst populations might make some populations more predisposed (in a biological sense) to violence or other antisocial behaviour. Given that violence and antisocial behaviour are relatively uncommon (e.g. <a href="https://www.statcan.gc.ca/pub/85-002-x/2015001/article/14163-eng.htm">about six in every one thousand Canadian adults</a> are incarcerated or under community supervision on any given day), any genetic effect that increases them would both be small on a social level and lead to a relatively large skew in terms of supervised populations.

This would occur in the same way that repeat offenders tend to be about one standard deviation below median societal IQ but the correlation between IQ and crime explains very little of the variation in crime. This effect exists <em><a href="http://slatestarcodex.com/2015/05/19/beware-summary-statistics/">because crime is so rare</a></em>.

It is unfortunately easy for people to take things like "Group X is 5% more likely to be violent", and believe that people in Group X are something like 5% likely to assault them. This obviously isn't true. Given that <a href="http://www.statcan.gc.ca/pub/85f0033m/2010024/part-partie1-eng.htm#h2_8">there are about 7.5 assaults for every 1000 Canadians</a> each year, a population that was instead 100% Group X (with their presumed 5% higher assault rate) would see about 7.875 assaults per 1000 people, a difference of about one additional assault per 3500 people.

Unfortunately, if society took its normal course, we could expect to see Group X very overrepresented in prison. As soon as Group X gets a reputation for violence, juries would be more likely to convict, bail would be less likely, sentences might be longer (out of fear of recidivism), etc. Because many jobs (and in America, social benefits and rights) are withdrawn after you've been sentenced to jail, formerly incarcerated members of Group X would see fewer legal avenues to make a living. This could become even worse if even <em>non-criminal members</em> of Group X would denied some jobs due to fear of future criminality, leaving Group X members with few overall options but the black and grey economies and further tightening the spiral of incarceration and discrimination.

In this case, I think the moral thing to do <em>as a society</em> is to ignore any evidence we have about between-group differences in genetic propensities to violence. Ignoring results isn't the same thing as pretending they are false or banning research; we aren't fighting against truth, simply saying that some small extra predictive power into violence <em>is not worth the social cost that Group X would face in a society that is entirely unable to productively reason about statistics. </em> <a href="#wtf-top-4">^</a>

<strong id="wtf-bot-5">[5]</strong> Although we <em>should</em> be ever vigilant against people who seek to do the opposite and use genetic differences between Ashkenazi Jews and other populations as a basis for their Nazi ideology. As Hannah Arendt said, the Holocaust was a crime against humanity perpetrated on the body of the Jewish people. It was a crime against humanity (rather than "merely" a crime against Jews) <em>because Jews are human. <a href="#wtf-top-5">^</a></em>

<strong id="wtf-bot-6">[6]</strong> Or at least, you would if I hadn't warned you that I was about to talk about biases. <a href="#wtf-top-6">^</a>

<strong id="wtf-bot-7">[7]</strong> My next blog post is going to be devoted to what I <em>did</em> like about the book, because I don't want to commit the mistakes I've just railed against (and because I think there was some good stuff in the book that bears reviewing). <a href="#wtf-top-7">^</a>
