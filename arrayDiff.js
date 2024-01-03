function arrayDiff(a, b) {
    for (let element of b) {
        let index = 0;
        while (index < a.length) a[index] === element ? a.splice(index, 1) : ++index
    }
    return a
}

function array_diff(a, b) {
    return a.filter(e => !b.includes(e));
  }

console.log(array_diff([1, 2, 2, 2, 3], [2]))