import numpy as np
from scipy.optimize import curve_fit
import time
import csv

def getCoordinates():
    return np.load("center_coords.npy")
    

def parabolic_model(x, a, b, c):
    return a * x**2 + b * x + c

def check_parabolic_path(points):
    # Extract x and y coordinates
    x_coords = np.array([p[0] for p in points])
    z_coords = np.array([p[1] for p in points])
    
    # Fit the parabolic model to the data
    popt, pcov = curve_fit(parabolic_model, x_coords, z_coords)
    
    # Get the fitted values
    y_fit = parabolic_model(x_coords, *popt)
    
    # Calculate R-squared value as goodness of fit measure
    residuals = z_coords - y_fit
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((z_coords - np.mean(z_coords))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    print(f"R-squared: {r_squared}")
    return r_squared  # Assuming a threshold of 0.9 for good fit

streak = 0
maxStreak = 0
streakCord = [0, 0]

def check_section(coordinates,start,end):
    global streak
    global maxStreak
    global streakCord
    #frame_rate = 30  # 30 coordinates per second
    #duration = 2  # Analyze for 2 seconds
    #total_frames = frame_rate * duration
    # for i in range(total_frames):
    #    coordinates.append(getCoordinates())
    #    time.sleep(1 / frame_rate)
    
    if check_parabolic_path(coordinates) > 0.9:
        with open("parabData.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            writer.writerows(coordinates)
            writer.writerow([check_parabolic_path(coordinates)])

#check_section()
def main():
    sectionLength = 20
    bigArray = np.load("center_coords.npy")
    for i in range(len(bigArray)-sectionLength):
        smallSection = bigArray[i: i+sectionLength]
        check_section(smallSection, i, i+sectionLength)
    #print(len(bigArray))

main()
print(np.load("center_coords.npy")[streakCord[0]:streakCord[1]])
dataArray = np.load("center_coords.npy")[streakCord[0]:streakCord[1]]