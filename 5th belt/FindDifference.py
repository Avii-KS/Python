def find_indices_with_difference(A, B):
    i, j = 0, 1

    while j < len(A):
        diff = A[j] - A[i]

        if diff == B and i != j:
            return 1

        if diff < B:
            j += 1
        else:
            i += 1

        if i == j:
            j += 1

    return 0

N = int(input())
A = list(map(int, input().split()))
B = int(input())

print(find_indices_with_difference(A, B))