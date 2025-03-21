// Translations and rotations to roughly level one face with the ground.
// This part by Slashee the Cow

use <platonic.scad>

// Tetrahedron
//color("SteelBlue") translate([0,0,0.334]) rotate([180,0,0]) rotate([45,35.25,90]) makeTetrahedron();

// Octahedron
//color("DarkMagenta")translate([0,0,0.576]) rotate([45, 35.3, 0]) makeOctahedron();

// Dodecahedron
//color("IndianRed") translate([0,0,.795]) rotate([0, -31.8, 0]) makeDodecahedron();

// Icosahedron
color("SpringGreen") translate([0,0,0.405]) resize([1,0,0], auto=true) rotate([0, 21, 0]) makeIcosahedron();