def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_text = book.read()
    return book_text

def main():
    book = get_book_text('books/frankenstein.txt')
    print(book)

main()