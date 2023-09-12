import numpy as np

from numpy.linalg import norm


# query, term frequencies and movies
query = ['earth', 'moon', 'astro']
tfs = {
    "2001: A Space Odyssey": [1, 2, 3],
    "The Hitchhiker's Guide to the Galaxy": [2, 0, 0],
    "The Martian": [0, 1, 1],
    "Interstellar": [3, 0, 0],
    "Elysium": [4, 0, 1]
}
movies = list(tfs.keys())


# calculate idf for a query term
def calculate_idf(term_freqs):
    return np.log10(len(movies) / np.count_nonzero(term_freqs))
    
idfs = {term: calculate_idf([tfs[movie][i] for movie in movies]) for i, term in enumerate(query)}


# calculate tfidf for a movie
def calculate_tfidf(movie_freqs):
    return [tf * idfs[term] for tf, term in zip(movie_freqs, query)]

tfidfs = {movie: calculate_tfidf(tfs[movie]) for movie in movies}
tfidfs = {"Query": calculate_tfidf([1, 1, 1]), **tfidfs}


# cosine similarity between two tfidf vectors
def calculate_cosine_similarity(movie_tfidf):
    query_tfidf = calculate_tfidf([1, 1, 1])
    return np.dot(query_tfidf, movie_tfidf)/(norm(query_tfidf) * norm(movie_tfidf))

cosine_similarities = {movie: calculate_cosine_similarity(tfidfs[movie]) for movie in movies}


# # function to print the results, with option for single results and list of results
def print_results(identifier, dictionary, is_list):
    print(identifier)
    for key, result in dictionary.items():
        if is_list:
            print(f"{key} - {[round(element, 5) for element in result]}")
        else:
            print(f"{key} - {round(result, 5)}")

identifiers = ["- TFs", "\n- IDFs", "\n- TFIDFs", "\n- Cosine Similarities"]
dictionaries = [tfs, idfs, tfidfs, cosine_similarities]
is_lists = [True, False, True, False]

for identifier, dictionary, is_list in zip(identifiers, dictionaries, is_lists):
    print_results(identifier, dictionary, is_list)
