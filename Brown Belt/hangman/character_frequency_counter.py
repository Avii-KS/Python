from collections import Counter
def find_highest_lowest_frequency(s):
    # Count the frequency of each character
    frequency = Counter(s)
    # Get the maximum and minimum frequency
    max_freq = max(frequency.values())
    min_freq = min(frequency.values())
    # Find characters with the highest and lowest frequency, sorted lexicographically
    highest_freq_chars = sorted([char for char in frequency if frequency[char] == max_freq])
    lowest_freq_chars = sorted([char for char in frequency if frequency[char] == min_freq])
    # Print the results
    print(f"Highest frequency character(s): {' '.join(highest_freq_chars)} {max_freq}")
    print(f"Lowest frequency character(s): {' '.join(lowest_freq_chars)} {min_freq}")
