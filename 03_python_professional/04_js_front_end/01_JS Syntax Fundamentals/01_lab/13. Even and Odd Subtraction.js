function solve(nums) {
    for(let i=0; i<nums.length; i++){
        nums[i]=Number(nums[i]);
    }
    let evenSum = 0;
    let oddSum = 0;

    for(let num of nums) {
        if (num % 2 === 0){
            evenSum += num
        }

        else {
            oddSum += num
        }
    }

    console.log(evenSum - oddSum)
}

solve([3,5,7,9])