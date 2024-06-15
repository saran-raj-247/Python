def main():
    # Initialize an empty dictionary to store genres and their corresponding book titles
    genre_books = {}

    # Read input lines until a blank line is entered
    while True:
        try:
            line = input().strip()
            if not line:
                break  # Exit loop when a blank line is encountered

            title, genre = map(str.strip, line.split(','))

            # Add the book title to the corresponding genre in the dictionary
            if genre in genre_books:
                genre_books[genre].append(title)
            else:
                genre_books[genre] = [title]

        except EOFError:
            break  # End of input reached

    # Display the categorized books
    for genre, titles in genre_books.items():
        print(f"{genre}: {', '.join(titles)}")

if __name__ == "__main__":
    main()
