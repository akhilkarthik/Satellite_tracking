# Satellite_tracking


# Real time Satellite location tracking


- This Python script utilizes the gmplot library to track and visualize the path of a satellite on a Google Map.
- The script also adds a marker to represent the observer's location on the map.

#### Requirements
- Python 3.x
- gmplot library (pip install gmplot)
- ephem library (pip install ephem)



- Satellite Name: IRNSS 1I

- After running the code we can check with the location given in the website 

![image](https://github.com/akhilkarthik/Satellite_tracking/assets/40953068/8217bbb6-b34a-45eb-8944-1767987db352)

Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/satellite-tracker.git
Navigate to the Project Directory:

bash
Copy code
cd satellite-tracker
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Script:

bash
Copy code
python satellite_tracker.py
Update the TLE set for the satellite with the latest data for accurate tracking.
Open the HTML Map:

The script will generate an HTML file named satellite_path_{satellite_name}.html.
Open this HTML file in a web browser to view the satellite's path on Google Maps.


Script Explanation
The script defines a function track_and_plot_satellite_on_map_with_marker that takes the satellite name, observer's location, and tracking duration as parameters.
The observer's location is configured using the ephem.Observer object.
The script then loops for the specified duration, tracking the satellite's position and adding the coordinates to lists.
The gmplot library is used to plot the satellite's path on a Google Map.
A marker in red is added to the observer's location.
The resulting map is saved as an HTML file.

Example Usage
python
Copy code
track_and_plot_satellite_on_map_with_marker("IRNSS 1I", (52.3, 1.5), 5)
This example tracks the satellite "IRNSS 1I" for 5 hours from the observer's location at latitude 52.3 and longitude 1.5.

Note
Ensure you have the required libraries installed (gmplot and ephem).
Update the TLE set for the satellite with the latest data for accurate tracking.
