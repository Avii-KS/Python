class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int) :
        n = len(arr)
        low, high = 0.0, 1.0  # All fractions lie between 0 and 1

        while True:
            mid = (low + high) / 2  # Mid fraction to check
            count = 0  # Count of fractions ≤ mid
            max_frac = 0  # Track max fraction ≤ mid
            numerator, denominator = 0, 1  # Track best fraction (i, j)
            
            j = 1  # Start denominator from second element
            for i in range(n - 1):  # Iterate numerators
                # Move j to the right until fraction > mid
                while j < n and arr[i] / arr[j] > mid:
                    j += 1
                if j == n:
                    break  # No more valid fractions with this i
                count += (n - j)  # All arr[i]/arr[j..n-1] are valid

                # Update best fraction seen so far
                if j < n and arr[i] / arr[j] > max_frac:
                    max_frac = arr[i] / arr[j]
                    numerator, denominator = arr[i], arr[j]
            
            if count == k:
                return [numerator, denominator]
            elif count < k:
                low = mid  # Not enough → increase the fraction
            else:
                high = mid  # Too many → decrease the fraction
