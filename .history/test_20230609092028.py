import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

class Airline:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Flight(Airline):
    def __init__(self, name, number, departure_city, destination_city, departure_time, arrival_time, price):
        super().__init__(name)
        self.number = number
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price

    def get_number(self):
        return self.number

    def get_departure_city(self):
        return self.departure_city

    def get_destination_city(self):
        return self.destination_city

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_price(self):
        return self.price

class BookingPortal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Airline Booking Portal")
        self.geometry("800x600")

        # Create a frame for the airline selection
        self.airline_frame = tk.Frame(self)
        self.airline_label = tk.Label(self.airline_frame, text="Airline")
        self.airline_combo = tk.Combobox(self.airline_frame, values=["American Airlines", "Delta Airlines", "United Airlines"])
        self.airline_frame.pack()

        # Create a frame for the flight selection
        self.flight_frame = tk.Frame(self)
        self.flight_label = tk.Label(self.flight_frame, text="Flight")
        self.flight_combo = tk.Combobox(self.flight_frame, values=[])
        self.flight_frame.pack()

        # Create a frame for the passenger details
        self.passenger_frame = tk.Frame(self)
        self.passenger_label = tk.Label(self.passenger_frame, text="Passenger Details")
        self.passenger_name_entry = tk.Entry(self.passenger_frame)
        self.passenger_last_name_entry = tk.Entry(self.passenger_frame)
        self.passenger_citizenship_number_entry = tk.Entry(self.passenger_frame)
        self.passenger_frame.pack()

        # Create a frame for the booking button
        self.booking_frame = tk.Frame(self)
        self.booking_button = tk.Button(self.booking_frame, text="Book Flight")
        self.booking_frame.pack()

        # Bind the event handlers
        self.airline_combo.bind("<<ComboboxSelected>>", self.on_airline_selected)
        self.flight_combo.bind("<<ComboboxSelected>>", self.on_flight_selected)
        self.booking_button.config(command=self.on_booking_button_clicked)

        # Initialize the data
        self.airlines = [Airline("American Airlines"), Airline("Delta Airlines"), Airline("United Airlines")]
        self.flights = []

    # This function is called when the airline is selected
    def on_airline_selected(self, event):
        airline = self.airline_combo.get()
        self.flights = [Flight(airline, i, "New York", "Los Angeles", "10:00 AM", "12:00 PM", 100) for i in range(1, 10)]
        self.flight_combo.config(values=self.flights)

    # This function is called when the flight is selected
    def on_flight_selected(self, event):
        flight = self.flight_combo.get()

    # This function is called when
