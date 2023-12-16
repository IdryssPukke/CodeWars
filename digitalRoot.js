function digitalRoot(n) {
    if(n < 10){
        return(n)
    }
    else{
        arr = n.toString().split("")
        arr = arr.reduce((a,b) => parseInt(a) + parseInt(b))
        return digitalRoot(arr)
    }  
  }

function digitalRoot2(n) {
    if(n < 10){
        return(n)
    }
    else{
        return digitalRoot2(n.toString().split("").reduce((a,b) => parseInt(a) + parseInt(b)))
    }  
  }

function digitalRoot3(n) {
    return (n - 1) % 9 + 1;
  }

console.log(digitalRoot3(888))