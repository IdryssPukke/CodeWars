// https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/javascript

function expandedForm(num) {
    result = []
    str = num.toString()
    for(let element in str){
        number = str[element] * 10**(str.length-1-element)
        if(number > 0 ){
            result.push(number.toString())
        }
    }
    return result.join(" + ");
  }


const expandedForm2 = n => n.toString()
  .split("")
  .reverse()
  .map( (a, i) => a * Math.pow(10, i))
  .filter(a => a > 0)
  .reverse()
  .join(" + ");


console.log(expandedForm2(42))