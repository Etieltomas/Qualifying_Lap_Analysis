import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

# Enable caching to speed up subsequent accesses
fastf1.Cache.enable_cache('cache')

def get_driver_telemetry(race, driver_name):
    driver_lap = race.laps.pick_drivers(driver_name).pick_fastest().get_telemetry()
    return driver_lap

def plot_telemetry(driver1_lap, driver2_lap, driver1, driver2, corners):
    plt.figure(figsize=(12, 6))

    # Speed Comparison
    plt.subplot(2, 1, 1)
    plt.plot(driver1_lap['Distance'], driver1_lap['Speed'], label=driver1, color='red')
    plt.plot(driver2_lap['Distance'], driver2_lap['Speed'], label=driver2, color='blue')
    max_throttle = max(driver1_lap['Speed'].max(), driver2_lap['Speed'].max())
    plt.vlines(corners['Distance'], ymin=0, ymax=max_throttle+10, label='Corners', color='green')
    plt.title('Speed Comparison (Fastest Lap)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (km/h)')
    plt.legend()
    plt.grid()

    # Throttle Comparison
    plt.subplot(2, 1, 2)
    plt.plot(driver1_lap['Distance'], driver1_lap['Throttle'], label=driver1, color='red')
    plt.plot(driver2_lap['Distance'], driver2_lap['Throttle'], label=driver2, color='blue')
    max_throttle = max(driver1_lap['Throttle'].max(), driver2_lap['Throttle'].max())
    plt.vlines(corners['Distance'], ymin=0, ymax=max_throttle+10, label='Corners', color='green')

    plt.title('Throttle Comparison (Fastest Lap)')
    plt.xlabel('Distance (m)')
    plt.ylabel('Throttle (%)')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

def get_race_name(year):
    races = fastf1.get_event_schedule(year)["Country"].unique()
    race_name = input("Enter the name of the race: ")
    while not (race_name in races):
        race_name = input("Race not found! Please, enter a valid race name: ")
    
    return race_name


def main():
    print("\n-----------------------------\nWelcome to the Qualifying Lap Analysis Tool!")
    print("This tool allows you to compare the telemetry data of the fasted qualifying laps of two drivers.")
    print("You can analyze speed and throttle data to understand their performance better.\n")

    year = int(input("Enter the year of the race: "))
    race_name = get_race_name(year)

    race = fastf1.get_session(year, race_name, 'Qualifying')
    race.load()

    driver1 = input("Enter the first driver's name: ").upper()
    driver2 = input("Enter the second driver's name: ").upper()

    driver1_lap = get_driver_telemetry(race, driver1)
    driver2_lap = get_driver_telemetry(race, driver2)

    corners = race.get_circuit_info().corners

    plot_telemetry(driver1_lap, driver2_lap, driver1, driver2, corners)

if __name__ == "__main__":
    main()
