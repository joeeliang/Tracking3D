import cv2
import numpy as np
import pickle
import time

# Create and initialize the color histogram
hist = None
roi = None

def load_histogram(filename='histogram.pkl'):
    with open(filename, 'rb') as file:
        hist = pickle.load(file)
    print(f"Histogram loaded from {filename}")
    return hist

hist_queue = [load_histogram()]

def update_histogram(new_hist):
    hist_queue.append(new_hist)
    if len(hist_queue) > 10:  # Keep a maximum of 10 histograms in the queue
        hist_queue.pop(0)
    
    weights = [1 / (i + 1) for i in range(len(hist_queue))]  # Assign weights to each histogram
    total = sum(weights)
    normalized_weights = [weight / total for weight in weights]
    weighted_avg_hist = np.zeros_like(new_hist)

    for i, hist in enumerate(hist_queue):
        weighted_avg_hist += hist * normalized_weights[i]
        print("Added")
    
    return weighted_avg_hist

for i in range(300):
    update_histogram(load_histogram())