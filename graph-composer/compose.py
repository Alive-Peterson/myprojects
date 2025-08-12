import os
import string
import random
from graph import Graph, Vertex

# Reads a text file and returns a list of cleaned words
def get_words_from_text(filename):
    # Get the absolute path to the texts folder next to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(script_dir, "texts", filename)

    print("DEBUG: Looking for file at:", text_path)

    # Check if file exists, otherwise raise error
    if not os.path.exists(text_path):
        raise FileNotFoundError(f"File not found at: {text_path}")

    # Open and read file, clean whitespace, lowercase, and remove punctuation
    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
        text = ' '.join(text.split())                  # normalize spaces
        text = text.lower()                            # lowercase for uniformity
        text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation

    return text.split()  # return list of words

# Creates a graph where each word is a vertex and edges show word-to-word connections
def make_graph(words):
    g = Graph()
    previous_word = None
    for word in words:
        word_vertex = g.get_vertex(word)               # get or create vertex for word
        if previous_word:                              # if not first word, connect to previous
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex                    # move to next word
    g.generate_probability_mappings()                  # prepare probability data for next-word selection
    return g

# Uses the graph to create a random composition of words
def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))          # pick a random starting word
    for _ in range(length):
        composition.append(word.value)                 # add current word to composition
        word = g.get_next_word(word)                   # choose next word based on probability
    return composition

# Main function: reads text, builds graph, composes text, and prints it
def main():
    words = get_words_from_text('hp_sorcerer_stone.txt')  # load and clean words from file
    g = make_graph(words)                                 # build graph of word connections
    composition = compose(g, words, 100)                  # generate 100-word composition
    print(' '.join(composition))                          # print the result

# Run main only if this script is executed directly
if __name__ == '__main__':
    main()
