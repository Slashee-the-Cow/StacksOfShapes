// Dominoes for Stacks of Shapes
// Copyright Slashee the Cow
//$fn = $preview ? 256 : 62;
$fa = $preview ? .5 : 1;
$fs = $preview ? 0.05 : 0.1;
domino_length = 48;
domino_depth = 24;
domino_height = 7.5;
domino_size = [domino_length, domino_depth, domino_height];

edge_radius = 0.5;

middle_divider_width = 2;
middle_divider_height = 0.5;

usable_width = (domino_length - middle_divider_width)/2;
usable_depth_offset = (domino_depth - usable_width) / 2;
usable_depth = domino_depth - (usable_depth_offset * 2);

pip_sphere_diameter = 4;
pip_sphere_height = 8.5;
pip_xy_scale = 1.6;

pip_edge_inset = 5;



difference(){
    rounded_domino(edge_radius);
    // middle divider
    translate([domino_length/2-middle_divider_width/2,0,domino_height-middle_divider_height])
        cube([middle_divider_width, domino_depth, middle_divider_height]);
    // *** LEFT SIDE *** //
    //one_pip();
    //two_pip();
    //three_pip();
    //four_pip();
    //five_pip();
    //six_pip();
    // *** RIGHT SIDE *** //
    translate([domino_length,0,0]){
        mirror([1,0,0]){
            //one_pip();
            //two_pip();
            //three_pip();
            //four_pip();
            //five_pip();
            six_pip();
        }
    }
}

module rounded_domino(corner_radius, bottom_round = true){
    hull(){
        //top
        translate([0,0,domino_height - corner_radius * 2])
            rounded_domino_level(corner_radius);
        //bottom
        if (bottom_round == true) rounded_domino_level(corner_radius);
        else cube([domino_length,domino_depth,corner_radius], center = false);
    }
}

module rounded_domino_level(corner_radius){
    translate([corner_radius, corner_radius, corner_radius]){
        sphere(r = corner_radius);
        translate([domino_length-corner_radius*2,0,0])
            sphere(r = corner_radius);
        translate([0,domino_depth - corner_radius*2,0])
            sphere(r = corner_radius);
        translate([domino_length-corner_radius*2,domino_depth - corner_radius*2,0])
            sphere(r = corner_radius);
    }
}

module pip(diameter = pip_sphere_diameter, xy_scale = pip_xy_scale){
    scale([xy_scale,xy_scale,1])
        sphere(d = diameter, $fn = $preview ? 256 : 32);
}

module one_pip(){
    translate([0,usable_depth_offset,pip_sphere_height]){
        translate([usable_width/2,usable_depth/2,0])
            pip();
    }
}
module two_pip(){
    translate([0,usable_depth_offset,pip_sphere_height]){
        translate([pip_edge_inset,usable_depth-pip_edge_inset,0])
            pip();
        translate([usable_width - pip_edge_inset,pip_edge_inset,0])
            pip();
    }
}

module three_pip(){
    one_pip();
    two_pip();
}

module four_pip(){
    two_pip();
    mirror([1,0,0])
        translate([-usable_width,0,0])
            two_pip();
}

module five_pip(){
    one_pip();
    four_pip();
}

module six_pip(){
    four_pip();
    translate([0,usable_depth_offset,pip_sphere_height]){
        translate([usable_width/2, pip_edge_inset,0])
            pip();
        translate([usable_width/2, usable_depth - pip_edge_inset,0])
            pip();
    }
}