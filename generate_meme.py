# generate_meme.py

import os
import random
import json
import cv2
from datetime import datetime

def generate_meme(emotion, meme_dir="meme_templates", caption_file="captions.json"):
    # Load captions
    with open(caption_file, "r") as f:
        captions = json.load(f)

    # Pick meme template
    emotion_dir = os.path.join(meme_dir, emotion)
    if not os.path.exists(emotion_dir):
        print(f"No memes found for emotion: {emotion}")
        return

    meme_files = os.listdir(emotion_dir)
    if not meme_files:
        print(f"No images in {emotion_dir}")
        return

    meme_path = os.path.join(emotion_dir, random.choice(meme_files))
    meme = cv2.imread(meme_path)
    if meme is None:
        print("Error loading meme image")
        return

    caption = random.choice(captions.get(emotion, ["Just vibes."]))

    # Add caption
    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1
    thickness = 2
    text_size = cv2.getTextSize(caption, font, font_scale, thickness)[0]
    text_x = (meme.shape[1] - text_size[0]) // 2
    text_y = meme.shape[0] - 30

    cv2.putText(meme, caption, (text_x, text_y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    # Show + save
    filename = f"generated_meme_{emotion}_{datetime.now().strftime('%H%M%S')}.jpg"
    cv2.imwrite(filename, meme)
    cv2.imshow("Generated Meme", meme)
    cv2.waitKey(0)
    cv2.destroyWindow("Generated Meme")
