# 🎶 Markov Chain Composer

A Python project that uses Markov Chains to generate either:

Song lyrics from a text dataset (compose-song.py)

Creative text in the style of a provided sample (compose-text.py)

It builds a graph of word transitions from the input and then generates new sequences based on probability.

## 📌 Overview

This project:

1. Reads a text source (lyrics or other text)

2. Builds a Markov Chain graph using graph.py

3. Generates new text based on the probabilities of word transitions

It’s a fun way to simulate “style” from any given text sample — whether it’s song lyrics, poetry, or any other body of work.

## 🛠 Installation

You only need Python 3 — no extra libraries required.

1. Clone this repository:
```bash
git clone https://github.com/Alive-Peterson/python-projects.git
cd python-projects/markov-composer
```

2. Prepare your text file (e.g., lyrics.txt) and place it in the texts folder.

## 🚀 Usage

### 🎵 Song Lyrics Generator

Generate new “lyrics” using a Markov Chain built from a text sample.
```bash
python compose-song.py
```

It will:

1. Load a lyrics file from texts/

2. Build a word transition graph

3. Print a randomly generated lyric

Sample Output:
```text
I walk this lonely road the only one that I have ever known
Don’t know where it goes but it’s home to me and I walk alone
```

### ✍ Text Generator

Generate any text based on a custom input sample.
```bash
python compose-text.py
```

It will:

1. Load a text file (e.g., sample.txt)

2. Build the Markov Chain graph

3. Print a random generated paragraph

Sample Output:
```text
The wind whispered softly across the fields as the sun dipped behind the horizon.
Shadows stretched long and the air grew still, carrying the scent of earth and rain.
```
## 🧠 How It Works

Graph Creation: graph.py stores each word as a vertex and records all possible next words.

Probability: The more often a word follows another in the text, the higher its selection probability in generation.

Generation: Starting from a random word, the program repeatedly chooses the next word until the sentence is complete.

## 🛠 Customization

Change the input file in the code to experiment with different styles.

Adjust generation length by modifying the loop in compose-song.py or compose-text.py.

You can feed it any text file — song lyrics, poems, novels, speeches.
