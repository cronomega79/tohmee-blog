# -*- coding: utf-8 -*-
import os, html
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://blog.tohmee.com"
STORE = "https://tohmee.com"
TODAY = date.today().isoformat()

POSTS = [
    dict(slug="ultimate-streetwear-gift-guide-2026", title="The Ultimate Streetwear Gift Guide (2026)",
        desc="A no-fluff gift guide for buying graphic tees and hoodies for the streetwear fan in your life, with sizing and style tips.",
        link=("/apparel", "browse the full apparel lineup"),
        body=[
            "Buying streetwear for someone else is harder than it looks. Get the graphic wrong and it sits in a drawer; get the fit wrong and it never leaves the closet. This guide is built around the two things that actually matter: the design speaks to something they're already into, and the fit matches how they actually dress.",
            "Start with what they already wear on repeat. If their rotation is oversized tees and sneakers, a boxy graphic tee in a bold colorway is a safe, high-impact pick. If they layer heavily in colder months, a pullover hoodie gives you more room to make a statement without it feeling loud.",
            "Graphic-wise, lean into designs with a story or a reference rather than generic logos — pop-culture nods, bold typography, and one strong focal image tend to outperform busy, all-over prints as gifts because they read well from a distance and don't go out of style in a season.",
            "On sizing: when in doubt, size up rather than down. Streetwear generally leans oversized, and a tee that's slightly too big reads as intentional, while one that's too small just looks like a mistake. If you know their usual size in fitted brands, add one size for a relaxed streetwear fit.",
            "Ring-spun cotton tees (like the ones we use) hold color and shape through repeat washes better than cheaper carded cotton, so a well-made graphic tee is a gift that still looks good six months later — not just on the day it's unwrapped.",
        ]),
    dict(slug="how-to-style-a-graphic-tee", title="How to Style a Graphic Tee: 5 Streetwear Outfit Ideas",
        desc="Five practical ways to style a graphic tee for everyday streetwear, from layered fits to clean minimalist pairings.",
        link=("/apparel", "shop graphic tees"),
        body=[
            "A good graphic tee is the easiest piece in a wardrobe to build around, because it does the visual work for you — everything else just needs to support it, not compete with it.",
            "1. The clean pairing: dark denim or black joggers, white sneakers, and let the tee be the only loud element. This is the fastest way to make any graphic look intentional rather than random.",
            "2. The layered fit: an open flannel or a light jacket over the tee, unbuttoned, so the graphic peeks through. Works especially well with bold single-image designs that read clearly even partially covered.",
            "3. The monochrome base: pick one color from the graphic and match it in your pants or shoes. It ties the fit together without you having to think about coordination.",
            "4. The hoodie combo: a cropped or oversized hoodie tied around the waist or layered underneath an open jacket, tee visible at the collar. Great for transitional weather.",
            "5. The sneakerhead fit: tee tucked or half-tucked, cuffed pants, and let your shoes do the second half of the talking. This is where a design like a sneaker-culture graphic really earns its place.",
            "The common thread: pick one focal point per outfit. A loud graphic tee paired with loud everything else just cancels itself out.",
        ]),
    dict(slug="graphic-hoodie-vs-graphic-tee", title="Graphic Hoodie vs. Graphic Tee: Which Fits Your Vibe?",
        desc="Comparing graphic hoodies and graphic tees for streetwear — fit, versatility, seasonality, and which to buy first.",
        link=("/accessories", "check out accessories"),
        body=[
            "If you're only buying one piece, the honest answer depends on climate and how you layer — not on which looks cooler, because both can look great with the right graphic.",
            "Tees win on versatility. A graphic tee works alone in warm weather, under a jacket in cold weather, and layered under a hoodie for extra depth. It's the more flexible base piece across a full year.",
            "Hoodies win on presence. A pullover hoodie gives a graphic more surface area and a heavier drape, which makes bold or detailed designs feel more substantial. It's also a complete outfit on its own — no layering required.",
            "Climate matters more than people admit. In consistently warm regions, tees will get more wear per dollar. In anywhere with a real fall or winter, a hoodie earns its price back faster because it replaces a jacket on mild days.",
            "Our take: build the base in tees first since they mix into more outfits, then add one or two hoodies in designs you'd be happy to wear as a standalone piece, not just a layer.",
        ]),
    dict(slug="next-level-3600-ring-spun-cotton-explained", title="Next Level 3600 Cotton Explained: Why Ring-Spun Feels Different",
        desc="What ring-spun cotton actually means, why the Next Level 3600 tee feels softer, and how it holds up over time.",
        link=("/apparel", "feel the difference yourself"),
        body=[
            "\"Ring-spun cotton\" gets thrown around a lot in product descriptions, but it's a real manufacturing difference, not marketing fluff.",
            "In ring-spinning, cotton fibers are twisted and thinned repeatedly during spinning, which aligns the fibers more tightly and produces a stronger, finer, smoother yarn. Cheaper \"open-end\" or carded cotton skips this step, leaving shorter, looser fibers that make the fabric feel rougher and pill faster.",
            "The practical result on a tee: a softer hand-feel straight out of the wash, a more consistent print surface for graphics, and better shape retention after repeated washing. Ring-spun tees are also generally lighter without feeling thin, which is why the Next Level 3600 has become a go-to blank for printed streetwear.",
            "It matters most for graphic tees specifically, because a tighter, smoother weave takes ink more evenly — that's why detailed prints stay crisp instead of cracking or fading unevenly after a dozen washes.",
            "None of this means you can skip basic care: wash inside-out in cold water and skip the high-heat dryer cycle, and a ring-spun graphic tee will outlast a cheaper blank by years, not months.",
        ]),
    dict(slug="tohmee-size-guide", title="TōhMee Size Guide: Finding Your Perfect Fit",
        desc="A practical size guide for TōhMee tees and hoodies, covering true-to-size vs. oversized fit and how to measure at home.",
        link=("/apparel", "shop the full size range"),
        body=[
            "Getting size right online comes down to two numbers you already have: your chest measurement and the length of a tee you already own and like the fit of.",
            "To measure chest width, lay a tee you like flat, measure straight across from armpit to armpit, and double it. Compare that number to the garment's width measurement (not just the size label) — labels vary between brands, but flat measurements don't lie.",
            "Our tees and hoodies are cut for a classic, slightly relaxed streetwear fit rather than an athletic taper. If you prefer a fitted look, order true to size. If you want the oversized streetwear silhouette you see in styling photos, size up one from your usual.",
            "Hoodies run slightly roomier than tees by design, since they're meant to layer over a shirt. If you plan to wear one alone, true-to-size is usually right; if you'll layer under it, sizing up gives more room.",
            "When between two sizes, we generally recommend sizing up for graphic pieces — a slightly looser fit reads as intentional streetwear styling, while a slightly tight one just looks like the wrong size.",
        ]),
    dict(slug="meaning-behind-our-designs", title="The Meaning Behind Our Designs: The TōhMee Story",
        desc="A look at the ideas, references, and process behind TōhMee's graphic tee and hoodie designs.",
        link=("/", "explore the collection"),
        body=[
            "Every design in the shop starts as a reaction to something — a phrase stuck in rotation, a piece of internet culture, a visual idea that wouldn't leave us alone until it became a tee.",
            "We lean toward designs with one strong idea rather than crowded, busy graphics. A single bold image or line of text tends to age better than an all-over print packed with detail, because it stays legible and relevant long after the reference that inspired it fades.",
            "A lot of the catalog draws from meme culture, sneaker culture, and everyday phrases turned into something wearable — the kind of designs that get a reaction from someone who gets the reference, without needing an explanation to look good on someone who doesn't.",
            "Colorways are chosen after the graphic, not before — we test each design across several base colors and keep only the combinations where the print actually pops, which is why some designs come in five colors and others in two.",
            "The goal with every drop is the same: something you'd still want to wear a year from now, not just the week it launched.",
        ]),
    dict(slug="sneakerhead-style-graphic-tees", title="Sneakerhead Style: Pairing Graphic Tees with Your Kicks",
        desc="How to build outfits around your sneaker collection using graphic tees, colorway matching, and proportion tips.",
        link=("/apparel", "shop sneaker-culture tees"),
        body=[
            "If your sneaker rotation is the anchor of your wardrobe, your tee's job is to support it, not fight it for attention.",
            "The easiest matching trick: pull one accent color from your sneakers and find it somewhere in the graphic or the tee's base color. It doesn't need to be an exact match — same color family is enough to read as intentional.",
            "Proportion matters more than people think. Bulkier, chunkier sneakers pair better with slightly oversized tees, since a slim-fit tee on top of a heavy shoe silhouette can look top-light and unbalanced. Cleaner, low-profile sneakers give you more room to wear a fitted tee.",
            "If your shoes are already the loudest piece in the fit — bold colorway, high-attention silhouette — let the tee be simpler: one graphic, one or two colors, nothing competing for the same attention your shoes are getting.",
            "Sneaker-culture graphics specifically work well here because they reinforce the theme instead of introducing a second unrelated idea into the outfit.",
        ]),
    dict(slug="best-streetwear-colors-fall-winter", title="Best Streetwear Colors for Fall/Winter",
        desc="Seasonal color guidance for streetwear layering in colder months, and how to pick graphic tee colorways that work with your outerwear.",
        link=("/apparel", "shop seasonal colorways"),
        body=[
            "Cold-weather streetwear lives and dies by layering, and layering lives and dies by color coordination — you're managing three or four garments' worth of color instead of one.",
            "Base layers (your tee) are the easiest place to take a color risk, because they're often only partially visible under a jacket or hoodie. This is where a bold colorway — like a graphic on a bright base — can peek through at the collar or cuffs without overwhelming the whole outfit.",
            "Mid layers (hoodies) work best in grounded, muted tones — charcoal, navy, heather grey, forest green — since they take up the most visual real estate in a winter fit and loud colors here get tiring fast.",
            "Outerwear should generally be the calmest piece color-wise, since it's the largest surface area and the first thing people see. Black, olive, and neutral tones let everything underneath do the personality work.",
            "A reliable formula: neutral outerwear, muted mid-layer, and let your graphic tee be the one place you go bold. It keeps the whole fit readable instead of competing for attention at every layer.",
        ]),
    dict(slug="how-to-care-for-graphic-tees", title="How to Care for Your Graphic Tees So Prints Never Crack",
        desc="Washing and drying tips that keep screen-printed graphics from cracking, fading, or peeling over time.",
        link=("/apparel", "shop new prints"),
        body=[
            "Most \"the print cracked\" complaints trace back to the dryer, not the shirt. Heat is the single biggest threat to a printed graphic.",
            "Wash inside-out, always. This protects the print from direct friction against zippers, buttons, and other fabric in the wash, which is the main cause of surface cracking over repeated cycles.",
            "Cold water, always. Hot water accelerates ink breakdown and causes shrinkage, which puts stress on the print as the fabric contracts around it.",
            "Skip the dryer when you can, or use the lowest heat, tumble-low setting if you must. Air-drying flat or on a hanger adds essentially zero effort and dramatically extends how long a graphic stays crisp.",
            "Skip fabric softener on printed tees — it leaves a residue that can dull both the fabric feel and the surface of the print over time. A normal detergent is all a ring-spun cotton tee needs.",
            "Store folded rather than on a tight hanger for graphic-heavy tees, since hanging can stretch the shoulder area and distort the print's proportions over months of storage.",
        ]),
    dict(slug="unisex-streetwear-101", title="Unisex Streetwear 101: Why Our Fits Work for Everyone",
        desc="How unisex tee and hoodie sizing works, and how to translate between men's and women's sizing for a streetwear fit.",
        link=("/apparel", "shop unisex fits"),
        body=[
            "Unisex sizing in streetwear isn't a compromise fit — it's the actual point. Boxy, relaxed silhouettes are designed to hang the same intentional way regardless of body type.",
            "If you're used to fitted women's sizing, the easiest translation is to size down 1-2 from your unisex size if you want a closer fit, or wear your usual number for the classic oversized streetwear look.",
            "Length is often the more useful measurement to check than chest width for unisex pieces, since the boxier cut means chest room is rarely the limiting factor — how it falls at the hip is what changes the silhouette most.",
            "The reason unisex sizing works so well for graphic tees specifically: a boxier fit gives the print more flat surface area to sit on, so the graphic reads clearly instead of stretching or distorting across a fitted silhouette.",
            "If you're between sizes and unsure, the size guide above walks through measuring a tee you already own — that's a faster path to the right fit than guessing from the size label alone.",
        ]),
    dict(slug="meme-culture-meets-fashion", title="Meme Culture Meets Fashion: Internet-Inspired Streetwear",
        desc="Why internet culture and memes have become a major source of streetwear graphics, and what makes a meme-inspired design last.",
        link=("/", "shop culture-inspired tees"),
        body=[
            "Streetwear has always borrowed from whatever culture is loudest at the moment — skate culture, hip-hop, sneaker culture — and internet culture is simply the current version of that same pattern.",
            "What makes a meme-inspired graphic actually work as clothing, rather than as a disposable joke, is distance from the original reference. The best designs take the energy or attitude of an internet moment and turn it into something visually strong on its own, so it still lands even for someone who's never seen the source.",
            "This is also why timing matters less than people assume for well-designed graphics: a design built around a strong visual idea outlasts the meme that inspired it, while a design that's just literal text of a joke expires the moment the joke does.",
            "The tension in this space is real — lean too hard into a specific reference and a shirt becomes a costume; lean too far away from it and you lose what made it interesting in the first place. The designs that hold up longest usually sit right in the middle.",
            "It's also why this category rewards limited drops over permanent restocks — the cultural moment a design captures is part of its appeal, and scarcity keeps that feeling intact.",
        ]),
    dict(slug="building-a-capsule-streetwear-wardrobe", title="Building a Capsule Streetwear Wardrobe on a Budget",
        desc="How to build a small, versatile streetwear wardrobe with a handful of tees, one hoodie, and pieces that all mix together.",
        link=("/apparel", "start your capsule"),
        body=[
            "A capsule wardrobe works when every piece can pair with every other piece — the goal isn't fewer clothes, it's fewer clothes that don't go together.",
            "Start with a neutral base: 2-3 tees in black, white, and one neutral color like heather grey. These become the foundation you build every outfit from, regardless of which graphic pieces you add on top.",
            "Add 2-3 graphic tees as your statement pieces, chosen for designs you're genuinely drawn to rather than what's trending — capsule wardrobes fail fastest when a piece was bought for a moment instead of for repeat wear.",
            "One hoodie, in a muted tone, does more work than a second flashy one. It becomes your default cold-weather layer and pairs with almost everything in the base and graphic tee groups.",
            "Bottoms should be the most boring part of the capsule on purpose: one dark denim, one black or grey jogger. They're not meant to be noticed — they're meant to make everything on top look intentional.",
            "The test for any new piece before buying it: can you picture it working with at least three things you already own? If not, it's probably not a capsule piece, even if you like it.",
        ]),
    dict(slug="pullover-hoodie-buying-guide", title="Pullover Hoodie Buying Guide: What to Look for Before You Buy",
        desc="What actually separates a good pullover hoodie from a cheap one — fabric weight, fit, print quality, and durability.",
        link=("/apparel", "shop pullover hoodies"),
        body=[
            "Most hoodies look similar in a product photo. The differences that actually matter show up after a few washes, which is exactly why they're easy to miss when buying.",
            "Fabric weight is the first thing to check. Heavier weights (measured in GSM, grams per square meter) hold their shape longer and drape better, while lighter weights feel less substantial and can start pilling sooner.",
            "Fleece construction matters more than most buyers realize — a good interior fleece stays soft through repeated washing, while a cheaper one flattens and loses its warmth-to-weight ratio within a season.",
            "For graphic hoodies specifically, check how the print is applied. Screen printing on quality cotton-poly blends holds up far better over time than heat-transfer vinyl, which is more prone to cracking and peeling with wear.",
            "Fit is a design choice, not a quality signal — a classic pullover cut works for layering, while a cropped or slim cut is a style decision you should make based on how you already wear hoodies, not based on which one photographs better.",
            "Rib-knit cuffs and hem that hold their shape after stretching (rather than going loose and floppy) are a small detail that separates a hoodie that looks good for a year from one that looks tired after a month.",
        ]),
    dict(slug="v-neck-vs-crew-neck-streetwear", title="V-Neck vs Crew Neck Tees: Streetwear Style Breakdown",
        desc="Comparing v-neck and crew neck tees for streetwear — how neckline changes proportion, layering, and overall look.",
        link=("/apparel", "shop v-neck and crew neck tees"),
        body=[
            "Neckline is one of the most overlooked style decisions in a tee, and it changes the whole proportion of an outfit more than most people expect.",
            "Crew necks are the streetwear default for a reason: the higher, closed neckline keeps focus on the chest graphic and works cleanly under jackets, hoodies, and flannels without exposing extra skin or competing necklines.",
            "V-necks elongate the torso visually and open up the chest area, which can work well for graphics placed lower on the tee or for a slightly dressed-up streetwear look, but they show more skin and layer less cleanly under a hoodie.",
            "For graphic-heavy designs specifically, crew necks are usually the safer pick, since the graphic placement is designed around a straight, high neckline — a v-neck can cut into the bottom of a design that wasn't built for it.",
            "If you're building a capsule wardrobe, crew necks are the more versatile choice to buy multiples of; save v-necks for one or two pieces where you specifically want that different silhouette.",
        ]),
    dict(slug="streetwear-layering-guide-cold-weather", title="Streetwear Layering Guide for Cold Weather",
        desc="A practical layering order for streetwear in cold weather — base, mid, and outer layers that keep graphics visible.",
        link=("/apparel", "shop layering pieces"),
        body=[
            "Cold-weather streetwear is a layering problem more than a shopping problem — the same three or four pieces can look completely different depending on the order and fit you layer them in.",
            "Base layer: your graphic tee. This is your foundation and, in cold weather, it's often only partially visible — which is exactly why a bold graphic near the collar can peek through and still make an impact.",
            "Mid layer: a hoodie or flannel, slightly roomier than your tee so it layers over cleanly without pulling or bunching at the shoulders. This is the layer doing most of the warmth work.",
            "Outer layer: a jacket sized to fit comfortably over both previous layers without looking bulky — this is where sizing mistakes compound, so always check a jacket's fit with your actual mid-layer on, not alone.",
            "The proportion rule that keeps layered fits from looking sloppy: each layer should be slightly roomier than the one underneath it. A tight tee under a tight hoodie under a tight jacket restricts movement and looks stiff; graduated roominess is what makes layering look effortless.",
        ]),
    dict(slug="top-streetwear-trends-2026", title="Top Streetwear Trends to Watch in 2026",
        desc="What's shaping streetwear design and buying habits going into 2026, from graphic styles to fit preferences.",
        link=("/", "shop the latest drops"),
        body=[
            "Streetwear trends move fast, but the underlying shifts tend to be slower and more durable than any single season's hype cycle.",
            "Bold, single-focal-point graphics continue to outperform busy all-over prints. Buyers increasingly favor one strong image or line over crowded designs, likely because a clean graphic photographs better for social sharing and ages better in a closet.",
            "Relaxed, boxier fits remain dominant over slim-fit streetwear, but with slightly less extreme oversizing than a few years ago — a \"true oversized but not swimming in fabric\" middle ground is where a lot of new drops are landing.",
            "Internet and meme-culture references keep growing as a design source, but the designs with staying power are the ones that stand alone visually rather than depending entirely on recognizing the reference.",
            "Muted, grounded colorways for mid-layer pieces (hoodies, flannels) paired with one bold graphic tee continue to be the dominant layering formula, reinforcing that color restraint elsewhere makes graphic pieces hit harder.",
            "Smaller, limited drops over large permanent catalogs keep gaining ground, since scarcity and timing have become part of what makes a streetwear piece feel worth buying now rather than \"eventually.\"",
        ]),
    dict(slug="how-graphic-tees-became-a-streetwear-staple", title="How Graphic Tees Became a Streetwear Staple: A Short History",
        desc="A brief look at how the graphic tee evolved from band merch and skate culture into a core streetwear category.",
        link=("/apparel", "shop the current lineup"),
        body=[
            "The graphic tee's path to streetwear staple runs through band merch, skate culture, and hip-hop — three scenes that all needed cheap, expressive clothing that said something about who was wearing it.",
            "Band and tour merch proved that a tee could function as identity, not just clothing — wearing one signaled which scene, sound, or crew you belonged to, long before \"streetwear\" was a category name.",
            "Skate culture pushed graphic design toward bold, single-image graphics that worked at a glance — skating is fast and visual, and tee graphics from that era favored strong shapes over fine detail, a preference that still shapes design today.",
            "Hip-hop culture brought scale and confidence to graphic design — bigger prints, bolder typography, and a comfort with clothing as a statement rather than something to blend in with.",
            "What ties all three eras together, and what still defines a good graphic tee now, is the same idea: a strong, legible design that says something about the wearer without needing an explanation.",
        ]),
    dict(slug="gifts-for-the-sneakerhead", title="Gifts for the Sneakerhead in Your Life",
        desc="Gift ideas built around sneaker culture — graphic tees, colorway-matching pieces, and low-risk picks for any sneakerhead.",
        link=("/apparel", "shop sneaker-culture graphics"),
        body=[
            "Buying for a sneakerhead doesn't mean buying sneakers — in fact, that's the riskiest gift in the category, since size, silhouette, and colorway preferences are hyper-specific. Apparel that complements their collection is a much safer bet.",
            "Sneaker-culture graphic tees are the easiest low-risk win: a design that nods to sneaker culture broadly (rather than one specific shoe) works with almost any rotation, since it's a statement about the interest, not a specific pair.",
            "Neutral colorways are the safe default — black, white, and grey graphic tees pair with more sneaker colorways than any bold color choice, which matters if you don't know their exact rotation.",
            "Sizing is more forgiving with tees than with shoes: when unsure, their normal streetwear size (often one up from fitted sizing) is a safe assumption, and a slightly-too-big tee reads as an intentional oversized fit rather than a mistake.",
            "If you want to go a step further, pair a graphic tee with a simple care note about washing inside-out in cold water — small, thoughtful, and it shows the gift was actually considered.",
        ]),
    dict(slug="sustainable-streetwear-ring-spun-cotton", title="Sustainable Streetwear: What Ring-Spun Cotton Means for the Planet",
        desc="How fabric choice and garment longevity connect to sustainability in streetwear, and why buying fewer, better tees matters.",
        link=("/apparel", "shop long-lasting basics"),
        body=[
            "The most overlooked lever in sustainable clothing isn't the fabric itself — it's how long a garment actually stays in rotation before it's discarded.",
            "A cheaper, lower-quality tee that pills, fades, and gets tossed after a season has a worse lifecycle footprint than a higher-quality tee worn for years, even before accounting for fiber source, because the manufacturing and shipping impact repeats every time a replacement is bought.",
            "Ring-spun cotton's practical sustainability benefit is durability: a tighter, stronger yarn resists pilling and holds its shape through more wash cycles, which directly extends how long a garment stays wearable before it's replaced.",
            "Print-on-demand production, which is how many smaller streetwear brands operate, also reduces overproduction waste compared to large speculative print runs — fewer unsold garments end up unsold or discarded, since pieces are produced closer to actual demand.",
            "The most sustainable move available to any buyer, regardless of brand, is still the simplest one: buy fewer pieces you'll actually wear on repeat, and take care of them so they last — fabric quality just makes that easier to do.",
        ]),
    dict(slug="from-design-to-drop", title="From Design to Drop: How a New Graphic Tee Gets Made",
        desc="A behind-the-scenes look at how a streetwear graphic goes from initial idea to a finished, printed tee ready to ship.",
        link=("/", "see the latest drop"),
        body=[
            "Every tee in the shop goes through the same rough path: an idea, a design pass, color and fit testing, and then production — the part people see is only the last step.",
            "It starts with a concept, usually something that's been rattling around for a while — a phrase, a cultural reference, a visual idea — until it feels strong enough to justify becoming a full design rather than a passing thought.",
            "The design pass is where a lot of ideas die. A concept that sounds good in theory often doesn't hold up as a single, legible graphic — if it needs a paragraph of explanation to land, it usually gets reworked or scrapped.",
            "Color and fit testing comes next: the same graphic gets tested across several base garment colors, because a design that pops on white might disappear on black, or vice versa. Only the strongest combinations make it to the actual product listing.",
            "Production, for a print-on-demand model, happens after the design is finalized and listed — each order is printed to fulfill actual demand rather than pre-made in bulk, which is part of why new drops focus on a handful of strong designs rather than dozens of untested ones at once.",
        ]),
]

assert len(POSTS) == 20, len(POSTS)

GA_ID = "G-J1R9FDDNLP"
GA_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID_PLACEHOLDER"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID_PLACEHOLDER');
</script>
""".replace("GA_ID_PLACEHOLDER", GA_ID)

NAV = f"""<nav class="site-nav">
  <a href="{SITE}/" class="brand">TōhMee Blog</a>
  <a href="{STORE}/" target="_blank" rel="noopener">Shop TōhMee &rarr;</a>
</nav>"""

FOOTER = f"""<footer class="site-footer">
  <p>&copy; {date.today().year} TōhMee. <a href="{STORE}/">Shop the store</a></p>
</footer>"""

POST_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
{ga}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | TōhMee Blog</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<link rel="stylesheet" href="{site}/style.css">
</head>
<body>
{nav}
<main class="post">
  <p class="breadcrumb"><a href="{site}/">Blog</a> / {title}</p>
  <h1>{title}</h1>
  {body}
  <p class="cta"><a href="{store}{link_href}" target="_blank" rel="noopener">{link_text} &rarr;</a></p>
</main>
{footer}
</body>
</html>
"""

INDEX_ITEM = """<li>
  <a href="{site}/posts/{slug}/">{title}</a>
  <p>{desc}</p>
</li>"""

INDEX_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
{ga}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TōhMee Blog — Streetwear Guides & Style Tips</title>
<meta name="description" content="Streetwear guides, sizing tips, and style advice from TōhMee — graphic tees and hoodies for sneakerheads and pop-culture fans.">
<link rel="canonical" href="{site}/">
<link rel="stylesheet" href="{site}/style.css">
</head>
<body>
{nav}
<main>
  <h1>TōhMee Blog</h1>
  <p class="lede">Streetwear guides, sizing tips, and style advice — straight from the team behind the graphics.</p>
  <ul class="post-list">
    {items}
  </ul>
</main>
{footer}
</body>
</html>
"""

CSS = """
:root{color-scheme:light dark;--fg:#1a1a1a;--bg:#fdfdfd;--muted:#666;--accent:#c1272d;--border:#e5e5e5;}
@media (prefers-color-scheme:dark){:root{--fg:#eee;--bg:#111;--muted:#aaa;--border:#333;}}
*{box-sizing:border-box;}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg);line-height:1.6;}
.site-nav{display:flex;justify-content:space-between;align-items:center;padding:1.25rem 1.5rem;border-bottom:1px solid var(--border);max-width:760px;margin:0 auto;}
.site-nav .brand{font-weight:700;text-decoration:none;color:var(--fg);letter-spacing:.02em;}
.site-nav a{color:var(--fg);text-decoration:none;}
.site-nav a:hover{color:var(--accent);}
main{max-width:760px;margin:0 auto;padding:2rem 1.5rem 3rem;}
h1{font-size:1.9rem;line-height:1.25;margin:0 0 .75rem;}
.lede{color:var(--muted);font-size:1.05rem;}
.breadcrumb{font-size:.85rem;color:var(--muted);margin-bottom:1.5rem;}
.breadcrumb a{color:var(--muted);}
.post p{margin:0 0 1.1rem;font-size:1.02rem;}
.cta{margin-top:2rem;}
.cta a{display:inline-block;padding:.7rem 1.3rem;background:var(--accent);color:#fff;text-decoration:none;border-radius:4px;font-weight:600;}
.cta a:hover{opacity:.9;}
.post-list{list-style:none;padding:0;margin:2rem 0 0;}
.post-list li{padding:1.1rem 0;border-bottom:1px solid var(--border);}
.post-list a{font-size:1.15rem;font-weight:600;color:var(--fg);text-decoration:none;}
.post-list a:hover{color:var(--accent);}
.post-list p{color:var(--muted);margin:.35rem 0 0;font-size:.95rem;}
.site-footer{max-width:760px;margin:0 auto;padding:1.5rem;color:var(--muted);font-size:.85rem;border-top:1px solid var(--border);}
.site-footer a{color:var(--muted);}
"""

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# style.css
write("style.css", CSS)

# posts
index_items = []
sitemap_urls = [f"{SITE}/"]
for p in POSTS:
    canonical = f"{SITE}/posts/{p['slug']}/"
    body_html = "\n  ".join(f"<p>{para}</p>" for para in p["body"])
    link_href, link_text = p["link"]
    html_out = POST_TEMPLATE.format(
        title=html.escape(p["title"]), desc=html.escape(p["desc"]),
        canonical=canonical, nav=NAV, footer=FOOTER, site=SITE, store=STORE,
        body=body_html, link_href=link_href, link_text=link_text, ga=GA_SNIPPET,
    )
    write(f"posts/{p['slug']}/index.html", html_out)
    index_items.append(INDEX_ITEM.format(site=SITE, slug=p["slug"], title=html.escape(p["title"]), desc=html.escape(p["desc"])))
    sitemap_urls.append(canonical)

write("index.html", INDEX_TEMPLATE.format(site=SITE, nav=NAV, footer=FOOTER, items="\n    ".join(index_items), ga=GA_SNIPPET))

# sitemap.xml
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in sitemap_urls:
    sm.append(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>")
sm.append("</urlset>")
write("sitemap.xml", "\n".join(sm))

# robots.txt
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print(f"Generated {len(POSTS)} posts + index + sitemap + robots.txt")
