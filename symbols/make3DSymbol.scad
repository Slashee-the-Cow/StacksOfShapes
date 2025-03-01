default_height = 5;
default_width = 100;
$fn = 64;

module make3DSymbol(filename){
    linear_extrude(default_height)
    resize([default_width,0,0], auto=[false, true, true])
    import(filename, center = true);
}

/* ARROWS */
//make3DSymbol("arrows/arrow_single.svg");

/* HEARTS */
//make3DSymbol("hearts/heart.svg");