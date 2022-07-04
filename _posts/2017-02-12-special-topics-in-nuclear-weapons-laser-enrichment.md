---
id: 269
title: "Special Topics in Nuclear Weapons: Laser Enrichment"
date: 2017-02-12T14:15:49-05:00
author: Zach
layout: post
guid: http://socratic-form-microscopy.com/?p=269
permalink: /2017/02/12/special-topics-in-nuclear-weapons-laser-enrichment/
categories:
  - Politics
  - Science
tags:
  - nuclear weapons
  - x-risk
---

In an effort to make my nuclear weapons post series a one stop resource for anyone interested in getting up to speed on nuclear weapons, I've decided to add supplementary materials filling any gaps that are pointed out to me. This supplementary post is on laser enrichment.

Enrichment is one of the more difficult steps in the building of certain nuclear weapons. Currently, enrichment is accomplished through banks of hundreds or thousands of centrifuges, feeding their products forward towards higher and higher enrichment percentages.

Significant centrifuge plants are relatively big (the Natanz plant in Iran covers 100,000m<sup>2</sup>, for example) and require a large and consistent supply of energy, which often <a href="https://www.google.ca/maps/place/Natanz+nuclear+plant/@33.7237908,51.7255067,1591m/data=!3m1!1e3!4m5!3m4!1s0x3f96419eff1700dd:0xfa1cc67ac8db241!8m2!3d33.7217884!4d51.7228483">makes it possible spot them in satellite imagery</a>. The centrifuges themselves require a recognizable combination of components, <a href="http://www.nuclearsuppliersgroup.org/en/news/148-update-of-nsg-control-lists">which are carefully monitored</a>. If a nation were to suddenly buy up components implicated in centrifuge design, it would clearly signal its intention to increase its enrichment capacity.

Recently, laser enrichment has emerged as an additional vector for proliferation. Properly called SILEX (separation of isotopes by laser excitation), this new technology has the potential to make enrichment (and therefore proliferation easier). This post discusses how laser enrichment works and puts the threat it represents in context. It's both a summarization (and simplification) of the <a href="http://scienceandglobalsecurity.org/archive/sgs24snyder.pdf">recent paper</a> on laser enrichment in published in <a href="https://www.researchgate.net/journal/0892-9882_Science_and_Global_Security">Science &amp; Global Security</a> by <a href="http://scholar.princeton.edu/rasnyder/publications">Ryan Snyder</a> and the product of my extensive background reading on nuclear weapons.

<h3 id="how">How It Works</h3>
Like gas centrifugation, laser enrichment requires gaseous uranium hexafluoride (Hex). While the preparation of uranium hexafluoride doesn't represent a significant technical challenge (compared to all of the rest of the work of building a nuclear weapon), it's still the sort of work that most reasonable chemists try to avoid. "Requires work with a poisonous, corrosive, radioactive gas" will never be a selling feature of enrichment work.

Laser enrichment also requires a large laser capable of outputting 10.2µm light (which must be converted to 16µm using Raman scattering off of H<sub>2</sub> gas), capable of pulsing 30,000 times per second. This appears to be just barely possible with current technology and impossible with off the shelf technology. It's the sort of thing that would have to be custom assembled.

Also requiring custom assembly is the enrichment cell, which must have a nozzle capable of injecting a supersonic stream of uranium hexafluoride in such a way as to minimize post-injection expansion. The cell also must have an optically transparent window for your laser to shine through and must have several egress lines – peripheral ones for enriched product and a central one for the jet to flow out of.

Finally, if you want to make this maximally efficient, you're going to need a mirror set up so as to have your laser pass through the gas twice. This corrects for the circular shape of the laser. Without this mirror, you won't have enough coverage at that edges of the gas and you're only going to operate at 78.5% of the maximum efficiency.

The whole setup looks like this:

{% capture caption %}
Schematic of a third generation laser isotope separation unit for uranium enrichment. Image Credit: <a href="https://scienceandglobalsecurity.org/archive/sgs24snyder.pdf">A Proliferation Assessment of Third Generation Laser Uranium Enrichment Technology</a>
{% endcapture %}
{% include image.html src="/wp-content/uploads/enrichment-cell-600x340.png" alt="" caption=caption %}

Once you've assembled all of this, you're good to start enriching.

Remember, natural Hex is largely made up of <sup>238</sup>UF<sub>6</sub> and is only about 0.7% <sup>235</sup>UF<sub>6</sub>. The purpose of enrichment is to increase the percentage of <sup>235</sup>UF<sub>6</sub> in the gas until it is almost entirely made up of this isotope of uranium.

The process SILEX uses to achieve this is relatively simple. You run the Hex and a carrier gas (the paper says SF<sub>6</sub>) through this system at supersonic speeds and low temperatures while pulsing the laser so as to hit the jet just as it leaves the nozzle. If you've tuned your wavelength as directed, then photons from the laser will kick any <sup>235</sup>UF<sub>6</sub> molecules they hit into a heightened vibrational state (called the <em>v</em><sub>3</sub> vibrational mode), while doing nothing to the <sup>238</sup>UF<sub>6</sub> molecules that make up most of the Hex.

<sup>235</sup>UF<sub>6</sub> in the <em>v<sub>3</sub> </em>vibrational mode will eventually revert to a lower energy (or "ground") state, but it is unlikely to spontaneously revert to a ground state during the few milliseconds it takes to traverse the cell. For the purposes of SILEX, <sup>235</sup>UF<sub>6</sub> in the <em>v<sub>3</sub> </em>vibrational mode will remain in that mode unless something acts on it to change it. To improperly anthropomorphize a particle for a second, this is "bad" for the excited <sup>235</sup>UF<sub>6</sub>, because it "wants" to be at a lower ground state.

The excited <sup>235</sup>UF<sub>6</sub> could get external "help" from a collision with <sup>238</sup>UF<sub>6</sub> (this collision would allow it to release a photon and revert to its ground state), but this is unlikely if you keep the overall concentration of UF<sub>6</sub> in the carrier gas low (the paper recommends 5%). This is in fact exactly what is done, because efficiency is maximized when <sup>238</sup>UF<sub>6</sub> doesn't get a chance to collide with <sup>235</sup>UF<sub>6</sub>.

When you put Hex in a carrier gas like SF<sub>6</sub>, you're going to see the formation of transitory dimers. These are temporary, weak bonds between one Hex molecule and one SF<sub>6</sub> molecule. These bonds are fairly stable, unless the Hex is in the <em>v<sub>3</sub></em> (or similar) vibrational mode. If dimer formation occurs between <em>v<sub>3</sub> </em><sup>235</sup>UF<sub>6</sub> and SF<sub>6</sub>, the dimer is very short-lived. The excited <sup>235</sup>UF<sub>6</sub> dumps all of its extra energy into the dimer bond, resulting in a lot of recoil; both the <sup>235</sup>UF<sub>6</sub> and the SF<sub>6</sub> go flying apart in opposite directions. It's the dimer formation that causes a very different outcome from a simple collision with <sup>238</sup>UF<sub>6</sub>.

This recoil tends to push <sup>235</sup>UF<sub>6</sub> to the edges of the stream. A skimmer positioned around the outlet collects this enriched product. Note that it won't be entirely enriched; the outside edges of the jet will have plenty of <sup>238</sup>UF<sub>6</sub> because the jet is going to be mostly <sup>238</sup>UF<sub>6</sub> – or at least, it will be when natural or lightly enriched uranium is the input.

If you were doing this on an industrial scale, you'd set a bunch of these cells up in series, with the enriched product of each cell being the feed for the next. In this way, you'd get the same sort of cascade towards higher enrichment as you would with centrifuges.

<h3 id="pro">Proliferation</h3>
Laser enrichment might be more space and energy efficient than centrifuge arrays.

I have to say <em>might</em> because there's some uncertainty here. A few key parameters that determine ease of proliferation using SILEX are missing. This isn't because of censors removing them for security reasons. It's because this technology is so new that there are serious question marks hanging over it. SILEX has shown promise in lab scale experiments, but there doesn't yet exist any proof that SILEX will be superior to centrifuge enrichment when it comes to enriching uranium on an industrial scale. Given that the pilot project has <a href="http://www.world-nuclear-news.org/UF-GE-Hitachi-to-exit-laser-enrichment-JV-1904168.html">been stalled since GE pulled out</a>, it may be quite a while before we know if SELIX will fulfill its promise or not.

It looks like a SILEX would allow a country with technology on the level of Iran to enrich the same amount of uranium with only 59% of the floor area. This would make enrichment a bit easier to hide, but would do nothing to stop leaks. It was human intelligence, not satellite photos <a href="https://en.wikipedia.org/wiki/Nuclear_facilities_in_Iran#Natanz">that allowed the west to discover the work at Natanz</a>.

The error bound on SILEX energy consumption is large enough that it's unclear if there would be a power consumption benefit or cost for rogue states switching to SILEX from indigenous centrifuge technology. State of the art American centrifuges still beat SILEX on floor space and they may beat it in energy use.

Estimates for SILEX efficiency span an order of magnitude and in the upper two-thirds of that range it seems to be a clear winner (in terms of amount of energy required per percent enrichment). I couldn't see any consensus on the relatively likelihood of high vs. low actual efficiency, but I would personally bet that a lot of the probability distribution exists near the bottom of the allowed efficiencies. I haven't worked in nuclear science, but I have done chemistry, and my experience is that few processes perform as well on an industrial scale as you might expect from efficiency calculations done at laboratory scale.

Enrichment with SILEX is quite possibly easier than enrichment with centrifuges. That is to say, even if SILEX doesn't allow rogue nations to enrich more efficiently, it might allow them to enrich at all. SILEX requires some advanced optics knowledge and the lasers needed aren't exactly available off the shelf, but they are easier to design and build than specialized enrichment centrifuges.

Before centrifugation became the preferred method of isotope separation for nuclear weapons (and nuclear energy), <a href="https://en.wikipedia.org/wiki/Gaseous_diffusion">gaseous diffusion</a> was used. Gaseous diffusion plants use truly prodigious amounts of space and energy. There is absolutely no way that these things can be hidden or disguised as something else.

With the advent of centrifuges, proliferation became significantly easier. Countries used to be faced with no good path to a functioning bomb. Plutonium is relatively easy to acquire and separate, but it is very difficult to build a successful <a href="#imp">implosion weapon</a> (and impossible to do so without alerting anyone with test detonations). Uranium was relatively difficult to enrich, which closed off the option of a simpler <a href="#gun">gun assembly</a> weapon (it is impossible to build a gun assembly weapon using plutonium).

If you want a nuclear arsenal and don't care that gun assembly weapons are wasteful and less useful for staging, then the advent of uranium enrichment via centrifugation was a boon to you. Gun assembly weapons don't even necessarily require test detonations, which allows for the (slim) possibility of entirely clandestine nuclear arsenals – assuming enough uranium can be secretly enriched.

SILEX may eventually exacerbate this problem, to the point where any country with access to uranium could conceivably build a relatively low yield bomb (say a dozen or two kilotons).

At present, the technology is too new for this to be true. SILEX almost certainly has a few kinks left to be worked out. Trying to work them out at the same time as your country builds a new nuclear program isn't ideal. Best to wait for India or Pakistan to figure them out and then leak them to you in exchange for favours or missile technology (this has been North Korea's approach to nuclear weapons and it has worked quite well).

In a decade, SILEX may make proliferation even easier. I don't think it will make it easy to the point where Al Qaeda or Daesh can attempt to build nuclear weapons (can you imagine Daesh setting up a high-energy laser laboratory in Raqqa?). But I do worry that countries like Saudi Arabia or the Philippines might see the calculus around proliferation change enough to justify their building of a small arsenal of uranium weapons.

That would be a disaster for world peace and stability.

Governments are already reacting to threat posed by SILEX by adding necessary components to export ban and international watch lists. If any nation buys up a bunch of laser components over a short time without a good explanation, the international community will now suspect enrichment. I'm sure there are many men and women in the basement of the Pentagon and CIA headquarters now watching all laser equipment sales for more subtle signals of gradual stockpiling. Don't think for a second that SILEX somehow represents a cheat code for proliferation. It's still untested and unproven and governments and international organizations are already taking steps to reduce the proliferation risk.

Most nuclear technology is dual use. Uranium enrichment by centrifugation has made proliferation easier. It also increased the <a href="https://en.wikipedia.org/wiki/Energy_returned_on_energy_invested">energy return on investment</a> from burning uranium in power plants from ~40x to over 1500x (see <a href="https://en.wikipedia.org/wiki/Separative_work_units#Example">here</a> if you want to double check my calculations). Because of centrifugation, nuclear power plants could permanently end our dependence on oil if coupled with new battery technologies (and upfront capital and political will to build them).

SILEX could further increase the energy return on investment, making nuclear power plants even more economical. But SILEX also has the potential to make proliferation easier. It's still a new, experimental technology and it might not even pan out. Until we know for sure, it is certainly best for the world to proceed with caution.

<br>
<table style="width:100%;border-width:0px 0px 0px 0px;background:transparent;">
  <tr style="border:0px solid;background:transparent;">
    <td style="border:0px solid;background:transparent;text-align:center;""><a href="{{ site.baseurl }}/2017/01/24/nuclear-weapons-3-0-proliferation/">main topic</a></th>
    <td style="border:0px solid;background:transparent;text-align:center;""><a href="{{ site.baseurl }}/2017/01/22/nuclear-weapons-1-0-introduction/">index</a></th>
  </tr>
</table>
