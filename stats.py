# This script provides functions to analyze a book's text.

# This function reads the book from the given path and returns its text
def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

# This function counts the occurrences of each character in the given book text
# and returns a dictionary with the character as the key and its count as the value
def get_character_count(book_text):
    character_count = {}
    for character in book_text:
        if character.isalpha(): # Only count alphabetic characters
            character = character.lower() # Convert to lowercase for case-insensitive counting
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

# This function receives a dictionary of character counts and returns a sorted list of dictionaries
def sort_character_count(character_count):
    sorted_character_count = []
    for character, count in character_count.items():
        sorted_character_count.append({'character': character, 'count': count})
    sorted_character_count.sort(key=lambda x: x['count'], reverse=True)
    return sorted_character_count