// Tube (Thick) for Basic Shapes
// by Slashee the Cow
$fn = 256;

difference(){
    linear_extrude(1)
        circle(d=1);
    linear_extrude(1)
        circle(d=0.45);
}