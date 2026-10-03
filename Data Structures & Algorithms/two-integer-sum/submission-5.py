class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedarr=sorted(nums)
        start=0
        end=len(sortedarr)-1
        
        while (start<end) :
            if (sortedarr[start]+sortedarr[end]>target):
                end=end-1
            elif(sortedarr[start]+sortedarr[end]<target) :
                start=start+1
            else : 
                a=nums.index(sortedarr[start])
                b=nums.index(sortedarr[end])
                if a==b:
                    b=nums.index(sortedarr[end],a+1)
                
                return [min(a,b),max(a,b)]

        