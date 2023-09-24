if __name__ == '__main__':
    # Prompt the user to enter a word
    word = input("Enter a word: ")

    # Convert the word to lowercase for comparison
    word = word.lower()

    # Determine if the word is a palindrome
    is_palindrome = word == word[::-1]

    # Print the result
    if is_palindrome:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")