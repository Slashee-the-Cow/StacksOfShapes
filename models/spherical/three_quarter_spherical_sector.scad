// Three Quarter Spherical Sector for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 256 : 128;
translate([0,0,0.5])
rotate([180,0,0])

color("blue")
difference(){
    sphere(d=1);
    translate([0,0.5,-.25])
        cube([1,1,0.5], true);
}