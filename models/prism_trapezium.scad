// Trapezium Prism (Isosceles) for Basic Shapes
// by Slashee the Cow

points = [
    [0,0],
    [0.3,1],
    [0.7,1],
    [1,0]
    ];

translate([-0.5,-0.5,0])
rotate([90,0,90])
linear_extrude(1)
polygon(points, [[0,1,2,3]]);