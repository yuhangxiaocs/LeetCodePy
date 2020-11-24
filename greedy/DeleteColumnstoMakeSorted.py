'''
    994, Delete Columns to Make Sorted
    就是统计没有排好序的列，这也能叫贪心问题吗，不太经典
'''

def minDeletionSize(self, A):
    """
    :type A: List[str]
    :rtype: int
    """
    res = 0
    for i in range(len(A[0])):
        isSorted = True
        for j in range(len(A) - 1):
            if A[j][i] > A[j+1][i]:
                isSorted = False
        if not isSorted:
            res += 1
            
    return res
