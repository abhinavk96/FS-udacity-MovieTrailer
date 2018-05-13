class Movie:
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		"""
			:param title: Title of the Movie
			:param poster_image_url: URL for the poster image of the movie
			:param trailer_youtube_url: URL for the youtube trailer of the movie
		"""
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
	
	def __repr__(self):
		# A representation of a Movie Object is specified here
		return "<Title: {}, Poster Url: {}, youtube trailer url: {}>".format(self.title, self.poster_image_url, self.trailer_youtube_url)
	
	
		
