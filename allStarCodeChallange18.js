// https://www.codewars.com/kata/5865918c6b569962950002a1/solutions/javascript


function strCount(str, letter){  
    return str.split("").filter(x => x===letter).length
  }