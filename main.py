import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_titles.csv")
movies = data[data["type"] == "Movie"]
shows = data[data["type"] == "TV Show"]


def clean_ratings(data):
    data = data[data["rating"] != "74 min"]
    data = data[data["rating"] != "84 min"]
    data = data[data["rating"] != "66 min"]


def years_and_ratings(data):
    years_and_ratings = data.groupby(["rating"]).aggregate({"release_year": "mean"})
    return years_and_ratings


def years_ratings_trends(data):
    return data.groupby(["release_year", "rating"]).size().unstack(fill_value=0)


def plot_trends(data, type):
    data.plot.bar(
        stacked=True,
        figsize=(10, 6),
        ylabel="Count",
        xlabel="Year",
        title=f"{type} Ratings over the Years",
    )
    plt.show()


if __name__ == "__main__":
    print("Summary Stats:", data.describe())
    clean_ratings(data)
    print("Ratings types:", data["rating"].value_counts())
    movie_years_and_ratings = years_and_ratings(movies)
    print("Movie years and ratings:", movie_years_and_ratings)
    shows_years_and_ratings = years_and_ratings(shows)
    print("Shows years and ratings:", shows_years_and_ratings)
    movie_trends = years_ratings_trends(movies)
    shows_trends = years_ratings_trends(shows)
    plot_trends(movie_trends, "Movie")
    plot_trends(movie_trends, "Shows")
