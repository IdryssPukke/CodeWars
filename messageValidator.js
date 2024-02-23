// https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/train/javascript


function isAValidMessage(message){
    numbers = message.match(/\d+/g)
    if(message == [] ){return true}
    if(numbers.reduce((a, b) => parseInt(a) + parseInt(b), 0) > message.length) {return false}
    index = 0
    message = [...message]
  
    for(let element of numbers){
        index += element.length
        message.splice(index, element)
    }
  
    if (message.join('').match(/[a-zA-Z]+/)) {
        return false
    } else {
        return true
    }
  }

  
function isAValidMessage1(message){
    return !message.replace(/(\d+)(\D*)/g,(_,m,n)=>m-n.length||'')
  }