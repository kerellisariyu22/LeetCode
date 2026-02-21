class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''res=[]
        nums.sort()
        length=len(nums)
        for i in range(length -2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l=i+1
            r=length-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total<0:
                    l=l+1
                elif total>0:
                    r=r-1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                    l=l+1
                    r=r-1
        return res'''
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return ans

        