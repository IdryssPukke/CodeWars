//https://www.codewars.com/kata/5601409514fc93442500010b/train/javascript


function betterThanAverage(classPoints, yourPoints) {
    sum = classPoints.reduce((a, b) => a + b, 0)
    return yourPoints > sum / classPoints.length
  }
  