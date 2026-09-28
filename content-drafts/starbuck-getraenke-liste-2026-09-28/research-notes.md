# Merge: "starbuck getränke liste" (260/mo, KD 21) → /blog/starbucks-getraenke#getraenke-liste

Run date: 2026-09-28. The calendar suggested starbucks-menu. We merged into **starbucks-getraenke** instead, because that page *is* the drinks list, and starbucks-menu is the food + drinks hub. The menu page now links to the new list anchor.

## SERP (WebSearch, 2026-09-28)
starbucks.de/de/menu-drinks-categories, weproudlyservestarbucks.com (foodservice, not the coffeehouse menu), germanmenus.de (403), fastfoodpreis-info.de (2026-03-04, lists **24 drinks** in 4 groups), eraofwe.com top-10, starbuckspreise.de. The intent is a list or know-simple query, and a table fits the likely snippet.

## Primary source: the official list (curl of each starbucks.de/de/menu-drinks-<cat> page, 2026-09-28)
- Hot Coffees 14: Filterkaffee, Caffè Misto, Flat White, Caffè Latte, Latte Macchiato, Cappuccino, Vanilla Latte, Caramel Macchiato, Caffè Mocha, White Chocolate Mocha, Caffè Americano, Espresso, Espresso Macchiato, Espresso con Panna
- Hot Chocolates 3: Classic, White, Signature Hot Chocolate
- Hot Teas 8: Chai Tea Latte, Matcha Tea Latte, English Breakfast, Earl Grey, Hibiscus, Emperor's Clouds & Mist, Mint Blend, Youthberry
- Iced Coffees 9: Cold Brew, Cold Brew Latte, Iced Latte Macchiato, Iced Cappuccino, Iced Latte, Iced Caramel Macchiato, Iced White Mocha, Iced Mocha, Iced Americano
- Iced Chocolates 2: Signature Iced White Chocolate, Iced Classic Chocolate
- Iced Teas 6: Iced Chai Tea Latte, Iced Matcha Tea Latte, Iced Green/Peach Green/Hibiscus/Black Tea Lemonade
- Refresha 4: Mango Dragonfruit, Dragon Coconut, Strawberry Acai, Pink Coconut
- Frappuccino 15: Espresso, Coffee, Mocha, White Mocha, Java Chip, Caramel, Java Chip Cream, Caramel Cream, White Chocolate Cream, Vanilla Cream, Strawberries & Cream, Chai Tea Cream, Matcha Tea Cream, Cookies and Cream, Chocolate Cream
- **Total: 61.** "Highlights" and "Flaschengetränke" are JS-rendered and returned no items through curl.

## Information gain
This is the only list that is complete and dated. Competitors list 20–25 drinks.

## Changes made
- New §7 "Starbucks Getränke Liste: Alle 61 Getränke der offiziellen Karte" (table: category, what it is, count, all drinks). The later sections are renumbered 8 and 9.
- The answer box changed from "über 50" to "61 in acht Kategorien (Stand 28.09.2026)".
- §6 "Mint Citrus" changed to "Mint Blend", matching the official name.
- A note that Salted Caramel Cold Brew, Iced Shaken Espresso, Iced Brown Sugar Oat Shaken Espresso and Cool Lime Refresha are **not** on the official DE card today (they are still in our §3/§5 text and price table).
- +4 FAQs (14 total), with schema matching the page verbatim. Meta description + dateModified updated, and a sitemap lastmod was added.

## Open flags
- Our §3, §5 and §8 price table still feature drinks that are not currently on the card (listed above), and "Pink Drink" is not listed under that name (the official card has Strawberry Acai and Pink Coconut Refresha). This needs a decision: remove them, or label them as seasonal.
- /blog/starbucks-refresha says "Alle 6 Refresha-Sorten", but the official card shows 4 today.
- The price table is unverified against a 2026 source (starbucks.de publishes no prices). This is a pre-existing issue.
