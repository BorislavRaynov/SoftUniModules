function solve(fstNum, secNum){
    let sum = 0
    let nums = []
    for (let i = fstNum; i <= secNum; i++){
        sum += i
        nums.push(i)
    }
    console.log(nums.join(' '))
    console.log(`Sum: ${sum}`)
}

solve(0, 26)