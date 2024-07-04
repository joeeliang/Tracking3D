import matplotlib.pyplot as plt
import numpy as np

# Simulate a stream of (x, y) data
def generate_data_stream():
    while True:
        x = np.random.rand()
        y = np.random.rand()
        yield (x, y)

data_stream = generate_data_stream()

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
scatter = ax.scatter([], [], c='b')  # 'b' stands for blue color
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Function to update the plot
def update_plot(x, y):
    scatter.set_offsets(np.array([[x, y]]))
    plt.draw()  # Update plot

plt.ioff()  # Turn off interactive mode
plt.show()

# Main loop to read data from the stream and update the plot
for _ in range(100):  # Limit to 100 points for this example
    x, y = next(data_stream)
    update_plot(x, y)
