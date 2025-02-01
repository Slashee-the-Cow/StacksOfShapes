// Helix for Basic Shapes
// by Slashee the Cow

$fn = $preview ? 8 : 16 ;

translate([-.35,0,0.05])
//resize([1,0,0], auto=[false,true,false])
union(){
minkowski(){
    linear_extrude(1, twist = 1080, convexity = 10)
        translate([0.35,0,0])
            circle(d=0.2);
    translate([0.35,0,0])
        sphere(d=0.10);
}
}