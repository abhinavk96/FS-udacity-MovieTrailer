import media
import requests
import json
import fresh_tomatoes
movie1 = media.Movie('THOR', 'https://lalala', "v(adk")

movieList = []
configUrl = "https://api.themoviedb.org/3/configuration?api_key=d52b401aad5afca8dc068a00604370d4"
movieUrl = "https://api.themoviedb.org/3/discover/movie?api_key=d52b401aad5afca8dc068a00604370d4&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=true&page=1"
trailerUrl = ""

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
                    movieList.append(media.Movie(result['title'], basePosterUrl + basePosterSize + result['poster_path'], youtubeUrl))
                    print("Please wait .. fetching movies from the API\n")
                except:
                    continue
    for movie in movieList:
        print(movie)
    fresh_tomatoes.open_movies_page(movieList)
