import ephem
import matplotlib.pyplot as plt
from datetime import datetime

# Define a function to track a satellite's position
def track_satellite(satellite_name, observer_location, duration_hours):

    observer = ephem.Observer()
    observer.lon, observer.lat = observer_location # Set your observer's longitude and latitude
    observer.date = datetime.utcnow()  # Set the observer's date and time

    for _ in range(duration_hours):
        satellite = ephem.readtle(
            satellite_name,
            "1 25544U 98067A   23301.52764947  .00019202  00000+0  34666-3 0  9994",
            "2 25544  51.6435  28.0714 0001006 114.0425 254.5243 15.49747991422472",
        )

        satellite.compute(observer)  # Pass the observer location to the compute() method

        print(f"Satellite: {satellite_name} - Altitude: {satellite.alt}, Azimuth: {satellite.az}")

# track_satellite("ISS (ZARYA)", ("1.5", "52.3"), 5)  # Track the ISS for 5 hours

def track_and_plot_satellite(satellite_name, observer_location, duration_hours):
    observer = ephem.Observer()
    observer.lon, observer.lat = observer_location
    observer.date = datetime.utcnow()

    altitudes = []
    azimuths = []
    for _ in range(duration_hours):
        satellite = ephem.readtle(
            satellite_name,
            "1 25544U 98067A   23301.52764947  .00019202  00000+0  34666-3 0  9994",
            "2 25544  51.6435  28.0714 0001006 114.0425 254.5243 15.49747991422472",
        )
        satellite.compute(observer)
        altitudes.append(satellite.alt)
        azimuths.append(satellite.az)
        observer.date += ephem.hour

    plt.figure(figsize=(10, 5))
    plt.plot(azimuths, altitudes)
    plt.title(f"Satellite Path - {satellite_name}")
    plt.xlabel("Azimuth (degrees)")
    plt.ylabel("Altitude (degrees)")
    plt.grid(True)
    plt.show()


#track_and_plot_satellite("ISS (ZARYA)", ("1.5", "52.3"), 5)

from gmplot import gmplot
import ephem
from datetime import datetime, timezone

def track_and_plot_satellite(satellite_name, observer_location, duration_hours):
    observer = ephem.Observer()
    observer.lon, observer.lat = observer_location
    observer.date = datetime.now(timezone.utc)  # Set the observer's date and time

    lats = []
    longs = []

    for _ in range(duration_hours):
        satellite = ephem.readtle(
            satellite_name,
            "1 25544U 98067A   23301.52764947  .00019202  00000+0  34666-3 0  9994",
            "2 25544  51.6435  28.0714 0001006 114.0425 254.5243 15.49747991422472",
        )

        satellite.compute(observer)  # Pass the observer location to the compute() method

        lat = satellite.sublat * 180 / 3.14159265358979323846  # Convert to degrees
        lon = satellite.sublong * 180 / 3.14159265358979323846  # Convert to degrees

        lats.append(lat)
        longs.append(lon)

        observer.date += ephem.hour  # Increment the observer's date by one hour

    # Create a gmplot object centered on the observer's location
    gmap = gmplot.GoogleMapPlotter(observer.lat, observer.lon, 5)

    # Plot the satellite's path
    gmap.plot(lats, longs, 'cornflowerblue', edge_width=2)

    # Draw the map to an HTML file
    gmap.draw(f"satellite_path_{satellite_name}.html")

# Example usage
track_and_plot_satellite("ISS (ZARYA)", (52.3, 1.5), 5)
