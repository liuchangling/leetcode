class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ans = arr[0]
        count = 0 
        for i in range(1, len(arr)):
            nextPlayer = arr[i]
            if ans > nextPlayer:
                count += 1
            else:
                ans = nextPlayer
                count = 1
            
            if count == k:
                return ans

        return ans

