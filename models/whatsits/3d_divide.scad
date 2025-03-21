// 3D Divide for Stacks of Shapes
// Copyright Slashee the Cow
$fn = $preview ? 256 : 64;

color("PowderBlue"){
translate([0,0,0.5])
sphere(d=1);
translate([0,0,2]){
    cube([3,1,1],center=true);
    cube([1,3,1],center=true);
}
translate([0,0,3.5])
sphere(d=1);
}