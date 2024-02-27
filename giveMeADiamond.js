/// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/javascript

function diamond(n){
    if(n <= 0 || n % 2 == 0) { return null};
    result=[]
    for(let i = 0; i < (n-1)/2; i ++){
        result.push(" ".repeat((n-1)/2-i) + "*".repeat(2 * i + 1))
    }
    result.push("*".repeat(n))
    for(let i = (n-1)/2; i > 0; i --){
        result.push(" ".repeat((n-1)/2-i+1) + "*".repeat(2 * i - 1))
    }
    return result.join("\n") + "\n";
  }

function diamond1(n) {
    if (n <= 0 || n % 2 === 0) return null
    str = ''
    for (let i = 0; i < n; i++) { 
      let len = Math.abs((n-2*i-1)/2)
      str += ' '.repeat(len)
      str += '*'.repeat(n-2*len)
      str += '\n'
    }
    return str
  }


console.log(diamond(5))