import os
import string
import random
import re
from graph import Graph, Vertex

# Reads a song lyric file and returns a list of cleaned words
def get_words_from_song(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

        # Remove content inside brackets like [Chorus], (Verse 1) etc.
        text = re.sub(r'\[.*?\]', ' ', text)
        text = re.sub(r'\(.*?\)', ' ', text)

        # Normalize spaces
        text = ' '.join(text.split())

        # Lowercase for uniformity
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

    return text.split()


# Creates a graph where each word is a vertex and edges show word-to-word connections
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

# Uses the graph to create a random composition of words
def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

# Main function for song lyrics
def main(artist):
    words = []

    # Locate songs folder relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    artist_folder = os.path.join(base_dir, 'songs', artist)

    if not os.path.exists(artist_folder):
        raise FileNotFoundError(f"Artist folder not found: {artist_folder}")

    for song_file in os.listdir(artist_folder):
        if not song_file.lower().endswith('.txt'):
            continue
        song_path = os.path.join(artist_folder, song_file)
        song_words = get_words_from_song(song_path)
        words.extend(song_words)

    if not words:
        raise ValueError(f"No valid text files found in {artist_folder}")

    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)

if __name__ == '__main__':
    print(main('alan_walker'))
