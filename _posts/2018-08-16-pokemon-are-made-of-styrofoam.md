---
id: 830
title: Pokémon Are Made of Styrofoam
date: 2018-08-16T08:30:42-04:00
author: Zach
layout: post
guid: https://socratic-form-microscopy.com/?p=830
permalink: /2018/08/16/pokemon-are-made-of-styrofoam/
inline_featured_image:
  - "0"
categories:
  - Falsifiable
  - Physics
  - Quick Fix
tags:
  - engineering
  - i apparently give writing advice now
  - silly
  - someone else probably came up with this first
  - zach does analysis
---

One of the best things about taking physics classes is that the equations you learn are directly applicable to the real world. Every so often, while reading a book or watching a movie, I'm seized by the sudden urge to check it for plausibility. A few scratches on a piece of paper later and I will generally know one way or the other.

One of the most amusing things I've found doing this is that the people who come up with the statistics for Pokémon definitely don't have any sort of education in physics.

Takes Onix. Onix is a rock/ground Pokémon renowned for its large size and sturdiness. Its physical statistics reflect this. It's 8.8 metres (28') long and 210kg (463lbs).

{% capture caption %}
Onix, being tough. I don't own the copyright to this image, but I'm claiming fair use for purpose of criticism. <a href="https://giphy.com/gifs/team-rocket-onix-see-you-in-the-next-episode-Hw3Txd9N17uxi">Source</a>.
{% endcapture %}
{% include image.html src="/wp-content/uploads/blasting_off.gif" alt="" caption=caption %}

Surely such a large and tough Pokémon should be very, very dense, right? Density is such an important tactile cue for us. Don't believe me? Pick up a large piece of solid medal. Its surprising weight will make you take it seriously.

Let's check if Onix would be taken seriously, shall we? Density is equal to mass divided by volume. We use the symbol ρ to represent density, which gives us the following equation:

<img class="size-full wp-image-834 aligncenter" src="/wp-content/uploads/rho-m-over-v.png" alt="" width="104" height="70" />

We already know Onix's mass. Now we just need to calculate its volume. Luckily Onix is pretty cylindrical, so we can approximate it with a cylinder. The equation for the volume of a cylinder is pretty simple:

<img class="size-full wp-image-833 aligncenter" src="/wp-content/uploads/v-pi-r-squared-h.png" alt="" width="153" height="58" />

Where <em>π</em> is the ratio between the diameter of a circle and its circumference (approximately 3.1415…, <a href="https://en.wikipedia.org/wiki/Indiana_Pi_Bill">no matter what Indiana says</a>), <em>r</em> is the radius of a circle (always one half the diameter), and h is the height of the cylinder.

Given that we know Onix's height, we just need its diameter. Luckily the Pokémon TV show gives us a sense of scale.

{% capture caption %}
Here's a picture of Onix. Note the kid next to it for scale. I don't own the copyright to this image, but I'm claiming fair use for purpose of criticism. <a href="http://pokemon.wikia.com/wiki/Roark%27s_Onix_(anime)?file=Roark_Onix.png">Source</a>.
{% endcapture %}
{% include image.html src="/wp-content/uploads/Roark_Onix-768x576.png" alt="" caption=caption %}

Judging by the image, Onix probably has an average diameter somewhere around a metre (3 feet for the Americans). This means Onix has a radius of 0.5 metres and a height of 8.8 metres. When we put these into our equation, we get:

<img class="size-full wp-image-832 aligncenter" src="/wp-content/uploads/v-sub-onix.png" alt="" width="300" height="78" />

For a volume of approximately 6.9m<sup>3</sup>. To get a comparison I turned to <a href="http://www.wolframalpha.com/input/?i=pi+*+(0.5m)%5E2+*+8.8m">Wolfram Alpha</a> which told me that this is about 40% of the volume of a gray whale or a freight container (which incidentally implies that gray whales are about the size of standard freight containers).

Armed with a volume, we can calculate a density.

<img class="size-full wp-image-831 aligncenter" src="/wp-content/uploads/rho-onix.png" alt="" width="295" height="105" />

Okay, so we know that Onix is 30.4 kg/m<sup>3</sup>, but what does that mean?

Well it's currently hard to compare. I'm much more used to seeing densities of sturdy materials expressed in tonnes per cubic metre or grams per cubic centimetre than I am seeing them expressed in kilograms per cubic metre. Luckily, it's easy to convert between these.

There are 1000 kilograms in a ton. If we divide our density by a thousand we can calculate a new density for Onix of 0.0304t/m<sup>3</sup>.

How does this fit in with common materials, like wood, Styrofoam, water, stone, and metal?

<table id="pkm-table-1">
<tbody>
<tr>
<td width="77">
<p style="text-align: center;"><strong>Material</strong></p>
</td>
<td style="text-align: center;" width="94"><strong>Density (t/m<sup>3</sup>)</strong></td>
</tr>
<tr>
<td width="77">
<p style="text-align: center;"><a href="https://en.wikipedia.org/wiki/Polystyrene#Extruded_polystyrene_foam">Styrofoam</a></p>
</td>
<td width="94">
<p style="text-align: center;">0.028</p>
</td>
</tr>
<tr>
<td width="77">
<p style="text-align: center;">Onix</p>
</td>
<td width="94">
<p style="text-align: center;">0.03</p>
</td>
</tr>
<tr>
<td width="77">
<p style="text-align: center;"><a href="http://www.wolframalpha.com/input/?i=density+of+balsa+wood">Balsa</a></p>
</td>
<td style="text-align: center;" width="94">
<p style="text-align: center;">0.16</p>
</td>
</tr>
<tr>
<td style="text-align: center;" width="77"><a href="http://www.wolframalpha.com/input/?i=density+of+oak">Oak</a>[^1]</td>
<td width="94">
<p style="text-align: center;">0.65</p>
</td>
</tr>
<tr>
<td style="text-align: center;" width="77">Water</td>
<td width="94">
<p style="text-align: center;">1</p>
</td>
</tr>
<tr>
<td width="77">
<p style="text-align: center;"><a href="http://www.wolframalpha.com/input/?i=density+of+granite">Granite</a></p>
</td>
<td width="94">
<p style="text-align: center;">2.6</p>
</td>
</tr>
<tr>
<td style="text-align: center;" width="77"><a href="http://www.wolframalpha.com/input/?i=density+of+steel">Steel</a></td>
<td width="94">
<p style="text-align: center;">7.9</p>
</td>
</tr>
</tbody>
</table>

From this chart, you can see that Onix's density is eerily close to Styrofoam. Even the notoriously light balsa wood is five times denser than him. Actual rock is about 85 times denser. If Onix was made of granite, it would weigh 18 tonnes, much heavier than even Snorlax (the heaviest of the original Pokémon at 460kg).

<img class="size-full wp-image-836 aligncenter" src="/wp-content/uploads/onix_styrofoam.png" alt="" width="717" height="717" />

While most people wouldn't be able to pick Onix up (it may not be dense, but it is big), it wouldn't be impossible to drag it. Picking up part of it would feel disconcertingly light, like picking up an aluminum ladder or carbon fibre bike, only more so.

{% capture caption %}
This picture is unrealistic. Because of its density, no more than 3% of Onix can be below the water. I don't own the copyright to this image, but I'm claiming fair use for purpose of criticism. <a href="https://giphy.com/gifs/pokemon-origins-dYzPR633vUW2c">Source</a>.
{% endcapture %}
{% include image.html src="/wp-content/uploads/onix_float.gif" alt="" caption=caption %}

How did the creators of Pokémon accidently bestow one of the most famous of their creations with a hilariously unrealistic density?

I have a pet theory.

I went to school for nanotechnology engineering. One of the most important things we looked into was how equations scaled with size.

Humans are really good at intuiting linear scaling. When something scales linearly, every twofold change in one quantity brings about a twofold change in another. Time and speed scale linearly (albeit inversely). Double your speed and the trip takes half the time. This is so simple that it rarely requires explanation.

Unfortunately for our intuitions, many physical quantities don't scale linearly. These were the cases that were important for me and my classmates to learn, because until we internalized them, our intuitions were useless on the nanoscale. Many forces, for example, scale such that they become incredibly strong incredibly quickly at small distances. This leads to nanoscale systems exhibiting a stickiness that is hard on our intuitions.

It isn't just forces that have weird scaling though. Geometry often trips people up too.

In geometry, perimeter is the only quantity I can think of that scales linearly with size. Double the length of the sides of a square and the perimeter doubles. The area, however does not. Area is <em>quadratically </em>related to side length. Double the length of a square and you'll find the area quadruples. Triple the length and the area increases nine times. Area varies with the square of the length, a property that isn't just true of squares. The area of a circle is just as tied to the square of its radius as a square is to the square of its length.

Volume is even trickier than radius. It scales with the third power of the size. Double the size of a cube and its volume increases eight-fold. Triple it, and you'll see 27 times the volume. Volume increases with the cube (which again works for shapes other than cubes) of the length.

If you look at the weights of Pokémon, you'll see that the ones that are the size of humans have fairly realistic weights. Sandslash is the size of a child (it stands 1m/3' high) and weighs <a href="https://bulbapedia.bulbagarden.net/wiki/Sandslash_(Pok%C3%A9mon)">a fairly reasonable 29.5kg</a>.

(This only works for Pokémon <em>really</em> close to human size. I'd hoped that Snorlax would be about as dense as marshmallows so I could do a fun comparison, but it turns out that marshmallows are four times as dense as Snorlax – despite marshmallows only having a density of ~0.5t/m<sup>3</sup>)

Beyond these touchstones, you'll see that the designers of Pokémon increased their weight linearly with size. Onix is a bit more than eight times as long as Sandslash and weighs seven times as much.

Unfortunately for realism, weight is just density times volume and as I just said, volume increases with the cube of length. Onix shouldn't weigh seven or even eight times as much as Sandslash. At a minimum, its weight should be eight times eight times eight multiples of Sandslash's; a full 512 times more.

Scaling properties determine how much of the world is arrayed. We see extremely large animals more often in the ocean than in the land because the strength of bones scales with the square of size, while weight scales with the cube. Become too big and <a href="https://irl.cs.ucla.edu/papers/right-size.html">you can't walk without breaking your bones</a>. Become small and <a href="https://www.youtube.com/watch?v=pAYS0pQ5Kf4">people animate kids' movies about how strong you are</a>. All of this stems from scaling.

These equations aren't just important to physicists. They're important to any science fiction or fantasy writer who wants to tell a realistic story.

Or, at least, to anyone who doesn't want their work picked apart by physicists.

<hr class="post-end" />

[^1]: Not the professor. His density <a href="https://www.google.ca/search?q=average+human+density&amp;rlz=1C5CHFA_enCA691CA692&amp;oq=average+human+density&amp;aqs=chrome..69i57j0l5.3857j1j1&amp;sourceid=chrome&amp;ie=UTF-8">is 0.985t/m<sup>3</sup></a>.
