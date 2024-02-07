function solution(str){
    word = ''
    for(let letter of str){
        word = letter + word
    }
    return word
};

function solution2(str){
    return str.split('').reverse().join('');  
  }

console.log(solution('world'))