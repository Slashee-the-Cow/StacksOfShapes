// Negative Spherical Octant (Corner) (1/8th sphere) for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 1024 : 256;

color("LightSkyBlue")
translate([-0.5, -0.5, 1.05])
rotate([180,0,90])
difference(){
    cube(1.05);
    sphere(d=2);
}