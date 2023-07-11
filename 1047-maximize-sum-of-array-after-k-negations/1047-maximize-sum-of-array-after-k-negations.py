class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 마이너스 갯수 
        # k 값 
        # 음수 없애기
        # 짝수 2번 적용 무효화 
        # 홀수 1번 적용 최소 값 찾기
        minus = []
        nums.sort()

        for n, v in enumerate(nums):
            if v < 0:
                minus.append([n,v])

        print(minus, nums)

        pos = 0
        minus_count = len(minus)
        while k > 0:
            if minus_count < 1:
                if k % 2 == 1 :
                    nums.sort()
                    nums[0] = -(nums[0])
                    k -= 1
                else:
                    break
            else :
                if minus_count < 1 and (k % 2 == 0):
                    break
                else:
                    nums[pos] = -(nums[pos])
                    k -= 1
                    pos += 1
                    minus_count -= 1
                    print(nums, k, pos, minus_count)
        
        print(nums)
            
        return sum(nums)