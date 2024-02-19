// https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/javascript

function deleteNth(arr, n) {
    dict = {};
    result = []
    for (let element of arr) {
        if (element in dict) { dict[element] += 1 } else { dict[element] = 1 };
        if (dict[element] <= n) {
            result.push(element)
        }
    }
    return result;
}

function deleteNth2(arr, x) {
    var cache = {};
    return arr.filter(function (n) {
        cache[n] = (cache[n] || 0) + 1;
        return cache[n] <= x;
    });
}

deleteNth([20, 37, 20, 21], 1)