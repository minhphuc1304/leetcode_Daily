func subarrayBitwiseORs(arr []int) int {
    res := make(map[int]bool)
    cur := make(map[int]bool)

    for _, num := range arr {
        next := make(map[int]bool)
        next[num] = true
        for x := range cur {
            next[x|num] = true
        }
        cur = next
        for x := range cur {
            res[x] = true
        }
    }
    return len(res)
}
