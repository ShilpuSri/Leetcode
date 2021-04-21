class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_index=[]
        flag=0
        for i in range(len(nums)):
            j=i+1
            while (j < len(nums)):
                add=nums[i]+nums[j]
                if add == target:
                    target_index.append(i)
                    target_index.append(j)
                    flag=1
                    break
                j+=1
            if flag == 1:
                break
        return target_index