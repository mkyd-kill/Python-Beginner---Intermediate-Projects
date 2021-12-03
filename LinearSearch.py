def Linear(A, n, x):
    """
        A: array
        n: number of elements in A
        x: elements used in the search
    """
    for i in range(0, n):
        if A[i] == x:
            return i # return the index of the array element
    return -1 # return no index

A = [3, 2, 1, 9, 0]
x = 9
n = len(A)

result = Linear(A, n, x)
if result == -1:
    print(f"Element {x} not present in the Array")
else:
    print(f"Element present at index {result}")