// Spherical Quadrant (1/4 sphere) for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 16 : 192;

translate([-0.5, -0.25, 0])
intersection(){
    translate([0.5,0,0])
        sphere(d=1);
    cube(1);
}