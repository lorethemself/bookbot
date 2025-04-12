# This script reads a book from a given path,
# analyzes its text,
# and generates a report with the word count and character count.
# The report is formatted for easy reading.

# Importing the required modules
import sys
from stats import get_word_count, get_character_count, sort_character_count

# This function reads the book from the given path and returns its text
def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

# This function formats the character count list of dictionaries into a single formatted string with new lines
def prettify_character_count(character_count):
    pretty_character_count = []
    # This loop iterates over the character count list of dictionaries
    # and formats each character and its count into a string
    # The character is converted to lowercase and checked if it is an alphabetic character
    # before adding it to the pretty_character_count list
    for item in character_count:
        character = item['character']
        count = item['count']
        pretty_character_count.append(f"{character}: {count}")
    # This line joins the formatted strings with new lines
    # and returns the result
    pretty_character_count = '\n'.join(pretty_character_count)
    return pretty_character_count

# This function creates a report of the book's statistics
def make_book_report(path_to_book):
    # These variables contain the book's statistics
    book_text = get_book_text(path_to_book)
    word_count = get_word_count(book_text)
    sorted_character_count = sort_character_count(get_character_count(book_text))
    pretty_character_count = prettify_character_count(sorted_character_count)

    # These variables contain the report's elements
    header = '============ BOOKBOT ============'
    path_section = f'Analyzing book found at {path_to_book}...'
    word_count_subheading = '----------- Word Count ----------'
    word_count_section = f'Found {word_count} total words'
    character_count_subheading = '--------- Character Count -------'
    character_count_section = f'{pretty_character_count}'
    footer = '============= END ==============='
    
    # This variable combines the elements into a single formatted string
    book_report = f'''{header}
{path_section}
{word_count_subheading}
{word_count_section}
{character_count_subheading}
{character_count_section}
{footer}
'''
    # This line prints the formatted report
    print(book_report)

def main():
    if len(sys.argv) > 1:
        path_to_book = sys.argv[1]
    make_book_report(path_to_book)
main()