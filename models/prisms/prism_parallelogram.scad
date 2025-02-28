// Parallelogram Prism for Stacks of Shapes
// by Slashee the Cow

points = [
    [0,0],
    [0.8,0],
    [1,0.5],
    [0.2,0.5]
    ];

color("orchid")
translate([-0.5,-0.5,0])
rotate([90,0,90])
linear_extrude(3)
polygon(points, [[3,2,1,0]]);