class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls=set(nums)
        best=0
        for num in nums :
            if num+1 not in ls :
                lenght=1
                while (num-lenght) in ls :
                    lenght+=1
                best=max(best,lenght)
        return best
                
                    


        