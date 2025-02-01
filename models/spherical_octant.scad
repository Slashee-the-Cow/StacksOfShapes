// Spherical Octant (1/8th sphere) for Basic Shapes
// by Slashee the Cow
$fn = $preview ? 16 : 256;

translate([-0.5, -0.5, 0])
intersection(){
    sphere(d=2);
    cube(1);
}