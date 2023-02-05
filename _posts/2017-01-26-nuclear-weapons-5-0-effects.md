---
id: 159
title: "Nuclear Weapons: 5.0 Effects"
date: 2017-01-26T19:08:57-05:00
author: Zach Jacobi
author_link: https://socratic-form-microscopy.com/about-me
layout: post
guid: http://socratic-form-microscopy.com/?p=159
permalink: /2017/01/26/nuclear-weapons-5-0-effects/
categories:
  - Falsifiable
  - Politics
  - Science
tags:
  - nuclear weapons
  - x-risk
nuclear-series:
  previous:
    title: "Nuclear Weapons: 4.0 Weapon Design"
    url: /2017/01/25/nuclear-weapons-4-0-weapon-design/
  next:
    title: "Nuclear Weapons: 6.0 Delivery Mechanisms"
    url: /2017/01/27/nuclear-weapons-6-0-delivery-mechanisms/
---

To understand the effects of nuclear weapons, you first need to understand how those effects scale with weapon yield.

<h3 id="1">5.1 Scaling</h3>
Modern bombs are much smaller than the Tsar Bomba. The standard US nuclear warhead, the W88, is a "mere" 475kt, a yield that is 100x less than that of the Tsar Bomba. On the other hand, the W88 weighs in at 360kg, 75x lighter.

This may seem like a poor trade, but it's actually a very good one, due to the fundamental properties of explosive scaling. Scaling factors are very important to weapons. They determine the stable equilibriums that designs fall into. For example: we have tanks instead of mechs because strength scaling and mass scaling together make tall vehicles very vulnerable to weapons.

Scaling factors for all nuclear weapon effects (the fireball, the shock wave, and electromagnetic radiation) are different, but we can use the scaling factor of electromagnetic radiation as an example.

A nuclear weapon emits a set amount of energy as photons – gamma rays and X-rays, as well as IR, UV, and visible light. These photons radiate out approximately equally in all directions. The energy that the photons carry is fixed, but the area that the energy covers isn't. We call the amount of energy per square meter "intensity".

Intensity is incredibly important. It's what drives the differences in climate between Mercury (surface temperature: 427ºC) and Pluto (surface temperature: -218ºC). In nuclear weapons, the intensity of radiated photons determines if buildings are set afire from the heat or people die of radiation sickness.

Since energy is constant, intensity will depend only on the area the energy is spread out over. Luckily, it's pretty easy for us to calculate this area as a function of distance from the bomb. Dividing the total energy by the surface area of a sphere of a certain radius, we get the following equation for intensity:

<img class="alignnone size-full wp-image-171" src="{{ site.baseurl }}/wp-content/uploads/intensity-equation.png" alt="" width="82" height="37" />

Where E<span style="font-size: 12px;">0</span> is the initial energy of the bomb and <em>d</em> is the distance from the epicentre of the explosion.

Ten meters out from a 10kt (in the SI unit, joules, this is 41.8 TJ) bomb, the energy per square metre 33,300 MJ. Ten times further away, the energy per square metre is 333 MJ, a 100-fold decrease.

To get the desired destructive power, a certain intensity is necessary. An intensity of 372kJ per square meter is necessary to give third degree burns, for example. Ignoring loss from the air, you get this effect from a 10kt bomb out to about 3km. Increase the bomb size 100-fold to 1Mt, and the radius expands only ten-fold, to 29.9km.

These examples illustrate one of the fundamental scaling factors of nuclear weapons. The photon effect radius of a nuclear weapon is proportional to – at best – the square root of the power of the weapon. This means that there are intense diminishing returns to increasing the power of a weapon. Increase its power 25 times and the radius of destruction becomes five times bigger. Increase the power 50 times and the radius only increases sevenfold.

Blast radius and fireball size scale differently than radiation, but in all cases the scaling is square root or worse. In fact, you'll soon see that radiation scales better than nearly every other destructive effect.

Taking into account this scaling factor, the W88 is (by one measure) 10x less destructive than the Tsar Bomba, but 75x lighter – a trade-off that makes much more sense. Keep this relationship in mind whenever nuclear weapons are described in terms of "the power of the atomic bomb that destroyed Hiroshima". The policy implications of this relationship will also become clear later. For now, it's important that you simply understand that relative destructive power and yield don't correspond 1:1.

**Additional Reading**: <a href="https://en.wikipedia.org/wiki/Inverse-square_law#Light_and_other_electromagnetic_radiation">Inverse Square Law</a>

<h3 id="2">5.2 Direct Effects</h3>
Thus far, we've restricted our discussion of nuclear weapon detonation to the technical. There's a cascade of neutrons and a bunch of energy is released as a by-product – that much is clear. But what does all that energy do? How do we get from neutrons to levelled cities and mushroom clouds?

There isn't as much clear, well-curated information on this topic as I'd like, but perhaps that's only to be expected. As near as I can tell, here's what happens:

<ol>
 	<li>A lot of heat (and some photons and neutrons) get generated by fission or fusion
<ol>
 	<li>The fission of an atom releases a huge amount of energy. Only 7% of this in the form of fission neutrons and gamma rays; most is in the kinetic energy of the atom fragments, which will be travelling at about 4% of the speed of light.</li>
 	<li>Fusion reactions output mainly high energy neutrons. These are captured by the dense tamper around the fusion core, allowing them to cause fission, or to impart their kinetic energy to another atom. Most fusion neutrons that don't collide with the tamper will escape.</li>
</ol>
</li>
 	<li>About one microsecond after detonation, the core and tamper of a bomb will be a cloud of plasma a couple metres in diameter, with temperatures exceeding 10,000,000ºC.</li>
 	<li>Via <a href="https://en.wikipedia.org/wiki/Black-body_radiation">blackbody radiation</a>, the plasma emits x-rays. These x-rays heat the surrounding air to a similar temperature.</li>
 	<li>The very air becomes incandescent, releasing a bright pulse of light.
<ol>
 	<li>Depending on yield, distance, and atmospheric conditions the pulse can be permanently or temporarily blinding for anyone who looks at it.</li>
 	<li>As well as visible light, IR and UV light is emitted. The combined radiance of all of this light can set buildings on fire or give people severe burns.</li>
</ol>
</li>
 	<li>The superheated air in the very centre of the explosion pushes against the surrounding air, acting like a giant piston and producing a massive shock front.</li>
 	<li>Compression in the shock front causes it to briefly become a dense plasma, temporarily blocking the light from the incandescent air closer to the core.</li>
 	<li>The compressed air of the shock front begins to expand rapidly, dropping in temperature and becoming clear. The fireball in the centre can once again be seen.</li>
 	<li>This shock wave travels at approximately the speed of sound. Whenever it hits something (a house, a vehicle, a tree), it causes damage via two mechanisms.
<ol>
 	<li>Static overpressure: the direct hammer-blow of all that dense air striking at once.</li>
 	<li>Dynamic overpressure: the drag associated with the wind of the shock-front's passage, which can tear, tumble and drag objects.</li>
</ol>
</li>
 	<li>Back in the centre of the blast, there's still a bunch of hot air. It will quickly cool to the point where it no longer glows, but it will still be much brighter than the surroundings.</li>
 	<li>This hot air begins to rise, pulling up debris from the ground (at this point, there will be plenty) into the vacuum its rising creates. The hot air also expands and the outside edges cool, which causes rotating internal air currents that help to draw in more air from below. This forms the characteristic mushroom cloud of a nuclear explosion.</li>
 	<li>Between the vacuum caused by the rising mushroom cloud and the vacuum caused by the initial shockwave, a steady wind will blow back towards ground zero until equilibrium is reached. This wind will further toss around debris and can help to fan the flames of any fires that have started.</li>
</ol>

{% capture caption %}
Image Credit: <a href="https://en.wikipedia.org/wiki/Mushroom_cloud#/media/File:Mushroom_cloud.svg"> Wikipedia/Mushroom Cloud</a>
{% endcapture %}
{% include image.html src="/wp-content/uploads/mushroom-cloud-300x275.png" caption=caption %}

<h5 id="21"> 5.2.1 Fireball</h5>
The nearby detonation of an atomic bomb is utterly devastating to infrastructure. Everything within the central fireball will be annihilated. The size of the fireball varies: 150m for a 10kt blast (slightly smaller than Hiroshima), 720m for the modern 475kt W-88 favoured by America, and 4.62km for the monstrous 50Mt Tsar Bomba. Ideally, fireball effects would scale as the square root of the yield. In actuality, they scale a bit worse than this, as the fifth root of the square of the radius (i.e. the 2.5<sup>th</sup> root). I'm not sure exactly what causes this, possibly some weird property of plasma, or just general fluid dynamics oddness.

{% capture caption %}
Data Source: <a href="http://nuclearsecrecy.com/nukemap/">Nukemap 2.42</a>. Trend line has equation <img class="alignnone size-full wp-image-168" src="{{ site.baseurl }}/wp-content/uploads/fireball-r-equation.png" alt="" width="103" height="19" />.
{% endcapture %}
{% include image.html src="/wp-content/uploads/Fireball-Radius.png" caption=caption %}

<h5 id="22">5.2.2 Shockwave</h5>
As deadly as the fireball is, most of the damage from a nuclear explosion comes from the shockwave. Weapon designers carefully model the shockwave and use these insights to come up with an optimal detonation height for various effects – like levelling reinforced buildings or destroying residential areas. Models take into account the "Mach stem", the angle at which some of the wave will be reflected off the ground and constructively interfere with the rest of it, leading to increased destruction.

To get an idea of the damage a shockwave causes, we can look at the radius within which the maximum pressure increase is 20 psi and the radius within which the maximum pressure increase is 5 psi. 5 psi is the blast pressure required to level residential buildings, while 20psi will demolish even heavy concrete buildings.

Unlike radiation effects, blast pressure increases with cube root of the yield. This scaling – like the shockwave itself – is driven by heat. The pressure air exerts is directly proportional to its temperature (this relationship is linear and given by the ideal gas law: <a href="https://en.wikipedia.org/wiki/Ideal_gas_law">PV = nRT</a>). To get a 5 psi overpressure at a certain radius, the bomb must ultimately heat all the air within the radius to a temperature that will cause a 5 psi increase in pressure. The energy taken to heat a material is proportional to the mass of material to be heated. The mass of air is proportional to its volume. And volume of a sphere is really easy to calculate: . Chaining all these observations together, we're left with radius increasing as the cube root of explosive power.

This means that for every 1000-fold increase in bomb power, you'll see a 10-fold increase in destructive radius. In terms of overpressure effects, the W88 is about 4.7 times less destructive than the Tsar Bomba, while being 75 times lighter. This trade-off comes up even better than for radiation.

{% capture caption %}
Data Source: <a href="http://nuclearsecrecy.com/nukemap/">Nukemap 2.42</a>. 5 psi trend line has equation <img class="alignnone size-full wp-image-166" src="{{ site.baseurl }}/wp-content/uploads/5-psi-overpressure-eq.png" alt="" width="99" height="21" />, 20 psi trend line has equation <img src="{{ site.baseurl }}/wp-content/uploads/20psi-overpressure-eq.png" alt="" width="101" height="20" class="alignnone size-full wp-image-165" />.
{% endcapture %}
{% include image.html src="/wp-content/uploads/Overpressure-Radius.png" caption=caption %}

<h5 id="23">5.2.3 Direct Radiation</h5>
Nuclear weapons produce two types of damaging radiation (they're both photons, just at different energy levels): thermal and ionizing. Ionization radiation (mainly gamma rays) is responsible for causing acute radiation poisoning and later cancers. Thermal radiation (light, from IR to UV) is responsible for the horrendous burns nuclear weapons survivors often bear.

In a vacuum, both of these would exhibit scaling with the square root of the yield, as discussed earlier. In real world conditions though, there's another key factor in play: the atmosphere. Air is actually fairly good at absorbing gamma radiation. For every 150m that a group of gamma rays travels through the air at sea level, about half of them are absorbed. This is cold comfort if you ever find yourself at ground zero of a nuclear explosion, but it means anyone more than a few kilometres away has fairly little to fear from direct radiation. Once atmospheric absorption is taken into account, the radius where gamma radiation is lethal increases with approximately the 6<sup>th</sup> root of the yield. This means that even very large bombs scarcely irradiate more people than their smaller counterparts.

As blasts become larger, fewer and fewer people are affected by direct radiation. The radius of complete destruction (20 psi overpressure) is smaller on 10kt bombs than the radius at which radiation fatalities are common. But the differences in scaling means that by the time a bomb is 575kt the radii are equal. Beyond this size, the radius of complete destruction will be larger than the radius of radiation effects and most casualties will come from the shockwave, not radiation.

IR, visible, and UV light are much less affected by the atmosphere. If the atmosphere absorbed light at the same rate it absorbs gamma rays, the sun would appear 717 billion billion times brighter on an airplane at cruising altitude as it does at sea level. This obviously isn't the case – the sun is approximately as bright in both cases. This difference in absorption means that the radius at which nuclear weapons cause burns scales with close to the square root of the yield (the small amount of energy absorbed by the air does mean that it scales slightly slower in atmosphere than in vacuum).

{% capture caption %}
Data Source: <a href="http://nuclearsecrecy.com/nukemap/">Nukemap 2.42</a>. 50% Deaths trend line has equation <img class="alignnone size-full wp-image-175" src="{{ site.baseurl }}/wp-content/uploads/50-deaths-equation.png" alt="" width="124" height="19" />, 3<sup>rd</sup> Degree burns trend line has equation <img class="alignnone size-full wp-image-162" src="{{ site.baseurl }}/wp-content/uploads/3rd-degree-burn-eq.png" alt="" width="117" height="22" />.
{% endcapture %}
{% include image.html src="/wp-content/uploads/Radiation-Radius.png" caption=caption %}

**Additional Reading**: <a href="https://en.wikipedia.org/wiki/Effects_of_nuclear_explosions">Effects of Nuclear Explosions</a>, <a href="https://en.wikipedia.org/wiki/Nuclear_weapon_design#Fission">Nuclear Weapon Design: Fission</a>, <a href="https://en.wikipedia.org/wiki/Nuclear_weapon_design#Fusion">Nuclear Weapon Design: Fusion</a>, <a href="https://en.wikipedia.org/wiki/Mushroom_cloud">Mushroom Cloud</a>, <a href="http://nuclearsecrecy.com/nukemap/">Nukemap</a> and <a href="http://wordpress.mrreid.org/2015/04/18/the-nuclear-double-flash/">The Nuclear Double Flash</a>.

<h3 id="3">5.3 Indirect Effects</h3>
Part of the horror of nuclear weapons comes from fallout, the lingering radiation left behind after a nuclear detonation. Fallout doesn't last forever (and remember, the more unstable and radioactive an element is, the quicker it breaks down into something stable), but while it is around it can sicken and kill. Fallout can also cause illness and death far from the site of the initial blast, increasing the human toll of any nuclear weapon detonation.

Fallout is composed of unstable, radioactive isotopes that are scattered after a nuclear bomb is detonated. Fallout is mainly comprised of fission by-products (some of these are stable, but many are themselves radioactive and must conduct additional decay before they become stable) and left over fuel (remember, fission efficiency is almost never higher than 40%, leaving 60% of the fuel weight in radioactive waste). Depending on bomb detonation height, there may also be neutron activated fallout. Neutron activated fallout arises when stable elements are bombarded with neutrons and either capture the neutron, or fission from the energy of the collision. Since nuclear weapons tend to be detonated high in the air (with the hope of maximizing the shock wave), neutron activated fallout is a small portion of the total fallout. Either way, all fallout behaves similarly.

Some of the fallout will be blown up into the stratosphere by the force of the blast, or carried up in the wake of the rapidly rising fireball. These fallout products end up distributed fairly evenly across the whole globe. Nuclear testing before the partial and complete test bans resulted in a dramatic rise in strontium-90 and caesium-137 levels in humans all over the globe. These isotopes can cause cancer and other problems if ingested in significant amounts and the threat posed by steadily increasing global levels was enough to prompt the test ban treaties.

Stratospheric fallout is the minority; most of the fallout remains in the area of the blast. It's still dispersed in the atmosphere, but its subject to local winds, not the global jet stream. The largest particles begin to fall immediately. Not all of them will be radioactive – some of the falling matter will be simple vaporized dirt or water – but it will never be safe to assume that any particles falling in the wake of a nuclear explosion are benign.

A high altitude burst doesn't guarantee that the particles that rain down will be fallout free. Even if no neutron activation occurs, some of the material that rains down will be contaminated with radioisotopes produced by the blast. After the Castle Bravo nuclear test, coral contaminated with radioisotopes fell like snow over a large area, causing severe radiation burns whenever it touched human skin.

In the first day after a bomb is detonated, half of the local fallout will be deposited – unless it rains, in which case even more will fall. Rain is actually quite likely after a nuclear weapon detonation because fine particles dispersed in the atmosphere (like the dirt drawn up in a mushroom cloud) can help start the process of raindrop formation. Rain makes decontamination even harder, as the radioactive ions that travel down with raindrops tend to bond to external surfaces, requiring sandblasting to remove them.

The danger of the fallout varies with local atmospheric conditions, the size of the bomb, the efficiency of the bomb, and where the bomb detonates. Winds can disperse fallout, affecting more people, but giving each person a lesser dose. Bombs with a high efficiency create less fallout than bombs with lower efficiency. Bombs that get more of their power from fusion will generally have less fallout than a bomb of the same yield that gets more energy from fission.

Because of the potential variance in conditions, there are few general rules about fallout. I've seen something called the "Seven Ten" rule bandied about. The rule claims that every sevenfold increase in time after the detonation leads to a tenfold decrease in radiation from fallout. So after seven hours there will be ten times less radiation compared to the first hour and after forty-nine hours (approximately 2 days) there will be one hundred times less radiation.

I spent a lot of time confused by this. Remember half-lives from earlier? Instead of a fixed ratio of times (i.e. seven times) producing a fractional drop in radioactivity (i.e. ten times), I thought there should be fixed <em>period</em> of time that produces a fractional drop in radioactivity. If there really is a tenfold drop in radiation after seven hours, then it means that the half-life of the isotopes in the fallout would average out to 2.1 hours. Which should predict there would be a one-hundred hold decrease in fallout after fourteen hours (The equation is <img class="alignnone size-full wp-image-161" src="{{ site.baseurl }}/wp-content/uploads/half-life-eq.png" alt="" width="54" height="38" /> which gives approximately 1/100). This definitely isn't the case, which was the cause of my confusion.

I think the 7-10 rule is correct because of the mixture of isotopes we see in fallout. The most common isotopes in fallout (and their half-lives are): neptunium-240 (61.9 minutes), neptunium-239 (2.1 days), uranium-237 (6.75 days), iodine-131 (8 days), tritium (12 years), caesium-134 (20 years), strontium-90 (28.8 years), caesium-137 (30 years), technetium-99 (211,000 years), and zirconium-93 (over 1,000,000 years). The widely disparate half-lives lead to a variety of zones, each of which is dominated by a different half-life.

The 7-10 rule is an approximation that more or less fits the wonky data that results from this mixture. But it isn't a very good approximation – it's accurate to within 25% for the first two weeks and accurate within 50% for the first six months. After that, fallout is dominated by isotopes with similar half-lives and fits an exponential decay model, rendering the 7-10 rule basically useless.

Iodine-131 is one of the most famous fallout products and is primarily dangerous if consumed. Once in the body, it will be concentrated in the thyroid, where it can cause immediate damage or eventual cancer. This effect can be minimized with iodine tablets, which essentially "fill-up" the thyroid with safe iodine, leaving no room for iodine-131. Recommended dosage of iodine varies with the severity of the radioactive contamination and isn't recommended for anyone over 40 except in cases where they may face acute thyroid damage. It's also recommended to avoid drinking milk if you suspect any contamination with iodine-131.

Neptunium-239 and uranium-237 are responsible for most of the gamma radiation in fallout in the early days after a nuclear blast (neptunium-240 dominates for a few hours, but promptly fades). This is actually fairly good. After 20 days, there will be 1000-fold less radiation from neptunium-239 as there was immediately preceding the blast. Uranium-237 is a bit longer lived, requiring about 67 days for a 1000-fold decrease in radioactivity. Whether this represents a safe level is dependent on the initial amount and the relative abundance of neptunium-239/uranium-237 and other elements.

If you know or suspect that your area has been exposed to fallout, minimize your time outdoors. Your dwelling will offer excellent protection against alpha and beta particles and some protection against gamma radiation. If you must venture outside, wear many layers of clothes to protect yourself from beta particles. Don't drink water without filtering it first. Try to avoid food produced after the fallout started, especially milk. Food produced before the nuclear exchange should be safe, as long as the outside is washed with clean water. Peeling fruit will also suffice. You can relax these precautions as the weeks and months wear on. In the years after fallout occurs, be aware of your surroundings. Hot spots (with fatal levels of radiation) may exist for several years. If you see dead trees or animals with no signs of rot, head in the other direction quickly.

This is just the barest of outlines. There are many guides out there that will go into specifics. Unfortunately, many guides have an implicit agenda (either: "scare people into becoming anti-nuclear activists", or "keep our population from panicking about nukes"). If you know of a good, scientifically accurate guide, please link it in the comments. As additional reading, I've provided the official US Government planning guide, which seems to be accurate. In addition, I've linked to a more technical overview of fallout production and decay (Residual Nuclear Radiation and Fallout).

**Additional Reading**: <a href="http://www.who.int/ionizing_radiation/pub_meet/Iodine_Prophylaxis_guide.pdf">Iodine Prophylaxis</a>, <a href="https://en.wikipedia.org/wiki/Nuclear_fallout">Nuclear Fallout</a>, <a href="https://www.remm.nlm.gov/PlanningGuidanceNuclearDetonation.pdf">Planning Guidance for Response to a Nuclear Detonation</a>, <a href="https://www.fourmilab.ch/etexts/www/effects/eonw_9.pdf">Residual Nuclear Radiation and Fallout</a>
<br>

<hr class="post-end" />
