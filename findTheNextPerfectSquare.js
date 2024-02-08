function findNextSquare(sq) {
    if (Math.floor(Math.sqrt(sq)) ** 2 != sq) {
        return -1;
    } else {
        while (true) {
            sq = sq + 1
            if (Math.floor(Math.sqrt(sq)) ** 2 == sq) {
                return sq
            }
        }
    }
}