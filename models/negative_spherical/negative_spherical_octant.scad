// Negative Spherical Octant (1/8th sphere) for Stacks of Shapes
// by Slashee the Cow
// This took me far longer to figure out than I care to admit.
$fn = $preview ? 1024 : 192;

color("MediumSlateBlue")
rotate([22.5,0,0])
difference(){
    //cube([1.1,0.55,0.55]);
    translate([-0.025,0,0.0])
    rotate([0,90,0])
    rotate([0,0,90])
    linear_extrude(1.05)
    polygon([[0,0],[0.5,0.20625],[0.5,-0.20625]]);
    intersection(){
        translate([0.5,0,0])
            sphere(d=1);
        rotate([-45,0,0])
        cube(1);
    }
}