#1 -> takes a single movie and returns True if its IMDB score is above 5.5
def above_5_5(movies):
    return movies["imdb"] > 5.5

#2 -> returns a sublist of movies with an IMDB score above 5.5.
def filter_above_5_5(movies):
    return list(filter(above_5_5, movies))

#3 -> takes a category name and returns just those movies under that category.
def filter_by_category(movies, category):
    return [if movie["category"] == category]

#4 -> takes a list of movies and computes the average IMDB score.
def average_imdb(movies):
    if not movies:
        return 0
    total_score = sum(movies["imdb"])
    return total_score / len(movies)

#5 -> takes a category and computes the average IMDB score.
def average_imdb_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb(category_movies)