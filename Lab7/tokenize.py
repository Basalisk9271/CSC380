# Name: Gabe Imlay
# Assignment: Lab 7 - tokenization code
# Due: Mar 20, 2024
# Sources: Chat-GPT and classmates referenced when debugging. 

import os
import re
from collections import Counter

def clean_text(text):
    # Remove special characters, symbols, and punctuation
    # Shown to me by Chat-GPT
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Make all words lowercase
    text = text.lower()
    return text

def tokenize(text):
    # Tokenize the text by splitting on spaces
    tokens = text.split()
    return tokens

def remove_stopwords(tokens):
    # Define the stop words to be removed
    stopwords = set([
        'this', 'that', 'take', 'want', 'which', 'then', 'than', 'will',
        'with', 'have', 'after', 'such', 'when', 'some', 'them', 'could',
        'make', 'though', 'from', 'were', 'also', 'into', 'they', 'their',
        'there', 'because'
    ])
    # Filter out stop words and words with length less than 4
    filtered_tokens = [word for word in tokens if len(word) >= 4 and word not in stopwords]
    return filtered_tokens

# Path to the folder containing review files
reviews_folder = './reviews'

# Initialize Counter objects for positive and negative reviews
positive_counter = Counter()
negative_counter = Counter()

# Process each review file
for filename in os.listdir(reviews_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(reviews_folder, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            text = clean_text(text)
            tokens = tokenize(text)
            filtered_tokens = remove_stopwords(tokens)
            rating = int(filename.split('_')[1].split('.')[0])
            if rating >= 6:
                positive_counter.update(filtered_tokens)
            else:
                negative_counter.update(filtered_tokens)

# Get the most common words in positive and negative reviews
most_common_positive = positive_counter.most_common(100)
most_common_negative = negative_counter.most_common(100)

# Determine the maximum word length for proper column alignment
max_word_length = max(len(word) for word, _ in most_common_positive)

# Print the most common positive words in descending order by frequency
words_per_line = 10

print("Top 100 Words Used in Positive Reviews\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(0, len(most_common_positive), words_per_line):
    words_line = most_common_positive[i:i + words_per_line]
    for word, _ in words_line:
        print(word.ljust(max_word_length + 2), end='')
    print()

# Potential loop to do the same thing with Negatives. 
# print()
# print("Top 100 Words Used in Negative Reviews\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# for i in range(0, len(most_common_negative), words_per_line):
#     words_line = most_common_negative[i:i + words_per_line]
#     for word, _ in words_line:
#         print(word.ljust(max_word_length + 2), end='')
#     print()