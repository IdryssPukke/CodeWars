///https://www.codewars.com/kata/57a083a57cb1f31db7000028/javascript


function powersOfTwo(n){
    result = []
    for( let id  = 0; id <= n; id ++){
        result.push(2**id)
    }
    return result
  }