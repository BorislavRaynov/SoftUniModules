function solve(nums){
    let result = []
    if (nums.length % 2 === 0){
        while (nums.length !== 0){
            let currentMax = Math.max(...nums)
            let currentMin = Math.min(...nums)
            result.push(currentMin)
            result.push(currentMax)
            nums.splice(nums.indexOf(currentMin), 1)
            nums.splice(nums.indexOf(currentMax), 1)
        }
    }
    else{
        while (nums.length > 1){
            let currentMax = Math.max(...nums)
            let currentMin = Math.min(...nums)
            result.push(currentMin)
            result.push(currentMax)
            nums.splice(nums.indexOf(currentMin), 1)
            nums.splice(nums.indexOf(currentMax), 1)
        }
        let lastNum = nums.pop()
        result.push(lastNum)
    }
    return result
}

console.log(solve([1]))