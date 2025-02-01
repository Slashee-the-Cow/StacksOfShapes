// Triangular Prism (Right) for Basic Shapes
// by Slashee the Cow

translate([-0.5, -0.5, 0])
    rotate([90,0,90])
        linear_extrude(1, true)
            polygon([[0,0],[0,1],[1,0]]);