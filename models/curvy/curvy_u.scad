$fn = $preview ? 256 : 64;
width = 2;

color("PaleGoldenrod"){
rotate_extrude(angle = 180)
//rotate([90,0,0])
translate([-width/2,0,0])
    circle(d=1);
translate([-width/2,0,0])
    sphere(d=1);
translate([width/2,0,0])
    sphere(d=1);
    }