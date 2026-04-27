class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        l,r = 0 , len (height)-1
        LeftMax, RightMax = height[l], height[r]
        res =0

        while l < r:
            if LeftMax < RightMax:
                l +=1 
                LeftMax = max(LeftMax,height[l])
                res += LeftMax - height[l]
            else:
                r-=1
                RightMax = max(RightMax , height[r])
                res += RightMax- height[r]
        return res



        