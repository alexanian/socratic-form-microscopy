---
id: 605
title: 'Two Ideas Worth Sharing From &#8216;Weapons of Math Destruction&#8217;'
date: 2017-11-22T20:29:34-05:00
author: Zach
layout: post
guid: https://socratic-form-microscopy.com/?p=605
permalink: /2017/11/22/two-ideas-worth-sharing-from-weapons-of-math-destruction/
inline_featured_image:
  - "0"
categories:
  - Data Science
  - Literature
  - Model
tags:
  - book review
  - MY HONOUR
---
<a href="https://socratic-form-microscopy.com/2017/11/19/two-fallacies-from-weapons-of-math-destruction/">Recently</a>, I talked about what I didn't like in Dr. Cathy O'Neil's book, <em>Weapons of Math Destruction</em>. This time around, I'd like to mention two parts of it I really liked. I wish Dr. O'Neil put more effort into naming the concepts she covered; I don't have names for them from <em>WMD</em>, but in my head, I've been calling them <em>Hidden Value Encodings</em> and <em>Axiomatic Judgements</em>.
<h1>Hidden Value Encodings</h1>
Dr. O'Neil opens the book with a description of the model she uses to cook for her family. After going into a lot of detail about it, she makes this excellent observation:
<blockquote>Here we see that models, despite their reputation for impartiality, reflect goals and ideology. When I removed the possibility of eating Pop-Tarts at every meal, I was imposing my ideology on the meals model. It’s something we do without a second thought. Our own values and desires influence our choices, from the data we choose to collect to the questions we ask. Models are opinions embedded in mathematics.</blockquote>
It is far too easy to view models as entirely empirical, as math made form and therefore blind to values judgements. But that couldn't be further from the truth. It's value judgements all the way down.

Imagine a model that tries to determine when a credit card transaction is fraudulent. Fraudulent credit cards transactions cost the credit card company money, because they must refund the stolen amount to the customer. Incorrectly identifying credit card transactions also costs a company money, either through customer support time, or if the customer gets so fed up by constant false positives that they switch to a different credit card provider.

If you were tasked with building a model to predict which credit card transactions were fraudulent by one of the major credit card companies, you would probably build into your model a variable cost for failing to catch fraudulent transactions (equivalent to the cost the company must bear if the transaction is fraudulent) and a fixed cost for labelling innocuous transactions as fraudulent (equivalent to the average cost of a customer support call plus the average chance of a false positive pushing someone over the edge into switching cards multiplied by the cost of their lost business over the next few years).

From this encoding, we can already see that our model would want to automatically approve all transactions below the fixed cost of dealing with false positives <a href="#til-bot-1" id="til-top-1">[1]</a>, while applying increasing scrutiny to more expensive items, especially expensive items with big resale value or items more expensive than the cardholder normally buys (as both of these point strongly toward fraud).

This seems innocuous and logical. It is also encoding <em>at least two</em> sets of values. First, it encodes the values associated with capitalism. At the most basic level, this algorithm "believes" that profit is good and losses are bad. It is aimed to maximize profit for the bank and while we may hold this as a default assumption for most algorithms associated with companies, that does not mean it is devoid of values; instead it encodes all of the values associated with capitalism <a href="#til-bot-2" id="til-top-2">[2]</a>. Second, the algorithm encodes some notion that <em>customers have freedom to choose between alternatives </em>(even more so than is encoded by default in accepting capitalism).

By applying a cost to false positives (and likely it would be a cost that rises with each previous false positive), you are tacitly acknowledging that customers could take their business elsewhere. If customers instead had no freedom to choose who they did business with, you could merely encode as your loss from false positives the fixed cost of fielding support calls. Since outsourced phone support is very cheap, your algorithm would care much less about false positives if there was no consumer choice.

As far as I can tell, there is no "value-free" place to stand. An algorithm in the service of a hospital that helps diagnose patients or focus resources on the most ill encodes the value that "it is better to be healthy than sick; better to be alive than dead". These values might be (<a href="https://en.wikipedia.org/wiki/Negative_utilitarianism#The_benevolent_world-exploder">almost-</a>)universal, but they still exist, they are still encoded, and they still deserve to be interrogated when we put functions of our society in the hands of software governed by them.
<h1>Axiomatic Judgements</h1>
One of the most annoying parts of being a child is the occasional requirement to accept an imposition on your time or preferences with the explanation "because I say so". "Because I say so" isn't an argument, it's a request that you acknowledge adults' overwhelming physical, earning, and social power as giving them a right to set arbitrary rules for you. Some algorithms, forced onto unwelcoming and less powerful populations (teachers, job-seekers, etc.) have adopted this MO as well. Instead of having to prove that they have beneficial effects or that their outputs are legitimate, they define things such that their outputs are always correct and brook no criticism.

Here's Dr. O'Neil talking about a value-added teaching model in Washington State:
<blockquote>When Mathematica’s scoring system tags Sarah Wysocki and 205 other teachers as failures, the district fires them. But how does it ever learn if it was right? It doesn’t. The system itself has determined that they were failures, and that is how they are viewed. Two hundred and six “bad” teachers are gone. That fact alone appears to demonstrate how effective the value-added model is. It is cleansing the district of underperforming teachers. Instead of searching for the truth, the score comes to embody it.</blockquote>
She contrasts this with how Amazon operates: "if Amazon.​com, through a faulty correlation, started recommending lawn care books to teenage girls, the clicks would plummet, and the algorithm would be tweaked until it got it right." On the other hand, the teacher rating algorithm doesn't update, doesn't look check if it is firing good teachers, and doesn't take an accounting of its own costs. It holds it as axiomatic ­–a basic fact beyond questioning– that its results are the right results.

I am in full agreement with Dr. O'Neil's criticism here. Not only does it push past the bounds of fairness to make important decisions, like hiring and firing, through opaque formulae that are not explained to those who are being judged and lack basic accountability, but it's a professional black mark on all of the statisticians involved.

Whenever you train a model, you hold some data back. This is your test data and you will use it to assess how well your model did. That gets you through to "production" – to having your model out in the field. This is an exciting milestone, not only because your model is now making decisions and (hopefully) making them well, but because now you'll have way more data. You can see how your new fraud detection algorithm does by the volume of payouts and customer support calls. You can see how your new leak detection algorithm does by customers replying to your emails and telling you if you got it right or not.

A friend of mine who worked in FinTech once told me that they approved 1.5% of everyone who applied for their financial product, no matter what. They'd keep the score their model gave to that person on record, then see how the person fared in reality. If they used the product responsibly despite a low score, or used it recklessly despite a high score, it was viewed as valuable information that helped the team make their model that much better. I can imagine a team of data scientists, heads together around a monitor, looking through features and asking each other "huh, do <em>any</em> of you see what we missed here?" and it’s a pleasant image <a href="#til-bot-3" id="til-top-3">[3]</a>.

Value added teaching models, or psychological pre-screens for hiring do nothing of the sort (even though it would be trivial for them to!). They give results and those results are <em>defined</em> as the ground truth. There's no room for messy reality to work its way back into the cycle. There's no room for the creators to learn. The algorithm will be flawed and imperfect, like all products of human hands. That is inevitable. But it will be far less perfect than it could be. Absent feedback, it is doomed to always be flawed, in ways both subtle and gross, and in ways unknown to its creators and victims.

Like most Canadian engineering students, I made a solemn vow:
<blockquote>…in the presence of these my betters and my equals in my calling, [I] bind myself upon my honour and cold iron, that, to the best of my knowledge and power, I will not henceforward suffer or pass, or be privy to the passing of, bad workmanship or faulty material in aught that concerns my works before mankind as an engineer…</blockquote>
Sloppy work, like that value-added teacher model is the very definition of bad workmanship. Would that I never suffer something like that to leave my hands and take life in the world! It is no <a href="https://en.wikipedia.org/wiki/Quebec_Bridge">Quebec Bridge</a>, but the value-added teaching model and other doomed to fail algorithms like it represent a slow-motion accident, steadily stealing jobs and happiness from people with no appeal or remorse.

I can accept stains on the honour of my chosen profession. Those are inevitable. But in a way, stains on our <em>competence</em> are so much worse. Models that take in no feedback are both, but the second <em>really</em> stings me.
<h1>Footnotes</h1>
<strong id="til-bot-1">[1]</strong> This first approximation isn't correct in practice, because certain patterns of small transactions are consistent with fraud. I found this out the hard way, when a certain Bitcoin exchange's credit card verification procedure (withdrawing less than a dollar, then refunding it a few days later, after you tell them how much they withdrew) triggered the fraud detection software at my bank. Apparently credit card thieves will often do a similar thing (minus the whole "ask the cardholder how much was withdrawn" step), as a means of checking if the card is good without cluing in the cardholder. <a href="#til-top-1">^</a>

<strong id="til-bot-2">[2]</strong> I don't mean this as a criticism of capitalism. I seek merely to point out (that like all other economic systems) capitalism is neither value neutral, nor inevitable. "Capitalism" encodes values like "people are largely rational", "people often act to maximize their gains" and "choice is fundamentally good and useful". <a href="#til-top-2">^</a>

If socialist banks had ever made it to the point of deploying algorithms (instead of collapsing under the weight of their flawed economic system), those algorithms would also encode values (like "people will work hard for the good of the whole" and "people are inherently altruistic" and "it is worth it to sacrifice efficiency in the name of fairness").

<strong id="til-bot-3">[3]</strong> Dulce et decorum est… get the fucking data science right. <a href="#til-top-3">^</a>