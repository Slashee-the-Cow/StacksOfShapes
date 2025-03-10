from UM.i18n import i18nCatalog

catalog = i18nCatalog("stacksofshapes")

PATH_KEY: str = "path"
TOOLTIP_KEY: str = "tooltip"
ALT_TOOLTIP_KEY: str = "altTooltip"

_shape_category_basics: str = catalog.i18nc("shape_category", "Basics")
_shape_category_spherical: str = catalog.i18nc("shape_category", "Spherical")
_shape_category_prisms: str = catalog.i18nc("shape_category", "Prisms")
_shape_category_pyramids_cones: str = catalog.i18nc("shape_category", "Pyramids & Cones")
_shape_category_platonics: str = catalog.i18nc("shape_category", "Platonic Solids")
_shape_category_torus: str = catalog.i18nc("shape_category", "Toruses")
_shape_category_curvy: str = catalog.i18nc("shape_category", "Curvy")
_shape_category_things: str = catalog.i18nc("shape_category", "Things")
_shape_category_whatsits: str = catalog.i18nc("shape_category", "Whatsits")
_shape_category_tetrominoes: str = catalog.i18nc("shape_category", "Tetrominoes")
_shape_category_negative_spherical: str = catalog.i18nc("shape_category", "Negative Spherical")

Shapes = {
    _shape_category_basics: {
        catalog.i18nc("shape_name_basics", "Cube"): {
            PATH_KEY: "platonics/hexahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:cube", "All faces are the same size and all the angles are equal.<br>It is one of the platonic solids."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_basics:cube", "If you want to sound smart, the technical term is \"hexahedron\"."),
        },
        catalog.i18nc("shape_name_basics", "Sphere"): {
            PATH_KEY: "spherical/sphere.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:sphere", "A perfectly round 3D shape. Often used as a ball.<br>Every part of the outside is the same distance from the centre."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name_basics", "Cylinder"): {
            PATH_KEY: "cylinders/cylinder.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:cylinder", "Two circles with a rounded surface connecting them.<br>A can of soup is a cylinder."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name_basics", "Cone"): {
            PATH_KEY: "pyramids_cones/cone.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:cone", "A round base which comes to a point at the top.<br>Can be different heights depending on the taper angle."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name_basics", "Square Pyramid"): {
            PATH_KEY: "pyramids_cones/pyramid_square.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:pyramid_square", "Similar to a cone except the base is a square.<br>The ancient Egyptians buried their pharoahs in buildings shaped like this."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name_basics", "Recangular Prism"): {
            PATH_KEY: "prisms/prism_rectangular.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:prism_rectangular", "A \"cuboid\", like a cube except the faces are not the same size.<br>Many things such as boxes are forms of this shape."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name_basics", "Torus (Donut)"): {
            PATH_KEY: "torus/torus.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_basics:torus", "A ring shaped surface created by revolving a circle around a centre point.<br>Also a delicious treat."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        }
    },
    _shape_category_spherical: {
        catalog.i18nc("shape_name", "Sphere"): {
            PATH_KEY: "spherical/sphere.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Three Quarter Spherical Sector"): {
            PATH_KEY: "spherical/three_quarter_spherical_sector.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Hemisphere"): {
            PATH_KEY: "spherical/hemisphere.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Spherical Quadrant"): {
            PATH_KEY: "spherical/spherical_quadrant.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Spherical Octant"): {
            PATH_KEY: "spherical/spherical_octant.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Spherical Octant (Corner)"):{
            PATH_KEY: "spherical/spherical_octant_corner.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
    },
    _shape_category_prisms: {
        catalog.i18nc("shape_name", "Rectangular Prism"): {
            PATH_KEY: "prisms/prism_rectangular.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Hexagonal Prism"): {
            PATH_KEY: "prisms/prism_hexagonal.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Octangonal Prism"): {
            PATH_KEY: "prisms/prism_octagonal.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Triangular Prism (Equilateral)"): {
            PATH_KEY: "prisms/prism_triangular_equilateral.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Triangular Prism (Right)"): {
            PATH_KEY: "prisms/prism_triangular_right.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Trapezium Prism"): {
            PATH_KEY: "prisms/prism_trapezium.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Rhombic Prism"): {
            PATH_KEY: "prisms/prism_rhombic.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Parallelogram Prism"): {
            PATH_KEY: "prisms/prism_parallelogram.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        }
    },
    _shape_category_pyramids_cones: {
        catalog.i18nc("shape_name", "Triangular Pyramid (3 sides)"): {
            PATH_KEY: "platonics/tetrahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Square Pyramid (4 sides)"): {
            PATH_KEY: "pyramids_cones/pyramid_square.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Cone"): {
            PATH_KEY: "pyramids_cones/cone.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_pyramids:cone", "A cone is just a pyramid with a round base."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Pentagonal Pyramid (5 sides)"): {
            PATH_KEY: "pyramids_cones/pyramid_pentagon.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Hexagonal Pyramid (6 sides)"): {
            PATH_KEY: "pyramids_cones/pyramid_hexagon.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Octagonal Pyramid (8 sides)"): {
            PATH_KEY: "pyramids_cones/pyramid_octagon.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Frustum (Conical)"): {
            PATH_KEY: "pyramids_cones/frustum_conical.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_pyramids_frustum:", "A cone with the top cut off"),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Frustum (Square)"): {
            PATH_KEY: "pyramids_cones/frustum_square.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_pyramids:frustum_square", "The frustum princieple can also be applied to regular pyramids"),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        }
    },
    _shape_category_platonics: {
        catalog.i18nc("shape_name", "Tetrahedron (4 sides)"): {
            PATH_KEY: "platonics/tetrahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Hexahedron (6 sides)"): {
            PATH_KEY: "platonics/hexahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_platonic", "Technically the term is *regular* hexahedron.<br>But I've gotten nerdy enough already."),
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Octahedron (8 sides)"): {
            PATH_KEY: "platonics/octahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Dodecahedron (12 sides)"): {
            PATH_KEY: "platonics/dodecahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Icosahedron (20 sides)"): {
            PATH_KEY: "platonics/icosahedron.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
    },
    _shape_category_torus: {
        catalog.i18nc("shape_name", "Torus (Thick)"): {
            PATH_KEY: "torus/torus_thick.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Torus"): {
            PATH_KEY: "torus/torus.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Torus (Thin)"): {
            PATH_KEY: "torus/torus_thin.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Torus (Extra Thin)"): {
            PATH_KEY: "torus/torus_thin_extra.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
    },
    _shape_category_curvy: {
        catalog.i18nc("shape_name", "Ellipsoid"): {
            PATH_KEY: "curvy/ellipsoid.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_curvy:ellipsoid", "An ellipsoid basically means a stretched out sphere."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_curvy:ellipsoid", ""),
        },
    },
    _shape_category_things: {
        catalog.i18nc("shape_names", "Capsule"): {
            PATH_KEY: "things/capsule.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_things:", "Everybody hates taking their medicine. But trust me, it's good for you.",),
        },
        catalog.i18nc("shape_names", "Helix"): {
            PATH_KEY: "things/helix.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_things:helix", "Springs are probably the best example of these.",),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_names", "Utah Teapot"): {
            PATH_KEY: "things/utah_teapot.stl",
            TOOLTIP_KEY: "The Utah Teapot is a standard reference object in 3D computer graphics, from 1975. It was created by Martin Newell at the University of Utah and has been used in countless graphics papers and demos.<br>Sounds boring, but trust me, it's a big deal.<br>You can see one in the original Toy Story if you look closely.",
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", "")
        }
    },
    _shape_category_whatsits: {
        catalog.i18nc("shape_name:whatsits", "3D Plus"): {
            PATH_KEY: "whatsits/3d_plus.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:3dplus", "An addition sign in all directions."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:3dplus", "As if maths wasn't hard enough, now this?"),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 3x3"): {
            PATH_KEY: "whatsits/tumbling_blocks_3x3.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks3x3", "If you look at it from the correct angle, it looks flat.<br>The name for a 2D version of this is \"rhombille tiling\"."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks3x3", "Also known as \"The World's Most Annoying Staircase\"."),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 5x5"): {
            PATH_KEY: "whatsits/tumbling_blocks_5x5.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks5x5", "This pattern can repeat as large as you want."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks5x5", "Don't look at it too long or you'll get a headache."),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 7x7"): {
            PATH_KEY: "whatsits/tumbling_blocks_7x7.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks7x7", "To produce a 2D version of the effect, you need to form hexagons out of three diamonds."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks7x7", "I'm only halfway through these and I'm already out of jokes."),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 9x9"): {
            PATH_KEY: "whatsits/tumbling_blocks_9x9.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks9x9", "The bigger it is, the easier to fool the eye into a flat or 3D perspective."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks9x9", "Easier to spot when hiding in carpet than a Lego brick, but much more painful to step on."),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 15x15"): {
            PATH_KEY: "whatsits/tumbling_blocks_15x15.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks15x15", "Technically there's no reason this pattern has to go by odd numbers. I just think they look better like that."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks15x15", "And with my \"odd numbers\" decree, I'm one step closer to becoming a dictator."),
        },
        catalog.i18nc("shape_name:whatsits", "Tumbling Blocks 50x50"): {
            PATH_KEY: "whatsits/tumbling_blocks_50x50.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_whatits:tumblingblocks50x50", "There comes a line that shouldn't be crossed when upscaling things. This is probably that line."),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_whatsits:tumblingblocks50x50", "English translation: I did make a 100x100 but it was going to eat up too much of the plugin size limit."),
        },
    },
    _shape_category_tetrominoes: {
        catalog.i18nc("shape_name", "J"): {
            PATH_KEY: "tetrominoes/tetromino_j.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "L"): {
            PATH_KEY: "tetrominoes/tetromino_l.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "S"): {
            PATH_KEY: "tetrominoes/tetromino_s.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "T"): {
            PATH_KEY: "tetrominoes/tetromino_t.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "Z"): {
            PATH_KEY: "tetrominoes/tetromino_z.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "Square"): {
            PATH_KEY: "tetrominoes/tetromino_square.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:square", "Also known as the \"O\""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        },
        catalog.i18nc("shape_name", "Straight"): {
            PATH_KEY: "tetrominoes/tetromino_straight.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_tetrominoes:", "Also known as the \"I\""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_tetrominoes:", ""),
        }
    },
    _shape_category_negative_spherical: {
        catalog.i18nc("shape_name", "Negative Three Quarter Spherical Segment"): {
            PATH_KEY: "negative_spherical/negative_three_quarter_spherical_sector.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Negative Hemisphere"): {
            PATH_KEY: "negative_spherical/negative_hemisphere.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Negative Spherical Quadrant"): {
            PATH_KEY: "negative_spherical/negative_spherical_quadrant.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Negative Spherical Octant"): {
            PATH_KEY: "negative_spherical/negative_spherical_octant.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
        catalog.i18nc("shape_name", "Negative Spherical Octant (Corner)"): {
            PATH_KEY: "negative_spherical/negative_spherical_octant_corner.stl",
            TOOLTIP_KEY: catalog.i18nc("shape_tooltip_:", ""),
            ALT_TOOLTIP_KEY: catalog.i18nc("shape_alt_tooltip_:", ""),
        },
    }
}

Shape_Category_Tooltips = {
    _shape_category_basics: catalog.i18nc("shape_category_tooltip", ""),
    f"{_shape_category_basics}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_spherical: catalog.i18nc("shape_category_tooltip", "Spheres. And parts of them."),
    f"{_shape_category_spherical}_alt": catalog.i18nc("shape_category_tooltip_alt", "Keep your \"ball\" jokes to yourself."),
    _shape_category_prisms: catalog.i18nc("shape_category_tooltip", ""),
    f"{_shape_category_prisms}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_pyramids_cones: catalog.i18nc("shape_category_tooltip", ""),
    f"{_shape_category_pyramids_cones}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_platonics: catalog.i18nc("shape_category_tooltip", "3D objects where all faces and angles are exactly the same.<br>Often used as dice."),
    f"{_shape_category_platonics}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_torus: catalog.i18nc("shape_category_tooltip", "Mmmm.... donuts. That's what they look like, at least."),
    f"{_shape_category_torus}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_curvy: catalog.i18nc("shape_category_tooltip", "Things without straight edges."),
    f"{_shape_category_curvy}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_things: catalog.i18nc("shape_category_tooltip", "You may have seen these objects in real life."),
    f"{_shape_category_things}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_whatsits: catalog.i18nc("shape_category_tooltip", "These may or may not be real things.<br>They are however interesting things."),
    f"{_shape_category_whatsits}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_tetrominoes: catalog.i18nc("shape_category_tooltip", "The different shapes possible when combining four cubes."),
    f"{_shape_category_tetrominoes}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
    _shape_category_negative_spherical: catalog.i18nc("shape_category_tooltip", f"Bits of sphere subtracted from their cubic surroundings.  <br><b>Note that these pieces need to be 10% larger than the spherical pieces they would contain if using spheres from this plugin</b>."),
    f"{_shape_category_negative_spherical}_alt": catalog.i18nc("shape_category_tooltip_alt", ""),
}

Shape_Category_Thumbnail_Filenames = {
    _shape_category_basics: "basics.png",
    _shape_category_spherical: "spherical.png",
    _shape_category_prisms: "prisms.png",
    _shape_category_pyramids_cones: "pyramids_cones.png",
    _shape_category_platonics: "platonics.png",
    _shape_category_torus:  "toruses.png",
    _shape_category_curvy: "curvy.png",
    _shape_category_things: "things.png",
    _shape_category_whatsits: "whatsits.png",
    _shape_category_tetrominoes: "tetrominoes.png",
    _shape_category_negative_spherical: "negative_spherical.png",
}