import cv2
import numpy as np
import mtcnn
from architecture import *
from scipy.spatial.distance import cosine
from keras.models import load_model
import pickle
import csv
import os
import random
from datetime import datetime
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Constants and paths
face_data = 'Dataset'
required_shape = (160, 160)
path = "facenet_keras_weights.h5"
confidence_t = 0.99
recognition_t = 0.5

# Function to normalize an image
def normalize(img):
    mean, std = img.mean(), img.std()
    return (img - mean) / std

l2_normalizer = Normalizer('l2')
# Function to train the face recognition model
def train_face_recognition():
    # Load FaceNet model weights
    face_encoder = InceptionResNetV2()
    face_encoder.load_weights(path)
    face_detector = mtcnn.MTCNN()
    encodes = []
    labels = []
    encoding_dict = {}

    # Process the dataset
    for idx, face_names in enumerate(os.listdir(face_data)):
        person_dir = os.path.join(face_data, face_names)

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)

            img_BGR = cv2.imread(image_path)
            img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

            x = face_detector.detect_faces(img_RGB)
            if x:
                x1, y1, width, height = x[0]['box']
                x1, y1 = abs(x1), abs(y1)
                x2, y2 = x1 + width, y1 + height
                face = img_RGB[y1:y2, x1:x2]

                face = normalize(face)
                face = cv2.resize(face, required_shape)
                face_d = np.expand_dims(face, axis=0)
                encode = face_encoder.predict(face_d)[0]
                encodes.append(encode)
                labels.append(idx)

                encoding_dict[face_names] = encoding_dict.get(face_names, []) + [encode]

    # Split the data into training and testing sets
    encodes, labels = shuffle(encodes, labels, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(encodes, labels, test_size=0.2, random_state=42)

    # Train a classifier on top of the embeddings
    classifier = SVC(kernel='linear', probability=True)

    # Lists to store training history
    num_epochs = 100
    history_loss = []
    history_accuracy = []

    # Training loop
    for epoch in range(num_epochs):
        classifier.fit(X_train, y_train)

        # Calculate accuracy on the test set
        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        history_accuracy.append(accuracy)

        print(f"Epoch {epoch + 1}/{num_epochs}: Accuracy = {accuracy * 100:.2f}%")

    # Plot training history
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history_accuracy)
    plt.title("Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")

    if len(history_loss) > 0:
        plt.subplot(1, 2, 2)
        plt.plot(history_loss)
        plt.title("Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")

    plt.tight_layout()
    plt.savefig("Training History")
    plt.show()

    plt.figure(figsize=(10, 6))
    # Generate a list of random colors for each dataset
    colors = [random.choice(['red', 'green', 'blue', 'yellow', 'purple']) for _ in range(len(encodes))]
    plt.hist(encodes, bins=50, color=colors, alpha=0.7)
    plt.title("Face Encodings Histogram")
    plt.xlabel("Encoding Values")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("Encoding Histogram")
    plt.show()

    # Save the classifier and encoding dictionary
    classifier_path = 'classifier/classifier.pkl'
    encoding_dict_path = 'encodings/encodings.pkl'

    with open(classifier_path, 'wb') as file:
        pickle.dump(classifier, file)

    with open(encoding_dict_path, 'wb') as file:
        pickle.dump(encoding_dict, file)

if __name__ == "__main__":
    train_face_recognition()
