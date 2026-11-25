# Unit II - Experiment 24: Reverse a string and check for palindrome

word = input("Enter a word: ")

reversed_word = word[::-1]

print("Reversed word:", reversed_word)

if word.lower() == reversed_word.lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
