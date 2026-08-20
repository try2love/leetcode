#
# @lc app=leetcode.cn id=380 lang=python3
# @lcpr version=30404
#
# [380] O(1) 时间插入、删除和获取随机元素
# 3:32 没做出来
from  random import choice
# @lc code=start
class RandomizedSet:
    # 变长数组和哈希表结合，变长数组中存储元素，哈希表中存储每个元素在变长数组中的下标
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end



#
# @lcpr case=start
# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n[[],[1],[2],[2],[],[1],[2],[]]\n
# @lcpr case=end

#

