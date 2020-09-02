class Author:
    def __init__ (self, name):
        self.name = name.strip()

        self.books = []

    def Publish (self, title):
        # This is one part of data validation, where it trims leading and ending spaces
        # before testing to see if the book has already been added to the list.
        title = title.strip()

        # More validation I wanted to do, but couldn't immediately figure out, was how to test
        # while ignoring case (by making the list and new entry temporarily lowercase), but it
        # became too difficult to find how to do it without at least a decent amount of research.

        # The only reason how I found "__contains__" is because of autocomplete.
        if self.books.__contains__(title):
            print (f'{title} is already in {self.name}\'s published books list, sorry!')
        else:
            self.books.append(title)

    def __str__ (self):
        # I know "self.books" returns false if it's empty, but I prefer making the IF
        # statement self-apparent to make it obvious what it does to anyone other than me.
        if len(self.books) > 0:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books published yet.'
        return f'Author: {self.name}, Book(s) published: {book_list}'

# Fake data to test output
def main():
    author1 = Author('Dan Greene')
    author1.Publish('How to Build a Birdhouse')
    author1.Publish('   How to Build a Birdhouse   ')
    author1.Publish('Guide to Basic Woodworking')
    print (author1)

    author2 = Author('Maddison Hale')
    author2.Publish('Nancy Drew')
    author2.Publish('Sherlock Holmes')
    author2.Publish('The Hardy Boys')
    print(author2)

    author3 = Author('  Franklin Woodrow ')
    print (author3)

main()