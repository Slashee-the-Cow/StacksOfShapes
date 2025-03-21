// Torus for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 256 : 64;

//color("SteelBlue") // 1/8
//color("Aquamarine") // 1/4
//color("DeepSkyBlue") // 1/2
//color("MediumBlue") // 3/4
color("Wheat") // Whole
//resize([1,1,0], true)
    translate([0,0,0.25])
        rotate_extrude(angle = 360)
            translate([0.5,0,0])
                circle(d=0.5);