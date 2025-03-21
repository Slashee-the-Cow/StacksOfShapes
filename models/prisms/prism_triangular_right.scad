// Triangular Prism (Right) for Stacks of Shapes
// by Slashee the Cow

color("Crimson")
translate([-1.5, -0.5, 0])
    rotate([90,0,90])
        linear_extrude(3, true)
            polygon([[0,0],[0,1],[1,0]]);