from collections import Counter

def checkInclusion(s1, s2):
    k = len(s1)  # Length of the string s1; this is the size of the window we'll slide over s2

    s1_count = Counter(s1)  # Create a frequency count (dictionary) of characters in s1
                            # e.g., if s1 = "abc", then s1_count = {'a':1, 'b':1, 'c':1}

    for i in range(len(s2) - k + 1):  # Loop through s2 using a window of size k
                                      # Stop at len(s2) - k + 1 so the last window is complete
                                      # For example, if s2 = "eidbaooo", and k = 3,
                                      # you check substrings: "eid", "idb", "dba", ..., "ooo"

        if Counter(s2[i:i+k]) == s1_count:  # Take a window of size k from s2 starting at index i
                                            # Use Counter to get the frequency of characters in this window
                                            # Compare it with s1_count
                                            # If both have exactly the same characters with same frequencies,
                                            # it means this window is a permutation of s1

            return True  # If a matching window is found, return True immediately

    return False  # If no matching window (permutation) is found after checking all, return False

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # If s1 is longer than s2, it's impossible

        k = len(s1)  # Length of the window we’ll slide over s2
        s1_count = Counter(s1)  # Count characters in s1 (target frequency)
        window_count = Counter(s2[:k])  # Count characters in the first window of s2

        if s1_count == window_count:
            return True  # First window is already a permutation

        # Slide the window across s2
        for i in range(k, len(s2)):
            start_char = s2[i - k]  # Character leaving the window (on the left)
            new_char = s2[i]        # Character entering the window (on the right)

            window_count[new_char] += 1        # Add new character to the count
            window_count[start_char] -= 1      # Remove old character from the count

            if window_count[start_char] == 0:  # Clean up to keep the dict small
                del window_count[start_char]

            if window_count == s1_count:  # If counts match, we found a permutation
                return True

        return False  # No permutation found

