function solve(fstNum, secNum, text) {

    let result;

    switch(text) {
        case '+': result = fstNum+secNum;
            break;
        case '-': result = fstNum-secNum;
            break;
        case '/': result = fstNum/secNum;
            break;
        case '*': 
            result = fstNum*secNum; 
            break;
        case '%': result = fstNum%secNum; 
            break;
        case '**': result = fstNum**secNum;
            break;
    }

    console.log(result)
}


solve(3, 5.5, '*')