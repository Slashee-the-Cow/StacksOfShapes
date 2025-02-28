// Rhombic Prism for Stacks of Shapes
// by Slashee the Cow

line_length = 0.5;
rhombus_angle = 60;
rhombus_height = line_length * sin(rhombus_angle);

module rhombus(side_length, angle) {
    height = side_length * sin(angle);
    half_width = side_length * cos(angle);
    points = [[0, 0], [half_width, height], [0, 2 * height], [-half_width, height]];
    polygon(points);
}
color("LimeGreen")
translate([-1.5,0,0])
rotate([0,90,0])
linear_extrude(3)
resize([1,0,0], auto = true)
rotate([0,0,90])
rhombus(line_length, rhombus_angle);