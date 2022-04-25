class Solution:
    def mySqrtJuanCarlos(self, x: int) -> int:
        counter = 0
        power = 0
        
        while (power <= x):
            counter += 1
            power = counter*counter
        
        
        return counter - 1

input = 11
sol = Solution()
print(sol.mySqrtJuanCarlos(input))