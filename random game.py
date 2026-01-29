# # List of sample words for the dictionary
sample_words = [
    "apple", "banana", "grape", "orange", "pear", "peach", "cherry", "mango", "watermelon", "kiwi",
    "kiwifruit", "melon", "avocado", "strawberry", "blueberry", "blackberry", "plum", "apricot",
    "papaya", "date", "fig", "pomegranate", "cantaloupe", "nectarine", "coconut", "lemon", "lime",
    "grapefruit", "tangerine", "mandarin", "kumquat", "lychee", "starfruit", "lingonberry", "clementine"
]

# Save this list to a text file
with open("word_list.txt", "w") as file:
    for word in sample_words:
        file.write(word + "\n")

print("Dictionary file 'word_list.txt' created successfully.")
