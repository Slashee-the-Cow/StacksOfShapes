// Hemisphere for Basic Shapes
// by Slashee the Cow
$fn = 128;

difference(){
    sphere(d=1);
    translate([0,0,-.25])
        cube([1,1,0.5], true);
}