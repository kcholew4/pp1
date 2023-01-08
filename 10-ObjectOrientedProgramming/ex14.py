from ebook import EBook

ebook = EBook("Javascript The Definitive Guide", "David Flanagan", 600)

ebook.open()

ebook.status()

[ebook.nextPage() for i in range(10)] #Read 10 pages

ebook.status()

ebook.close()

ebook.nextPage()