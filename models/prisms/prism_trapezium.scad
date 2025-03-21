// Trapezium Prism (Isosceles) for Stacks of Shapes
// by Slashee the Cow

points = [
    [0,0],
    [0.3,1],
    [0.7,1],
    [1,0]
    ];

color("Goldenrod")
translate([-1.5,-0.5,0])
rotate([90,0,90])
linear_extrude(3)
polygon(points, [[0,1,2,3]]);