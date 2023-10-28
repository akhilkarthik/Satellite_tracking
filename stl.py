from gmplot import gmplot
import ephem
from datetime import datetime, timezone

def track_and_plot_satellite_on_map_with_marker(satellite_name, observer_location, duration_hours):
    observer = ephem.Observer()
    observer.lon, observer.lat = observer_location
    observer.date = datetime.now(timezone.utc)  # Set the observer's date and time

    lats = []
    longs = []

    for _ in range(duration_hours):
        satellite = ephem.readtle(
            satellite_name,
            "1 43286U 18035A   23301.04215991  .00000109  00000-0  00000+0 0  9999",
            "2 43286  29.3770  89.3358 0021386 176.4450 200.6588  1.00267956 20418",
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

    # Add a marker at the observer's location
    gmap.marker(observer.lat, observer.lon, 'red')  # we can customize the marker color and style

    # Draw the map to an HTML file
    gmap.draw(f"satellite_path_{satellite_name}.html")

# Example usage
track_and_plot_satellite_on_map_with_marker("IRNSS 1I", (52.3, 1.5), 5)
