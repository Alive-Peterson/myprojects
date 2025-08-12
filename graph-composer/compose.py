import os
import string
import random
from graph import Graph, Vertex

def get_words_from_text(filename):
    # Get the absolute path to the texts folder next to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(script_dir, "texts", filename)

    print("DEBUG: Looking for file at:", text_path)

    if not os.path.exists(text_path):
        raise FileNotFoundError(f"File not found at: {text_path}")

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
        text = ' '.join(text.split())  # normalize spaces
        text = text.lower()  # lowercase for uniformity
        text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation

    return text.split()

def make_graph(words):
    g = Graph()
    previous_word = None
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))  # pick random start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main():
    # Use only the filename here — folder is handled in get_words_from_text()
    words = get_words_from_text('hp_sorcerer_stone.txt')
    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))

if __name__ == '__main__':
    main()
