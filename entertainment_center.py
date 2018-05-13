import media
import requests
import json
import fresh_tomatoes

# An empty list is initialised which will later store all the movie obects
movieList = []

# configUrl stores the URL which fetches configuration from The Movie DB API. It is required to get Base Url for the poster images.
configUrl = "https://api.themoviedb.org/3/configuration?api_key=d52b401aad5afca8dc068a00604370d4"

# movieUrl stores the URL which fetches a single page of movies from The Movie DB API based on their popularity in descending order.
movieUrl = "https://api.themoviedb.org/3/discover/movie?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"

# make a GET request to API to fetch the movies
movieResponse = requests.get(movieUrl)

# make a GET request to API to fetch the configuration
configResponse = requests.get(configUrl)


if configResponse.ok:  # Check if a success status of 200 is returned.
    jsonData = json.loads(configResponse.content) # parses the json response of the API
    basePosterUrl = jsonData['images']['secure_base_url'] # fetch the secure base url of the posters which is required for fetching the image
    basePosterSize = 'w500' # specify the size of the image desired
    if movieResponse.ok: # Check if a success status of 200 is returned while fetching movies.
        movieJsonData = json.loads(movieResponse.content) # Parse the json data of the movies fetched from the API
        for result in movieJsonData['results']: # Iterate over all the movies fetched from the API
            trailerResponse = requests.get("https://api.themoviedb.org/3/movie/"+str(result['id'])+"/videos?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US") # Make a request for the movie's trailer
            if trailerResponse.ok: # Check if the trailer of the movie is successfully retrieved
                trailerJsonData = json.loads(trailerResponse.content) # Parse the json trailer response 
                try:
                    youtubeUrl = "https://www.youtube.com/watch?v=" + trailerJsonData['results'][0]['key'] # Generate the youtube URL of the movie trailer
                    print("Please wait .. fetching movies from the API\n") # Helper text               
                    movie = media.Movie(result['title'], basePosterUrl + basePosterSize + result['poster_path'], youtubeUrl) # Create a movie object
                    print("\033[92m Fetched: \033[94m{}\033[0m".format(movie)) # Helper text
                    movieList.append(movie) # Append the obect to the movie list
                except:
                    continue
    fresh_tomatoes.open_movies_page(movieList) # Call the ooen_movies_page function with the list of movies as it's parameter
