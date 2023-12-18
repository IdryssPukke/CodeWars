function alphabetPosition(text) {
    results = ''
    for(const l in text){
        if(text[l].toLowerCase() != text[l].toUpperCase()){
            if(text[l] == text[l].toUpperCase()){
                results += text.charCodeAt(l)-64 + ' ';
            } else {
                results += text.charCodeAt(l)-96 + ' ';
            }     
        }
    }
    return results.slice(0, -1);
  }

console.log(alphabetPosition("Kaslo"));