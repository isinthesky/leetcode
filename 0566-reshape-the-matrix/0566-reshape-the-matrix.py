class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp=[]
        result=[]

        for i in mat:
            for j in i:
                temp.append(j)

        if r * c!=len(temp):
            return mat
        else:
            for i in range(r):
                result.append(temp[i * c : i * c + c])

        return result
