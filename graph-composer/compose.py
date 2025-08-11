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
#for each word we check if it is in the graph if not we add it 
    for word in words:
        word_vertex = g.get_vertex(word)
        
def compose(g, words, length=50):
    pass

def main():
    words = get_words_from_text('texts/hp_sorceror_stone.txt')


if __name__ == '__main__':
    main()