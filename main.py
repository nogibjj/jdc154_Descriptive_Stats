"""Code to look at Netflix Movie and Show rating trends"""

import pandas as pd
import matplotlib.pyplot as plt


def generate_summary_stats(filename):
    """Generate summary stats of data"""
    data = pd.read_csv(filename)
    return data.describe()


def clean_ratings(data):
    """Cleans up rating column of data"""
    data = data[data["rating"] != "74 min"]
    data = data[data["rating"] != "84 min"]
    data = data[data["rating"] != "66 min"]
    return data


def years_and_ratings(data):
    """Looks at the number of films released per rating"""
    return data.groupby(["rating"]).aggregate({"release_year": "mean"})


def years_ratings_trends(data):
    """Looks at number of films released per year with each rating"""
    return data.groupby(["release_year", "rating"]).size().unstack(fill_value=0)


def plot_trends(data, category):
    """Plots the number of films released per year with each rating"""
    data.plot.bar(
        stacked=True,
        figsize=(10, 6),
        ylabel="Count",
        xlabel="Year",
        title=f"{category} Ratings over the Years",
    )
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("netflix_titles.csv")
    movies = df[df["type"] == "Movie"]
    shows = df[df["type"] == "TV Show"]
    generate_summary_stats("netflix_titles.csv")
    clean_ratings(df)
    print("Ratings types:", df["rating"].value_counts())
    movie_years_and_ratings = years_and_ratings(movies)
    print("Movie years and ratings:", movie_years_and_ratings)
    shows_years_and_ratings = years_and_ratings(shows)
    print("Shows years and ratings:", shows_years_and_ratings)
    movie_trends = years_ratings_trends(movies)
    shows_trends = years_ratings_trends(shows)
    plot_trends(movie_trends, "Movie")
    plot_trends(movie_trends, "Shows")
