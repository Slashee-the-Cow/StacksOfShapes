// Negative Hemisphere for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 1024: 128;

color("Maroon")
translate([0,0,0.575])
difference(){
    translate([0,0,-0.275])
        cube([1.1,1.1,0.55], true);
    sphere(d=1);
}