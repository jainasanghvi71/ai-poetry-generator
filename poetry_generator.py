import numpy as np
import random

# Load words
with open("dataset/words.txt", "r") as f:
    words = [w.strip() for w in f.read().split(",")]

# Create random embeddings for words (simulate semantic meaning)
word_vectors = {w: np.random.rand(3) for w in words}

def blend_words(w1, w2, intensity=0.5):
    """Blend two word embeddings to create a poetic combination."""
    v1, v2 = word_vectors[w1], word_vectors[w2]
    mixed_vector = (v1 * intensity + v2 * (1 - intensity))
    closest = min(words, key=lambda w: np.linalg.norm(word_vectors[w] - mixed_vector))
    return closest

def generate_poem():
    lines = []
    for _ in range(4):
        w1, w2 = random.sample(words, 2)
        blended = blend_words(w1, w2, intensity=np.random.rand())
        line = f"{w1} and {w2} make {blended}"
        lines.append(line.capitalize())
    return "\n".join(lines)

if __name__ == "__main__":
    print("✨ AI-Generated Poem ✨\n")
    print(generate_poem())
