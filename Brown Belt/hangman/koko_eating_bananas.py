import math
def min_eating_speed(piles: list[int], h: int ) -> int:
    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / mid)
        if hours_needed <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

piles = [30, 11, 23, 4, 20]
h = 5
print(min_eating_speed(piles, h))
