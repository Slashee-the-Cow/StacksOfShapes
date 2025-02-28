// Torus (extra thin) for Stacks of Shapes
// by Slashee the Cow
$fn = 64;

resize([1,1,0], true)
    translate([0,0,0.05])
        rotate_extrude()
            translate([0.45,0,0])
                circle(d=0.1);