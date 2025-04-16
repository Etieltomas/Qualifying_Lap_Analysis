# Qualifying Lap Analysis Tool

This project provides a **Qualifying Lap Analysis Tool** to compare the telemetry data of the fastest qualifying laps of two Formula 1 drivers. Using the FastF1 library and Matplotlib, this tool enables in-depth performance analysis, including speed and throttle comparisons, to better understand driver performance.

## Features
- **Telemetry Comparison**: Compare speed and throttle data between two drivers for their fastest laps.
- **Dynamic Circuit Corner Visualization**: Overlay corner locations on telemetry graphs for enhanced context.
- **Interactive Race Selection**: Select the race year and event name for analysis.
- **Caching for Speed**: Utilizes FastF1's caching system to improve performance by reducing data retrieval time.

## Technologies Used
- **FastF1**: For fetching and processing Formula 1 telemetry and event data.
- **Matplotlib**: For visualizing speed and throttle comparisons graphically.
- **Python**: Backend scripting for telemetry processing and visualization.

## Usage
1. Clone the repository and ensure Python 3.x is installed.
2. Install dependencies using:
   ```bash
   pip install fastf1 matplotlib
3. Run the script:
   ```bash
   python3 main.py

4. Enter the race year, select a race from the schedule, and specify the drivers for analysis.
5. View the comparison plots for speed and throttle with circuit corners annotated.
