from nltk.tokenize import WhitespaceTokenizer
from nltk import FreqDist, bigrams, trigrams
import re
from collections import defaultdict
from collections import Counter
import random

#opening text from Game of thrones and seperate into list of words by whitespace
input_text = open("corpus.txt", "r", encoding="utf-8").read()

input_text_words = WhitespaceTokenizer().tokenize(input_text)

#statistics of text
def corpus_statistic(text):
    print("Corpus statistics")

    #number of words
    words = len(text)
    print(f'All tokens: {words}')

    #number of words that are used in text
    uniq_word = len(set(text))
    print(f'Unique tokens: {uniq_word}')

#creating bigrams from text (bigram = par of word that are next to eachother)
def bigrams_(text):
    # using zip() + split() + list comprehension
    # for Bigram formation
    bigrams_words = list(bigrams(text))
    #print(f'Number of bigrams: {len(bigrams_words)}')
    return bigrams_words

#creating dicitonary from bigrams as first word as head and second as tail. 
#Then arraging and counting how many times same tail appears in text
def bigrams_combinations(text):
 
    bigrams = bigrams_(text)
    bigrams_dict = {}
    #creating dictionary
    for word in bigrams:
        bigrams_dict.setdefault(word[0], [])
        bigrams_dict[word[0]].append(word[1])

    #counting apperance of same tail
    for bigr in bigrams_dict:
        bigr_words = bigrams_dict[bigr]
        count_words = Counter(bigr_words)
        bigrams_dict[bigr] = count_words

    return bigrams_dict

#creating dicitonary from trigrams as first word as head and second as tail. 
#Then arraging and counting how many times same tail appears in text
def trigrams_combinations(text):
    trigrams_ = list(trigrams(text))
    
    trigrams_dict = {}
    #creating directory from first two words in trigram as head and last as tail
    for word in trigrams_:
        new_word = word[0] + " " + word[1]
        trigrams_dict.setdefault(new_word, [])
        trigrams_dict[new_word].append(word[2])
    
    #counting how many times same tail appears
    for tri in trigrams_dict:
        tri_words = trigrams_dict[tri]
        count_words = Counter(tri_words)
        trigrams_dict[tri] = count_words
    return trigrams_dict

#creating sentance from bigrams or trigams
def generate_random_text(text):
    list_of_tails = trigrams_combinations(text)

    #First word of a sentance should have Upper first letter and shoundnt end with .?!
    first_word = random.choices(list(list_of_tails.keys()))[0]
    while(True):
        if((first_word[0].isupper() == True) and (re.search(r'[.?!]', first_word) is None)):
            break
        else:
            first_word = random.choices(list(list_of_tails.keys()))[0]

    #list_of_tails = bigrams_combinations(text)
    sentance = first_word
    
    while(True):
        #searching for a tail in dictionary with first word as key
        second_word_list = dict(list_of_tails[first_word])
        #all possible choices for second word
        words_choice = list(second_word_list.keys())
        #how many times the word appears for weights for random choice
        wights = list(second_word_list.values())

        #random choice from list of tails 
        second_word = random.choices(words_choice, weights=wights, k=1)[0]
        #putting the word in the sentance
        sentance = sentance + " " + second_word

        #assinging second word to first word to find new word/bigram/trigram
        #working with bigrams
        #first_word = second_word

        #working with trigrams
        for letter in first_word:
            if letter == " ":
                space_index = first_word.index(letter)

        first_word = first_word[space_index+1:] + " " + second_word

        #checking if the sentance is 5 words long before it finish with . and if not it continue until fist word with. at the end appears
        if (len(sentance.split()) == 5) and (re.search(r'[.?!]', sentance[-1]) is not None):
            break
        elif (len(sentance.split()) > 5) and (re.search(r'[.?!]', sentance[-1]) is not None):
            break
        else:
            continue

    return sentance
    

""" Calling functions if we want specific data

corpus_statistic(input_text_words)
list_of_bigrams = bigrams_(input_text_words)
dictionary_of_bigrams = bigrams_combinations(input_text_words)
list_of_trigrams = working_with_trigrams(input_text_words)
"""

#to generate n sentances and getting longer text
n = 10
for _ in range(n):
    sentance_ = generate_random_text(input_text_words)
    print(sentance_)


"""using with bigrams
    With index(int) as user input, can get which word/bigrams in text is on the index location
    Or with word as user input, can het all possible tails with number how many times the bigram appear
    If the user puts wrong input, it will print different warning depence on produced error

while(True):
    try:
        user_input = input()
        if user_input == "exit":
            exit()
        index  = int(user_input)
        
        #searching for word
        searched_word = input_text_words[index]
        print(searched_word)

        #searching for bigram
        searched_bigram = list_of_bigrams[index]
        print(f'Head: {searched_bigram[0]}  Tail: {searched_bigram[1]}')
        
        #printing connections with bigrams by word
        searched_conn = dictionary_of_bigrams[user_input]
        print(f'Head: {user_input}')
        for item in searched_conn:
            print(f'Tail: {item} Count: {searched_conn[item]}')
    
    except KeyError:
        print(user_input)
        print("The requested word is not in the model. Please input another word.")
    except TypeError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
        print("Index Error. Please input a value that is not greater than the number of all bigrams.")
    except ValueError:
        print("Type Error. Please input an integer.")
"""