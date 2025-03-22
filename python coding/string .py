sentence = input("Enter a sentence: ")

# Convert the sentence to title case
title_case = sentence.title()

# Count total number of words
word_count = len(sentence.split())

# Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Reverse the sentence
reversed_sentence = sentence[::-1]

# Display the results
print("\n--- Results ---")
print(f"Title Case: {title_case}")
print(f"Total Words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Reversed Sentence: {reversed_sentence}")
