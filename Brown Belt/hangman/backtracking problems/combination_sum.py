def combinationSum(arr, target):
    res=[]

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if i>=len(arr) or total > target:
            return
        cur.append(arr[i])
        dfs(i, cur, total+arr[i])
        cur.pop()
        dfs(i+1, cur, total)

    dfs(0, [], 0)

    return res


arr = [1, 4, 6, 8]
target = 8

res = combinationSum(arr, target)

for i in res:
    print(*i)