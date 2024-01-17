function squareDigits(num){
    let result = '';
    for(let element of num.toString()){
        result += String(parseInt(element**2))
    }
    return parseInt(result);
  }

function squareDigits1(num){
    return Number(('' + num).split('').map(function (val) { return val * val;}).join(''));
    
  }
  
console.log(squareDigits(3212))