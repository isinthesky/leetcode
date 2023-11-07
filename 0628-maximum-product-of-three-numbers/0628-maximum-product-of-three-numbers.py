class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sortedList1 = sorted(nums, reverse=True)
        bigs = sortedList1[:3]

        # sortedList2 = sorted(nums)
        smalls = sortedList1[-2:]

        print(smalls, bigs)

        return max(bigs[0] * bigs[1] * bigs[2] , bigs[0] * smalls[0] * smalls[1] )

        # minus = 0

        # sort = []
        # minusArr = []

        # for num in nums:
        #     if num < 0:
        #         minus += 1

        #     if num != 0:
        #         sort.append(num)

        # if minus % 2 == 1:
        #     result = 1
        #     for num in range(3):
        #         result *= sortedList[num]
        # else:
        #     for value in sort()

        # minus = 0
        # bigNumberDict = {}

        # for num in nums:
        #     if num != 0:
        #         bigNumberDict[abs(num)] = True if num > 0 else False

        # bigNumbers = sorted(bigNumberDict.items(), reverse=True)

        # print("dict", bigNumberDict)
        # print("arr", bigNumbers)

        # minus = 0
        # multi = []
        # for big in bigNumbers:
        #     multi.append(big)
            

        return 0