import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import os
import tensorflow as tf
from tensorflow.keras.utils import load_img


emotion_df = pd.read_csv('project/Dataset/icml_face_data.csv')
print("show first 5 row of data: \n", emotion_df.head(5))
emotion_labels = {0: 'Angry', 1: 'Digust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

def check_balance(emotion_df):
    
    counts = emotion_df['emotion'].value_counts(sort=False).reset_index()
    counts.columns = ['emotion', 'number']
    counts['emotion'] = counts['emotion'].map(emotion_labels)
    print("emotion balance:\n", counts)
    
    # Plotting a bar graph of the class distributions
    plt.figure(figsize=(6,4))
    sns.barplot(counts.emotion, counts.number)
    plt.title('Class distribution')
    plt.ylabel('Number', fontsize=12)
    plt.xlabel('Emotions', fontsize=12)
    plt.show()
    return emotion_labels

def row2image(row):
    pixels, emotion = row['pixels'], emotion_labels[row['emotion']]
    img = np.array(pixels.split())
    img = img.reshape(48,48)
    image = np.zeros((48,48,3))
    image[:,:,0] = img
    image[:,:,1] = img
    image[:,:,2] = img
    return np.array([image.astype(np.uint8), emotion])

def show_image():
    plt.figure(0, figsize=(16,10))
    for i in range(1,8):
        face = emotion_df[emotion_df['emotion'] == i-1].iloc[0]
        img = row2image(face)
        plt.subplot(2,4,i)
        plt.imshow(img[0])
        plt.title(img[1])
    plt.show()  
    
def show_emotion_category():
    plt.figure(figsize=(14,22))
    i = 1
    train_dir = 'project/Dataset/test_train_val/train/'
    for expression in os.listdir(train_dir):
        img = load_img((train_dir + expression +'/'+ os.listdir(train_dir + expression)[1]))
        plt.subplot(1,7,i)
        plt.imshow(img)
        plt.title(expression)
        plt.axis('off')
        i += 1
    plt.show()
  
if __name__ == "__main__":
    #check_balance(emotion_df)
    show_emotion_category()
    # show_image()
