import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox

class Form:
    """
    Getting information of Flight from user, this Information will be using to filter the data and do the predictions.
    """
    def __init__(self):
        self.root = Tk()
        self.root.title("Registration Form")
        self.root.geometry('300x300')

        # Create labels and entry fields for each input
        self.airline_label = Label(self.root, text="Select Your Prefer Airline (SpiceJet, AirAsia , Vistara, GO_FIRST, Indigo, Air_India) :")
        self.airline_label.pack()
        self.airline_entry = Entry(self.root)
        self.airline_entry.pack()

        self.source_city_label = Label(self.root, text="Enter Your Source City ('Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'): ")
        self.source_city_label.pack()
        self.source_city_entry = Entry(self.root)
        self.source_city_entry.pack()

        self.destination_city_label = Label(self.root, text="Enter Your Destination (Mumbai, Bangalore, Kolkata, Hyderabad, Chennai, Delhi):")
        self.destination_city_label.pack()
        self.destination_city_entry = Entry(self.root)
        self.destination_city_entry.pack()

        self.flight_class_label = Label(self.root, text="Choose your prefer flight class ('Economy', 'Business') :")
        self.flight_class_label.pack()
        self.flight_class_entry = Entry(self.root)
        self.flight_class_entry.pack()

        self.stops_label = Label(self.root, text="Enter Number of Stops ('zero', 'one', 'two_or_more'): ")
        self.stops_label.pack()
        self.stops_entry = Entry(self.root)
        self.stops_entry.pack()

        self.register_button = Button(self.root, text="Register", command=self.register)
        self.register_button.pack()

    def register(self):
        # Get the user input from the form
        airline = self.airline_entry.get()
        source_city = self.source_city_entry.get()
        destination_city = self.destination_city_entry.get()
        flight_class = self.flight_class_entry.get()
        stops = self.stops_entry.get()

        # For now, we will just print the collected data to the console
        print(f"Airline: {airline}")
        print(f"Source City: {source_city}")
        print(f"Destination City: {destination_city}")
        print(f"Flight Class: {flight_class}")
        print(f"Stops: {stops}")

        messagebox.showinfo("Success", "Registration successful!")
        return [airline, source_city, destination_city, flight_class, stops]

    def run(self):
        self.root.mainloop()





class Data:

    def __init__(self) -> None:
        self.data_path = './Data/Clean_Dataset.csv'
        self.data = pd.read_csv(self.data_path)
    
    def filter_data(self, selection_list):
        airline = 0 
        sourse_city = 0 
        destination_city = 0 
        flight_class = 0
        stops = 0

        data = 



# Create an instance of the form and run the GUI
form = Form()
form.run()
