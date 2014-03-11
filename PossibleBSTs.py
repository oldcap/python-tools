#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def generateTreesInternal(self, m, n):
        # print(str(m) + ',' + str(n))
        if m > n:
            return [None]
        if m == n:
            return [TreeNode(m)]
        ret = []
        for i in range(m, n+1):
            for l in self.generateTreesInternal(m, i - 1):
                for r in self.generateTreesInternal(i + 1, n):
                    # print('i=' + str(i) + ',l=' + str(l.val) + ',r=' + str(r.val))
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret.append(root)
                    # print("Adding " + str(root.val))
        return ret
        
    # @return a list of tree node 
    def generateTrees(self, n):
        return self.generateTreesInternal(1,n)
            

def main():
    s = Solution()
    for n in s.generateTrees(3):
        print(n.val)

if __name__ == "__main__":
    main()