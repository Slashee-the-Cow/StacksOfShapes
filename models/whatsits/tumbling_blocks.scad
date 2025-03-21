
grid_size = 100;

zgs = grid_size - 1; // Short for "Zero Grid Size" because we're working with 0 based loops

//color("DarkOrchid") // 3x3
//color("Coral") // 5x5
//color("CornflowerBlue") // 7x7
//color("BurlyWood") // 9x9
//color("Teal") // 15x15
//color("DarkKhaki") // 50x50
color("Red") // 100x100
translate([-grid_size/2,-grid_size/2,0])
union(){
for(row = [0:zgs]){
    for(column = [0:zgs]){
        translate([row,column,0])
            cube([column == zgs ? 1 : 1.1,row == zgs ? 1.1: 1,column + row + 1], center = false);
    }
}
}