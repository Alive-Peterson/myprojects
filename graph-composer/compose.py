import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open (text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split()) #turns whitespaces into just spaces
        text = text.lower() #makes everything lower case inorder to compare 
        text = text.translate(str.maketrans('','', string.punctuation)) # removes all the punctuations
    words = text.split() # splits on spaces again
    return words

def make_graph(words):
    g = Graph()
    previous_word = None
    #for each word we check if it is in the graph if not we add it 
    for word in words:
        word_vertex = g.get_vertex(word)
        # if there is a previous word, then add an edge if it does not already exist
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our word to previous word and then iterate
        previous_word = word_vertex

        #generate the probability mappings before composing
    g.generate_probability_mappings()
    return g




def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) #pick a random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition




def main():
    #get words from text
    words = get_words_from_text('texts/hp_sorceror_stone.txt')

    #make a graph using those words
    g = make_graph(words)

    #get the next word for x number of words (defined by user)
    #show the user
    composition = compose(g, words, 100)
    return ' '.join(composition) #returns a string where all the words seperated by space

if __name__ == '__main__':
    main()