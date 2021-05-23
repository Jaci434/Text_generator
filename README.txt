TEXT GENERATOR
	2 files: corpus.txt, text_generator.py

Project using nltk librabry

Text generator is program to generate n numbers of sentances. 
The words are taken from input text (corpus) and it has to be text multiple words (in our case
the text is from Game of thornes text = corpus.txt)

After opening&reading the text, we seperate each word by white space (function WhitespaceTokenizer())
to create tokens and put them in list.

Functions:

corpus_statistic-> input: a list of tokens
		   return: printing number of all tokens and number of used words in the text

bigrams_ -> input: a list of tokens
	    return: list of bigrmas from text

bigrams_combinations -> input: a list of tokens
			return: dictionary of bigrams as Head (word in text), Tails (bigrams to head word
			that appears) : number of how many times the bigrams with head and specific tail appears in text


trigrams_combinations -> input: a list of tokens
			 return: dictionary of trigrams as Head (first and second word in trigram), Tails (bigrams to head word
			that appears) : number of how many times the trigrams with head and specific tail appears in text

generate_random_text-> input: a list of tokens
		       return: sentence, which is long 5 words and finish with (.!?). If first sentance finish before count
			of 5 words (word with .?! appears before) the output sentance is actually 2 sentances.


If we want specific data from functions, we can call each one seperatly.
For getting longer text we have to call function generate_random_text, n times to get n sentance long text.

We can get specific word from text or bigrams or in how many bigrams one word is and how many times the bigram appear in text.
For that we need to call user input, where the user has to write the index or word. To use that part, the code has to be uncommented.
If the user put wrong input the exceptions are called and it print the message depence on th error.

Jacinta, April 2021