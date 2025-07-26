// https://leetcode.com/problems/even-odd-tree/

class Solution {
    func isEvenOddTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        guard root.val % 2 != 0 else { return false }
        var stack: [TreeNode] = [root]
        var levelIndex = 0
        
        while !stack.isEmpty {
            var level: [TreeNode] = []
            
            for i in 0 ..< stack.count {
                let node = stack[i]
                if let left = node.left {
                    level.append(left)
                }
                if let right = node.right {
                    level.append(right)
                }
            }
            
            levelIndex += 1
            
            if levelIndex % 2 == 0 {
                if level.count > 1 {
                    for i in 1 ..< level.count {
                        let prev = level[i - 1]
                        let curr = level[i]
                        
                        guard prev.val % 2 != 0 else { return false }
                        guard curr.val % 2 != 0 else { return false }
                        guard curr.val > prev.val else { return false }
                    }
                } else if level.count == 1, level[0].val % 2 == 0 {
                    return false
                }
            } else {
                if level.count > 1 {
                    for i in 1 ..< level.count {
                        let prev = level[i - 1]
                        let curr = level[i]
                        
                        guard prev.val % 2 == 0 else { return false }
                        guard curr.val % 2 == 0 else { return false }
                        guard curr.val < prev.val else { return false }
                    }
                } else if level.count == 1, level[0].val % 2 != 0 {
                    return false
                }
            }
            
            stack = level
        }
        
        return true
    }
}
