import tkinter as tk

import gensim
import inflect
import random
import numpy as np

# from gensim.models.word2vec import Word2Vec
# from multiprocessing import cpu_count
# import gensim.downloader as api
# dataset = api.load("text8")
# data = [d for d in dataset]
# print(len(data))
# type(data[0])
# print(len(data[0]))
# print(len(data[1699]))
# print(len(data[1700]))
# print(data[0][0:20])
# print(data[1700][0:20])
# model = Word2Vec(data, min_count = 0, workers=cpu_count())

HEIGHT = 700
WIDTH = 500
custom_blue = '#80b3ff'
model = gensim.models.KeyedVectors.load_word2vec_format(
    'C:/Users/212318026/PycharmProjects/codeNames/codenames-master/GoogleNews-vectors-negative300.bin', binary=True,
    limit=200000
)
result = model.most_similar(positive=['queen', 'man'], negative=['woman'], topn=1)
print(result)

with open("C:/Users/212318026/PycharmProjects/codeNames/codenames-master/words.txt", encoding="utf8") as f:
    words = f.readlines()

words = [w.strip() for w in words]

"""Generates team word lists and a random game board based on the word lists.

:param word_list: Codenames master word list, generated in block above
:return: 5x5 numpy board, red team words, blue team words, neutral words, assassin
:rtype: tuple
"""
"""Generates team word lists and a random game board based on the word lists.

:param word_list: Codenames master word list, generated in block above
:return: 5x5 numpy board, red team words, blue team words, neutral words, assassin
:rtype: tuple
"""
"""Generates team word lists and a random game board based on the word lists.

:param word_list: Codenames master word list, generated in block above
:return: 5x5 numpy board, red team words, blue team words, neutral words, assassin
:rtype: tuple
"""


def generate_board(word_list):
    used = set()
    red = []
    blue = []
    neutral = []
    assassin = []

    # Generate 9 random words for red team.
    while len(red) < 9:
        index = random.choice(range(len(word_list)))
        word = word_list[index]
        if index not in used:
            red.append(word)
            used.add(index)

    # Generate 8 random words for blue team.
    while len(blue) < 8:
        index = random.choice(range(len(word_list)))
        word = word_list[index]
        if index not in used:
            blue.append(word)
            used.add(index)

    # Generate 7 random neutral words.
    while len(neutral) < 7:
        index = random.choice(range(len(word_list)))
        word = word_list[index]
        if index not in used:
            neutral.append(word)
            used.add(index)

    # Generate assassin word.
    while not assassin:
        index = random.choice(range(len(word_list)))
        word = word_list[index]
        if index not in used:
            assassin.append(word)
            used.add(index)
    board = red + blue + neutral + assassin
    random.shuffle(board)
    board = np.reshape(board, (5, 5))
    return board, red, blue, neutral, assassin


"""Guesses the most similar n words out of given words list based on given clue.

Threshold similarity for guessed words must be greater than 0.2

:param clue: given clue
:param words: given list of words to guess from
:param n: max number of words to guess
:return: list of length at most n of best guesses
"""


def guess(clue, words, n):
    poss = {}
    for w in words:
        poss[w] = model.similarity(clue, w)
    poss_lst = sorted(poss, key=poss.__getitem__, reverse=True)
    top_n = poss_lst[:n]
    return [w for w in top_n if poss[w] > 0.2]


"""Verifies that a clue is valid.

A clue (word2) is invalid if either word is a substring of the other, if there is an underscore
in word2, if word2 is the plural form of word1, or if the length of word2 is less than or equal to 2.
Uses inflect.engine() to check plurality.

:param word1: a word from the codenames list of words
:param word2: a model generated clue to be verified
:return: False if word2 is invalid, True if word2 is valid
"""


def clean_clue(word1, word2):
    engine = inflect.engine()
    word1 = word1.lower()
    word2 = word2.lower()
    return not (word1 in word2 or word2 in word1 or "_" in word2 or word2 == engine.plural(word1) or len(word2) <= 2)


"""Gives an optimal length clue based on current board state.

This function computes the similarity index between all pairs and triples of words.
Then, it iteratively computes an optimal clue based on the number of words left
and the max between the highest pair similarity and the highest triplet similarity.

:param words: list of words to generate a clue for
:param bad_words: list of words to avoid giving clues for
:return: tuple of optimal clue, the words intended to be guessed
"""


def give_clue(words, bad_words):
    # מחבר כל שתי צמדים אפשריות למילון ערך ה- key הוא tuple :(מילה 1, מילה 2) וערך ה- value שלהן הוא ה-similarity המשותף
    similarities = {}
    if len(words) >= 2:
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                similarities[(words[i], words[j])] = model.similarity(words[i], words[j])

    # מחבר כל שלשות אפשרים למילון ערך ה- key הוא set :(מילה 1, מילה 2, מילה 3) וערך ה- value שלהן הוא ה-similarity המשותף
    triple_similarities = {}
    if len(words) >= 3:
        seen = set()
        for w in words:
            for key in similarities.keys():
                z = key + (w,)
                if w not in key and tuple(sorted(z)) not in seen:
                    triple_similarities[z] = model.n_similarity([w], list(key))
                    seen.add(tuple(sorted(z)))

    # ריצת לולאה עד מציאת הרמז האופטימלי.
    while True:
        # אם נשארה מילה אחת לנחש או שנגמרו לנו קווי הדמיון הזוגיים אז:
        # נגדיר את max_correlated_n למילה שנותרה
        if len(words) == 1 or not similarities:
            max_correlated_n = (words[0],)

        # אם האורך של רשימת המילים היא 2, הגדר את max_correlated_n ל-max_correlated_pair
        elif len(words) >= 2:
            max_correlated_pair = max(similarities, key=similarities.get)
            max_correlated_n = max_correlated_pair

        # אם האורך הוא 3, הגדר את max_correlated_n ל:
        # max_correlated_triple-אם הדמיון המשולש * 0.9 >= מהדמיון הזוגי הגדר ל
        # max_correlated_pair-אחרת הגדר ל
        if len(words) >= 3:
            max_correlated_triple = max(triple_similarities, key=triple_similarities.get)
            if triple_similarities[max_correlated_triple] * 0.9 >= similarities[max_correlated_pair]:
                max_correlated_n = max_correlated_triple
            else:
                max_correlated_n = max_correlated_pair
        # הדפסת הרמז האפשרי בלוח הבקרה למעקב
        print("Giving clue for:", max_correlated_n)
        c_words = list(max_correlated_n)

        # מצא את המילים הדומות ביותר למילים ב-max_correlated_n
        clues = model.most_similar(positive=c_words, topn=10, restrict_vocab=10000)

        #  ניקוי המילים הבעיתיות שנמצאו דומות
        clues_dict = dict(clues)
        cleaned_clues = [c[0] for c in clues if all([clean_clue(w, c[0]) for w in c_words])]

        # ריצה בלולאה כל עוד ש-cleaned_clues לא ריק או שנמצא רמז אופטימלי
        while cleaned_clues:
            # מצא את הרמז העדכני והטוב ביותר
            possible_clue = max(cleaned_clues, key=lambda x: clues_dict[x])

            # אם המשחק מתקרב לסיום דלג על סינון הרמזים
            if len(words) == len(max_correlated_n):
                return possible_clue, tuple(max_correlated_n)

            # מצא את המילה (הדומה ביותר) לרמז הנוכחי (הטוב ביותר) מ-bad_word
            enemy_match = model.most_similar_to_given(possible_clue, bad_words)

            # חשב את הדמיון בין השתיים
            enemy_sim = model.similarity(enemy_match, possible_clue)

            # אם המילה של האויב (enemy_match) גדולה יותר בדמיון מכל המילים ב-max_correlated_pair,
            # הסרת הרמז הנוכחי הטוב ביותר מ-cleaned_clues והמשך באיטרציה
            # אם לא, החזר את הרמז הנוכחי, מכיוון שהוא אופטימלי
            optimal = True
            for n in max_correlated_n:
                if enemy_sim >= model.similarity(n, possible_clue):
                    # הדפסת המילה שנפלה על איזה מילה בעיתית, ללוח הבקרה
                    print("Foreign word " + enemy_match + " was too similar. Removing clue: " + possible_clue)
                    cleaned_clues.remove(possible_clue)
                    optimal = False
                    break

            if optimal:
                return possible_clue, tuple(max_correlated_n)

        # כל הרמזים של האויב היו דומים יותר מאחת המילים ב-max_correlated_pair
        # אז הוצא את max_correlated_n מנקודות הדמיון התואמות והמשיכו באיטרציה
        print("Too many enemy correlations. Removing ", max_correlated_n)
        if len(max_correlated_n) == 2:
            similarities.pop(max_correlated_n)
        elif len(max_correlated_n) == 3:
            triple_similarities.pop(max_correlated_n)
wordsred=['agent',
'air',
'apple',
'arm',
'back',
'bank',
'board',
'bow',
'box']
wordBlue=['dice',
'dinosaur',
'doctor',
'dog',
'dress',
'dwarf',
'eagle',
'engine',
'england',
'europe',
'eye',
'fish']
# a=give_clue(wordsred,wordBlue)
# print(a)
# b=guess("animal",wordBlue+wordsred,2)




