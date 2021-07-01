class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return([])
        else:
            result = []
            nums.sort()
            print(nums)
            for i in range(len(nums)-2):
                if (i==0 or (i>0 and (nums[i] != nums[i-1]))):
                    j = i+1
                    k = len(nums)-1
                    while(j<k):
                        triplet = nums[i]+nums[j]+nums[k]
                        if(triplet == 0):
                            result.append([nums[i], nums[j], nums[k]])
                            while(j<k and nums[j] == nums[j+1]):
                                j+=1
                            while(j<k and nums[k] == nums[k-1]):
                                k-=1
                            j+=1
                            k-=1
                        elif(nums[i]+nums[j]+nums[k] < 0):
                            j+=1
                        else:
                            k-=1
            return(result)
