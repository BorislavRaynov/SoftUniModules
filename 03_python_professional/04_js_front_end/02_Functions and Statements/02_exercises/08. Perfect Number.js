function perfectNumber(num){
    let dividersSum = 0
    for (let i = 1; i < num; i++){
        if (num % i === 0){
            dividersSum += i
        }
    }
    if (num === dividersSum){
        console.log('We have a perfect number!')
    } else {
        console.log("It's not so perfect.")
    }
}

perfectNumber(1236498)