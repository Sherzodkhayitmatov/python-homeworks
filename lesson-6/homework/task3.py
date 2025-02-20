import os
import string
from collections import Counter

def create_sample_file():
    """Prompt the user to enter text if 'sample.txt' does not exist."""
    user_text = input("File not found. Please enter a paragraph: ")
    with open("sample.txt", "w") as file:
        file.write(user_text)

def read_file():
    """Read from 'sample.txt' or prompt the user to create it."""
    if not os.path.exists("sample.txt"):
        create_sample_file()
        
    with open("sample.txt", "r") as file:
        return file.read()
    
def clean_text(text):
    """Convert text to lowercase, remove punctuation, and return words."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def count_words(words):
    """Count word occurrences and return total words and top 5 words."""
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)
    return total_words, top_words

def save(total_words, top_words):
    """Save word count results to 'word_count_report.txt'."""
    with open("word_count_report.txt", "w") as file:
        file.write(f"Total words: {total_words}\n\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    """Main function to analyze word frequency."""
    text = read_file()
    words = clean_text(text)
    total_words, top_words = count_words(words)

    print(f"Total words: {total_words}")
    print("\nTop 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    save(total_words, top_words)
    print("\nWord count report saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    main()
