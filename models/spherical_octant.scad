// Spherical Octant (1/8th sphere) for Basic Shapes
// by Slashee the Cow
$fn = $preview ? 16 : 192;

translate([-0.5, -0.25, 0])
intersection(){
    translate([0.5,0,0])
        sphere(d=1);
    rotate([-45,0,0])
    cube(1);
    #cube(1);
}