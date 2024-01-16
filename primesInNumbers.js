function primeFactors(n){
    let k = 2;
    let dict = {};
    let result = '';
    while(n > 1){
        if (n % k === 0){
            dict[k] = (dict[k] || 0) + 1;
            n = n / k;
        } else{
            k += 1;
        }
    }
    for(let [key, value] of Object.entries(dict)){
        if(value > 1) result += '(' + key + '**' + value + ')'
        else result += '('+key+')'
    }
    return result
}

function primeFactors2(n){
    for (var i=2, res="", f; i <= n; i++) {
      f=0;
      while (n%i == 0) { f++; n/=i }
      res += f ? "(" + ( f>1 ? i+"**"+f  : i ) +")" : ""
    }
    return res || "("+n+")"
  }

console.log(primeFactors(86240))
