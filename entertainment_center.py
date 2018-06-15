import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story2 = media.Movie("Toy Story 2",
                        "A story of a boy and his toys that come to life...again",
                        "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
                        "https://www.youtube.com/watch?v=Lu0sotERXhI")

toy_story3 = media.Movie("Toy Story 3",
                        "Another story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

movies = [toy_story,toy_story2,toy_story3]

fresh_tomatoes.open_movies_page(movies)
