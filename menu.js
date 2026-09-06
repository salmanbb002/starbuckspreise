/* Starbucks Preise 2026 - menu data + renderer (home page only) */
const slug = s => s.replace(/[^\w.-]+/g,'-').replace(/-+/g,'-').replace(/^-|-$/g,'');
const IMG = base => `/img/${slug(base)}.webp`;

const DATA = [
 {id:'getraenke', h:'Kaffee-Klassiker: Espresso-Getränke im Überblick', groups:[
   {g:'Hot Espresso Drinks &#8211; Starbucks Preis Deutschland', items:[
     ["Toffee Nut Latte","Toffee-Nut-Latte","6,20 €","993kJ/237kcal"],
     ["Lebkuchen Latte","Lebkuchen-Latte","6,70 €","1148kJ/274kcal"],
     ["Pumpkin Spice Latte","Pumpkin-Spice-Latte","6,20 €","1116kJ/266kcal"],
     ["Flat White","Flat-White","4,71 €","318kJ/76kcal"],
     ["Caffè Latte","Caffe-Latte","4,59 €","636kJ/151kcal"],
     ["Tiramisu Velvet Latte","Tiramisu-Velvet-Latte","6,20 €","1033kJ/245kcal"],
     ["Cappuccino","Cappuccino","3,90 €","546kJ/130kcal"],
     ["Iced Cappuccino","Iced-Cappuccino","4,65 €","302kJ/72kcal"],
     ["Latte Macchiato","Latte-Macchiato","4,70 €","616kJ/147kcal"],
     ["Caramel Macchiato","Caramel-Macchiato","4,99 €","901kJ/214kcal"],
     ["Caffè Americano","Caffe-Americano","3,10 €","44kJ/11kcal"],
     ["White Chocolate Mocha","White-Chocolate-Mocha","5,99 €","1448kJ/345kcal"],
     ["Caffè Mocha","Caffe-Mocha","5,90 €","1187kJ/283kcal"],
     ["Espresso Macchiato","Espresso-Macchiato","3,20 €","25kJ/6kcal"],
     ["Espresso","Espresso","2,75 €","15kJ/4kcal"]
   ]}
 ]},
 {id:'iced-espresso', h:'Kalte Espresso-Drinks für unterwegs', groups:[
   {items:[
     ["Iced Toffee Nut Latte","Iced-Toffee-Nut-Latte","6,70 €","727kJ/172kcal"],
     ["Iced Mocha Mousse Latte","Iced-Mocha-Mousse-Latte","6,20 €","1180kJ/281kcal"],
     ["Iced Lebkuchen Latte","Iced-Lebkuchen-Latte","6,70 €","749kJ/178kcal"],
     ["Iced Caffè Latte","Iced-Caffe-Latte","5,40 €","536kJ/128kcal"],
     ["Iced Pumpkin Spice Latte","Iced-Pumpkin-Spice-Latte","6,20 €","837kJ/199kcal"],
     ["Iced Caramel Macchiato","Iced-Caramel-Macchiato","5,79 €","847kJ/201kcal"],
     ["Iced Latte Macchiato","Iced-Latte-Macchiato","7,40 €","552kJ/132kcal"],
     ["Iced Caffè Americano","Iced-Caffe-Americano","4,39 €","44kJ/11kcal"],
     ["Iced White Chocolate Mocha","Iced-White-Chocolate-Mocha","5,99 €","1680kJ/401kcal"],
     ["Iced Caffè Mocha","Iced-Caffe-Mocha","5,79 €","1431kJ/342kcal"]
   ]}
 ]},
 {id:'filterkaffee', h:'Filterkaffee &amp; Cold Brew: die einfachen Klassiker', groups:[
   {items:[
     ["Frisch gebrühter Filterkaffee – Pike Place® Roast","Frisch-gebruhter-Filterkaffee-Pike-Place®-Roast","5 €","132kJ/31kcal"],
     ["Cold Brew Latte","Cold-Brew-Latte","5,90 €","520kJ/123kcal"],
     ["Cold Brew","Cold-Brew","4,60 €","97kJ/22kcal"]
   ]}
 ]},
 {id:'teavana-hot', h:'Warme Tees und Matcha-Spezialitäten', groups:[
   {items:[
     ["Lebkuchen Matcha Latte","Lebkuchen-Matcha-Latte","7,40 €","1299kJ/310kcal"],
     ["Pumpkin Spice Matcha Latte","Pumpkin-Spice-Matcha-Latte","7,90 €","1271kJ/303kcal"],
     ["Toffee Nut Matcha Latte","Toffee-Nut-Matcha-Latte","7,40 €","1144kJ/272kcal"],
     ["Winter Spiced Apple Tea","Winter-Spiced-Apple-Tea","4,20 €","38kJ/9kcal"],
     ["Chai Tea Latte","Chai-Tea-Latte","6,90 €","764kJ/181kcal"],
     ["Matcha Green Tea Latte","Matcha-Green-Tea-Latte","7,90 €","699kJ/166kcal"],
     ["English Breakfast Tea","English-Breakfast-Tea","4,90 €","23kJ/5kcal"],
     ["Mint Herbal Blend Tea","Mint-Herbal-Blend-Tea","3,69 €","18kJ/4kcal"],
     ["Hibiscus Herbal Blend Tea","Hibiscus-Herbal-Blend-Tea","4,90 €","24kJ/6kcal"],
     ["Earl Grey Tea","Earl-Grey-Tea","3,69 €","17kJ/4kcal"],
     ["Emperor's Clouds & Mist Tea","Emperor26-Mist","4,90 €","15kJ/4kcal"]
   ]}
 ]},
 {id:'teavana-iced', h:'Eistees und kalte Matcha-Kreationen', groups:[
   {items:[
     ["Toffee Nut Cream Iced Matcha Latte","Toffee-Nut-Cream-Iced-Matcha-Latte","7,40 €","1147kJ/274kcal"],
     ["Iced Pumpkin Spice Matcha Latte","Iced-Pumpkin-Spice-Matcha-Latte","8,90 €","1003kJ/240kcal"],
     ["Lebkuchen Cream Iced Matcha Latte","Lebkuchen-Cream-Iced-Matcha-Latte","7,40 €","1140kJ/273kcal"],
     ["Iced Chai Tea Latte","Iced-Chai-Tea-Latte","6,40 €","760kJ/180kcal"],
     ["Iced Matcha Green Tea Latte","Iced-Matcha-Green-Tea-Latte","6,90 €","513kJ/122kcal"],
     ["Iced Green Tea","Iced-Green-Tea","3,99 €","306kJ/72kcal"],
     ["Iced Peach Tea","Iced-Peach-Tea","6,90 €","182kJ/43kcal"]
   ]}
 ]},
 {id:'refresha', h:'Fruchtige Refresha-Erfrischungsgetränke', groups:[
   {items:[
     ["Dragon Coconut Starbucks Refresha®","Dragon-Coconut-Starbucks-Refresha®","7,40 €","664kJ/158kcal"],
     ["Strawberry Acai Starbucks Refresha®","Strawberry-Acai-Starbucks-Refresha®","6,40 €","369kJ/87kcal"],
     ["Pink Coconut Starbucks Refresha®","Pink-Coconut-Starbucks-Refresha®","7,90 €","606kJ/144kcal"],
     ["Mango Dragonfruit Starbucks Refresha®","Mango-Dragonfruit-Starbucks-Refresha®","6,90 €","427kJ/101kcal"]
   ]}
 ]},
 {id:'frappuccino', h:'Frappuccino: die cremigen Eiskaffee-Mixgetränke', groups:[
   {g:'Coffee Frappuccino®', items:[
     ["Toffee Nut Coffee Frappuccino®","Toffee-Nut-Coffee-Frappuccino®","7,40 €","1339kJ/319kcal"],
     ["Pumpkin Spice Frappuccino®","Pumpkin-Spice-Frappuccino®","7,40 €","1563kJ/372kcal"],
     ["Tiramisu Frappuccino®","Tiramisu-Frappuccino®","8,50 €","1693kJ/404kcal"],
     ["Lebkuchen Coffee Frappuccino®","Lebkuchen-Coffee-Frappuccino®","7,40 €","1382kJ/330kcal"],
     ["Caramel Frappuccino®","Caramel-Frappuccino®","6,90 €","1517kJ/362kcal"],
     ["White Chocolate Mocha Frappuccino®","White-Chocolate-Mocha-Frappuccino®","5,79 €","1556kJ/371kcal"],
     ["Coffee Frappuccino®","Coffee-Frappuccino®","5,29 €","1255kJ/299kcal"],
     ["Mocha Frappuccino®","Mocha-Frappuccino®","6,90 €","1383kJ/330kcal"],
     ["Espresso Frappuccino®","Espresso-Frappuccino®","5,69 €","608kJ/144kcal"]
   ]},
   {g:'Cream Frappuccino®', items:[
     ["Pumpkin Spice Cream Frappuccino®","Pumpkin-Spice-Cream-Frappuccino®","7,40 €","1524kJ/364kcal"],
     ["Lebkuchen Cream Frappuccino®","Lebkuchen-Cream-Frappuccino®","7,90 €","1364kJ/326kcal"],
     ["Toffee Nut Cream Frappuccino®","Toffee-Nut-Cream-Frappuccino®","7,40 €","1321kJ/316kcal"],
     ["Strawberries and Cream Frappuccino®","Strawberries-and-Cream-Frappuccino®","4,79 €","1389kJ/331kcal"],
     ["Vanilla Cream Frappuccino®","Vanilla-Cream-Frappuccino®","5,35 €","1307kJ/312kcal"],
     ["Chocolate Cream Frappuccino®","Chocolate-Cream-Frappuccino®","4,85 €","1447kJ/346kcal"],
     ["Java Chip Chocolate Cream Frappuccino®","Java-Chip-Chocolate-Cream-Frappuccino®","5,35 €","1684kJ/403kcal"],
     ["Caramel Cream Frappuccino®","Caramel-Cream-Frappuccino®","6,90 €","1500kJ/358kcal"],
     ["Matcha Cream Frappuccino®","Matcha-Cream-Frappuccino®","6,90 €","1359kJ/325kcal"],
     ["Chai Tea Cream Frappuccino®","Chai-Tea-Cream-Frappuccino®","6,40 €","1336kJ/319kcal"],
     ["White Chocolate Mocha Cream Frappuccino®","White-Chocolate-Mocha-Cream-Frappuccino®","5,29 €","1539kJ/367kcal"],
     ["Cookies and Cream Frappuccino®","Cookies-and-Cream-Frappuccino®","6,90 €","1621kJ/387kcal"]
   ]}
 ]},
 {id:'schokolade', h:'Heiße Schokolade und Milchgetränke', groups:[
   {g:'Hot Chocolate', items:[
     ["Signature Hot Chocolate","Signature-Hot-Chocolate","6,40 €","1471kJ/351kcal"],
     ["Hot White Chocolate","Hot-White-Chocolate","6,40 €","1498kJ/357kcal"],
     ["Classic Hot Chocolate","Classic-Hot-Chocolate","4,99 €","1308kJ/311kcal"]
   ]},
   {g:'Iced Chocolate', items:[
     ["Iced White Chocolate","Iced-White-Chocolate","6,40 €","1736kJ/414kcal"],
     ["Classic Iced Chocolate","Classic-Iced-Chocolate","5,90 €","1532kJ/366kcal"]
   ]},
   {g:'Milch', items:[
     ["Hot Milk","Hot-Milk","8,50 €","849kJ/203kcal"]
   ]}
 ]},
 {id:'essen', divider:true, h:'Snacks &amp; Gebäck: die Food-Auswahl'},
 {id:'desserts', h:'Süßes zum Kaffee: Desserts &amp; Kuchen', groups:[
   {g:'Breakfast Bakery', items:[
     ["Lebkuchen Zimtschnecke","Lebkuchen-Zimtschnecke","4,80 €","1649kJ/394kcal"],
     ["Ofenfrisch – Signature Cone Pistachio","Ofenfrisch-Signature-Cone-Pistachio","2,10 €","946kJ/227kcal"],
     ["Ofenfrisch – Signature Cone Hazelnut","Ofenfrisch-Signature-Cone-Hazelnut","2,10 €","963kJ/231kcal"],
     ["Ofenfrisch – Pain au chocolat vegan","Ofenfrisch-Pain-au-chocolat-vegan","2,50 €","1322kJ/316kcal"],
     ["Ofenfrisch – Croissant vegan","Ofenfrisch-Croissant-vegan","2,40 €","1026kJ/245kcal"],
     ["Zimtschnecke","Zimtschnecke","3,60 €","1488kJ/355kcal"],
     ["Pain au Chocolat","Pain-au-Chocolat","2,50 €","1305kJ/312kcal"],
     ["Croissant vegan","Croissant-vegan","2,40 €","1056kJ/253kcal"],
     ["Pain au Chocolat vegan","Pain-au-Chocolat-vegan","2,50 €","1222kJ/292kcal"]
   ]},
   {g:'Muffins', items:[
     ["Blaubeer Muffin","Blaubeer-Muffin","3,80 €","1739kJ/415kcal"],
     ["Chocolate Cheesecake Muffin","Chocolate-Cheesecake-Muffin","3,80 €","1928kJ/462kcal"],
     ["Triple Chocolate Muffin","Triple-Chocolate-Muffin","3,99 €","2063kJ/494kcal"]
   ]},
   {g:'Cookies', items:[
     ["Choc Chunk Cookie","Choc-Chunk-Cookie","2,90 €","1349kJ/322kcal"],
     ["Double Choc Cookie","Double-Choc-Cookie","2,90 €","1340kJ/319kcal"],
     ["Red Velvet Cookie","Red-Velvet-Cookie","2,90 €","1447kJ/346kcal"]
   ]},
   {g:'Kuchen', items:[
     ["Red Velvet Cookie & Cream Cake","Red-Velvet-Cookie-Cream-Cake","5,40 €","2239kJ/533kcal"],
     ["Blueberry-Lemon Curd Cheesecake","Blueberry-Lemon-Curd-Cheesecake","4,90 €","1750kJ/418kcal"],
     ["Apple Caramel Cake","Apple-Caramel-Cake","4,90 €","2093kJ/499kcal"],
     ["Chocolate Lover Cake","Chocolate-Lover-Cake","4,90 €","2479kJ/590kcal"],
     ["Red Velvet Cake","Red-Velvet-Cake","3,70 €","1575kJ/377kcal"],
     ["Carrot Cake","Carrot-Cake","3,99 €","3409kJ/817kcal"],
     ["New York Cheesecake","New-York-Cheesecake","4,80 €","1545kJ/370kcal"],
     ["Ofenfrisch – Mini Pastel de Nata","Ofenfrisch-Mini-Pastel-de-Nata","1,80 €","362kJ/86kcal"],
     ["Schoko Torte","Schoko-Torte","3,99 €","2716kJ/652kcal"],
     ["Banana Bread","Banana-Bread","3,00 €","1553kJ/370kcal"],
     ["Zitronenkuchen","Zitronenkuchen","3,60 €","1638kJ/392kcal"],
     ["Marmorkuchen","Marmorkuchen","3,20 €","1640kJ/392kcal"],
     ["Chocolate Brownie","Chocolate-Brownie","4,39 €","1281kJ/308kcal"],
     ["Cake Pop – Polar","Cake-Pop-Polar","2,80 €","685kJ/164kcal"]
   ]}
 ]},
 {id:'sandwiches', h:'Herzhafte Sandwiches &amp; Snacks', groups:[
   {items:[
     ["Breakfast Croissant","Breakfast-Croissant","4,90 €","1666kJ/399kcal"],
     ["Ofenfrisch – Tomato Franz","Ofenfrisch-Tomato-Franz","2,90 €","1417kJ/339kcal"],
     ["Ham & Cheese Pocket","Ham-Cheese-Pocket","4,20 €","1757kJ/418kcal"],
     ["Sauerteig Cranberry & Brie Sandwich","Sauerteig-Cranberry-Brie-Sandwich","4,90 €","1032kJ/276kcal"],
     ["Spicy Curry Falafel Naan","Spicy-Curry-Falafel-Naan","4,90 €","1702kJ/405kcal"],
     ["Sandwich Käse","Sandwich-Kase","4,39 €","1965kJ/472kcal"],
     ["Sandwich Pute & Ei","Sandwich-Pute-Ei","4,10 €","2137kJ/512kcal"],
     ["Sandwich Schinken & Gouda","Sandwich-Schinken-Gouda","4,10 €","2092kJ/501kcal"],
     ["Laugenzopf Hähnchen Käse","Laugenzopf-Hahnchen-Kase","4,90 €","1687kJ/402kcal"],
     ["Veganes Italian Antipasti Sandwich","Veganes-Italian-Antipasti-Sandwich","3,69 €","1751kJ/418kcal"],
     ["Sandwich Bacon & Egg","Sandwich-Bacon-Egg","4,90 €","2154kJ/514kcal"],
     ["Focaccia Caprese Style","Focaccia-Caprese-Style","5,10 €","1854kJ/440kcal"],
     ["Lachs Bagel","Lachs-Bagel","5,60 €","1449kJ/245kcal"],
     ["Ofenfrisch – Laugentwister Frischkäse","Ofenfrisch-Laugentwister-Frischkase","3,90 €","1343kJ/321kcal"],
     ["Melted Cheese Croissant","Melted-Cheese-Croissant","3,20 €","1355kJ/324kcal"]
   ]}
 ]},
 {id:'snacks', h:'Kleine Snacks, Riegel &amp; Süßigkeiten', groups:[
   {items:[
     ["Gold Coin","Gold-Coin","3.650 €","501kJ/119kcal"],
     ["Cookie Straw","Cookie-Straw","3,90 €","377kJ/90kcal"],
     ["Karamell Waffeln","Karamell-Waffeln","2,40 €","1477kJ/352kcal"],
     ["Max´s Menthol Mints","Max´s-Menthol-Mints","3,13 €","581kJ/139kcal"],
     ["Max´s Lemon Mints","Max´s-Lemon-Mints","3,02 €","581kJ/139kcal"],
     ["Joghurt – Tropical Mango","Joghurt-Tropical-Mango","3,20 €","1085kJ/260kcal"],
     ["Joghurt – Verry Berry","Joghurt-Verry-Berry","3,20 €","1072kJ/257kcal"],
     ["Mermaids","Mermaids","2,30 €","716kJ/168kcal"],
     ["Lil´Monster Cooki","Lil´Monster-Cooki","2,90 €","1033kJ/248kcal"],
     ["Roasted & Salted mixed nuts","Roasted-Salted-mixed-nuts","2,30 €","933kJ/225kcal"],
     ["Chia Lemon Cookie vegan","Chia-Lemon-Cookie-vegan","2,99 €","987kJ/236kcal"],
     ["Fruit & Nut Mix","Fruit-Nut-Mix","2,30 €","844kJ/203kcal"],
     ["Cashew Butter Cups Raspberry Rumble","Cashew-Butter-Cups-Raspberry-Rumble","2,25 €","2614kJ/630kcal"],
     ["Peanut Butter Cups Salted Caramel","Peanut-Butter-Cups-Salted-Caramel","2,50 €","2640kJ/636kcal"],
     ["Oat Bar Cacao","Oat-Bar-Cacao","2,80 €","711kJ/170kcal"],
     ["Oat Bar Peanut","Oat-Bar-Peanut","2,80 €","792kJ/190kcal"]
   ]}
 ]},
 {id:'flaschen', divider:true, h:'Wasser, Saft &amp; Flaschengetränke'},
 {id:'wasser', h:'Wasser', groups:[
   {items:[
     ["Stilles Wasser Volvic 0,75l EINWEG","Stilles-Wasser-Volvic-075l-EINWEG","0,25 €","0kJ/0kcal"],
     ["Stilles Wasser Volvic 0,5l EINWEG","Stilles-Wasser-Volvic-05l-EINWEG","0,25 €","0kJ/0kcal"],
     ["Sprudelwasser Adelholzener 0,5l EINWEG","Sprudelwasser-Adelholzener-05l-EINWEG","0,15 €","0kJ/0kcal"]
   ]}
 ]},
 {id:'erfrischung', h:'Erfrischungsgetränke', groups:[
   {items:[
     ["Volvic Touch Mango","Volvic-Touch-Mango","1,19 €","19kJ/4kcal"],
     ["Volvic Touch Cherry","Volvic-Touch-Cherry","1,19 €","8kJ/2kcal"],
     ["Protein Drink Caramel Hazelnut","Protein-Drink-Caramel-Hazelnut","2,94 €","706kJ/168kcal"],
     ["Protein Drink Caffe Latte","Protein-Drink-Caffe-Latte","2,94 €","706kJ/168kcal"],
     ["Untouched Blueberry","Untouched-Blueberry","3,20 €","625kJ/145kcal"],
     ["Volvic Active 0,75l EINWEG","Volvic-Active-075l-EINWEG","1,99 €","54kJ/12kcal"],
     ["Volvic Recharge 0,75l EINWEG","Volvic-Recharge-075l-EINWEG","1,54 €","39kJ/9kcal"],
     ["Untouched Water+Limette Minze 0,50l EINWEG","Untouched-WaterLimette-Minze-050l-EINWEG","2,00 €","10kJ/5kcal"],
     ["Adelholzener Multivitamin 0,5l EINWEG","Adelholzener-Multivitamin-05l-EINWEG","1,74 €","770kJ/185kcal"],
     ["Adelholzener Mango 0,5l EINWEG","Adelholzener-Mango-05l-EINWEG","1,90 €","690kJ/165kcal"],
     ["Apfelschorle Adelholzener 0,5l EINWEG","Apfelschorle-Adelholzener-05l-EINWEG","1,60 €","485kJ/115kcal"]
   ]}
 ]},
 {id:'saefte', h:'Frische Säfte und Smoothies', groups:[
   {items:[
     ["Strawberry Smash","Strawberry-Smash","6,50 €","505kJ/120kcal"],
     ["Grandmade Orangensaft 0,25l EINWEG","Grandmade-Orangensaft-025l-EINWEG","3,29 €","420kJ/102kcal"],
     ["Ginger Volcano","Ginger-Volcano","8,50 €","74kJ/18kcal"]
   ]}
 ]},
 {id:'togo', divider:true, h:'Zum Mitnehmen: Verpackung &amp; To-Go'},
 {id:'verpackung', h:'Tüten &amp; Verpackungsmaterial', groups:[
   {items:[
     ["Große Papiertüte","Grose-Papiertute","0,42 €",""],
     ["Kleine Papiertüte","Kleine-Papiertute","0,50 €",""]
   ]}
 ]},
 {id:'kaffee-hause', divider:true, h:'Kaffeebohnen für zu Hause'},
 {id:'kaffeebohnen', h:'Röstungen im Vergleich: Blonde, Medium &amp; Dark', groups:[
   {g:'Blonde Roast', items:[
     ["Starbucks® Blonde 2026 250g","Starbucks®-Blonde-2025-250g","9,90 €",""],
     ["Starbucks® Blonde Espresso Roast 250g","Starbucks®-Blonde-Espresso-Roast-250g","9,90 €",""]
   ]},
   {g:'Medium Roast', items:[
     ["Starbucks® Single Origin Kenya 250g","Starbucks®-Single-Origin-Kenya-250g","9,90 €",""],
     ["Starbucks® Single Origin Guatemala Antigua 250g","Starbucks®-Single-Origin-Guatemala-Antigua-250g","9,90 €",""],
     ["Starbucks® Pike Place® Roast 250g","Starbucks®-Pike-Place®-Roast-250g","6,99 €",""]
   ]},
   {g:'Dark Roast', items:[
     ["Starbucks® Single Origin Sumatra 250g","Starbucks®-Single-Origin-Sumatra-250g","9,90 €",""],
     ["Starbucks® Espresso Roast 250g","Starbucks®-Espresso-Roast-250g","9,90 €",""],
     ["Starbucks® Caffè Verona™ 250g","Starbucks®-Caffe-Verona™-250g","6,99 €",""],
     ["Starbucks® Decaf Espresso Roast 250g","Starbucks®-Decaf-Espresso-Roast-250g","9,99 €",""]
   ]}
 ]},
 {id:'merch', divider:true, h:'Merchandise: Tassen, Becher &amp; mehr'},
 {id:'mehrwegbecher', h:'Wiederverwendbare Mehrwegbecher', groups:[
   {items:[
     ["Reusable Hot Cup Red","Reusable-Hot-Cup-Red","2,40 €",""],
     ["Reusable Cold Cup Gingerbread","Reusable-Cold-Cup-Gingerbread","2,50 €",""],
     ["Reusable Cup White","Reusable-Cup-White","2,50 €",""],
     ["Reusable Hot Cup Color Change","Reusable-Hot-Cup-Color-Change","2,50 €",""],
     ["Reusable Asst. Heritage Logo Hot Cups","Reusable-Asst.-Heritage-Logo-Hot-Cups","2,50 €",""],
     ["Reusable Cold Cup Dome Lid","Reusable-Cold-Cup-Dome-Lid","2,50 €",""],
     ["Reusable Cold Cup","Reusable-Cold-Cup","2,50 €",""]
   ]}
 ]},
 {id:'tassen', h:'Klassische Tassen &amp; Mugs', groups:[
   {items:[
     ["Mug Gold Pleat","Mug-Gold-Pleat","40,00 €",""],
     ["Mug Brown Bear","Mug-Brown-Bear","49 €",""],
     ["Mug Bulb Marbled","Mug-Bulb-Marbled","15,90 €",""],
     ["Mug White Gingerbread Peep","Mug-White-Gingerbread-Peep","47,49 €",""],
     ["Mug Glass Green Gradient","Mug-Glass-Green-Gradient","15,90 €",""],
     ["Mug Siren Tail White","Mug-Siren-Tail-White","29,95 €",""],
     ["Recycled Coffee Cup","Recycled-Coffee-Cup","12,90 €",""]
   ]}
 ]},
 {id:'becher', h:'Tumbler, Cold Cups &amp; Trinkbecher', groups:[
   {items:[
     ["Tumbler Green","Tumbler-Green","41,00 €",""],
     ["Tumbler Red Brushed","Tumbler-Red-Brushed","39 €",""],
     ["Tumbler Sugarplum Gold","Tumbler-Sugarplum-Gold","42,99 €",""],
     ["Dual Tumbler Gold Swirl","Dual-Tumbler-Gold-Swirl","44,95 € – 79,00 €",""],
     ["Tumbler Gold Prism","Tumbler-Gold-Prism","39 € – 89 €",""],
     ["Cold Cup Gingerstraw","Cold-Cup-Gingerstraw","39 €",""],
     ["Cold Cup Green Diamond","Cold-Cup-Green-Diamond","26,90 €",""],
     ["Cold Cup Plum Gem","Cold-Cup-Plum-Gem","50 € – ~60 €",""],
     ["Tumbler Lucy Matte Black Green Band","Tumbler-Lucy-Matte-Black-Green-Band","19,90 €",""],
     ["Bottle Sugarplum Swirl","Bottle-Sugarplum-Swirl","39 €",""],
     ["Cold Cup Champ Gold Swirl","Cold-Cup-Champ-Gold-Swirl","88,00 €",""],
     ["Cold Cup Dual Lid Green","Cold-Cup-Dual-Lid-Green","26,90 €",""],
     ["Tumbler Plastic Grid Green","Tumbler-Plastic-Grid-Green","19,90 €",""],
     ["Tumbler Luxor Black","Tumbler-Luxor-Black","44 € – 59 €",""],
     ["Tumbler Grid Green","Tumbler-Grid-Green","41 €",""],
     ["Cold Cup Plastic Terrazzo Black","Cold-Cup-Plastic-Terrazzo-Black","12,90 €",""],
     ["Cold Cup Grid Green","Cold-Cup-Grid-Green","19,90 €",""],
     ["Cold Cup Beans","Cold-Cup-Beans","26,90 €",""],
     ["Cold Cup Marbled Black","Cold-Cup-Marbled-Black","19,90 €",""],
     ["Cold Cup Bling Soft Touch Black","Cold-Cup-Bling-Soft-Touch-Black","19,90 €",""]
   ]}
 ]},
 {id:'stabfilterkanne', h:'Kaffeezubehör: Stempelkanne &amp; Co.', groups:[
   {items:[
     ["Coffee Press Black","Coffee-Press-Black","61,90 €",""]
   ]}
 ]},
 {id:'sonstiges', h:'Weiteres Zubehör &amp; Extras', groups:[
   {items:[
     ["Pin Badge Set 4","Pin-Badge-Set-4","89,00 €",""],
     ["HOL25 Pin Badge Gingerbread MOP","HOL25-Pin-Badge-Gingerbread-MOP","29,95 €",""],
     ["Ornament Brown Bear","Ornament-Brown-Bear","30 €",""],
     ["Keychain Silicone Bearista Gingerbread","Keychain-Silicone-Bearista-Gingerbread","35 €",""],
     ["Bearista Germany","Bearista-Germany","24,90 €",""]
   ]}
 ]}
];

const FAQ = [
 ["Wie viel kostet ein Getränk bei Starbucks in Deutschland?","Die meisten Getränke liegen zwischen 2,75 € (Espresso) und 8,50 € (große Frappuccinos). Im Schnitt zahlst du für einen Kaffee oder Latte etwa 4,50 € bis 6,50 €, je nach Größe und Extras."],
 ["Ist Starbucks teuer im Vergleich zu anderen Cafés?","Starbucks liegt preislich über klassischen Bäckereien oder Imbiss-Cafés, ist aber ähnlich positioniert wie andere Premium-Ketten. Für den Preis bekommst du individuell anpassbare Getränke, WLAN und eine feste Sitzgelegenheit."],
 ["Was kostet eine Tasse Kaffee bei Starbucks?","Ein Filterkaffee (Pike Place Roast) startet bei etwa 5 €, ein Caffè Americano bei rund 3,10 €. Milchgetränke wie Caffè Latte oder Cappuccino liegen zwischen 3,90 € und 6,20 €, abhängig von der Größe."],
 ["Was kostet der teuerste Kaffee bei Starbucks?","Aufwendige Signature-Drinks wie Iced Pumpkin Spice Matcha Latte oder große Frappuccino-Varianten in Venti-Größe erreichen die höchsten Preise, meist zwischen 7,90 € und 8,90 €."],
 ["Wie viel kostet ein Cappuccino bei Starbucks?","Ein Cappuccino kostet ab etwa 3,90 € in der Standardgröße. Mit pflanzlicher Milch oder zusätzlichem Espresso-Shot kommen üblicherweise 0,50 € bis 0,80 € dazu."],
 ["Was kostet ein Caramel Frappuccino bei Starbucks?","Ein Caramel Frappuccino kostet je nach Größe zwischen etwa 6,90 € (Tall) und 7,90 € (Venti). Die Cream-Variante liegt in einem ähnlichen Preisbereich."],
 ["Wie teuer ist der Iced Matcha Latte bei Starbucks?","Der Iced Matcha Latte kostet zwischen 6,90 € und 7,90 €, abhängig von der gewählten Größe. Die heiße Variante ist minimal günstiger."],
 ["Wie viel kostet die komplette Starbucks Speisekarte an Preisen im Schnitt?","Getränke bewegen sich zwischen 2,75 € und 8,90 €, Snacks und Gebäck zwischen 1,80 € und 5,60 €. Eine vollständige Übersicht mit allen Kategorien findest du weiter oben auf dieser Seite."],
 ["Was kostet ein Sandwich oder Snack bei Starbucks?","Herzhafte Snacks wie Sandwiches oder Bagels liegen meist zwischen 3,20 € und 5,60 €. Süße Snacks wie Cookies oder Riegel starten bereits bei 1,80 €."],
 ["Wie viel kostet ein Muffin oder Kuchen bei Starbucks?","Muffins kosten meist um 3,80 € bis 3,99 €, Kuchenstücke wie New York Cheesecake liegen bei etwa 4,80 € bis 4,90 €."],
 ["Gibt es bei Starbucks vegane Optionen und was kosten sie?","Ja, unter anderem veganes Pain au Chocolat, vegane Croissants und pflanzliche Milchalternativen. Preislich unterscheiden sich diese kaum von den klassischen Varianten, pflanzliche Milch kostet meist 0,50 € bis 0,80 € Aufpreis."],
 ["Was kostet eine Starbucks Tasse oder ein Becher?","Einfache Keramiktassen starten bei etwa 12,90 €, Sammler-Mugs kosten teils deutlich mehr. Wiederverwendbare Becher und Tumbler liegen meist zwischen 15 € und 45 €, limitierte Editionen auch darüber."],
 ["Wie viel kosten Kaffeebohnen zum Mitnehmen bei Starbucks?","Eine 250g-Packung Kaffeebohnen kostet meist zwischen 6,99 € und 9,99 €, abhängig von Röstung und Sorte."],
 ["Wie finde ich Starbucks Filialen in meiner Nähe?","Am einfachsten über den offiziellen Store-Locator, die Starbucks App oder Google Maps. Alle drei zeigen dir aktuelle Öffnungszeiten und die Entfernung zur nächsten Filiale an."],
 ["Wie viele Starbucks-Filialen gibt es in Deutschland?","Aktuell gibt es über 160 Filialen bundesweit, mit den meisten Standorten in Berlin, München, Hamburg, Köln und Frankfurt sowie an großen Bahnhöfen und Flughäfen."],
 ["Wann haben die meisten Starbucks-Filialen geöffnet?","In Innenstadtlagen meist Montag bis Samstag von 7 oder 8 Uhr bis 20 oder 21 Uhr. Filialen an Bahnhöfen und Flughäfen haben oft deutlich längere oder durchgehende Öffnungszeiten."],
 ["Sind die Preise in allen Starbucks-Filialen in Deutschland gleich?","Nein, die Preise können je nach Standort leicht variieren. In Flughafen- oder Bahnhofsfilialen sowie in Innenstadt-Lagen mancher Großstädte sind einzelne Getränke teils etwas teurer."],
 ["Was kostet der Iced Caramel Macchiato bei Starbucks?","Der Iced Caramel Macchiato kostet ab etwa 5,79 € in der Standardgröße, je nach Filiale und Größe bis knapp 7 €."],
 ["Was kostet ein Frappuccino im Vergleich zu einem Latte?","Frappuccinos sind meist teurer als klassische Milchgetränke, da sie aufwendiger zubereitet werden. Ein Frappuccino kostet ab ca. 5,29 €, ein Caffè Latte bereits ab 4,59 €."],
 ["Lohnt sich die Starbucks Rewards App preislich?","Mit der App sammelst du bei jedem Einkauf Sterne, die sich gegen kostenlose Getränke eintauschen lassen. Bei regelmäßigem Besuch kann sich das langfristig lohnen, auch wenn es keinen direkten Rabatt auf den Einzelpreis gibt."],
 ["Was kostet ein Getränk mit pflanzlicher Milch zusätzlich?","Der Aufpreis für Hafer-, Soja- oder Mandelmilch liegt in der Regel bei 0,50 € bis 0,80 € pro Getränk, unabhängig von der gewählten Größe."],
 ["Was kostet eine heiße Schokolade bei Starbucks?","Eine klassische Hot Chocolate kostet ab etwa 4,99 €, Varianten mit weißer Schokolade oder gesalzenem Karamell liegen meist zwischen 5,40 € und 6,40 €."],
 ["Ändern sich die Starbucks Preise saisonal?","Ja, saisonale Editionen wie Lebkuchen- oder Pumpkin-Spice-Getränke sind meist etwas teurer als die Standardvarianten und nur für einen begrenzten Zeitraum verfügbar."],
 ["Was ist die günstigste Möglichkeit, bei Starbucks einzukaufen?","Ein kleiner Filterkaffee oder Espresso ab 2,75 € ist die preisgünstigste Getränkeoption. Bei Snacks sind einzelne Cookies oder kleine Gebäckstücke ab etwa 1,80 € am günstigsten."]
];

const esc = s => s.replace(/&(?!#?\w+;)/g,'&amp;');
const card = (name,src,price,kcal) => `<article class="card">
  <div class="thumb"><img loading="lazy" decoding="async" width="256" height="256" alt="${esc(name)}" src="${src}" onerror="this.closest('.card').classList.add('noimg')"></div>
  <h4 class="pname">${esc(name)}</h4>
  <p class="pmeta"><strong>Preise</strong> : ${price}${kcal?`<span class="sep">|</span><strong>Kalorien&sup1;</strong> : ${kcal}`:''}</p>
</article>`;

const menu = document.getElementById('menu');
const toc = document.getElementById('toc-list');

DATA.forEach(sec=>{
  toc.insertAdjacentHTML('beforeend', `<li><a href="#${sec.id}">${sec.h}</a></li>`);
  const s = document.createElement('section');
  s.className = 'sec' + (sec.divider ? ' divider' : '');
  s.id = sec.id;
  s.innerHTML = `<h2 class="sec-h">${sec.h}</h2>`;
  (sec.groups||[]).forEach(gr=>{
    if(gr.g) s.insertAdjacentHTML('beforeend', `<h3 class="grp-label">${gr.g}</h3>`);
    const grid = document.createElement('div');
    grid.className = 'grid';
    gr.items.forEach(it=> grid.insertAdjacentHTML('beforeend', card(it[0], IMG(it[1]), it[2], it[3])));
    s.appendChild(grid);
  });
  menu.appendChild(s);
});

toc.insertAdjacentHTML('beforeend',
  '<li><a href="#highlights">So setzen sich die Starbucks Preise 2026 zusammen</a></li>' +
  '<li><a href="#faq">Starbucks Preise: Häufige Fragen &amp; Antworten (2026)</a></li>');

document.getElementById('faq-list').innerHTML =
  FAQ.map(([q,a])=>`<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`).join('');
