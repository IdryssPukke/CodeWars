/// https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/javascript


var number=function(array){
    if(!array) return []
    for(element in array){
        array[element] = 1 + Number(element) + ": " + array[element]
    }
    return array
  }