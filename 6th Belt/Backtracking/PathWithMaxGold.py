class Solution:
    def getMaximumGold(self, grid) :
        rows, cols = len(grid), len(grid[0])  # Get grid dimensions
        max_gold = 0  # Track the maximum gold collected

        def backtrack(r, c, visited):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == 0 or (r, c) in visited):  # ❌ Stop if out of bounds, 0 gold, or already visited
                return 0

            visited.add((r, c))  # ✅ Mark current cell as visited
            gold = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:  # Explore all 4 directions
                gold = max(gold, backtrack(r+dr, c+dc, visited))  # Choose the best path from here
            visited.remove((r, c))  # 🔙 Backtrack: unmark the current cell
            return grid[r][c] + gold  # Total gold = current + max from neighbors

        for r in range(rows):
            for c in range(cols):
                max_gold = max(max_gold, backtrack(r, c, set()))  # Try starting from every cell

        return max_gold