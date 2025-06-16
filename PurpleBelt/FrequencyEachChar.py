def char_frequency(S):
    frequency = {}
    for char in S:
        frequency[char] = frequency.get(char, 0) + 1

    max_freq = max(frequency.values())
    min_freq = min(frequency.values())

    chars_with_max_freq = [char for char, freq in frequency.items() if freq == max_freq]
    highest_freq_chars = sorted(chars_with_max_freq)

    chars_with_min_freq = [char for char, freq in frequency.items() if freq == min_freq]
    lowest_freq_chars = sorted(chars_with_min_freq)

    return highest_freq_chars, max_freq, lowest_freq_chars, min_freq

S = input()
highest_freq_chars, max_freq, lowest_freq_chars, min_freq = char_frequency(S)

print("Highest frequency character(s):", " ".join(highest_freq_chars), max_freq)
print("Lowest frequency character(s):", " ".join(lowest_freq_chars), min_freq)
