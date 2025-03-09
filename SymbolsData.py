from UM.i18n import i18nCatalog

catalog = i18nCatalog("stacksofshapes")

PATH_KEY: str = "path"
TOOLTIP_KEY: str = "tooltip"
ALT_TOOLTIP_KEY: str = "altTooltip"

_symbols_category_arrows: str = catalog.i18nc("symbol_category", "arrows")
_symbols_category_astrological_signs: str = catalog.i18nc("symbol_category", "astrological_signs")
_symbols_category_card_suits: str = catalog.i18nc("symbol_category", "card_suits")
_symbols_category_emojis: str = catalog.i18nc("symbol_category", "emojis")
_symbols_category_geometric: str = catalog.i18nc("symbol_category", "geometric")
_symbols_category_hearts: str = catalog.i18nc("symbol_category", "hearts")
_symbols_category_stars: str = catalog.i18nc("symbol_category", "stars")
_symbols_category_symbols_icons: str = catalog.i18nc("symbol_category", "symbols_icons")
_symbols_category_weather: str = catalog.i18nc("symbol_category", "weather")

Symbols = {
    _symbols_category_arrows: {  # Category: _symbols_category_arrows
        catalog.i18nc("symbol_name", "Arrow Chevron"): {
            PATH_KEY: "symbols/arrows/arrow_chevron.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_chevron", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_chevron", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Chevron Short"): {
            PATH_KEY: "symbols/arrows/arrow_chevron_short.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_chevron_short", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_chevron_short", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Curve Clockwise"): {
            PATH_KEY: "symbols/arrows/arrow_curve_clockwise.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_curve_clockwise", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_curve_clockwise", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Dual"): {
            PATH_KEY: "symbols/arrows/arrow_dual.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_dual", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_dual", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Short"): {
            PATH_KEY: "symbols/arrows/arrow_short.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_short", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_short", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Single"): {
            PATH_KEY: "symbols/arrows/arrow_single.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_single", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_single", ""),
        },
        catalog.i18nc("symbol_name", "Arrow Tail"): {
            PATH_KEY: "symbols/arrows/arrow_tail.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_arrows:arrow_tail", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_arrows:arrow_tail", ""),
        },
    },

    _symbols_category_astrological_signs: {  # Category: _symbols_category_astrological_signs
        catalog.i18nc("symbol_name", "Aquarius 11"): {
            PATH_KEY: "symbols/astrological_signs/aquarius_11.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aquarius_11", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aquarius_11", ""),
        },
        catalog.i18nc("symbol_name", "Aquarius Circled 11"): {
            PATH_KEY: "symbols/astrological_signs/aquarius_circled_11.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aquarius_circled_11", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aquarius_circled_11", ""),
        },
        catalog.i18nc("symbol_name", "Aries 1"): {
            PATH_KEY: "symbols/astrological_signs/aries_1.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aries_1", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aries_1", ""),
        },
        catalog.i18nc("symbol_name", "Aries Circled 1"): {
            PATH_KEY: "symbols/astrological_signs/aries_circled_1.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:aries_circled_1", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:aries_circled_1", ""),
        },
        catalog.i18nc("symbol_name", "Cancer 4"): {
            PATH_KEY: "symbols/astrological_signs/cancer_4.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:cancer_4", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:cancer_4", ""),
        },
        catalog.i18nc("symbol_name", "Cancer Circled 4"): {
            PATH_KEY: "symbols/astrological_signs/cancer_circled_4.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:cancer_circled_4", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:cancer_circled_4", ""),
        },
        catalog.i18nc("symbol_name", "Capricorn 10"): {
            PATH_KEY: "symbols/astrological_signs/capricorn_10.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:capricorn_10", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:capricorn_10", ""),
        },
        catalog.i18nc("symbol_name", "Capricorn Circled 10"): {
            PATH_KEY: "symbols/astrological_signs/capricorn_circled_10.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:capricorn_circled_10", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:capricorn_circled_10", ""),
        },
        catalog.i18nc("symbol_name", "Gemini 3"): {
            PATH_KEY: "symbols/astrological_signs/gemini_3.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:gemini_3", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:gemini_3", ""),
        },
        catalog.i18nc("symbol_name", "Gemini Circled 3"): {
            PATH_KEY: "symbols/astrological_signs/gemini_circled_3.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:gemini_circled_3", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:gemini_circled_3", ""),
        },
        catalog.i18nc("symbol_name", "Leo 5"): {
            PATH_KEY: "symbols/astrological_signs/leo_5.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:leo_5", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:leo_5", ""),
        },
        catalog.i18nc("symbol_name", "Leo Circled 5"): {
            PATH_KEY: "symbols/astrological_signs/leo_circled_5.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:leo_circled_5", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:leo_circled_5", ""),
        },
        catalog.i18nc("symbol_name", "Libra 7"): {
            PATH_KEY: "symbols/astrological_signs/libra_7.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:libra_7", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:libra_7", ""),
        },
        catalog.i18nc("symbol_name", "Libra Circled 7"): {
            PATH_KEY: "symbols/astrological_signs/libra_circled_7.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:libra_circled_7", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:libra_circled_7", ""),
        },
        catalog.i18nc("symbol_name", "Pisces 12"): {
            PATH_KEY: "symbols/astrological_signs/pisces_12.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:pisces_12", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:pisces_12", ""),
        },
        catalog.i18nc("symbol_name", "Pisces Circled 12"): {
            PATH_KEY: "symbols/astrological_signs/pisces_circled_12.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:pisces_circled_12", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:pisces_circled_12", ""),
        },
        catalog.i18nc("symbol_name", "Sagittarius 9"): {
            PATH_KEY: "symbols/astrological_signs/sagittarius_9.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:sagittarius_9", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:sagittarius_9", ""),
        },
        catalog.i18nc("symbol_name", "Sagittarius Circled 9"): {
            PATH_KEY: "symbols/astrological_signs/sagittarius_circled_9.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:sagittarius_circled_9", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:sagittarius_circled_9", ""),
        },
        catalog.i18nc("symbol_name", "Scorpio 8"): {
            PATH_KEY: "symbols/astrological_signs/scorpio_8.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:scorpio_8", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:scorpio_8", ""),
        },
        catalog.i18nc("symbol_name", "Scorpio Circled 8"): {
            PATH_KEY: "symbols/astrological_signs/scorpio_circled_8.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:scorpio_circled_8", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:scorpio_circled_8", ""),
        },
        catalog.i18nc("symbol_name", "Taurus 2"): {
            PATH_KEY: "symbols/astrological_signs/taurus_2.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:taurus_2", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:taurus_2", ""),
        },
        catalog.i18nc("symbol_name", "Taurus Circled 2"): {
            PATH_KEY: "symbols/astrological_signs/taurus_circled_2.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:taurus_circled_2", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:taurus_circled_2", ""),
        },
        catalog.i18nc("symbol_name", "Virgo 6"): {
            PATH_KEY: "symbols/astrological_signs/virgo_6.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:virgo_6", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:virgo_6", ""),
        },
        catalog.i18nc("symbol_name", "Virgo Circled 6"): {
            PATH_KEY: "symbols/astrological_signs/virgo_circled_6.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_astrological_signs:virgo_circled_6", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_astrological_signs:virgo_circled_6", ""),
        },
    },

    _symbols_category_card_suits: {  # Category: _symbols_category_card_suits
        catalog.i18nc("symbol_name", "Heart"): {
            PATH_KEY: "symbols/hearts/heart.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:heart", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:heart", ""),
        },
        catalog.i18nc("symbol_name", "Heart Outline"): {
            PATH_KEY: "symbols/hearts/heart_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:heart_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:heart_outline", ""),
        },
        catalog.i18nc("symbol_name", "Diamond"): {
            PATH_KEY: "symbols/geometric/diamond.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:diamond", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:diamond", ""),
        },
        catalog.i18nc("symbol_name", "Diamond Outline"): {
            PATH_KEY: "symbols/geometric/diamond_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond_outline", ""),
        },
        catalog.i18nc("symbol_name", "Club"): {
            PATH_KEY: "symbols/card_suits/club.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:club", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:club", ""),
        },
        catalog.i18nc("symbol_name", "Club Outline"): {
            PATH_KEY: "symbols/card_suits/club_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:club_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:club_outline", ""),
        },
        catalog.i18nc("symbol_name", "Spade"): {
            PATH_KEY: "symbols/card_suits/spade.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:spade", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:spade", ""),
        },
        catalog.i18nc("symbol_name", "Spade Outline"): {
            PATH_KEY: "symbols/card_suits/spade_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_card_suits:spade_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_card_suits:spade_outline", ""),
        },
    },

    _symbols_category_emojis: {  # Category: _symbols_category_emojis
        catalog.i18nc("symbol_name", "Grin"): {
            PATH_KEY: "symbols/emojis/grin.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin", ""),
        },
        catalog.i18nc("symbol_name", "Grin Toothy"): {
            PATH_KEY: "symbols/emojis/grin_toothy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:grin_toothy", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:grin_toothy", ""),
        },
        catalog.i18nc("symbol_name", "Smile"): {
            PATH_KEY: "symbols/emojis/smile.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:smile", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:smile", ""),
        },
        catalog.i18nc("symbol_name", "Wink"): {
            PATH_KEY: "symbols/emojis/wink.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_emojis:wink", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_emojis:wink", ""),
        },
    },

    _symbols_category_geometric: {  # Category: _symbols_category_geometric
        catalog.i18nc("symbol_name", "Circle"): {
            PATH_KEY: "symbols/geometric/circle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:circle", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:circle", ""),
        },
        catalog.i18nc("symbol_name", "Circle Outline"): {
            PATH_KEY: "symbols/geometric/circle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:circle_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:circle_outline", ""),
        },
        catalog.i18nc("symbol_name", "Diamond"): {
            PATH_KEY: "symbols/geometric/diamond.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond", ""),
        },
        catalog.i18nc("symbol_name", "Diamond Outline"): {
            PATH_KEY: "symbols/geometric/diamond_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:diamond_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:diamond_outline", ""),
        },
        catalog.i18nc("symbol_name", "Hexagon"): {
            PATH_KEY: "symbols/geometric/hexagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:hexagon", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:hexagon", ""),
        },
        catalog.i18nc("symbol_name", "Hexagon Outline"): {
            PATH_KEY: "symbols/geometric/hexagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:hexagon_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:hexagon_outline", ""),
        },
        catalog.i18nc("symbol_name", "Octagon"): {
            PATH_KEY: "symbols/geometric/octagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:octagon", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:octagon", ""),
        },
        catalog.i18nc("symbol_name", "Octagon Outline"): {
            PATH_KEY: "symbols/geometric/octagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:octagon_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:octagon_outline", ""),
        },
        catalog.i18nc("symbol_name", "Oval"): {
            PATH_KEY: "symbols/geometric/oval.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:oval", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:oval", ""),
        },
        catalog.i18nc("symbol_name", "Oval Outline"): {
            PATH_KEY: "symbols/geometric/oval_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:oval_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:oval_outline", ""),
        },
        catalog.i18nc("symbol_name", "Parallelogram"): {
            PATH_KEY: "symbols/geometric/parallelogram.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:parallelogram", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:parallelogram", ""),
        },
        catalog.i18nc("symbol_name", "Parallelogram Outline"): {
            PATH_KEY: "symbols/geometric/parallelogram_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:parallelogram_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:parallelogram_outline", ""),
        },
        catalog.i18nc("symbol_name", "Pentagon"): {
            PATH_KEY: "symbols/geometric/pentagon.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:pentagon", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:pentagon", ""),
        },
        catalog.i18nc("symbol_name", "Pentagon Outline"): {
            PATH_KEY: "symbols/geometric/pentagon_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:pentagon_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:pentagon_outline", ""),
        },
        catalog.i18nc("symbol_name", "Rectangle"): {
            PATH_KEY: "symbols/geometric/rectangle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle", ""),
        },
        catalog.i18nc("symbol_name", "Rectangle Outline"): {
            PATH_KEY: "symbols/geometric/rectangle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_outline", ""),
        },
        catalog.i18nc("symbol_name", "Rectangle Rounded"): {
            PATH_KEY: "symbols/geometric/rectangle_rounded.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_rounded", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_rounded", ""),
        },
        catalog.i18nc("symbol_name", "Rectangle Rounded Outline"): {
            PATH_KEY: "symbols/geometric/rectangle_rounded_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:rectangle_rounded_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:rectangle_rounded_outline", ""),
        },
        catalog.i18nc("symbol_name", "Square"): {
            PATH_KEY: "symbols/geometric/square.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square", ""),
        },
        catalog.i18nc("symbol_name", "Square Outline"): {
            PATH_KEY: "symbols/geometric/square_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_outline", ""),
        },
        catalog.i18nc("symbol_name", "Square Rounded"): {
            PATH_KEY: "symbols/geometric/square_rounded.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_rounded", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_rounded", ""),
        },
        catalog.i18nc("symbol_name", "Square Rounded Outline"): {
            PATH_KEY: "symbols/geometric/square_rounded_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:square_rounded_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:square_rounded_outline", ""),
        },
        catalog.i18nc("symbol_name", "Trapezoid"): {
            PATH_KEY: "symbols/geometric/trapezoid.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:trapezoid", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:trapezoid", ""),
        },
        catalog.i18nc("symbol_name", "Trapezoid Outline"): {
            PATH_KEY: "symbols/geometric/trapezoid_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:trapezoid_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:trapezoid_outline", ""),
        },
        catalog.i18nc("symbol_name", "Triangle"): {
            PATH_KEY: "symbols/geometric/triangle.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle", ""),
        },
        catalog.i18nc("symbol_name", "Triangle Outline"): {
            PATH_KEY: "symbols/geometric/triangle_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_outline", ""),
        },
        catalog.i18nc("symbol_name", "Triangle Right"): {
            PATH_KEY: "symbols/geometric/triangle_right.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_right", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_right", ""),
        },
        catalog.i18nc("symbol_name", "Triangle Right Outline"): {
            PATH_KEY: "symbols/geometric/triangle_right_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_geometric:triangle_right_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_geometric:triangle_right_outline", ""),
        },
    },

    _symbols_category_hearts: {  # Category: _symbols_category_hearts
        catalog.i18nc("symbol_name", "Heart"): {
            PATH_KEY: "symbols/hearts/heart.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart", ""),
        },
        catalog.i18nc("symbol_name", "Heart Outline"): {
            PATH_KEY: "symbols/hearts/heart_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_outline", ""),
        },
        catalog.i18nc("symbol_name", "Heart Arrow"): {
            PATH_KEY: "symbols/hearts/heart_arrow.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_arrow", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_arrow", ""),
        },
        catalog.i18nc("symbol_name", "Heart Arrow Outline"): {
            PATH_KEY: "symbols/hearts/heart_arrow_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_arrow_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_arrow_outline", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken"): {
            PATH_KEY: "symbols/hearts/heart_broken.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken Outline"): {
            PATH_KEY: "symbols/hearts/heart_broken_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_outline", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken Left"): {
            PATH_KEY: "symbols/hearts/heart_broken_left.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_left", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_left", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken Left Outline"): {
            PATH_KEY: "symbols/hearts/heart_broken_left_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_left_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_left_outline", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken Right"): {
            PATH_KEY: "symbols/hearts/heart_broken_right.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_right", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_right", ""),
        },
        catalog.i18nc("symbol_name", "Heart Broken Right Outline"): {
            PATH_KEY: "symbols/hearts/heart_broken_right_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_hearts:heart_broken_right_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_hearts:heart_broken_right_outline", ""),
        },
    },

    _symbols_category_stars: {  # Category: _symbols_category_stars
        catalog.i18nc("symbol_name", "Double Star 5 Point"): {
            PATH_KEY: "symbols/stars/double_star_5_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:double_star_5_point", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:double_star_5_point", ""),
        },
        catalog.i18nc("symbol_name", "Double Star 5 Point Outline"): {
            PATH_KEY: "symbols/stars/double_star_5_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:double_star_5_point_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:double_star_5_point_outline", ""),
        },
        catalog.i18nc("symbol_name", "Star 5 Point"): {
            PATH_KEY: "symbols/stars/star_5_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point", ""),
        },
        catalog.i18nc("symbol_name", "Star 5 Point Outline"): {
            PATH_KEY: "symbols/stars/star_5_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_5_point_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_5_point_outline", ""),
        },
        catalog.i18nc("symbol_name", "Star 8 Point"): {
            PATH_KEY: "symbols/stars/star_8_point.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_8_point", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_8_point", ""),
        },
        catalog.i18nc("symbol_name", "Star 8 Point Outline"): {
            PATH_KEY: "symbols/stars/star_8_point_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_stars:star_8_point_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_stars:star_8_point_outline", ""),
        },
    },

    _symbols_category_symbols_icons: {  # Category: _symbols_category_symbols_icons
        catalog.i18nc("symbol_name", "Add"): {
            PATH_KEY: "symbols/symbols_icons/add.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:add", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:add", ""),
        },
        catalog.i18nc("symbol_name", "Agender"): {
            PATH_KEY: "symbols/symbols_icons/agender.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:agender", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:agender", ""),
        },
        catalog.i18nc("symbol_name", "Biohazard Warning"): {
            PATH_KEY: "symbols/symbols_icons/biohazard_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:biohazard_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:biohazard_warning", ""),
        },
        catalog.i18nc("symbol_name", "Check"): {
            PATH_KEY: "symbols/symbols_icons/check.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:check", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:check", ""),
        },
        catalog.i18nc("symbol_name", "Circle Warning"): {
            PATH_KEY: "symbols/symbols_icons/circle_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:circle_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:circle_warning", ""),
        },
        catalog.i18nc("symbol_name", "Circle Warning Outline"): {
            PATH_KEY: "symbols/symbols_icons/circle_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:circle_warning_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:circle_warning_outline", ""),
        },
        catalog.i18nc("symbol_name", "Cog"): {
            PATH_KEY: "symbols/symbols_icons/cog.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cog", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cog", ""),
        },
        catalog.i18nc("symbol_name", "Cog Outline"): {
            PATH_KEY: "symbols/symbols_icons/cog_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cog_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cog_outline", ""),
        },
        catalog.i18nc("symbol_name", "Cross"): {
            PATH_KEY: "symbols/symbols_icons/cross.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:cross", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:cross", ""),
        },
        catalog.i18nc("symbol_name", "Dangerous"): {
            PATH_KEY: "symbols/symbols_icons/dangerous.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:dangerous", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:dangerous", ""),
        },
        catalog.i18nc("symbol_name", "Dangerous Outline"): {
            PATH_KEY: "symbols/symbols_icons/dangerous_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:dangerous_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:dangerous_outline", ""),
        },
        catalog.i18nc("symbol_name", "Divide"): {
            PATH_KEY: "symbols/symbols_icons/divide.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:divide", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:divide", ""),
        },
        catalog.i18nc("symbol_name", "Donut"): {
            PATH_KEY: "symbols/symbols_icons/donut.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:donut", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:donut", ""),
        },
        catalog.i18nc("symbol_name", "Donut Outline"): {
            PATH_KEY: "symbols/symbols_icons/donut_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:donut_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:donut_outline", ""),
        },
        catalog.i18nc("symbol_name", "Exclamation"): {
            PATH_KEY: "symbols/symbols_icons/exclamation.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:exclamation", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:exclamation", ""),
        },
        catalog.i18nc("symbol_name", "Female"): {
            PATH_KEY: "symbols/symbols_icons/female.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:female", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:female", ""),
        },
        catalog.i18nc("symbol_name", "Hang Up"): {
            PATH_KEY: "symbols/symbols_icons/hang up.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:hang up", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:hang up", ""),
        },
        catalog.i18nc("symbol_name", "Home"): {
            PATH_KEY: "symbols/symbols_icons/home.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:home", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:home", ""),
        },
        catalog.i18nc("symbol_name", "Key"): {
            PATH_KEY: "symbols/symbols_icons/key.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:key", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:key", ""),
        },
        catalog.i18nc("symbol_name", "Keyboard"): {
            PATH_KEY: "symbols/symbols_icons/keyboard.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:keyboard", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:keyboard", ""),
        },
        catalog.i18nc("symbol_name", "Keyboard Outline"): {
            PATH_KEY: "symbols/symbols_icons/keyboard_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:keyboard_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:keyboard_outline", ""),
        },
        catalog.i18nc("symbol_name", "Lightbulb"): {
            PATH_KEY: "symbols/symbols_icons/lightbulb.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:lightbulb", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:lightbulb", ""),
        },
        catalog.i18nc("symbol_name", "Lightbulb Outline"): {
            PATH_KEY: "symbols/symbols_icons/lightbulb_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:lightbulb_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:lightbulb_outline", ""),
        },
        catalog.i18nc("symbol_name", "Male"): {
            PATH_KEY: "symbols/symbols_icons/male.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:male", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:male", ""),
        },
        catalog.i18nc("symbol_name", "Man"): {
            PATH_KEY: "symbols/symbols_icons/man.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:man", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:man", ""),
        },
        catalog.i18nc("symbol_name", "Microphone"): {
            PATH_KEY: "symbols/symbols_icons/microphone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:microphone", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:microphone", ""),
        },
        catalog.i18nc("symbol_name", "Microphone Outline"): {
            PATH_KEY: "symbols/symbols_icons/microphone_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:microphone_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:microphone_outline", ""),
        },
        catalog.i18nc("symbol_name", "Minus"): {
            PATH_KEY: "symbols/symbols_icons/minus.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:minus", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:minus", ""),
        },
        catalog.i18nc("symbol_name", "Mouse"): {
            PATH_KEY: "symbols/symbols_icons/mouse.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse", ""),
        },
        catalog.i18nc("symbol_name", "Mouse Cursor"): {
            PATH_KEY: "symbols/symbols_icons/mouse_cursor.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_cursor", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_cursor", ""),
        },
        catalog.i18nc("symbol_name", "Mouse Cursor Outline"): {
            PATH_KEY: "symbols/symbols_icons/mouse_cursor_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_cursor_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_cursor_outline", ""),
        },
        catalog.i18nc("symbol_name", "Mouse Outline"): {
            PATH_KEY: "symbols/symbols_icons/mouse_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:mouse_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:mouse_outline", ""),
        },
        catalog.i18nc("symbol_name", "No Smoking"): {
            PATH_KEY: "symbols/symbols_icons/no_smoking.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:no_smoking", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:no_smoking", ""),
        },
        catalog.i18nc("symbol_name", "No Symbol"): {
            PATH_KEY: "symbols/symbols_icons/no_symbol.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:no_symbol", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:no_symbol", ""),
        },
        catalog.i18nc("symbol_name", "Octagonal Warning"): {
            PATH_KEY: "symbols/symbols_icons/octagonal_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:octagonal_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:octagonal_warning", ""),
        },
        catalog.i18nc("symbol_name", "Octagonal Warning Outline"): {
            PATH_KEY: "symbols/symbols_icons/octagonal_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:octagonal_warning_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:octagonal_warning_outline", ""),
        },
        catalog.i18nc("symbol_name", "Paw"): {
            PATH_KEY: "symbols/symbols_icons/paw.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:paw", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:paw", ""),
        },
        catalog.i18nc("symbol_name", "Phone"): {
            PATH_KEY: "symbols/symbols_icons/phone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:phone", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:phone", ""),
        },
        catalog.i18nc("symbol_name", "Plus"): {
            PATH_KEY: "symbols/symbols_icons/plus.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:plus", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:plus", ""),
        },
        catalog.i18nc("symbol_name", "Radiation Warning"): {
            PATH_KEY: "symbols/symbols_icons/radiation_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:radiation_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:radiation_warning", ""),
        },
        catalog.i18nc("symbol_name", "Recycling"): {
            PATH_KEY: "symbols/symbols_icons/recycling.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:recycling", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:recycling", ""),
        },
        catalog.i18nc("symbol_name", "Rocket"): {
            PATH_KEY: "symbols/symbols_icons/rocket.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:rocket", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:rocket", ""),
        },
        catalog.i18nc("symbol_name", "Search"): {
            PATH_KEY: "symbols/symbols_icons/search.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:search", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:search", ""),
        },
        catalog.i18nc("symbol_name", "Shield Warning"): {
            PATH_KEY: "symbols/symbols_icons/shield_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:shield_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:shield_warning", ""),
        },
        catalog.i18nc("symbol_name", "Shield Warning Outline"): {
            PATH_KEY: "symbols/symbols_icons/shield_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:shield_warning_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:shield_warning_outline", ""),
        },
        catalog.i18nc("symbol_name", "Smartphone"): {
            PATH_KEY: "symbols/symbols_icons/smartphone.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:smartphone", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:smartphone", ""),
        },
        catalog.i18nc("symbol_name", "Tear"): {
            PATH_KEY: "symbols/symbols_icons/tear.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:tear", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:tear", ""),
        },
        catalog.i18nc("symbol_name", "Tear Outline"): {
            PATH_KEY: "symbols/symbols_icons/tear_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:tear_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:tear_outline", ""),
        },
        catalog.i18nc("symbol_name", "Thumbs Down"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_down.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_down", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_down", ""),
        },
        catalog.i18nc("symbol_name", "Thumbs Down Outline"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_down_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_down_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_down_outline", ""),
        },
        catalog.i18nc("symbol_name", "Thumbs Up"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_up.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_up", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_up", ""),
        },
        catalog.i18nc("symbol_name", "Thumbs Up Outline"): {
            PATH_KEY: "symbols/symbols_icons/thumbs_up_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:thumbs_up_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:thumbs_up_outline", ""),
        },
        catalog.i18nc("symbol_name", "Transgender"): {
            PATH_KEY: "symbols/symbols_icons/transgender.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:transgender", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:transgender", ""),
        },
        catalog.i18nc("symbol_name", "Triangle Warning"): {
            PATH_KEY: "symbols/symbols_icons/triangle_warning.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:triangle_warning", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:triangle_warning", ""),
        },
        catalog.i18nc("symbol_name", "Triangle Warning Outline"): {
            PATH_KEY: "symbols/symbols_icons/triangle_warning_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:triangle_warning_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:triangle_warning_outline", ""),
        },
        catalog.i18nc("symbol_name", "Woman"): {
            PATH_KEY: "symbols/symbols_icons/woman.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_symbols_icons:woman", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_symbols_icons:woman", ""),
        },
    },

    _symbols_category_weather: {  # Category: _symbols_category_weather
        catalog.i18nc("symbol_name", "Cloud"): {
            PATH_KEY: "symbols/weather/cloud.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:cloud", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:cloud", ""),
        },
        catalog.i18nc("symbol_name", "Cloud Outline"): {
            PATH_KEY: "symbols/weather/cloud_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:cloud_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:cloud_outline", ""),
        },
        catalog.i18nc("symbol_name", "Electric Bolt"): {
            PATH_KEY: "symbols/weather/electric_bolt.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:electric_bolt", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:electric_bolt", ""),
        },
        catalog.i18nc("symbol_name", "Electric Bolt Outline"): {
            PATH_KEY: "symbols/weather/electric_bolt_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:electric_bolt_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:electric_bolt_outline", ""),
        },
        catalog.i18nc("symbol_name", "Night"): {
            PATH_KEY: "symbols/weather/night.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:night", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:night", ""),
        },
        catalog.i18nc("symbol_name", "Night Outline"): {
            PATH_KEY: "symbols/weather/night_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:night_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:night_outline", ""),
        },
        catalog.i18nc("symbol_name", "Partly Cloudy"): {
            PATH_KEY: "symbols/weather/partly_cloudy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:partly_cloudy", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:partly_cloudy", ""),
        },
        catalog.i18nc("symbol_name", "Partly Cloudy Outline"): {
            PATH_KEY: "symbols/weather/partly_cloudy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:partly_cloudy_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:partly_cloudy_outline", ""),
        },
        catalog.i18nc("symbol_name", "Rainy"): {
            PATH_KEY: "symbols/weather/rainy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:rainy", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:rainy", ""),
        },
        catalog.i18nc("symbol_name", "Rainy Outline"): {
            PATH_KEY: "symbols/weather/rainy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:rainy_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:rainy_outline", ""),
        },
        catalog.i18nc("symbol_name", "Snowy"): {
            PATH_KEY: "symbols/weather/snowy.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:snowy", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:snowy", ""),
        },
        catalog.i18nc("symbol_name", "Snowy Outline"): {
            PATH_KEY: "symbols/weather/snowy_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:snowy_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:snowy_outline", ""),
        },
        catalog.i18nc("symbol_name", "Sunny"): {
            PATH_KEY: "symbols/weather/sunny.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:sunny", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:sunny", ""),
        },
        catalog.i18nc("symbol_name", "Sunny Outline"): {
            PATH_KEY: "symbols/weather/sunny_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:sunny_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:sunny_outline", ""),
        },
        catalog.i18nc("symbol_name", "Thunderstorm"): {
            PATH_KEY: "symbols/weather/thunderstorm.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:thunderstorm", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:thunderstorm", ""),
        },
        catalog.i18nc("symbol_name", "Thunderstorm Outline"): {
            PATH_KEY: "symbols/weather/thunderstorm_outline.stl",
            TOOLTIP_KEY: catalog.i18nc("symbol_tooltip_weather:thunderstorm_outline", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("symbol_alt_tooltip_weather:thunderstorm_outline", ""),
        },
    },

}

Symbol_Category_Tooltips = {
    _symbols_category_arrows: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_arrows}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_astrological_signs: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_astrological_signs}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_card_suits: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_card_suits}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_emojis: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_emojis}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_geometric: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_geometric}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_hearts: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_hearts}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_stars: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_stars}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_symbols_icons: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_symbols_icons}_alt": catalog.i18nc("category_tooltip_key_alt",""),
    _symbols_category_weather: catalog.i18nc("category_tooltip_key",""),
    f"{_symbols_category_weather}_alt": catalog.i18nc("category_tooltip_key_alt",""),
}

Symbol_Category_Thumbnail_Filenames = {
    _symbols_category_arrows: "symbols/arrows.png",
    _symbols_category_astrological_signs: "symbols/astrological_signs.png",
    _symbols_category_card_suits: "symbols/card_suits.png",
    _symbols_category_emojis: "symbols/emojis.png",
    _symbols_category_geometric: "symbols/geometric.png",
    _symbols_category_hearts: "symbols/hearts.png",
    _symbols_category_stars: "symbols/stars.png",
    _symbols_category_symbols_icons: "symbols/symbols_icons.png",
    _symbols_category_weather: "symbols/weather.png",
}
