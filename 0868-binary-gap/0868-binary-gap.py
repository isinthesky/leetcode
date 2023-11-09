class Solution:
    def binaryGap(self, n: int) -> int:
        binString = "{0:b}".format(n)

        max = 0
        acc = 0
        count = 0

        for char in binString:
            if char == "1":
                count += 1
                if count > 0:
                    if max < acc:
                        max = acc
                acc = 1
            else:
                acc += 1

        return 0 if count <= 1 else max
