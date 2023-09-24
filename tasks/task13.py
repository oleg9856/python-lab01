if __name__ == '__main__':
    # Prompt the user to enter a word
    word = input("Enter a word: ")

    # Convert the word to lowercase for comparison
    word = word.lower()

    # Initialize a variable for the count of vowels
    vowel_count = 0

    # English vowel letters
    vowels = "aeiou"

    # Calculate the number of vowels
    for letter in word:
        if letter in vowels:
            vowel_count += 1

    # Print the result
    print(f"The number of vowels in the word '{word}' is {vowel_count}")