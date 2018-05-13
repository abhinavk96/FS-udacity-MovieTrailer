import media
import requests
import json
import fresh_tomatoes

movieList = []
configUrl = "https://api.themoviedb.org/3/configuration?api_key=d52b401aad5afca8dc068a00604370d4"
movieUrl = "https://api.themoviedb.org/3/discover/movie?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"

movieResponse = requests.get(movieUrl)
configResponse = requests.get(configUrl)
if configResponse.ok:
    jsonData = json.loads(configResponse.content)
    basePosterUrl = jsonData['images']['secure_base_url']
    basePosterSize = 'w500'
    if movieResponse.ok:
        movieJsonData = json.loads(movieResponse.content)
        for result in movieJsonData['results']:
            trailerResponse = requests.get("https://api.themoviedb.org/3/movie/"+str(result['id'])+"/videos?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US")
            if trailerResponse.ok:
                trailerJsonData = json.loads(trailerResponse.content)
                try:
                    youtubeUrl = "https://www.youtube.com/watch?v=" + trailerJsonData['results'][0]['key']
                    print("Please wait .. fetching movies from the API\n")                    
                    movie = media.Movie(result['title'], basePosterUrl + basePosterSize + result['poster_path'], youtubeUrl)
                    print("\033[92m Fetched: \033[94m{}\033[0m".format(movie))
                    movieList.append(movie)
                except:
                    continue
    fresh_tomatoes.open_movies_page(movieList)
