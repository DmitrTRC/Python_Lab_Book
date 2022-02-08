def is_anagram(word1, word2):
    """
    Checks if two words are anagrams of each other.
    """
    return set(word1.lower()) == set(word2.lower())


if __name__ == '__main__':

    w1, w2 = input("Enter two words: ").split()
    if is_anagram(w1, w2):
        print("{} and {} are anagrams of each other.".format(w1, w2))
    else:
        print("{} and {} are not anagrams of each other.".format(w1, w2))
