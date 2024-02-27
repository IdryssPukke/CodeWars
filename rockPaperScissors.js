/// https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/javascript

const rps = (p1, p2) => {
    if(p1 === p2){return "Draw!"}
    if(["scissorspaper", "paperrock", "rockscissors"].includes(p1+p2)){
        return "Player 1 won!"
    } else {
        return "Player 2 won!"
    }
};