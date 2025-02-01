// Capsule for Basic Shapes
// by Slashee the Cow
$fn = 128;

hull(){
    translate([-0.25,0,0.25])
        sphere(d=0.5);
    translate([0.25,0,0.25])
        sphere(d=0.5);
}