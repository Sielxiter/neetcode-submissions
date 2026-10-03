class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k=len(numbers)-1
        r=0
        while r<k :
            if numbers[r]+numbers[k] > target :
                k-=1
            elif numbers[r]+numbers[k] < target :
                r+=1
            elif numbers[r]+numbers[k] == target :
                return [r+1,k+1]
            else :
                return


