# test_generate.py
from generate_meme import get_meme_caption

emotions = ["happy", "sad", "angry", "surprised", "fear", "neutral"]

for emotion in emotions:
    caption = get_meme_caption(emotion)
    print(f"{emotion.capitalize()} 🤖: {caption}")
