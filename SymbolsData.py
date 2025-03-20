from UM.i18n import i18nCatalog

catalog = i18nCatalog("stacksofshapes")

PATH_KEY: str = "path"
TOOLTIP_KEY: str = "tooltip"
ALT_TOOLTIP_KEY: str = "altTooltip"

_symbols_category_arrows: str = catalog.i18nc("symbol_category", "Arrows")
_symbols_category_astrological_signs: str = catalog.i18nc("symbol_category", "Astrological Signs")
_symbols_category_card_suits: str = catalog.i18nc("symbol_category", "Card Suits")
_symbols_category_emojis: str = catalog.i18nc("symbol_category", "Emojis")
_symbols_category_geometric: str = catalog.i18nc("symbol_category", "Geometric Shapes")
_symbols_category_hearts: str = catalog.i18nc("symbol_category", "Hearts")
_symbols_category_pies: str = catalog.i18nc("symbol_category", "Pie Segments")
_symbols_category_stars: str = catalog.i18nc("symbol_category", "Stars")
_symbols_category_symbols_icons: str = catalog.i18nc("symbol_category", "Symbols & Icons")
_symbols_category_weather: str = catalog.i18nc("symbol_category", "Weather")

Symbols = {
    _symbols_category_arrows: {
        catalog.i18nc("symbol_name", "Arrow"): {
            PATH_KEY: "symbols/arrows/arrow_single.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_single", "An arrow with a regular point."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_single", "If you're wondering \"what's the point?\", you're missing the point.<br>The point is \"<b>where's</b> the point\"."),
        },
        catalog.i18nc("symbol_name", "Short Arrow"): {
            PATH_KEY: "symbols/arrows/arrow_short.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_short", "A short arrow with a regular head."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_short", "Yeah... last time I used one of these was when I forgot to change my printer from portrait to landscape."),
        },
        catalog.i18nc("symbol_name", "Arrow (Chevron)"): {
            PATH_KEY: "symbols/arrows/arrow_chevron.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_chevron", "An arrow with a chevron head."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_chevron", "The head is extra pointy so it hurts on the way out as well as in."),
        },
        catalog.i18nc("symbol_name", "Short Arrow (Chevron)"): {
            PATH_KEY: "symbols/arrows/arrow_chevron_short.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_chevron_short", "A short arrow with a chevron head."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_chevron_short", "More chevron for your buck! I'm definitely not going to complain."),
        },
        catalog.i18nc("symbol_name", "Arrow with Tail"): {
            PATH_KEY: "symbols/arrows/arrow_tail.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_tail", "An arrow with a regular head and a barbed tail."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_tail", "I'm no aerodynamicist, but this one probably flies better."),
        },
        catalog.i18nc("symbol_name", "Dual-Headed Arrow"): {
            PATH_KEY: "symbols/arrows/arrow_dual.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_dual", "An arrow with a head at each end."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_dual", "For when you can't decide which way to go. I usually split the difference and start walking through peoples' backyards."),
        },
        catalog.i18nc("symbol_name", "Curved Arrow (Clockwise)"): {
            PATH_KEY: "symbols/arrows/arrow_curve_clockwise.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_curve_clockwise", "A circular arrow curved in a clockwise direction."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_curve_clockwise", "For some reason I <i><b>really</b></i> want to press F5."),
        },
    },

    _symbols_category_astrological_signs: {
        catalog.i18nc("symbol_name", "Aries"): {
            PATH_KEY: "symbols/astrological_signs/aries_1.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aries", "<b>Aries (March 21 - April 19):</b><br>Energetic, courageous, independent, enthusiastic, pioneering, often the first to act."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aries", "While I quite enjoy the thought of ramming things, last time the insurance bill was quite not enjoyable."),
        },
        catalog.i18nc("symbol_name", "Aries (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/aries_circled_1.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aries_circled", "<b>Aries (March 21 - April 19):</b> (circled symbol)<br>Energetic, courageous, independent, enthusiastic, pioneering, often the first to act."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aries_circled", "<i>*wipes forehead*</i>. Getting hot in here. I think it's been too long since I was last shorn."),
        },
        catalog.i18nc("symbol_name", "Taurus"): {
            PATH_KEY: "symbols/astrological_signs/taurus_2.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:taurus", "<b>Taurus (April 20 - May 20):</b><br>Patient, reliable, practical, devoted, sensual, enjoys comfort and stability."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:taurus", "Wow. Writing these tooltips is taking me a while. I really need to get mooving."),
        },
        catalog.i18nc("symbol_name", "Taurus (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/taurus_circled_2.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:taurus_circled", "<b>Taurus (April 20 - May 20):</b> (circled symbol)<br>Patient, reliable, practical, devoted, sensual, enjoys comfort and stability."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:taurus_circled", "If you think the weather is hot, spare a though for those of us wearing permanent leather jumpsuits."),
        },
        catalog.i18nc("symbol_name", "Gemini"): {
            PATH_KEY: "symbols/astrological_signs/gemini_3.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:gemini", "<b>Gemini (May 21 - June 20):</b><br>Curious, adaptable, gentle, affectionate, communicative, loves variety and conversation."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:gemini", "Sometimes I can get a bit lost in my thoughts. If I had a twin I could really get a hold of myself."),
        },
        catalog.i18nc("symbol_name", "Gemini (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/gemini_circled_3.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:gemini_circled", "<b>Gemini (May 21 - June 20):</b> (circled symbol)<br>Curious, adaptable, gentle, affectionate, communicative, loves variety and conversation."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:gemini_circled", "Being a twin isn't all it's cracked up to be. You never get your own birthday party."),
        },
        catalog.i18nc("symbol_name", "Cancer"): {
            PATH_KEY: "symbols/astrological_signs/cancer_4.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:cancer", "<b>Cancer (June 21 - July 22):</b><br>Emotional, intuitive, imaginative, tenacious, nurturing, family-oriented and protective."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:cancer", "The great thing about having the sign that's the crab is that you're <i>really</i> good at opening stuck jars.<br>Even if you do it by cutting the whole top off."),
        },
        catalog.i18nc("symbol_name", "Cancer (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/cancer_circled_4.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:cancer_circled", "<b>Cancer (June 21 - July 22):</b> (circled symbol)<br>Emotional, intuitive, imaginative, tenacious, nurturing, family-oriented and protective."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:cancer_circled", "<i>*sees approaching crowd*</i> They... don't look very happy. I better scuttle."),
        },
        catalog.i18nc("symbol_name", "Leo"): {
            PATH_KEY: "symbols/astrological_signs/leo_5.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:leo", "<b>Leo (July 23 - August 22):</b><br>Creative, passionate, generous, warm-hearted, cheerful, loves being admired."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:leo", "Having a Leo in the car is great for dealing with traffic. You can't do anything about the other cars, but one roar and they stop honking."),
        },
        catalog.i18nc("symbol_name", "Leo (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/leo_circled_5.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:leo_circled", "<b>Leo (July 23 - August 22):</b> (circled symbol)<br>Creative, passionate, generous, warm-hearted, cheerful, loves being admired."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:leo_circled", "You, too, shall one day rule The Pride Lands."),
        },
        catalog.i18nc("symbol_name", "Virgo"): {
            PATH_KEY: "symbols/astrological_signs/virgo_6.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:virgo", "<b>Virgo (August 23 - September 22):</b><br>Logical, practical, hardworking, analytical, kind, pays attention to detail."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:virgo", "I think Virgos have the tidiest houses I've ever seen.</br>I am definitely <b>not</b> a Virgo."),
        },
        catalog.i18nc("symbol_name", "Virgo (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/virgo_circled_6.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:virgo_circled", "<b>Virgo (August 23 - September 22): (circled symbol)</b><br>Logical, practical, hardworking, analytical, kind, pays attention to detail."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:virgo_circled", "Always willing to lend a hand, as long as you're willing to put in two of your own."),
        },
        catalog.i18nc("symbol_name", "Libra"): {
            PATH_KEY: "symbols/astrological_signs/libra_7.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:libra", "<b>Libra (September 23 - October 22):</b><br>Cooperative, gracious, fair-minded, social, strives for balance and harmony."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:libra", "I'm not sure people born on the 1st, 3rd, 5th, 7th, etc, should count as Libra. They're not even!"),
        },
        catalog.i18nc("symbol_name", "Libra (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/libra_circled_7.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:libra_circled", "<b>Libra (September 23 - October 22):</b> (circled symbol)<br>Cooperative, gracious, fair-minded, social, strives for balance and harmony."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:libra_circled", "As someone so well balanced, you should definitely get into gymnastics."),
        },
        catalog.i18nc("symbol_name", "Scorpio"): {
            PATH_KEY: "symbols/astrological_signs/scorpio_8.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:scorpio", "<b>Scorpio (October 23 - November 21):</b><br>Resourceful, brave, passionate, stubborn, assertive, can be intense and mysterious."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:scorpio", "Don't worry, I'm not venomous or anything. Well, as long as you don't make me angry."),
        },
        catalog.i18nc("symbol_name", "Scorpio (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/scorpio_circled_8.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:scorpio_circled", "<b>Scorpio (October 23 - November 21):</b> (circled symbol)<br>Resourceful, brave, passionate, stubborn, assertive, can be intense and mysterious."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:scorpio_circled", "Having a tailwind isn't as cooling as it sounds when you have to do it by waving your own tail."),
        },
        catalog.i18nc("symbol_name", "Sagittarius"): {
            PATH_KEY: "symbols/astrological_signs/sagittarius_9.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:sagittarius", "<b>Sagittarius (November 22 - December 21):</b><br>Generous, idealistic, humorous, adventurous, loves freedom and exploration."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:sagittarius", "Nice aim! Remind me never to bet against you at darts."),
        },
        catalog.i18nc("symbol_name", "Sagittarius (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/sagittarius_circled_9.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:sagittarius_circled", "<b>Sagittarius (November 22 - December 21):</b> (circled symbol)<br>Generous, idealistic, humorous, adventurous, loves freedom and exploration."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:sagittarius_circled", "Don't worry, if something goes wrong, you've always got another plan just a nock away."),
        },
        catalog.i18nc("symbol_name", "Capricorn"): {
            PATH_KEY: "symbols/astrological_signs/capricorn_10.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:capricorn", "<b>Capricorn (December 22 - January 19):</b><br>Responsible, disciplined, self-controlled, ambitious, practical and goal-oriented."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:capricorn", "If you're feeling down, just remember that things are never as bleat as they seem."),
        },
        catalog.i18nc("symbol_name", "Capricorn (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/capricorn_circled_10.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:capricorn_circled", "<b>Capricorn (December 22 - January 19):</b> (circled symbol)<br>Responsible, disciplined, self-controlled, ambitious, practical and goal-oriented."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:capricorn_circled", "Wow. Some Capricorns will eat almost anything. You have a much more refined palate."),
        },
        catalog.i18nc("symbol_name", "Aquarius"): {
            PATH_KEY: "symbols/astrological_signs/aquarius_11.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aquarius", "<b>Aquarius (January 20 - February 18):</b><br>Progressive, original, independent, humanitarian, intellectual and innovative."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aquarius_", "Thanks, you've always got some water for when I'm thirsty. How do you manage that?"),
        },
        catalog.i18nc("symbol_name", "Aquarius (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/aquarius_circled_11.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aquarius_circled", "<b>Aquarius (January 20 - February 18):</b> (circled symbol)<br>Progressive, original, independent, humanitarian, intellectual and innovative."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aquarius_circled", "How is it you always manage to look like you've just come out of the shower?"),
        },
        catalog.i18nc("symbol_name", "Pisces"): {
            PATH_KEY: "symbols/astrological_signs/pisces_12.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:pisces", "<b>Pisces (February 19 - March 20):</b><br>Compassionate, artistic, intuitive, gentle, wise, imaginative and sensitive."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:pisces", "Try not to complain about your internet speeds. There could be worse things downstream."),
        },
        catalog.i18nc("symbol_name", "Pisces (Circled)"): {
            PATH_KEY: "symbols/astrological_signs/pisces_circled_12.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:pisces_circled", "<b>Pisces (February 19 - March 20):</b> (circled symbol)<br>Compassionate, artistic, intuitive, gentle, wise, imaginative and sensitive."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:pisces_circled", "Just keep swimming, just keep swimming, just keep swimming, swimming, swimming, what do we do, we swim, swim."),
        },
    },

    _symbols_category_card_suits: {
        catalog.i18nc("symbol_name", "Heart"): {
            PATH_KEY: "symbols/hearts/heart.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:heart", "Heart (card suit)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:heart", "Someone just broke my heart. Why'd they have to change the trump suit?"),
        },
        catalog.i18nc("symbol_name", "Heart (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:heart_outline", "Heart (card suit) (outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:heart_outline", "I don't think this makes you look heartless. Half-hearted, at worst."),
        },
        catalog.i18nc("symbol_name", "Diamond"): {
            PATH_KEY: "symbols/geometric/diamond.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:diamond", "Diamond (card suit)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:diamond", "I took a pack of cards to the jeweller and they said it was worthless. What gives? There's thirteen diamonds in here."),
        },
        catalog.i18nc("symbol_name", "Diamond (Outline)"): {
            PATH_KEY: "symbols/geometric/diamond_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond_outline", "Diamond (card suit) (outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond_outline", "I'm sure this is on a road sign. But I can never remember what it means."),
        },
        catalog.i18nc("symbol_name", "Club"): {
            PATH_KEY: "symbols/card_suits/club.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:club", "Club (card suit)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:club", "At least if someone beats you with a club, it's much less painful than someone beating you with a club."),
        },
        catalog.i18nc("symbol_name", "Club (Outline)"): {
            PATH_KEY: "symbols/card_suits/club_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:club_outline", "Club (card suit) (outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:club_outline", "Pretty sure this is the icon which comes up on your HUD when your melee weapon is about to break."),
        },
        catalog.i18nc("symbol_name", "Spade"): {
            PATH_KEY: "symbols/card_suits/spade.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:spade", "Spade (card suit)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:spade", "If a magician ever lets you pick a card, pick a spade. They'll have to keep digging for it."),
        },
        catalog.i18nc("symbol_name", "Spade (Outline)"): {
            PATH_KEY: "symbols/card_suits/spade_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:spade_outline", "Spade (card suit) (outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:spade_outline", "What's the point of a spade when all the dirt just falls straight through?"),
        },
    },

    _symbols_category_emojis: {
        catalog.i18nc("symbol_name", "Angry"): {
            PATH_KEY: "symbols/emojis/angry.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:angry", "Angry Emoji: 😠"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:angry", "Hey, don't look at me. It was <i>*eyes dart around*</i> that guy! <i>*starts running*</i>"),
        },
        catalog.i18nc("symbol_name", "Angry (Filled)"): {
            PATH_KEY: "symbols/emojis/angry_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:angry_filled_no_outline", "Angry Emoji: 😠 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:angry_filled_no_outline", "I just heard that guy Star Wars is better than Star Trek too. You don't have to get <i>this</i> worked up about it."),
        },
        catalog.i18nc("symbol_name", "Angry (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/angry_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:angry_filled", "Angry Emoji: 😠 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:angry_filled", "If that store didn't want me to knock over all their bookshelves, they would have had the block set I wanted in stock."),
        },
        catalog.i18nc("symbol_name", "Cow"): {
            PATH_KEY: "symbols/emojis/cow.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:cow", "Cow Emoji: 🐄"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:cow", "Mooooooooooo. That means either hello or goodbye, depending on how I feel.<br>Sometimes I'm conflicted and it's both. We're actually quite emotional creatures."),
        },
        catalog.i18nc("symbol_name", "Cow (Filled)"): {
            PATH_KEY: "symbols/emojis/cow_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:cow_filled", "Cow Emoji: 🐄 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:cow_filled", "Standing around chewing the cud all day might not <i>sound</i> fun, but you do basically the same thing with beer at night."),
        },
        catalog.i18nc("symbol_name", "Crying"): {
            PATH_KEY: "symbols/emojis/crying.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying", "Crying Emoji: 😢"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying", "Buck up kiddo, things could be worse. There's someone loudly crying not too far away."),
        },
        catalog.i18nc("symbol_name", "Crying (Filled)"): {
            PATH_KEY: "symbols/emojis/crying_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying_filled_no_outline", "Crying Emoji: 😢 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying_filled_no_outline", "Fake tears will get you everywhere, except the front of the line at theme parks."),
        },
        catalog.i18nc("symbol_name", "Crying (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/crying_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying_filled", "Crying Emoji: 😢 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying_filled", "All this time spent messing around with crying emojis and now I feel like joining them."),
        },
        catalog.i18nc("symbol_name", "Loudly Crying"): {
            PATH_KEY: "symbols/emojis/crying_loudly.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying_loudly", "Loudly Crying Emoji: 😭"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying_loudly", "Look, I know you didn't mean to knock over that milk truck. But there's no need to cry about it."),
        },
        catalog.i18nc("symbol_name", "Crying Loudly (Filled)"): {
            PATH_KEY: "symbols/emojis/crying_loudly_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying_loudly_filled_no_outline", "Loudly Crying Emoji: 😭 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying_loudly_filled_no_outline", "If your child is acting like this, you either just backed over their favourite toy in your driveway</br>or you should back over their favourite toy as a distraction from their other problem."),
        },
        catalog.i18nc("symbol_name", "Loudly Crying (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/crying_loudly_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:crying_loudly_filled", "Loudly Crying Emoji: 😭 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:crying_loudly_filled", "Don't blame yourself. If the circus had trained their elephant better it wouldn't have gotten startled<br>and run over eleven people when you accidentally brushed by it."),
        },
        catalog.i18nc("symbol_name", "Facepalm"): {
            PATH_KEY: "symbols/emojis/facepalm.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:facepalm", "Facepalm Emoji: 🤦"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:facepalm", "Really? I have to explain this one? UGGGHHH."),
        },
        catalog.i18nc("symbol_name", "Facepalm (Filled)"): {
            PATH_KEY: "symbols/emojis/facepalm_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:facepalm_filled", "Facepalm Emoji: 🤦 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:facepalm_filled", "I did two of these stupid things? What the heck is wrong with me?"),
        },
        catalog.i18nc("symbol_name", "Facepalm (Filled) (No Outline)"): {
            PATH_KEY: "symbols/emojis/facepalm_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:facepalm_filled_no_outline", "Facepalm Emoji: 🤦 (Filled) (No Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:facepalm_filled_no_outline", "Learn from my mistakes. Don't try to help people on the internet."),
        },
        catalog.i18nc("symbol_name", "Frown"): {
            PATH_KEY: "symbols/emojis/frown.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:frown", "Frown Emoji: ☹️"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:frown", "They might have replaced your steak with steamed tofu, but I still think we need to split the bill."),
        },
        catalog.i18nc("symbol_name", "Frown (Filled)"): {
            PATH_KEY: "symbols/emojis/frown_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:frown_filled_no_outline", "Frown Emoji: ☹️ (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:frown_filled_no_outline", "People with this expression are either depressed, unimpressed or frowning."),
        },
        catalog.i18nc("symbol_name", "Frown (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/frown_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:frown_filled", "Frown Emoji: ☹️ (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:frown_filled", "I don't care whether you agree with me or not, I am <b>not</b> going to fill your car's fuel tank with whiskey."),
        },
        catalog.i18nc("symbol_name", "Grin"): {
            PATH_KEY: "symbols/emojis/grin.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin", "Grin Emoji: 😀"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin", "I know that look. Your seventeen hour print just finished successfully, didn't it?"),
        },
        catalog.i18nc("symbol_name", "Grin (Filled)"): {
            PATH_KEY: "symbols/emojis/grin_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_filled_no_outline", "Grin Emoji: 😀 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_filled_no_outline", "The last time I saw someone that happy was after<br>the claw machine picked up two things stuck together."),
        },
        catalog.i18nc("symbol_name", "Grin (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/grin_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_filled", "Grin Emoji: 😀 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_filled", "Go ahead. Tell me how much you won on that lottery ticket. I know you want to."),
        },
        catalog.i18nc("symbol_name", "Toothy Grin"): {
            PATH_KEY: "symbols/emojis/grin_toothy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_toothy", "Toothy Grin Emoji: 😁"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_toothy", "Finally beat Dark Souls, eh?"),
        },
        catalog.i18nc("symbol_name", "Grin Toothy (Filled)"): {
            PATH_KEY: "symbols/emojis/grin_toothy_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_toothy_filled_no_outline", "Toothy Grin Emoji: 😁 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_toothy_filled_no_outline", "Warning: Just because you have paid for extensive dental work does<br>not mean people won't try and <i>undo</i> if you shove it in their face."),
        },
        catalog.i18nc("symbol_name", "Toothy Grin (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/grin_toothy_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_toothy_filled", "Toothy Grin Emoji: 😁 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_toothy_filled", "Finally win that game of Monopoly did you? You've only been playing what, seven years?"),
        },
        catalog.i18nc("symbol_name", "Money Bag"): {
            PATH_KEY: "symbols/emojis/money_bag.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:money_bag", "Money Bag Emoji: 💰"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:money_bag", "Feed the birds, tuppence a bag.<br>Tuppence, tuppence, tuppence a bag."),
        },
        catalog.i18nc("symbol_name", "Money Bag (Filled)"): {
            PATH_KEY: "symbols/emojis/money_bag_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:money_bag_filled", "Money Bag Emoji: 💰 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:money_bag_filled", "Why wouldn't you want the <b>filled</b> money bag?"),
        },
        catalog.i18nc("symbol_name", "Monocle"): {
            PATH_KEY: "symbols/emojis/monocle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:monocle", "Monocle Emoji: 🧐"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:monocle", "This is actually a resourceful use of a broken pair of glasses and a broken necklace."),
        },
        catalog.i18nc("symbol_name", "Monocle (Filled)"): {
            PATH_KEY: "symbols/emojis/monocle_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:monocle_filled", "Monocle Emoji: 🧐 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:monocle_filled", "This is a resourceful usage of the other half of the broken glasses and a lanyard from a boring conference."),
        },
        catalog.i18nc("symbol_name", "Monocle (Filled) (No Outline)"): {
            PATH_KEY: "symbols/emojis/monocle_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:monocle_filled_no_outline", "Monocle Emoji: 🧐 (Filled) (No Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:monocle_filled_no_outline", "This is a wasteful usage of vector artwork and an image editor."),
        },
        catalog.i18nc("symbol_name", "Poop"): {
            PATH_KEY: "symbols/emojis/poop.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:poop", "Poop Emoji: 💩"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:poop", "Look, I know it stinks, but if I didn't include it people would just hassle me until I did."),
        },    
        catalog.i18nc("symbol_name", "Poop (Outline)"): {
            PATH_KEY: "symbols/emojis/poop_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:poop_outline", "Poop Emoji: 💩 (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:poop_outline", "Okay, who quit cleaning the toilet halfway through?"),
        },
        catalog.i18nc("symbol_name", "Raised Eyebrow"): {
            PATH_KEY: "symbols/emojis/raised_eyebrow.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:raised_eyebrow", "Raised Eyebrow Emoji: 🤨"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:raised_eyebrow", "Yes, I am sure about this. Don't give me that look."),
        },
        catalog.i18nc("symbol_name", "Raised Eyebrow (Filled)"): {
            PATH_KEY: "symbols/emojis/raised_eyebrow_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:raised_eyebrow_filled_no_outline", "Raised Eyebrow Emoji: 🤨 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:raised_eyebrow_filled_no_outline", "Whether or not you believe me, I <b>saw</b> that shark kiss a dolphin."),
        },
        catalog.i18nc("symbol_name", "Raised Eyebrow (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/raised_eyebrow_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:raised_eyebrow_filled", "Raised Eyebrow Emoji: 🤨 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:raised_eyebrow_filled", "I didn't think the filled versions of the emojis were a good idea at first either, but I think it works."),
        },
        catalog.i18nc("symbol_name", "Rolling On Floor Laughing"): {
            PATH_KEY: "symbols/emojis/rofl.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rofl", "Rolling On Floor Laughing Emoji: 🤣"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rofl", "...I must have just come up with the best ever version of \"why did the chicken cross the road?\""),
        },
        catalog.i18nc("symbol_name", "Rolling On Floor Laughing (Filled)"): {
            PATH_KEY: "symbols/emojis/rofl_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rofl_filled", "Rolling On Floor Laughing Emoji: 🤣 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rofl_filled", "It's just a show of people getting hit in the crotch. Why has it beein going ten seasons and how is it still so ahahahahahhaahahahahaahahahahaa freaking hilarious?"),
        },
        catalog.i18nc("symbol_name", "Rolling on Floor Laughing (Filled) (No Outline)"): {
            PATH_KEY: "symbols/emojis/rofl_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rofl_filled_no_outline", "Rolling On Floor Laughing Emoji: 🤣 (Filled) (No Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rofl_filled_no_outline", "Uh oh. Someone let him read another book of dad jokes."),
        },
        catalog.i18nc("symbol_name", "Rolling Eyes"): {
            PATH_KEY: "symbols/emojis/rolling_eyes.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rolling_eyes", "Rolling Eyes Emoji: 🙄"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rolling_eyes", "Look, I know the Unicode Consortium might <b>sound</b> boring, but you wanted to know about emojis."),
        },
        catalog.i18nc("symbol_name", "Rolling Eyes (Filled)"): {
            PATH_KEY: "symbols/emojis/rolling_eyes_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rolling_eyes_filled_no_outline", "Rolling Eyes Emoji: 🙄 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rolling_eyes_filled_no_outline", "Personally I consider it a success if I can get anyone under the age of 20 to give me this look."),
        },
        catalog.i18nc("symbol_name", "Rolling Eyes (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/rolling_eyes_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:rolling_eyes_filled", "Rolling Eyes Emoji: 🙄 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:rolling_eyes_filled", "I don't care what you think. I think The Rolling Stones have still got it."),
        },
        catalog.i18nc("symbol_name", "Slanted Mouth"): {
            PATH_KEY: "symbols/emojis/slanted_mouth.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:slanted_mouth", "Slanted Mouth Emoji: 🫤"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:slanted_mouth", "Fine. Believe me or not. Your choice. But I <b>swear</b> I saw a responsible motorcyclist."),
        },
        catalog.i18nc("symbol_name", "Slanted Mouth (Filled)"): {
            PATH_KEY: "symbols/emojis/slanted_mouth_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:slanted_mouth_filled_no_outline", "Slanted Mouth Emoji: 🫤 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:slanted_mouth_filled_no_outline", "How can you say no? I know the reputation \"get rich quick\" schemes have,<br>but trust me, this one works!"),
        },
        catalog.i18nc("symbol_name", "Slanted Mouth (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/slanted_mouth_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:slanted_mouth_filled", "Slanted Mouth Emoji: 🫤 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:slanted_mouth_filled", "Spelunking without bringing lights was <b>your</b> idea. Don't look at me like that."),
        },
        catalog.i18nc("symbol_name", "Smile"): {
            PATH_KEY: "symbols/emojis/smile.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smile", "Smiling Emoji: 🙂"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smile", "Always look on the bright side of life.<br>Always look on the the right side of life."),
        },
        catalog.i18nc("symbol_name", "Smile (Filled)"): {
            PATH_KEY: "symbols/emojis/smile_filled_no_outline.stl",
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smile_filled_no_outline", "Smiling Emoji: 🙂 (Filled)"),
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smile_filled_no_outline", "These happy days are yours and mine."),
        },
        catalog.i18nc("symbol_name", "Smile (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/smile_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smile_filled", "Smiling Emoji: 🙂 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smile_filled", "Come on, get happy.<br>A whole lotta lovin' is what we'll be bringin'.<br>We'll make you happy."),
        },
        catalog.i18nc("symbol_name", "Smirk"): {
            PATH_KEY: "symbols/emojis/smirk.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smirk", "Smirking Emoji: 😏"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smirk", "What, you think you know something I don't?"),
        },
        catalog.i18nc("symbol_name", "Smirk (Filled)"): {
            PATH_KEY: "symbols/emojis/smirk_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smirk_filled_no_outline", "Smirking Emoji: 😏 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smirk_filled_no_outline", "Last time I saw someone looking that confident was<br>right before the cops broke the door down and arrested him."),
        },
        catalog.i18nc("symbol_name", "Smirk (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/smirk_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smirk_filled", "Smirking Emoji: 😏 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smirk_filled", "Quit it with that look. You're nowhere near as punny as you think you are."),
        },
        catalog.i18nc("symbol_name", "Thinking"): {
            PATH_KEY: "symbols/emojis/thinking.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:thinking", "Thinking Emoji: 🤔"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:thinking", "I don't know why I thought writing all these jokes was a good idea either. But it's too late now."),
        },
        catalog.i18nc("symbol_name", "Thinking (Filled)"): {
            PATH_KEY: "symbols/emojis/thinking_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:thinking_filled", "Thinking Emoji: 🤔 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:thinking_filled", "Oh, I could tell you why<br>the ocean's near the shore.<br>I could think of things I'd never thunk before.<br>And then I'd sit, and think some more."),
        },
        catalog.i18nc("symbol_name", "Thinking (Filled) (No Outline)"): {
            PATH_KEY: "symbols/emojis/thinking_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:thinking_filled_no_outline", "Thinking Emoji: 🤔 (Filled) (No Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:thinking_filled_no_outline", "Why some of these emojis are labelled \"outline\" and some \"no outline\"? That's a noodle-scratcher."),
        },
        catalog.i18nc("symbol_name", "Wink"): {
            PATH_KEY: "symbols/emojis/wink.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:wink", "Winking Emoji: 😉"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:wink", "This guy gets me."),
        },
        catalog.i18nc("symbol_name", "Wink (Filled)"): {
            PATH_KEY: "symbols/emojis/wink_filled_no_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:wink_filled_no_outline", "Winking Emoji: 😉 (Filled)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:wink_filled_no_outline", "Okay, they're giving me the sign it's time to do <i>something</i> in this heist... if only I could remember what."),
        },
        catalog.i18nc("symbol_name", "Wink (Filled) (Outline)"): {
            PATH_KEY: "symbols/emojis/wink_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:wink_filled", "Winking Emoji: 😉 (Filled) (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:wink_filled", "If there was a joke somewhere I'm not sure I'm in on it. Awww carp, that joke's on me, isn't it?"),
        },
    },

    _symbols_category_geometric: {
        catalog.i18nc("symbol_name", "Circle"): {
            PATH_KEY: "symbols/geometric/circle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:circle", "A completely round shape with no corners."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:circle", "If you're in a cartoon, it also makes for a great escape hole. Just put it on the ground/"),
        },
        catalog.i18nc("symbol_name", "Circle (Outline)"): {
            PATH_KEY: "symbols/geometric/circle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:circle_outline", "A completely round shape with no corners. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:circle_outline", "Technically this can be a black hole if you print it in black."),
        },
        catalog.i18nc("symbol_name", "Oval"): {
            PATH_KEY: "symbols/geometric/oval.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:oval", "Round like a circle, but its height and width aren't the same."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:oval", "If you think this looks like a football, go back to the Shapes side and look up my ellipsoid."),
        },
        catalog.i18nc("symbol_name", "Oval (Outline)"): {
            PATH_KEY: "symbols/geometric/oval_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:oval_outline", "Round like a circle, but its height and width aren't the same. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:oval_outline", "They just make it not a circle so my description of car racing as \"cars driving around in circles all day\" isn't technically accurate."),
        },
        catalog.i18nc("symbol_name", "Triangle"): {
            PATH_KEY: "symbols/geometric/triangle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle", "A shape with three sides. This one has three equal sides and is an <b>equilateral</b> triangle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle", "Back when we were in 1D land we had our lines and we were happy with them. What's so great about the second dimension?"),
        },
        catalog.i18nc("symbol_name", "Triangle (Outline)"): {
            PATH_KEY: "symbols/geometric/triangle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_outline", "A shape with three sides. This one has three equal sides and is an <b>equilateral</b> triangle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_outline", "No, this isn't how triangulation works."),
        },
        catalog.i18nc("symbol_name", "Right Angled Triangle"): {
            PATH_KEY: "symbols/geometric/triangle_right.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_right", "A shape with three sides. This one has a 90° corner (a \"right angle\") and two 45° corners."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_right", "This makes for a much better ramp than the equilateral triangle, unless you have your front suspension far higher than is sane."),
        },
        catalog.i18nc("symbol_name", "Right Angled Triangle (Outline)"): {
            PATH_KEY: "symbols/geometric/triangle_right_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_right_outline", "A shape with three sides. This one has a 90° corner (a \"right angle\") and two 45° corners. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_right_outline", "Not very fun fact: the inner edge is <b>also</b> a right angled triangle."),
        },
        catalog.i18nc("symbol_name", "Square"): {
            PATH_KEY: "symbols/geometric/square.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square", "A shape with four equal sides."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square", "This <i>will</i> fit in a round hole. Anything will fit anywhere if you apply enough pressure."),
        },
        catalog.i18nc("symbol_name", "Square (Outline)"): {
            PATH_KEY: "symbols/geometric/square_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_outline", "A shape with four equal sides. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_outline", "Do the kids still use \"square\" to mean uncool? If I have to ask, does that mean I'm a square?"),
        },
        catalog.i18nc("symbol_name", "Square (Rounded)"): {
            PATH_KEY: "symbols/geometric/square_rounded.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_rounded", "A shape with four equal sides and rounded corners."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_rounded", "This version is child-proofed to stop you poking your eye out.<br>I do <b>not</b> offer any guarantees on my work."),
        },
        catalog.i18nc("symbol_name", "Square (Rounded) (Outline)"): {
            PATH_KEY: "symbols/geometric/square_rounded_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_rounded_outline", "A shape with four equal sides and rounded corners. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_rounded_outline", "This one isn't child-proof. They can get trapped in the centre."),
        },
        catalog.i18nc("symbol_name", "Rectangle"): {
            PATH_KEY: "symbols/geometric/rectangle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle", "A shape with four sides, two pairs of equal length."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle", "Very convenient if you couldn't be bothered stretching out a square yourself."),
        },
        catalog.i18nc("symbol_name", "Rectangle (Outline)"): {
            PATH_KEY: "symbols/geometric/rectangle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_outline", "A shape with four sides, two pairs of equal length. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_outline", "You couldn't actually get this one from stretching a square. The line would be an uneven width. But who'd notice?"),
        },
        catalog.i18nc("symbol_name", "Rectangle (Rounded)"): {
            PATH_KEY: "symbols/geometric/rectangle_rounded.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_rounded", "A shape with four sides, two pairs of equal length and rounded corners."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_rounded", "Once again I'm here trying to protect you from yourself on pointy corners."),
        },
        catalog.i18nc("symbol_name", "Rectangle (Rounded) (Outline)"): {
            PATH_KEY: "symbols/geometric/rectangle_rounded_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_rounded_outline", "A shape with four sides, two pairs of equal length and rounded corners. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_rounded_outline", "This one can be used as a racetrack like the oval. But only if you really hate driving cars."),
        },
        catalog.i18nc("symbol_name", "Pentagon"): {
            PATH_KEY: "symbols/geometric/pentagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:pentagon", "A regular polygon with 5 equal sides."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:pentagon", "What use are pentagons? 5 people isn't enough to party. 5 slices isn't a pizza. You're nothing. You don't even tessellate."),
        },
        catalog.i18nc("symbol_name", "Pentagon (Outline)"): {
            PATH_KEY: "symbols/geometric/pentagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:pentagon_outline", "A regular polygon with 5 equal sides. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:pentagon_outline", "Sorry to disappoint, but if you're looking for a penta<i>gram</i> I didn't include one."),
        },
        catalog.i18nc("symbol_name", "Hexagon"): {
            PATH_KEY: "symbols/geometric/hexagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:hexagon", "A regular polygon with 6 equal sides."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:hexagon", "Much more useful than the pentagon. It assembles furniture. It tesselates.<br>It's getting close enough to round that you <i>might</i> be able to use it as a wheel in an emergency."),
        },
        catalog.i18nc("symbol_name", "Hexagon (Outline)"): {
            PATH_KEY: "symbols/geometric/hexagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:hexagon_outline", "A regular polygon with 6 equal sides. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:hexagon_outline", "This doesn't have the structural integrity of the whole hexagon. But it is better for smuggling things."),
        },
        catalog.i18nc("symbol_name", "Octagon"): {
            PATH_KEY: "symbols/geometric/octagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:octagon", "A regular polygon with 8 equal sides."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:octagon", "Consider yourself lucky I didn't include a septagon. A nonagon. A hendecagon. Any of those and you might have learned something."),
        },
        catalog.i18nc("symbol_name", "Octagon (Outline)"): {
            PATH_KEY: "symbols/geometric/octagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:octagon_outline", "A regular polygon with 8 equal sides. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:octagon_outline", "I don't care if it's traditional in your culture. I am not climbing into that thing to fight you. Just where did you say you were from, anyway?"),
        },
        catalog.i18nc("symbol_name", "Diamond"): {
            PATH_KEY: "symbols/geometric/diamond.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond", "Technically it's a type of rhombus. But this version is best known as a diamond."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond", "Technically, I don't think anyone cares if it's a type a rhombus."),
        },
        catalog.i18nc("symbol_name", "Diamond (Outline)"): {
            PATH_KEY: "symbols/geometric/diamond_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond_outline", "Technically it's a type of rhombus. But this version is best known as a diamond. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond_outline", "I promise you I put literally as much effort into this as the one in the \"Card Suits\" group. Because they're the same thing."),
        },
        catalog.i18nc("symbol_name", "Parallelogram"): {
            PATH_KEY: "symbols/geometric/parallelogram.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:parallelogram", "Two sets of parallel lines, one set at an angle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:parallelogram", "Believe it or not, this <i>isn't</i> the longest shape name. You don't want to know what is."),
        },
        catalog.i18nc("symbol_name", "Parallelogram (Outline)"): {
            PATH_KEY: "symbols/geometric/parallelogram_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:parallelogram_outline", "Two sets of parallel lines, one set at an angle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:parallelogram_outline", "Rotate it slightly and it makes for a great mouth on a slanted mouth emoji 🫤."),
        },
        catalog.i18nc("symbol_name", "Trapezoid"): {
            PATH_KEY: "symbols/geometric/trapezoid.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:trapezoid", "Also known as a \"trapezium\". Four lines. Two are parellel. The other two are mirror images."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:trapezoid", "As someone who speaks <i>English</i> English, if I have to type \"trapezoid\" once more, I swear I'm going to lose it. I don't care what \"it\" is."),
        },
        catalog.i18nc("symbol_name", "Trapezoid (Outline)"): {
            PATH_KEY: "symbols/geometric/trapezoid_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:trapezoid_outline", "Also known as a \"trapezium\". Four lines. Two are parellel. The other two are mirror images. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:trapezoid_outline", "OH FOR THE LOVE OF ALL THINGS BEEFY (╯°□°）╯︵ ┻━┻"),
        },
    },

    _symbols_category_hearts: {
        catalog.i18nc("symbol_name", "Heart"): {
            PATH_KEY: "symbols/hearts/heart.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart", "A typical illustration of a heart."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart", "Hearts don't really look like this. Most people prefer this version. I don't."),
        },
        catalog.i18nc("symbol_name", "Heart (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_outline", "A typical illustration of a heart. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_outline", "Actually I think this is a typical illustration of open heart surgery."),
        },
        catalog.i18nc("symbol_name", "Heart Arrow"): {
            PATH_KEY: "symbols/hearts/heart_arrow.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_arrow", "A heart icon with an arrow going through it, evoking the \"Cupid\" myth."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_arrow", "To me it looks more like William Tell shooting an apple off someone's head."),
        },
        catalog.i18nc("symbol_name", "Heart Arrow (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_arrow_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_arrow_outline", "A heart icon with an arrow going through it, evoking the \"Cupid\" myth. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_arrow_outline", "The arrow <i>should</i> have achieved better penetration due to the lower density of the interior."),
        },
        catalog.i18nc("symbol_name", "Heart Broken"): {
            PATH_KEY: "symbols/hearts/heart_broken.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken", "A heart illustration with a shatter line down the middle and<br>the two halves sitting slightly offset each other."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken", "Don't worry, hearts can be mended. Medicine can do wonders these days."),
        },
        catalog.i18nc("symbol_name", "Heart Broken (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_broken_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_outline", "A heart illustration with a shatter line down the middle and<br>the two halves sitting slightly offset each other. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_outline", "Clean-up at aisle 6. I think whatever was in here drained out when it broke."),
        },
        catalog.i18nc("symbol_name", "Heart Broken Left"): {
            PATH_KEY: "symbols/hearts/heart_broken_left.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_left", "The left half of the \"Heart Broken\" symbol."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_left", "I've heard you can tell someone's political viewpoint by which part of their heart they have. I try not to get involved. For my own safety."),
        },
        catalog.i18nc("symbol_name", "Heart Broken Left (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_broken_left_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_left_outline", "The left half of the \"Heart Broken\" symbol. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_left_outline", "I know it hurts now. But it will get better. Probably. Maybe. There's a chance it will get better."),
        },
        catalog.i18nc("symbol_name", "Heart Broken Right"): {
            PATH_KEY: "symbols/hearts/heart_broken_right.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_right", "The right half of the \"Heart Broken\" symbol."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_right", "Let me guess, he got the other half in the divorce?"),
        },
        catalog.i18nc("symbol_name", "Heart Broken Right (Outline)"): {
            PATH_KEY: "symbols/hearts/heart_broken_right_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_right_outline", "The right half of the \"Heart Broken\" symbol. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_right_outline", "At least you know you're right. You and every single other person on the internet. But you have the heart to prove it."),
        },
    },

    _symbols_category_pies: {
        catalog.i18nc("symbol_name", "Pie (Whole)"): {
            PATH_KEY: "symbols/geometric/circle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_whole", "It's literally just a circle. It uses the same files and everything."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_whole", "Didn't anyone ever tell you to shut your whole pie?"),
        },
        catalog.i18nc("symbol_name", "Pie (Whole) (Outline)"): {
            PATH_KEY: "symbols/geometric/circle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_whole_outline", "The outline of a whole pie. It's just the outline of a whole circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_whole_outline", "It's either a really bad donut or a stain from a coffee mug."),
        },
        catalog.i18nc("symbol_name", "Pie Seven Eighths"): {
            PATH_KEY: "symbols/pies/pie_seven_eighths.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_seven_eighths", "Seven eighths of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_seven_eighths", "You still have 87.5% of your HP left. You can do this."),
        },
        catalog.i18nc("symbol_name", "Pie Seven Eighths (Outline)"): {
            PATH_KEY: "symbols/pies/pie_seven_eighths_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_seven_eighths_outline", "Seven eighths of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_seven_eighths_outline", "Just say it's \"outsider art\" called \"meeting time\"."),
        },
        catalog.i18nc("symbol_name", "Pie Three Quarters"): {
            PATH_KEY: "symbols/pies/pie_three_quarters.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_three_quarters", "Three quarters of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_three_quarters", "OKAY, WHO TOOK A PIECE OF MY CAKE?"),
        },
        catalog.i18nc("symbol_name", "Pie Three Quarters (Outline)"): {
            PATH_KEY: "symbols/pies/pie_three_quarters_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_three_quarters_outline", "Three quarters of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_three_quarters_outline", "I think this means your time is running out. Or something is 75% loaded.<br>I'm conflicted as to whether you should stick around."),
        },
        catalog.i18nc("symbol_name", "Pie Five Eighths"): {
            PATH_KEY: "symbols/pies/pie_five_eighths.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_five_eighths", "Five eighths of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_five_eighths", "If you squint hard, you can't really see the difference between this and three quarters."),
        },
        catalog.i18nc("symbol_name", "Pie Five Eighths (Outline)"): {
            PATH_KEY: "symbols/pies/pie_five_eighths_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_five_eighths_outline", "Five eighths of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_five_eighths_outline", "It looks like one of those \"smart speakers\" that try to blend in by looking like nothing else you own."),
        },
        catalog.i18nc("symbol_name", "Pie Half"): {
            PATH_KEY: "symbols/pies/pie_half.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_half", "Half of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_half", "It says a lot about your personality whether you see it as \"half a pie eaten\" or \"half a pie left\"."),
        },
        catalog.i18nc("symbol_name", "Pie Half (Outline)"): {
            PATH_KEY: "symbols/pies/pie_half_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_half_outline", "Half of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_half_outline", "That looks like a bowl. Which someone... managed to stand on its edge? Nice balance."),
        },
        catalog.i18nc("symbol_name", "Pie Three Eighths"): {
            PATH_KEY: "symbols/pies/pie_three_eighths.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_three_eighths", "Three eighths of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_three_eighths", "I can't remember whether the moon looking like this means it's high or low tide."),
        },
        catalog.i18nc("symbol_name", "Pie Three Eighths (Outline)"): {
            PATH_KEY: "symbols/pies/pie_three_eighths_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_three_eighths_outline", "Three eighths of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_three_eighths_outline", "No, it's not a pizza, it's a pie. Why is it a pie? <b>Because I say so, that's why!</b>"),
        },
        catalog.i18nc("symbol_name", "Pie Quarter"): {
            PATH_KEY: "symbols/pies/pie_quarter.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_quarter", "One quarter of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_quarter", "I'm sure at least 1 in 4 people are still paying attention."),
        },
        catalog.i18nc("symbol_name", "Pie Quarter (Outline)"): {
            PATH_KEY: "symbols/pies/pie_quarter_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_quarter_outline", "One quarter of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_quarter_outline", "Okay, I got one hit left. Save point? Save point? Come heeeere, save pointy!"),
        },
        catalog.i18nc("symbol_name", "Pie One Eighth"): {
            PATH_KEY: "symbols/pies/pie_one_eighth.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_one_eighth", "One eighth of a circle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_one_eighth", "You <i>could</i> call it a round-bottom isosceles triangle if you want. I'd advise against it though."),
        },
        catalog.i18nc("symbol_name", "Pie One Eighth (Outline)"): {
            PATH_KEY: "symbols/pies/pie_one_eighth_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_pies:pie_one_eighth_outline", "One eighth of a circle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_pies:pie_one_eighth_outline", "I swear I'm going to drain this symbol for every octant it's worth."),
        },
    },

    _symbols_category_stars: {
        catalog.i18nc("symbol_name", "Star 5 Point"): {
            PATH_KEY: "symbols/stars/star_5_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point", "A typical 5 pointed star."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point", "*Note: Not astronomically correct."),
        },
        catalog.i18nc("symbol_name", "Star 5 Point (Outline)"): {
            PATH_KEY: "symbols/stars/star_5_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point_outline", "A typical 5 pointed star. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point_outline", "*Note: May be astrologically correct.<br>I don't know enough astrology to say one way or the other."),
        },
        catalog.i18nc("symbol_name", "Star 5 Point Half"): {
            PATH_KEY: "symbols/stars/star_5_point_half.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point_half", "Half of a typical 5 pointed star."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point_half", "Half a star is more important than you think. Take one away from your ride share driver and they might be delisted."),
        },
        catalog.i18nc("symbol_name", "Star 5 Point Half (Outline)"): {
            PATH_KEY: "symbols/stars/star_5_point_half_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point_half_outline", "Half of a typical 5 pointed star. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point_half_outline", "In Hollywood terms, I think this represents a has-been \"celebrity\"."),
        },
        catalog.i18nc("symbol_name", "Double Star 5 Point"): {
            PATH_KEY: "symbols/stars/double_star_5_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:double_star_5_point", "Two 5 pointed stars overlaid on each other."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:double_star_5_point", "In real life two stars on each other is less pretty and more boom-y."),
        },
        catalog.i18nc("symbol_name", "Double Star 5 Point (Outline)"): {
            PATH_KEY: "symbols/stars/double_star_5_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:double_star_5_point_outline", "Two 5 pointed stars overlaid on each other. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:double_star_5_point_outline", "If you think this looks cluttered, try closing one eye.<br>If it looks any less cluttered, get your eyes tested."),
        },
        catalog.i18nc("symbol_name", "Star 8 Point"): {
            PATH_KEY: "symbols/stars/star_8_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_8_point", "An 8 pointed star, more typically used for achievements or for emphasis."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_8_point", "You're #1, according to this card I got you that says you're #1."),
        },
        catalog.i18nc("symbol_name", "Star 8 Point (Outline)"): {
            PATH_KEY: "symbols/stars/star_8_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_8_point_outline", "An 8 pointed star, more typically used for achievements or for emphasis. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_8_point_outline", "Ironically, the more points something has, as a general rule, the less likely it is considered dangerous."),
        },
    },

    _symbols_category_symbols_icons: {
        catalog.i18nc("symbol_name", "Add"): {
            PATH_KEY: "symbols/symbols_icons/add.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:add", "An addition sign used in mathematics."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:add", "At least when it's only addition you're not getting into the <b>complex</b> (and by that I mean boring) parts of math first."),
        },
        catalog.i18nc("symbol_name", "Agender"): {
            PATH_KEY: "symbols/symbols_icons/agender.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:agender", "A symbol representing people who do not identify as any gender."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:agender", "Getting these gender symbols in without them being too obvious was my secret a-gender."),
        },
        catalog.i18nc("symbol_name", "Biohazard Warning"): {
            PATH_KEY: "symbols/symbols_icons/biohazard_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:biohazard_warning", "A biohazard warning symbol"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:biohazard_warning", "I have no idea what all those lines are supposed to mean. And I've never stuck around long enough to find out."),
        },
        catalog.i18nc("symbol_name", "Biohazard Warning (Filled)"): {
            PATH_KEY: "symbols/symbols_icons/biohazard_warning_filled.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:biohazard_warning_filled", "A visual negative of biohazard warning symbol"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:biohazard_warning_filled", "Be honest. You've stuck one of these to the back of <b>someone</b> in your office's chair."),
        },
        catalog.i18nc("symbol_name", "Check"): {
            PATH_KEY: "symbols/symbols_icons/check.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:check", "A \"check\" (or tick) mark, usually used to indicate acknowledgement of something."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:check", "My name is Slashee the Cow and I approve this message. ✅"),
        },
        catalog.i18nc("symbol_name", "Circle Warning"): {
            PATH_KEY: "symbols/symbols_icons/circle_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:circle_warning", "Exclamation mark in a circle, used to indicate caution should be taken."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:circle_warning", "I always have one of these up because the real danger is the unknown, so I don't know what to be cautious about."),
        },
        catalog.i18nc("symbol_name", "Circle Warning (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/circle_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:circle_warning_outline", "Exclamation mark in a circle, used to indicate caution should be taken. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:circle_warning_outline", "They might want to hang one of these on cows' necks so you know to stay away from the face. Methane burps stink."),
        },
        catalog.i18nc("symbol_name", "Cog"): {
            PATH_KEY: "symbols/symbols_icons/cog.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cog", "A cog or gear used in machinery."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cog", "If you can find one that doesn't <i>look</i> important, it's also fun to grab them and push them along like a wheel."),
        },
        catalog.i18nc("symbol_name", "Cog (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/cog_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cog_outline", "A cog or gear used in machinery. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cog_outline", "When I see one of these worn out it makes me feel better because finally something has worse teeth than I do."),
        },
        catalog.i18nc("symbol_name", "Cross"): {
            PATH_KEY: "symbols/symbols_icons/cross.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cross", "The letter X, placed in the middle of something to indicate \"cross\"."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cross", "<i>Technically</i> it doesn't mean <i>angry</i> cross, but when a program keeps freezing, clicking this icon is a great way to let that anger out.<br>Unless you forgot to save your work."),
        },
        catalog.i18nc("symbol_name", "Dangerous"): {
            PATH_KEY: "symbols/symbols_icons/dangerous.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:dangerous", "The letter X inside an octagon, indicating danger is nearby."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:dangerous", "What's so bad about octagons? X by itself, a little bad. X in octagon, <b>really</b> bad."),
        },
        catalog.i18nc("symbol_name", "Dangerous (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/dangerous_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:dangerous_outline", "The letter X inside an octagon, indicating danger is nearby. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:dangerous_outline", "I'm never afraid to do dangerous things. Mostly because I don't see the signs saying they're dangerous."),
        },
        catalog.i18nc("symbol_name", "Divide"): {
            PATH_KEY: "symbols/symbols_icons/divide.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:divide", "A division sign used in mathematics."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:divide", "Great military strategy: Divide and Conquer!<br>Tedious military strategy: Long Divide and Squander!"),
        },
        catalog.i18nc("symbol_name", "Donut"): {
            PATH_KEY: "symbols/symbols_icons/donut.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:donut", "A hollow circle that resembles a donut."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:donut", "You'll get a much better donut if you go to the Shapes section and make a \"torus\"."),
        },
        catalog.i18nc("symbol_name", "Donut (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/donut_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:donut_outline", "A hollow circle that resembles a donut. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:donut_outline", "Mmmmm, donuts."),
        },
        catalog.i18nc("symbol_name", "Exclamation"): {
            PATH_KEY: "symbols/symbols_icons/exclamation.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:exclamation", "An exclamation mark, generally used to emphasise something."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:exclamation", "This tooltip is important!!!"),
        },
        catalog.i18nc("symbol_name", "Female"): {
            PATH_KEY: "symbols/symbols_icons/female.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:female", "A symbol representing people that identify as female."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:female", "Unfortunately there's only so many of these symbols, because I have a gender-ous helping jokes available."),
        },
        catalog.i18nc("symbol_name", "Hang Up"): {
            PATH_KEY: "symbols/symbols_icons/hang up.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:hang up", "A picture of an old telephone handset pointed down, ready to hang up a call."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:hang up", "Given most of the calls I get are scams, I should probably replace my Phone app with this."),
        },
        catalog.i18nc("symbol_name", "Home"): {
            PATH_KEY: "symbols/symbols_icons/home.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:home", "Simplified illustration of a house."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:home", "Home is where the heart is. Unless you're on the organ transplant waiting list."),
        },
        catalog.i18nc("symbol_name", "Key"): {
            PATH_KEY: "symbols/symbols_icons/key.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:key", "A design of a key that would fit into a lock. May also represent \"password\" in computer usage."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:key", "Of course thieves always check for a spare key under the fake rock near the front door. That's why I keep my spare under a <i>real</i> rock."),
        },
        catalog.i18nc("symbol_name", "Keyboard"): {
            PATH_KEY: "symbols/symbols_icons/keyboard.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:keyboard", "A simplified icon of a computer keyboard."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:keyboard", "I've been holding onto spare computer parts long enough that I have a million of these. Now I just need to find some monkeys and Shakespeare, here I come!"),
        },
        catalog.i18nc("symbol_name", "Keyboard (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/keyboard_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:keyboard_outline", "A simplified icon of a computer keyboard. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:keyboard_outline", "I'd actually like some feedback here. Is it weird that I love both Cherry Blue <b>and</b> Cherry Red switches?"),
        },
        catalog.i18nc("symbol_name", "Kitchen Counter"): {
            PATH_KEY: "symbols/symbols_icons/kitchen_counter.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:kitchen_counter", "Kitchen counter with tap and pot."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:kitchen_counter", "<b>Literally</b> the only reason I put that in here was so that I would have the kitchen sink. I'm serious."),
        },
        catalog.i18nc("symbol_name", "Lightbulb"): {
            PATH_KEY: "symbols/symbols_icons/lightbulb.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:lightbulb", "A lightbulb, often used to indicate an idea."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:lightbulb", "Seriously, incandescent? Replace that with an LED bulb already!"),
        },
        catalog.i18nc("symbol_name", "Lightbulb (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/lightbulb_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:lightbulb_outline", "A lightbulb, often used to indicate an idea."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:lightbulb_outline", "I think someone turned off the switch on this one. Or maybe they're just a little dim."),
        },
        catalog.i18nc("symbol_name", "Male"): {
            PATH_KEY: "symbols/symbols_icons/male.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:male", "A symbol representing people who identify as male."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:male", "Gender-ally, I don't judge people based on labels like this."),
        },
        catalog.i18nc("symbol_name", "Man"): {
            PATH_KEY: "symbols/symbols_icons/man.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:man", "A very commonly used illustration of a man's figure."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:man", "How is it this symbol became practically synonymous with toilets?"),
        },
        catalog.i18nc("symbol_name", "Microphone"): {
            PATH_KEY: "symbols/symbols_icons/microphone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:microphone", "A simplified depiction of a microphone in a stand."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:microphone", "I thought free speech meant you didn't have to pay anyone to be allowed to speak. Imagine how great the internet would be if you did."),
        },
        catalog.i18nc("symbol_name", "Microphone (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/microphone_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:microphone_outline", "A simplified depiction of a microphone in a stand. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:microphone_outline", "If it looks like this, you're probably muted. Whether that's a good thing or a bad thing is not for me to judge."),
        },
        catalog.i18nc("symbol_name", "Mouse"): {
            PATH_KEY: "symbols/symbols_icons/mouse.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse", "A mouse used with a computer."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse", "Not to be confused with a rodent.<br>They get pretty annoyed when you double click."),
        },
        catalog.i18nc("symbol_name", "Mouse (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/mouse_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_outline", "A mouse used with a computer. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_outline", "This mouse has two buttons. My mouse has fourteen. Yours is probably somewhere between the two."),
        },
        catalog.i18nc("symbol_name", "Mouse Cursor"): {
            PATH_KEY: "symbols/symbols_icons/mouse_cursor.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_cursor", "The mouse cursor used in most computer operating systems."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_cursor", "Technically I'm not sure this <i>doesn't</i> belong in the \"arrows\" category."),
        },
        catalog.i18nc("symbol_name", "Mouse Cursor (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/mouse_cursor_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_cursor_outline", "The mouse cursor used in most computer operating systems. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_cursor_outline", "While some users may be less experienced, I'm sure they could figure out a mouse cursor<br>which isn't <i>literally</i> pointing at the mouse's location."),
        },
        catalog.i18nc("symbol_name", "Multiplication"): {
            PATH_KEY: "symbols/symbols_icons/cross.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cross", "The symbol for multiplication calculations in mathematics."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cross", "Yes, it's exactly the same as the \"cross\" earlier. I just multiplied its entry in the list by two."),
        },
        catalog.i18nc("symbol_name", "No Symbol"): {
            PATH_KEY: "symbols/symbols_icons/no_symbol.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:no_symbol", "A circle with a thick line going from top left to bottom right,<br>a universally recognised symbol saying that something is not permitted."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:no_symbol", "As a daredevil, I ignore these \"no\" signs all the time. Like at the theater, the one that says you're supposed to turn off your phone."),
        },
        catalog.i18nc("symbol_name", "No Smoking"): {
            PATH_KEY: "symbols/symbols_icons/no_smoking.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:no_smoking", "An illustration of a lit cigarette with the thick line from the \"no symbol\" overlaid."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:no_smoking", "Look, I'm not going to joke about this one. Don't do it. It's bad for you and anyone around you.<br>And the smoking? Double the \"joking\" part. Don't do it. Don't do it. It's bad for you and anyone around you. It's bad for you and anyone around you."),
        },
        catalog.i18nc("symbol_name", "Octagonal Warning"): {
            PATH_KEY: "symbols/symbols_icons/octagonal_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:octagonal_warning", "An octagon with an exclamation mark in the middle to indicate a warning."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:octagonal_warning", "The \"it's not deadly serious\" of the circle warning combined with the \"it's deadly serious\" of the X in the octagon? Kinda sending mixed signals."),
        },
        catalog.i18nc("symbol_name", "Octagonal Warning (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/octagonal_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:octagonal_warning_outline", "An octagon with an exclamation mark in the middle to indicate a warning."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:octagonal_warning_outline", "Don't quote me on this, but I <i>think</i> from least to most serious, it's ! in circle, ! in octagon, X in octagon."),
        },
        catalog.i18nc("symbol_name", "Paw"): {
            PATH_KEY: "symbols/symbols_icons/paw.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:paw", "Illustration of an animal's paw."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:paw", "All the pawful jokes have been done to death. So it behooves me to say I much prefer ungulates anyway."),
        },
        catalog.i18nc("symbol_name", "Phone"): {
            PATH_KEY: "symbols/symbols_icons/phone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:phone", "An illustration of an old-fashioned phone handset."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:phone", "The last time I used a phone like this, computers weren't advanced enough to depict them like this."),
        },
        catalog.i18nc("symbol_name", "Radiation Warning"): {
            PATH_KEY: "symbols/symbols_icons/radiation_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:radiation_warning", "A large circle with a small circle in the middle surrounded by three trapezoids with curved edges at equal angles apart."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:radiation_warning", "The number of scans I've had lately, I would definitely have superpowers by now if radiation actually did that."),
        },
        catalog.i18nc("symbol_name", "Recycling"): {
            PATH_KEY: "symbols/symbols_icons/recycling.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:recycling", "Three arrows forming a circle, each with a \"folded over\" effect."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:recycling", "Recycling is important. I even recycle all the pawful jokes that have been done to death."),
        },
        catalog.i18nc("symbol_name", "Rocket"): {
            PATH_KEY: "symbols/symbols_icons/rocket.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:rocket", "An illustration of a rocket in a cartoon style."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:rocket", "How long until we get rockets that actually look like this? I think it's gonna be a long, long time."),
        },
        catalog.i18nc("symbol_name", "Search"): {
            PATH_KEY: "symbols/symbols_icons/search.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:search", "A magnifying glass, usually used as a \"search\" icon in computers programs and websites."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:search", "Why is it a magnifying glass? That just makes your search take <i>longer</i> because you can't see as much at once."),
        },
        catalog.i18nc("symbol_name", "Shield Warning"): {
            PATH_KEY: "symbols/symbols_icons/shield_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:shield_warning", "A outline of a traditional style shield with an explanation mark in the middle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:shield_warning", "Ummm... you did remember to update your antivirus software, right?"),
        },
        catalog.i18nc("symbol_name", "Shield Warning (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/shield_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:shield_warning_outline", "A outline of a traditional style shield with an explanation mark in the middle. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:shield_warning_outline", "This icon has pretty much lost all its meaining now because people have seen it so much they don't treat it any different. Like \"breaking news\"."),
        },
        catalog.i18nc("symbol_name", "Smartphone"): {
            PATH_KEY: "symbols/symbols_icons/smartphone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:smartphone", "An illustration of a generic smartphone."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:smartphone", "In however much time it takes to disseminate an icon set like this, smartphones will no longer look like that icon."),
        },
        catalog.i18nc("symbol_name", "Subtract"): {
            PATH_KEY: "symbols/symbols_icons/minus.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:minus", "A single horizontal line representing mathematical subtraction."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:minus", "Taking one part of this symbol away from the other is pretty hard when it's so simple."),
        },
        catalog.i18nc("symbol_name", "Tear"): {
            PATH_KEY: "symbols/symbols_icons/tear.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:tear", "The shape of a stereotypical illustration of a teardrop."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:tear", "I understand you're upset that you accidentally knocked over a pallet of biscuits. But if you cry about it, things are just going to get crumby."),
        },
        catalog.i18nc("symbol_name", "Tear (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/tear_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:tear_outline", "The shape of a stereotypical illustration of a teardrop. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:tear_outline", "Why is this also used as a warning light to show you're almost out of fuel?"),
        },
        catalog.i18nc("symbol_name", "Thumbs Down"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_down.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_down", "An illustration of a hand with its fingers curled up and the thumb pointing down in a sign of disapproval."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_down", "Not cool. A fully grown adult jumping into a ball pit and accidentally breaking a few kids' bones? That's <b>my</b> job."),
        },
        catalog.i18nc("symbol_name", "Thumbs Down (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_down_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_down_outline", "An illustration of a hand with its fingers curled up and the thumb pointing down in a sign of disapproval. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_down_outline", "Due to your natural arm position, giving a thumbs down is actually harder work than a thumbs up, but nobody appreciates the effort."),
        },
        catalog.i18nc("symbol_name", "Thumbs Up"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_up.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_up", "An illustration of a hand with its fingers curled up and the thumb pointing up in a sign of approval."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_up", "Awesome! I have no idea what you just did, but I'm sure it was great."),
        },
        catalog.i18nc("symbol_name", "Thumbs Up (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_up_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_up_outline", "An illustration of a hand with its fingers curled up and the thumb pointing up in a sign of approval. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_up_outline", "I AM DEFINITELY HUMAN NOT AI AND I APPROVE OF YOUR CONTENT SO I WILL GIVE YOU THIS GENERIC SIGN OF \"LIKING\"."),
        },
        catalog.i18nc("symbol_name", "Transgender"): {
            PATH_KEY: "symbols/symbols_icons/transgender.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:transgender", "A symbol representing people who do not identify as the gender they were assigned at birth."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:transgender", "Hopefully these puns don't make it on the engendered species list."),
        },
        catalog.i18nc("symbol_name", "Triangle Warning"): {
            PATH_KEY: "symbols/symbols_icons/triangle_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:triangle_warning", "A triangle with an exclamation mark in it, indcating a warning."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:triangle_warning", "Seriously??? <b>Another</b> shape with a ! in it you want me to rank based on severity?"),
        },
        catalog.i18nc("symbol_name", "Triangle Warning (Outline)"): {
            PATH_KEY: "symbols/symbols_icons/triangle_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:triangle_warning_outline", "A triangle with an exclamation mark in it, indcating a warning. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:triangle_warning_outline", "The most dangerous sign usually seen bearing a ! in a triangle is \"wet floor\"."),
        },
        catalog.i18nc("symbol_name", "Woman"): {
            PATH_KEY: "symbols/symbols_icons/woman.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:woman", "A very commonly used illustration of a woman's figure, expressed with the silhouette of wearing a dress."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:woman", "I didn't actually think you could get away with wearing dresses that short when they started using that symbol."),
        },
    },

    _symbols_category_weather: {
        catalog.i18nc("symbol_name", "Sunny"): {
            PATH_KEY: "symbols/weather/sunny.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:sunny", "An icon representing sunny weather. It can also be used to represent the daytime."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:sunny", "Surely I'm not the only one who finds it ironic that both you need time in the sun to make you generate vitamin D<br>but that spending time in the sun can cause cancer."),
        },
        catalog.i18nc("symbol_name", "Sunny (Outline)"): {
            PATH_KEY: "symbols/weather/sunny_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:sunny_outline", "An icon representing sunny weather. It can also be used to represent the daytime. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:sunny_outline", "Some places welcome this in their weather forecast. I am not in some places."),
        },
        catalog.i18nc("symbol_name", "Partly Cloudy"): {
            PATH_KEY: "symbols/weather/partly_cloudy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:partly_cloudy", "An icon representing partly cloudy weather."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:partly_cloudy", "This is the weather <i>wanting</i> to rain, but giving up a third of the way in because it's too hard."),
        },
        catalog.i18nc("symbol_name", "Partly Cloudy (Outline)"): {
            PATH_KEY: "symbols/weather/partly_cloudy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:partly_cloudy_outline", "An icon representing partly cloudy weather. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:partly_cloudy_outline", "I'm not sure I ever really understood \"partly\" cloudy. Either there's clouds or there aren't."),
        },
        catalog.i18nc("symbol_name", "Cloud"): {
            PATH_KEY: "symbols/weather/cloud.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:cloud", "Icon representing cloudy weather."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:cloud", "Used both in weather and IT companies trying to make their product sound impressive."),
        },
        catalog.i18nc("symbol_name", "Cloud (Outline)"): {
            PATH_KEY: "symbols/weather/cloud_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:cloud_outline", "Icon representing cloudy weather. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:cloud_outline", "Is it going to rain? If you bring an umbrella, no. If you don't bring an umbrella, yes."),
        },
        catalog.i18nc("symbol_name", "Rainy"): {
            PATH_KEY: "symbols/weather/rainy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:rainy", "A symbol depicting rainy weather."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:rainy", "The chances it will rain are directly proprotional<br>to whether you're going to do something that requires being outdoors."),
        },
        catalog.i18nc("symbol_name", "Rainy (Outline)"): {
            PATH_KEY: "symbols/weather/rainy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:rainy_outline", "A symbol depicting rainy weather. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:rainy_outline", "If you're singing outside \"Rain, Rain, Go Away\" does that mean you're \"Singing In The Rain\"?"),
        },
        catalog.i18nc("symbol_name", "Thunderstorm"): {
            PATH_KEY: "symbols/weather/thunderstorm.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:thunderstorm", "Icon representing weather with rain and lightning."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:thunderstorm", "I actually like the sound of a storm, the thunder, the rain, the lightning... as long as I'm inside, of course.<br>Does that make me weird?"),
        },
        catalog.i18nc("symbol_name", "Thunderstorm (Outline)"): {
            PATH_KEY: "symbols/weather/thunderstorm_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:thunderstorm_outline", "Icon representing weather with rain and lightning. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:thunderstorm_outline", "I'd like to think that the weather has a sense of irony because rain puts out fires but lightning starts them."),
        },
        catalog.i18nc("symbol_name", "Electric Bolt"): {
            PATH_KEY: "symbols/weather/electric_bolt.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:electric_bolt", "Icon representing a lightning bolt."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:electric_bolt", "Despite popular belief, lightning can strike in the same place twice.<br>Especially if that place is a lightning rod."),
        },
        catalog.i18nc("symbol_name", "Electric Bolt (Outline)"): {
            PATH_KEY: "symbols/weather/electric_bolt_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:electric_bolt_outline", "Icon representing a lightning bolt. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:electric_bolt_outline", "You probably shouldn't try to use lightning to cook food. It'll probably end up a little <i>too</i> crispy."),
        },
        catalog.i18nc("symbol_name", "Snowy"): {
            PATH_KEY: "symbols/weather/snowy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:snowy", "An icon illustrating snowy weather."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:snowy", "I'm going to have to take this one on faith. I have literally never seen snow."),
        },
        catalog.i18nc("symbol_name", "Snowy (Outline)"): {
            PATH_KEY: "symbols/weather/snowy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:snowy_outline", "An icon illustrating snowy weather. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:snowy_outline", "Just because rain is technically snow which isn't cold enough to be snow doesn't mean you can say you're in a snowy area."),
        },
        catalog.i18nc("symbol_name", "Night"): {
            PATH_KEY: "symbols/weather/night.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:night", "A symbol resembling a waning moon. It is used to represent night-time."),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:night", "Don't forget that the moon affects the ocean tide, folks. It's actually pretty cool science.<br>Don't forget that tides affect coastal erosion, folks with waterfront houses."),
        },
        catalog.i18nc("symbol_name", "Night (Outline)"): {
            PATH_KEY: "symbols/weather/night_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:night_outline", "A symbol resembling a waning moon. It is used to represent night-time. (Outline)"),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:night_outline", "After a hard, long day, there's nothing better than coming home and writing hundreds of tooltips for a Cura plugin."),
        },
    },

}

Symbol_Category_Tooltips = {
    _symbols_category_arrows: catalog.i18nc("symbol_category_tooltip:arrows","Arrows: they point at things!<br>If you rotate or mirror them, they point at <i>other</i> things!"),
    f"{_symbols_category_arrows}_alt": catalog.i18nc("symbol_category_tooltip_alt:arrows","I actually created this category first.<br>I figured I needed to get myself pointed in the right direction."),
    _symbols_category_astrological_signs: catalog.i18nc("symbol_category_tooltip:astrological_signs","Known as astrological, zodiac or birth signs, they are said to influence your personality."),
    f"{_symbols_category_astrological_signs}_alt": catalog.i18nc("symbol_category_tooltip_alt:astrological_signs","\"said to influence your personality\" <i>Pfffftt....</i> Whoever came up with that was probably under the influence."),
    _symbols_category_card_suits: catalog.i18nc("symbol_category_tooltip:card_suits","The suits in a standard deck of playing cards and their outlines."),
    f"{_symbols_category_card_suits}_alt": catalog.i18nc("symbol_category_tooltip_alt:card_suits","No, I'm not going to teach you how to count cards. I'm pretty sure it's about memory. I forget how."),
    _symbols_category_emojis: catalog.i18nc("symbol_category_tooltip:emojis","Emojis! 😀 Some people can't get enough."),
    f"{_symbols_category_emojis}_alt": catalog.i18nc("symbol_category_tooltip_alt:emojis","I don't care how many times people ask, there are two particular fruit emojis I <b>will not</b> add to this."),
    _symbols_category_geometric: catalog.i18nc("symbol_category_tooltip:geometric","Basic geometric shapes, slight variations (rounded rectangle, yay!) and outline variations."),
    f"{_symbols_category_geometric}_alt": catalog.i18nc("symbol_category_tooltip_alt:geometric","Only two thirds as much fun as the \"Basics\" category of Shapes because you're missing a dimension.<br>The \"Basics\" category was fun... wasn't it?"),
    _symbols_category_hearts: catalog.i18nc("symbol_category_tooltip:hearts","Hearts, broken heart, arrow through the heart and outline versions."),
    f"{_symbols_category_hearts}_alt": catalog.i18nc("symbol_category_tooltip_alt:hearts","Not that I'm a lawyer, but I think you should leave the \"arrow through heart\" as a 2D symbol and as inspiration."),
    _symbols_category_pies: catalog.i18nc("symbol_category_tooltip:pies","Pies, segments and outline versions.<br>Really give the charts in your next business presentations a boost!"),
    f"{_symbols_category_pies}_alt": catalog.i18nc("symbol_category_tooltip_alt:pies","I was considering creating a Shapes version with tapered edges and crusts,<br>but then I realised that the toruses were probably teasing people enough already."),
    _symbols_category_stars: catalog.i18nc("symbol_category_tooltip:stars","A few kinds of stars and their outlines."),
    f"{_symbols_category_stars}_alt": catalog.i18nc("symbol_category_tooltip_alt:stars","This doesn't have an outline of your favourite celebrity. Not that kind of star."),
    _symbols_category_symbols_icons: catalog.i18nc("symbol_category_tooltip:symbols_icons","Symbols & Icons: For everything which didn't get its own category."),
    f"{_symbols_category_symbols_icons}_alt": catalog.i18nc("symbol_category_tooltip_alt:symbols_icons","I only just realised when I was writing this tooltip that I had not literally included the kitchen sink so I had to find one of those to add to it."),
    _symbols_category_weather: catalog.i18nc("symbol_category_tooltip:weather","Icons representing various weather conditions"),
    f"{_symbols_category_weather}_alt": catalog.i18nc("symbol_category_tooltip_alt:weather","Today's forecast: all of these. Within about four hours of each other. Either buckle up or get ready to tan."),
}

Symbol_Category_Thumbnail_Filenames = {
    _symbols_category_arrows: "symbols/arrows.webp",
    _symbols_category_astrological_signs: "symbols/astrological_signs.webp",
    _symbols_category_card_suits: "symbols/card_suits.webp",
    _symbols_category_emojis: "symbols/emojis.webp",
    _symbols_category_geometric: "symbols/geometric.webp",
    _symbols_category_hearts: "symbols/hearts.webp",
    _symbols_category_pies: "symbols/pies.webp",
    _symbols_category_stars: "symbols/stars.webp",
    _symbols_category_symbols_icons: "symbols/symbols_icons.webp",
    _symbols_category_weather: "symbols/weather.webp",
}
