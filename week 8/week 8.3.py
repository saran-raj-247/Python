def uncommon_words(s1, s2):
    # Tokenize the sentences
    words1 = s1.split()
    words2 = s2.split()

    # Create dictionaries to store word frequencies
    freq1 = {}
    freq2 = {}

    # Count word frequencies in s1
    for word in words1:
        freq1[word] = freq1.get(word, 0) + 1

    # Count word frequencies in s2
    for word in words2:
        freq2[word] = freq2.get(word, 0) + 1

    # Find uncommon words
    uncommon = []
    for word, count in freq1.items():
        if count == 1 and word not in freq2:
            uncommon.append(word)

    for word, count in freq2.items():
        if count == 1 and word not in freq1:
            uncommon.append(word)

    # Join uncommon words into a space-separated string
    result = " ".join(uncommon)
    return result

# Example usage
s1 = input()
s2=input()
result = uncommon_words(s1, s2)
print(result)  # Output: "sweet sour"
