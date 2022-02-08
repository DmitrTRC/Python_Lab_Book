def is_palindrome(word):
    """
    Checks if a word is a palindrome.

    Args:
        word: string to check

    Returns:
        True if word is a palindrome, False otherwise
    """
    return word == word[::-1]


if __name__ == '__main__':
    while unknown_word := input("Enter a word: "):
        print(is_palindrome(unknown_word))
