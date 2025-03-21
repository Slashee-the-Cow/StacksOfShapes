// Negative Three Quarter Spherical Sector for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 256 : 128;
translate([0,0,0.5])
rotate([180,0,0])

color("MediumAquamarine")
translate([0,0,-0.05])
difference(){
    union(){
    translate([0,0,.275])
        cube([1.1,1.1,0.55], true);
    translate([0,0.275,-.275])
        cube([1.1,0.55,0.55], true);
        }
    sphere(d=1);
}