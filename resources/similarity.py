import numpy as np

from itertools import combinations


# movie ratings and users
ratings = {
    "User 1": {"Space Odyssey": 4, "Hitchhiker": 3, "Interstellar": 7, "Elysium": 7},
    "User 2": {"Space Odyssey": 7, "Hitchhiker": 1, "Interstellar": 2, "Elysium": 5},
    "User 3": {"Space Odyssey": 8, "Hitchhiker": 2, "Martian": 4, "Interstellar": 2, "Elysium": 4},
    "User 4": {"Space Odyssey": 3, "Hitchhiker": 3, "Martian": 2, "Interstellar": 7, "Elysium": 3},
    "User 5": {"Hitchhiker": 3, "Martian": 4, "Interstellar": 7, "Elysium": 6},
    "User 6": {"Space Odyssey": 9, "Hitchhiker": 4, "Martian": 5, "Interstellar": 4, "Elysium": 9}
}
users = list(ratings.keys())


# calculate euclidean similarity between two users
def euclidean_similarity(user1, user2):
    common_movies = set(ratings[user1].keys()) & set(ratings[user2].keys())
    summary = sum((ratings[user1][movie] - ratings[user2][movie]) ** 2 for movie in common_movies)
    return 1 / (1 + np.sqrt(summary))

user_combinations = combinations(users, 2)
euclidean_similarities = {f"{user1} and {user2}": euclidean_similarity(user1, user2) for user1, user2 in user_combinations}


# calculate pearson correlation similarity between two users
def pearson_correlation_similarity(user1, user2):
    common_movies = set(ratings[user1].keys()) & set(ratings[user2].keys())
    n = len(common_movies)
    sum1 = sum([ratings[user1][movie] for movie in common_movies])
    sum2 = sum([ratings[user2][movie] for movie in common_movies])
    sum1sq = sum([ratings[user1][movie] ** 2 for movie in common_movies])
    sum2_sq = sum([ratings[user2][movie] ** 2 for movie in common_movies])
    psum = sum([ratings[user1][movie] * ratings[user2][movie] for movie in common_movies])

    num = psum - (sum1 * sum2) / n
    den = np.sqrt((sum1sq - sum1 ** 2 / n) * (sum2_sq - sum2 ** 2 / n))
    correlation = num / den

    return (1 + correlation) / 2

user_combinations = combinations(users, 2)
pearson_correlation_similarities = {f"{user1} and {user2}": pearson_correlation_similarity(user1, user2) for user1, user2 in user_combinations}


# function to print the results
def print_results(identifier, dictionary):
    print(identifier)
    for key, result in dictionary.items():
        print(f"{key} - {round(result, 5)}")

identifiers = ["- Euclidean Similarities", "\n- Pearson Correlation Similarities"]
dictionaries = [euclidean_similarities, pearson_correlation_similarities]

for identifier, dictionary in zip(identifiers, dictionaries):
    print_results(identifier, dictionary)
