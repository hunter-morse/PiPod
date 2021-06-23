
class MenuPage():
	def __init__(self, title, options, prev_page):
		self.title = title
		self.options = options
		self.prevpage = prevpage

		self.index = 0		# index of current selection
		self.top_index = 0	# index of first entry on page
