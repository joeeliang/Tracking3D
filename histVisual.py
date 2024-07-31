import cv2
import matplotlib.pyplot as plt
import numpy as np
import pickle

class HistogramVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 2, figsize=(12, 6))
        self.ax[0].set_title('Hue-Saturation Histogram')
        self.ax[0].set_xlabel('Hue (degrees)')
        self.ax[0].set_ylabel('Saturation')
        self.ax[1].set_title('Color Map')
        self.ax[1].set_xlabel('Hue (degrees)')
        self.ax[1].set_ylabel('Saturation')
        self.threshold = 0.05

    def load_histogram(self, filename='histogram.pkl'):
        with open(filename, 'rb') as file:
            hist = pickle.load(file)
        print(f"Histogram loaded from {filename}")
        return hist

    def visualize_histogram(self, hist):
        self.ax[0].cla()
        self.ax[1].cla()
        mask = hist > self.threshold
        color_map = np.zeros((hist.shape[0], hist.shape[1], 3), np.uint8)
        for i in range(hist.shape[0]):
            for j in range(hist.shape[1]):
                if mask[i, j]:
                    color_map[i, j, 0] = i  # Hue
                    color_map[i, j, 1] = j  # Saturation
                    color_map[i, j, 2] = 255  # Value (maximum brightness)
                else:
                    color_map[i, j, :] = 0  # Set to black if below threshold
        color_map = cv2.cvtColor(color_map, cv2.COLOR_HSV2RGB)
        self.ax[0].imshow(hist, aspect='auto', cmap='viridis', vmin=0, vmax=1)
        self.ax[1].imshow(color_map)
        plt.draw()
        plt.pause(0.01)

    def animate(self, hist, isFile=False):
        if isFile:
            hist = self.load_histogram(hist)
        self.visualize_histogram(hist)

if __name__ == "__main__":
# Create a HistogramVisualizer object
    visualizer = HistogramVisualizer()

    # Load and visualize the first histogram
    visualizer.animate('orange.pkl', True)

    # Continue animating as you make new histograms
    while True:
        filename = input("Enter the filename of the next histogram (or 'quit' to exit): ")
        if filename.lower() == 'quit':
            break
        visualizer.animate(filename)