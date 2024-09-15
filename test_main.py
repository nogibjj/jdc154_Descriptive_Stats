from main import (
    generate_summary_stats,
    clean_ratings,
    years_and_ratings,
    years_ratings_trends,
)
import pandas as pd


def test_summary_stats():
    stats = generate_summary_stats("netflix_titles.csv")
    assert stats.loc["mean"]["release_year"] == 2014.1801975701146
    assert stats.loc["min"]["release_year"] == 1925.0
    assert stats.loc["max"]["release_year"] == 2021.000000


def test_clean_ratings():
    "checking that the correct rating categories are there"
    # only works on this specific dataset clean up
    ratings = clean_ratings(pd.read_csv("netflix_titles.csv"))
    assert "74 min" not in ratings["rating"]
    assert "84 min" not in ratings["rating"]
    assert "66 min" not in ratings["rating"]


def test_years_ratings():
    ratings = clean_ratings(pd.read_csv("netflix_titles.csv"))
    yrs_and_rtes = years_and_ratings(ratings)
    assert len(yrs_and_rtes["release_year"] == 14)


def test_trends():
    ratings = clean_ratings(pd.read_csv("netflix_titles.csv"))
    assert years_ratings_trends(ratings).shape == (74, 14)


if __name__ == "__main__":
    test_clean_ratings()
    test_years_ratings()
    test_trends()
