from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()  # Sort potions to apply binary search
        n = len(potions)
        result = []  # Stores the final count of successful potions for each spell

        for spell in spells:
            # Minimum potion strength needed for success
            min_needed = success / spell

            # Binary search: find leftmost index where potion ≥ min_needed
            index = bisect_left(potions, min_needed)

            # All potions from 'index' to end will be successful
            count = n - index
            result.append(count)

        return result
