import media
import fresh_tomatoes1
"""Put the movies objects into the website and display them"""


gladiator=media.Movie("Gladiator",
"A story of warrior",
"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
"https://www.youtube.com/watch?v=owK1qxDselE",
"May 1, 2000",
"Ridley Scott")


the_shawshank_redemption=media.Movie("The Shawshank Redemption",
"A formar banker escape from jail",
"http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
"https://www.youtube.com/watch?v=6hB3S9bIaco&t=40s",
"Sep 10, 1994",
"Frank Darabont")


titanic=media.Movie("Titanic",
"The love story happen in a cruise",
"https://i.ytimg.com/vi/jIhicnTgArM/movieposter.jpg",
"https://www.youtube.com/watch?v=zCy5WQ9S4c0",
"Nov 1, 1997",
"James Cameron")


john_wick=media.Movie("John Wick",
"The story about a retired killer",
"https://i.ytimg.com/vi/ZdOmCSmI4X0/movieposter.jpg",
"https://www.youtube.com/watch?v=2AUmvWm5ZDQ",
"Oct 24, 2014",
"Chad Stahelski")


interstellar=media.Movie("Interstellar",
"The story about time traveling and saving the world",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
"https://www.youtube.com/watch?v=Lm8p5rlrSkY",
"Oct 26, 2014",
"Christopher Nolan"
)

prometheus=media.Movie("Prometheus",
"A team taking spaceship to search for ancestor of human being",
"https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
"https://www.youtube.com/watch?v=yA6OKoW30Pk",
"Apr 11, 2014",
"Ridley Scott")


the_dark_knight_rises=media.Movie("The Dark Knight Rises",
"The story of gotam city hero - batman",
"http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
"https://www.youtube.com/watch?v=z5Humz3ONgk",
"July 16, 2012",
"Christopher Nolan")


dunkirk=media.Movie("Dunkirt",
"The movie depicts the Dunkirk evacuation of World WarII",
"https://www.bleedingcool.com/wp-content/uploads/2017/06/Christopher-Nolans-Dunkirk-IMAX-poster.jpg",
"https://www.youtube.com/watch?v=F-eMt3SrfFU",
"Jul 13, 2017",
"Christopher Nolan")


justic_league=media.Movie("Justic league",
"About heros league to fight with evil",
"https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
"https://www.youtube.com/watch?v=r9-DM9uBtVI",
"Nov 17, 2017",
"Zack Snyder")
"""Here are the movies objects being created,
they attach with the movie information i want to show on the website"""


movies=[
justic_league,
the_dark_knight_rises,
prometheus,
interstellar,
john_wick,
dunkirk,
gladiator,
titanic,
the_shawshank_redemption,
]
"""Store the movie objects in a list"""


fresh_tomatoes1.open_movies_page(movies)
"""Open the movies in user's browser."""
