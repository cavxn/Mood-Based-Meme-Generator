# generate_meme.py (offline version)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

# Prompt template
def get_prompt(emotion):
    return f"Generate a funny meme caption for a person feeling {emotion.lower()}."

# Meme caption generator
def get_meme_caption(emotion):
    prompt = get_prompt(emotion)
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=30, temperature=0.9, do_sample=True)
    caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption
