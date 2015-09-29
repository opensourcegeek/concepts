class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        answers_dict = {}

        for a_idx, a in enumerate(nums):
            diff = target - a

            print diff
            print answers_dict
            if a not in answers_dict:
                answers_dict[diff] = a
                print answers_dict

            else:
                print a
                print "Found b: ", answers_dict
                return nums.index(answers_dict[a]) + 1, nums.index(a, a_idx) + 1


print Solution().twoSum([3,2,4], 6)
print Solution().twoSum([0,4,3,0], 0)
