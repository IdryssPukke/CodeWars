String.prototype.toAlternatingCase = function () {
    return this.split('').map((c) =>
        c.toUpperCase() === c ? c.toLowerCase() : c.toUpperCase()).join('')
}


console.log("Hello World".toAlternatingCase())