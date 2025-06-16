def partition(string):
    res = []
    part = []

    def dfs(i):
        if i >= len(string):
            res.append()