// Translations and rotations to roughly level one face with the ground.
// This part by Slashee the Cow

use <platonics.scad>

// Octahedron
//translate([0,0,0.408]) rotate([54.7, 0, 0]) octahedron();

// Dodecahedron
//rotate([-31.7, 0, 0]) dodecahedron();

// Icosahedron
translate([0,0,0.405]) resize([1,0,0], auto=true) rotate([0, 21, 0]) icosahedron();
