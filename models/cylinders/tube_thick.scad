// Tube (Thick) for Stacks of Shapes
// by Slashee the Cow
$fn = 256;

color("GreenYellow")
difference(){
    linear_extrude(3)
        circle(d=1);
    linear_extrude(4)
        circle(d=0.45);
}