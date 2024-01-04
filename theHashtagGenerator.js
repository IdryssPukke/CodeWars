function generateHashtag (str) {
    if (str.trim().length === 0) {return false}
    words = "#" + str.trim().split(' ').map((x) => x.charAt(0).toUpperCase() + x.slice(1)).join('')
    if (words.length > 140) { return false } else return words
}

function generateHashtag (str) {

    var hashtag = str.split(' ').reduce(function(tag, word) {
      return tag + word.charAt(0).toUpperCase() + word.substring(1);
    }, '#');
    
    return hashtag.length == 1 || hashtag.length > 140 ? false : hashtag;
  }


console.log(generateHashtag("Codewars is nice"))