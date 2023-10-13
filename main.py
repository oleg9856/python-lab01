import pandas as pd
import matplotlib.pyplot as plt

netflix_full_df = pd.read_csv(r"https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/netflix_titles.csv")
plt.style.use('ggplot')


def task01():
    count_2023 = len(netflix_full_df[netflix_full_df["release_year"] == 2023])
    print(f"Number of movies released in 2023: {count_2023}")


def task02():
    # Count the number of projects per country
    country_counts = netflix_full_df['country'].value_counts()

    # Select the top 10 countries
    top_10_countries = country_counts.head(10)

    # Create a bar chart to visualize the distribution
    plt.figure(figsize=(18, 15))
    top_10_countries.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Countries with the Most Netflix Projects')
    plt.xlabel('Country')
    plt.ylabel('Number of Projects')
    plt.xticks(rotation=45)  # Rotate the country names for better visibility
    plt.show()


def task03():
    # Movies before 1960 year
    movies_before_1960 = netflix_full_df[netflix_full_df["release_year"] < 1960]
    # Count the number of projects per country
    country_counts = movies_before_1960['country'].value_counts()

    # Create a bar chart to visualize the distribution
    plt.figure(figsize=(15, 20))
    country_counts.plot(kind='bar', color='skyblue')
    plt.title('Countries that have released the most old movies (premiere date before 1960)')
    plt.xlabel('Country')
    plt.ylabel('Number of Projects')
    plt.xticks(rotation=45)  # Rotate the country names for better visibility
    plt.show()


def task04():
    netflix_full_df['date_added'] = pd.to_datetime(netflix_full_df['date_added'], format='%B %d, %Y', errors='coerce')

    # Filter out rows with missing or incorrect date values
    netflix_date_added_df = netflix_full_df.dropna(subset=['date_added'])

    # Extract the month from the 'date_added' column using .loc
    netflix_date_added_df.loc[:, 'month_added'] = netflix_date_added_df['date_added'].dt.month

    # Define the seasons (Spring: March, April, May; Fall: September, October, November)
    spring_months = [3, 4, 5]
    fall_months = [9, 10, 11]

    # Filter movies and TV shows for spring and fall
    movies_spring = netflix_date_added_df[
        (netflix_date_added_df['type'] == 'Movie') & (netflix_date_added_df['month_added'].isin(spring_months))]
    movies_fall = netflix_date_added_df[
        (netflix_date_added_df['type'] == 'Movie') & (netflix_date_added_df['month_added'].isin(fall_months))]
    tv_spring = netflix_date_added_df[
        (netflix_date_added_df['type'] == 'TV Show') & (netflix_date_added_df['month_added'].isin(spring_months))]
    tv_fall = netflix_date_added_df[
        (netflix_date_added_df['type'] == 'TV Show') & (netflix_date_added_df['month_added'].isin(fall_months))]

    # Count the number of movies and TV shows released in spring and fall
    movie_counts = [len(movies_spring), len(movies_fall)]
    tv_counts = [len(tv_spring), len(tv_fall)]

    # Create a bar chart to visualize the results
    seasons = ['Spring', 'Fall']

    plt.figure(figsize=(10, 6))
    plt.bar(seasons, movie_counts, width=0.4, label='Movies', align='center', alpha=0.6)
    plt.bar(seasons, tv_counts, width=0.4, label='TV Shows', align='edge', alpha=0.6)
    plt.xlabel('Season')
    plt.ylabel('Number of Projects')
    plt.title('Netflix Projects Released by Season')
    plt.legend()
    plt.show()


def task05():
    # Assuming you have already loaded your Netflix data into the 'netflix_full_df' DataFrame

    # Convert 'release_year' column to integers
    netflix_full_df['release_year'] = pd.to_numeric(netflix_full_df['release_year'])

    # Group the data by 'release_year' and count the number of movies per year
    movies_per_year = netflix_full_df.groupby('release_year')['show_id'].count()

    # Find the year with the most movies
    year_with_most_movies = movies_per_year.idxmax()
    num_movies_in_most_movies_year = movies_per_year.max()

    print(
        f"The year with the most movies on Netflix was {year_with_most_movies} with "
        f"{num_movies_in_most_movies_year} movies.")


if __name__ == '__main__':
    a = int(input("Input the number: "))
    if a == 1:
        task01()
    elif a == 2:
        task02()
    elif a == 3:
        task03()
    elif a == 4:
        task04()
    elif a == 5:
        task05()
    else:
        print("Incorrect input")
