// Capsule for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 512 : 128;

color("Red")
hull(){
    translate([-0.25,0,0.25])
        sphere(d=0.5);
    translate([0.25,0,0.25])
        sphere(d=0.5);
}