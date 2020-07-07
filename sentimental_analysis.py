import re
import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


def count_positive_negative_certain_uncertain(word_tokens):
    positive_count = 0
    negative_count = 0
    uncertain_count = 0
    constrain_count = 0
    with open("word_dict.json", "r") as jf:
        data = jf.read()
        jobject = json.loads(data)
        for word in word_tokens:
            if word in jobject["positive_words"]:
                positive_count += 1
            elif word in jobject["negative_words"]:
                negative_count -= 1
            elif word in jobject["uncertainty_words"]:
                uncertain_count += 1
            elif word in jobject["constraining_words"]:
                constrain_count += 1
    return (positive_count,
        -1 * (negative_count),
        uncertain_count,
        constrain_count,)
    
    

def count_complex_words(word_tokens):
    vowels = list("aeiou")
    complex_word_count = 0
    for word in word_tokens:
        vowels_count = 0
        exception_vowels_count = 0
        total_vowels_count = 0
        exception_vowels_count = word.count("es") + word.count("ed")
        for vowel in vowels:
            vowels_count = vowels_count + word.count(vowel)

        total_vowels_count = vowels_count - exception_vowels_count

        if total_vowels_count > 2:
            complex_word_count += 1
    return complex_word_count



def calculate_average_sentence_length(word_tokens_count, sentences_count):
    average_sentence_length = 0
    if sentences_count != 0:
        average_sentence_length = word_tokens_count / sentences_count
    # print(average_sentence_length)
    return average_sentence_length


def calculate_percentage_complex_words(complex_word_count, word_tokens_count):
    if word_tokens_count != 0:
        percentage_complex_words = complex_word_count / word_tokens_count
    else:
        percentage_complex_words = 0
    return percentage_complex_words



def calculate_fog_index(average_sentence_length, percentage_complex_words):
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    # print(fog_index)
    return fog_index



def calculate_word_proportion(
    positive_score,
    negative_score,
    uncertainty_score,
    constraining_score,
    word_tokens_count,
   ):
    
    positive_word_proportion = (
        negative_word_proportion
    ) = uncertainty_word_proportion = constraining_word_proportion = 0
    if word_tokens_count != 0:
        positive_word_proportion = positive_score / word_tokens_count
    
    if word_tokens_count != 0:
        negative_word_proportion = negative_score / word_tokens_count
    
    if word_tokens_count != 0:
        uncertainty_word_proportion = uncertainty_score / word_tokens_count
    
    if word_tokens_count != 0:
        constraining_word_proportion = constraining_score / word_tokens_count
    return (
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    )


def analyse_sentiments(string):
   
    
    string_readbility = string
    
    temp = re.sub("[^a-z ]", "", string)
    string = temp

    
    f_stop_words = open("StopWords_Generic.txt", "r")
    f_stop_words_list = f_stop_words.read().lower()
    f_stop_words_list = f_stop_words_list.split("\n")

    
    tokens = word_tokenize(string)

    
    word_tokens = []
    for i in range(0, len(tokens)):
        token = tokens[i]
        if token not in f_stop_words_list:
            word_tokens.append(tokens[i])

    
    (
        positive_score,
        negative_score,
        uncertainty_score,
        constraining_score,
    ) = count_positive_negative_certain_uncertain(word_tokens)
    polarity_score = (positive_score - negative_score) / (
        (positive_score + negative_score) + 0.000001
    )

    
    word_tokens_count = len(word_tokens)

    

    
    sentences = sent_tokenize(string_readbility)

    # CALCULATE AVERAGE SENTENCE LENGTH
    sentences_count = len(sentences)
    average_sentence_length = calculate_average_sentence_length(
        word_tokens_count, sentences_count
    )

    # COUNT THE COMPLEX WORDS IN ALL SENTENCES
    complex_word_count = count_complex_words(word_tokens)

    # PERCENTAGE OF COMPLEX WORDS
    percentage_complex_words = calculate_percentage_complex_words(
        complex_word_count, word_tokens_count
    )

    # FOG INDEX
    fog_index = calculate_fog_index(average_sentence_length, percentage_complex_words)

    
    (
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    ) = calculate_word_proportion(
        positive_score,
        negative_score,
        uncertainty_score,
        constraining_score,
        word_tokens_count,
    )

    sentiment_score_list = [
        positive_score,
        negative_score,
        polarity_score,
        average_sentence_length,
        percentage_complex_words,
        fog_index,
        complex_word_count,
        word_tokens_count,
        uncertainty_score,
        constraining_score,
        positive_word_proportion,
        negative_word_proportion,
        uncertainty_word_proportion,
        constraining_word_proportion,
    ]

    return sentiment_score_list


def calculate_constrain_words_whole_report(string):
    temp = re.sub("[^a-z ]", " ", string)
    stop_words = open("StopWords_Generic.txt", "r")
    stop_words = stop_words.read().lower()
    stop_words_list = stop_words.split("\n")
   

    
    tokens = word_tokenize(temp)
    constrain_words_count = 0
    with open("word_dict.json", "r") as jf:
        data1 = jf.read()
        jobject = json.loads(data1)
        for word in tokens:
            if word in jobject["constraining_words"]:
                constrain_words_count += 1
    return constrain_words_count

