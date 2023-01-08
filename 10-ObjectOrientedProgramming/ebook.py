class EBook:
  
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

    self.currentPage = 0
    self.isOpen = False

  def open(self):
    self.isOpen = True;

  def close(self):
    self.isOpen = False

  def nextPage(self):
    if self.isOpen and self.currentPage != self.pages:
      self.currentPage += 1
    elif not self.isOpen:
      print("Cannot read closed book!")
    
  def previousPage(self):
    if self.isOpen and self.currentPage != 0:
      self.currentPage -= 1
    elif not self.isOpen:
      print("Cannot read closed book!")

  def status(self):
    print(f"Title: {self.title}\nAuthor: {self.author}\nPage numbers: {self.pages}\nCurrent page: {self.currentPage}\n")