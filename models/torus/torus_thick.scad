// Torus (thick) for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 1024 : 128;

color("Sienna")
resize([1,1,0], true)
    translate([0,0,0.35])
        rotate_extrude()
            translate([0.4,0,0])
                circle(d=0.7);