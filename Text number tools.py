
# Task 01: Text and Number Tools
# Python Programming Internship

# Function 1: Count the words in a sentence
def word_count(sentence):
    words = sentence.split()
    return len(words)


# Function 2: Find the longest word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return "No words entered"

    longest = max(words, key=len)
    return longest


# Function 3: Reverse the sentence
def reverse_sentence(sentence):
    return sentence[::-1]


# Function 4: Check whether a number is prime
def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Main program
print("================================")
print("     TEXT AND NUMBER TOOLS")
print("================================")

# Get sentence from user
sentence = input("\nEnter a sentence: ")

# Get number from user
number = int(input("Enter a number: "))

# Display results
print("\n========== RESULTS ==========")

print("Word Count:", word_count(sentence))

print("Longest Word:", longest_word(sentence))

print("Reversed Sentence:", reverse_sentence(sentence))

if is_prime(number):
    print("Prime Check:", number, "is a Prime Number")
else:
    print("Prime Check:", number, "is Not a Prime Number")

print("==============================")
