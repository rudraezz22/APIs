import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC

dataset_path = "ravdess_data"

emotion_map = {
    "01": "neutral", "02": "calm", "03": "happy", "04": "sad",
    "05": "angry", "06": "fearful", "07": "disgust", "08": "surprised"
}

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=2.5, offset=0.6)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

x = []
y = []

for file in os.listdir(dataset_path):
    if file.endswith(".wav"):
        parts = file.split("-")
        if len(parts) < 3:
            print("Skipping bad file name")
            continue
        emotion_code = parts[2]
        emotion = emotion_map.get(emotion_code)
        if emotion is None:
            print("Unknown emotion")
            continue
        try:
            file_path = os.path.join(dataset_path, file)
            features = extract_features(file_path)
            x.append(features)
            y.append(emotion)
        except Exception as e:
            print(e)

if len(x) == 0:
    print("No audio files found")
    exit()
elif len(x) < 2:
    print(f"Only {len(x)} files — skipping train/test split")
    x_train, x_test, y_train, y_test = x, x, y, y
else:
    x = np.array(x)
    y = np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(classification_report(y_test, y_pred))
