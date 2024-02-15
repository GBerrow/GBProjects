"""
This script creates a graphical user interface (GUI) for calculating the distance between two addresses.
It allows users to input home and target addresses, select the desired unit of measurement for the distance calculation
and then displays the calculated distance. The GUI provides a more user-friendly way to interact with the functionality
previously available only through the command line.
"""

import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from enum import Enum


class DistanceUnit(Enum):
    KILOMETERS = 'kilometers'
    MILES = 'miles'
    METRES = 'meters'
    YARDS = 'yards'
    FEET = 'feet'


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude

    @staticmethod
    def get_coordinates(address: str) -> 'Coordinates | None':
        geolocator = Nominatim(user_agent='distance_calculator')
        location = geolocator.geocode(address)

        if location:
            return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance(home: Coordinates, target: Coordinates, unit: DistanceUnit = DistanceUnit.KILOMETERS) -> float | None:
    if home and target:
        if unit == DistanceUnit.KILOMETERS:
            return geodesic(home.coordinates(), target.coordinates()).kilometers
        elif unit == DistanceUnit.MILES:
            return geodesic(home.coordinates(), target.coordinates()).miles
        elif unit == DistanceUnit.METRES:
            return geodesic(home.coordinates(), target.coordinates()).meters
        elif unit == DistanceUnit.YARDS:
            return geodesic(home.coordinates(), target.coordinates()).yards
        elif unit == DistanceUnit.FEET:
            return geodesic(home.coordinates(), target.coordinates()).feet
    return None


def calculate_distance_and_update_label():
    home_address = home_entry.get()
    target_address = target_entry.get()
    unit = DistanceUnit(unit_combobox.get())

    home_coordinates = Coordinates.get_coordinates(home_address)
    target_coordinates = Coordinates.get_coordinates(target_address)

    if home_coordinates and target_coordinates:
        distance = calculate_distance(home_coordinates, target_coordinates, unit)
        if distance is not None:
            result_label.config(text=f'{home_address} -> {target_address}\n{distance:.2f} {unit.value}')
            return

    result_label.config(text='Failed to calculate the distance.')

root = tk.Tk()
root.title("Distance Calculator")

home_label = tk.Label(root, text="Home Address:")
home_label.grid(row=0, column=0, sticky='w')
home_entry = tk.Entry(root)
home_entry.grid(row=0, column=1)

target_label = tk.Label(root, text="Target Address:")
target_label.grid(row=1, column=0, sticky='w')
target_entry = tk.Entry(root)
target_entry.grid(row=1, column=1)

unit_label = tk.Label(root, text="Distance Unit:")
unit_label.grid(row=2, column=0, sticky='w')
unit_combobox = ttk.Combobox(root, values=[unit.value for unit in DistanceUnit])
unit_combobox.grid(row=2, column=1)
unit_combobox.current(0)

calculate_button = tk.Button(root, text="Calculate", command=calculate_distance_and_update_label)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()



