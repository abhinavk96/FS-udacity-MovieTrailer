import media
import requests
import json
import fresh_tomatoes

# An empty list is initialised which will later store all the movie obects
movieList = []

configUrl = "https://api.themoviedb.org/3/configuration?api_key=d52b401aad5afca8dc068a00604370d4"  # NOQA
movieUrl = "https://api.themoviedb.org/3/discover/movie?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"  # NOQA

# make GET requests to API to fetch movies and basic poster config
movieResponse = requests.get(movieUrl)
configResponse = requests.get(configUrl)


if configResponse.ok:
    # parse config JSON data and specify poster size
    jsonData = json.loads(configResponse.content)
    basePosterUrl = jsonData['images']['secure_base_url']
    posterSize = 'w500'
    if movieResponse.ok:
        # parse movie JSON data and iteratively fetch movie trailer
        movieJsonData = json.loads(movieResponse.content)
        for result in movieJsonData['results']:
            trailerResponse = requests.get("https://api.themoviedb.org/3/movie/"+str(result['id'])+"/videos?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US")  # NOQA
            if trailerResponse.ok:
                trailerJsonData = json.loads(trailerResponse.content)
                try:
                    # Generate youtube URL
                    videoId = trailerJsonData['results'][0]['key']
                    youtubeUrl = "https://www.youtube.com/watch?v=" + videoId
                    print("Please wait .. fetching movies from the API\n")
                    posterUrl = basePosterUrl+posterSize+result['poster_path']
                    # Create Movie objects and append to movie list
                    movie = media.Movie(result['title'], posterUrl, youtubeUrl)
                    print("\033[92m Fetched: \033[94m{}\033[0m".format(movie))
                    movieList.append(movie)
                except:
                    continue
    # Call to open_movies_page function with movie list
    fresh_tomatoes.open_movies_page(movieList)
