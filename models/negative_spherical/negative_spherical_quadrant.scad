// Negative Spherical Quadrant (1/4 sphere) for Stacks of Shapes
// by Slashee the Cow
$fn = $preview ? 512 : 192;

color("Gold")
rotate([180,0,0])
translate([-0.5, -0.25, -0.5])
difference(){
translate([-0.05,-0.025,0])
    cube([1.1,0.55,0.55]);
    translate([0.5,0,0])
        sphere(d=1);
    
}