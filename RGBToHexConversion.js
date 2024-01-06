function elementToHex(x) {
    if(x < 0) {x = 0}
    if(x > 255) {x = 255}
    let hex = x.toString(16).toUpperCase();
    return hex.length === 1 ? "0" + hex : hex;
};

function rgb(r, g, b) {
    return elementToHex(r) + elementToHex(g) + elementToHex(b);
}

console.log(rgb(0, 0, 0))