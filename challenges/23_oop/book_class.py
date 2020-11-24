class Booklist():
	def __init__(self):
		pass
		self.books = []

	def add(self, title, author):
		pass
		book = {}
		book['title'] = title
		book['author'] = author

		self.books.append(book)

	def count_books(self):
		pass
		return len(self.books)

	def remove_title(self, title):
		pass
		for book in self.books:
			if book['title'] == title:
				self.books.remove(book)


	def display_titles(self):
		pass
		titles = []
		for book in self.books:
			titles.append(book['title'])

		titles.sort()

		print(titles)






