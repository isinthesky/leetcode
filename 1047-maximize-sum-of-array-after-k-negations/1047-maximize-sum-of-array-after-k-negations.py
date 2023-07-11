class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 마이너스 갯수 
        # k 값 
        # 음수 없애기
        # 짝수 2번 적용 무효화 
        # 홀수 1번 적용 최소 값 찾기
        minus = 0
        nums.sort()

        for n, v in enumerate(nums):
            if v < 0:
                minus += 1

        pos = 0
        while k > 0:
            if minus < 1:
                if k % 2 == 1 :
                    nums.sort()
                    nums[0] = -(nums[0])
                else:
                    break
            else :
                if minus < 1 and (k % 2 == 0):
                    break
                else:
                    nums[pos] = -(nums[pos])
                    pos += 1
                    minus -= 1
            
            k -= 1
        
        return sum(nums)