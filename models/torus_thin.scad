// Torus (thin) for Stacks of Shapes
// by Slashee the Cow
$fn = 64;

resize([1,1,0], true)
    translate([0,0,0.1])
        rotate_extrude()
            translate([0.5,0,0])
                circle(d=0.2);