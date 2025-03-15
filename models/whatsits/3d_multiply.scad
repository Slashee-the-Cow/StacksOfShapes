// 3D Multiplication for Stacks of Shapes
// Copyright Slashee the Cow
x_thickness = 0.75;

color("Gold")
translate([0,0,1.5])
intersection(){
    cube(3, center=true);
    //translate([-0.5,0.5,2.5])
    union(){
    rotate([0,45,0])
        cube([5,x_thickness,x_thickness], center=true);
    rotate([0,-45,0])
        cube([5,x_thickness,x_thickness], center=true);
     rotate([0,45,90])
        cube([5,x_thickness,x_thickness], center=true);
    rotate([0,-45,90])
        cube([5,x_thickness,x_thickness], center=true);
     }
     
}