import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:

        # Helper: Given a speed `k`, how many hours does Koko need?
        def hours_needed(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile / speed)  # Eat `speed` bananas/hour
            return total

        # Binary search between 1 and max pile size
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2  # Try this speed
            if hours_needed(mid) <= h:
                high = mid  # Try a smaller speed (still valid)
            else:
                low = mid + 1  # Too slow, need to go faster

        return low  # Smallest speed that works
