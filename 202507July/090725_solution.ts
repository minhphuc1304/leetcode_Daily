function maxFreeTime(eventTime: number, k: number, startTime: number[], endTime: number[]): number {
    let freeList = []
    let currTime = 0
    for(let i = 0; i < startTime.length; i+=1) {
        if (i === 0 && startTime[i] === 0) {
            currTime = endTime[i]
            continue
        }
        freeList.push(startTime[i] - currTime)
        currTime = endTime[i]
    }
    freeList.push(eventTime - currTime)

    if(freeList[0] === 0) {
        freeList = freeList.slice(1)
    }

    const n = freeList.length
    k = Math.min(k, n - 1)

    let res = 0
    for(let i = 0; i < k + 1; i+=1) {
        res += freeList[i]
    }

    let currSum = res
    for (let right = k + 1; right < n; right += 1) {
        currSum -= freeList[right - k - 1]
        currSum += freeList[right]
        res = Math.max(res, currSum)
    }

    return res
};
