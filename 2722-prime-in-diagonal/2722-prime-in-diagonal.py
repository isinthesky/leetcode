class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        length = len(nums)

        arr = []
        i = 0
        rev = length

        while i < length:
            if nums[i][i] % 2 == 1 or nums[i][i] <= 3:
                arr.append(nums[i][i])

            rev -= 1

            if nums[i][rev] % 2 == 1 or nums[i][rev] <= 3:
                arr.append(nums[i][rev])

            i += 1

        myset = set(arr)
        mylist = list(myset)
        mylist.sort(reverse=True)

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        for num in mylist:
            if is_prime(num) == True:
                return num

        return 0
