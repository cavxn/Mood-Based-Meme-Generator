Mood-Based Meme Generator

A real-time meme generator that uses facial expressions to detect the user's mood and generate a matching meme with a relevant caption — powered by deep learning and OpenAI's GPT.

---

Features

- 🎭 Real-time facial emotion recognition using webcam  
- 🧠 Custom-trained deep learning model (ResNet50 + CBAM)  
- 🗨️ Auto-generated meme captions using OpenAI GPT  
- 🖼️ Meme templates with emotion-specific punchlines  
- 🌈 Clean UI, lightweight performance, and extendable design  

---

Emotion Detection Model

- **Input**: 48x48 grayscale facial images (live webcam frames)  
- **Architecture**: ResNet50 + CBAM (Convolutional Block Attention Module)`  
- **Trained on**: FER-2013 + custom-augmented dataset  
- **Output**: 7 emotions — Happy`, `Sad`, `Angry`, `Surprise`, `Neutral`, `Disgust`, `Fear`  

---

Meme Captioning

- Uses **OpenAI's GPT model** via API  
- Emotion → Meme Caption → Overlayed on meme image  
- Custom templates for each emotion  

---

Tech Stack

| Component         | Technology          |
|------------------|---------------------|
| Emotion Detection| TensorFlow / Keras  |
| Attention Module | CBAM                |
| Face Detection   | MediaPipe / MTCNN   |
| Backend Logic    | Python (OpenCV, NumPy) |
| Captioning       | OpenAI GPT API      |
| UI/Display       | OpenCV GUI or Streamlit (optional) |

---

 Project Structure

bash
Mood-Based-Meme-Generator/
├── emotion_model_cbam.keras      # [⚠️ Excluded from GitHub]
├── label_map.pkl
├── meme_templates/               # Meme images per emotion
├── images/
│   └── preprocessed_data/        # [⚠️ Not pushed to GitHub]
├── app.py                        # Main app logic
├── detect_emotion.py             # Webcam-based emotion detector
├── generate_meme.py              # Meme + caption generator
├── download_assets.py            # Optional downloader for large files
├── requirements.txt
└── README.md

Installation
1. Clone the repo
bash
git clone https://github.com/cavxn/Mood-Based-Meme-Generator.git
cd Mood-Based-Meme-Generator

3. Set up the environment
bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

5. Add API key (for OpenAI)
Create a .env file:
env
OPENAI_API_KEY=your-api-key-here
Or directly set it using os.environ in Python.

⚠Large Files Notice
Some files are not included in this repo due to GitHub's 100MB file size limit:

emotion_model_cbam.keras (282 MB)
X_train.npy, preprocessed_data.npz, etc.

📌 TODO
 Add Streamlit interface

 Auto-crop faces for accuracy

 Support batch meme generation

 Add voice-based captioning (optional)

Contributing
Pull requests are welcome! If you have better meme ideas or models — let’s collaborate.

License
MIT License. See LICENSE.

Acknowledgements
FER-2013 Dataset
OpenAI GPT
CBAM Paper
Meme Template Sources
