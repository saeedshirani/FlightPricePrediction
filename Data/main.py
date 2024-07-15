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
        self.root.geometry('500x300')

        # Create labels and entry fields for each input

        self.airline_clicked = StringVar()
        self.airline_clicked.set("Select an Airline")
        self.airline_label = OptionMenu(self.root, self.airline_clicked, 'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India')
        self.airline_label.pack()


        self.source_city = StringVar()
        self.source_city.set("Select the source city")
        self.source_city_label = OptionMenu(self.root, self.source_city, 'Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore', 'Hyderabad')
        self.source_city_label.pack()


        self.destination_city = StringVar()
        self.destination_city.set("Select the destination city")
        self.destination_city_label = OptionMenu(self.root, self.destination_city, 'Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore', 'Hyderabad')
        self.destination_city_label.pack()


        self.flight_class = StringVar()
        self.flight_class.set("Select the flight class")
        self.flight_class_label = OptionMenu(self.root, self.flight_class, 'Economy', 'Business')
        self.flight_class_label.pack()

        self.stops_count = StringVar()
        self.stops_count.set("Select the stops count")
        self.stops_count_label = OptionMenu(self.root, self.stops_count, 'zero', 'one', 'two_or_more')
        self.stops_count_label.pack()

        self.submit_button = Button(self.root, text="Submit", command=self.register)
        self.submit_button.pack()

    def register(self):
        # Get the user input from the form
        airline = self.airline_clicked.get()
        source_city = self.source_city.get()
        destination_city = self.destination_city.get()
        flight_class = self.flight_class.get()
        stops = self.stops_count.get()

        messagebox.showinfo("Success", f"Registration successful!\n{airline}, {source_city}, {destination_city}, {flight_class}, {stops}")
        self.user_input = [airline, source_city, destination_city, flight_class, stops]
        self.root.quit()
        
    def run(self):
        self.root.mainloop()
        return self.user_input

class Data:

    def __init__(self) -> None:
        self.data_path = './Data/Clean_Dataset.csv'
        self.data = pd.read_csv(self.data_path)
    
    def filter_data(self):
       
        form = Form()
        user_input = form.run()

        
        airline, source_city, destination_city, flight_class, stops = user_input
        print(stops,stops)

        # Placeholder for actual data filtering logic
        self.filtered_data = self.data.loc[
            
            (self.data['airline'] == airline) &
            (self.data['source_city'] == source_city) &
            (self.data['destination_city'] == destination_city) & 
            (self.data['class'] == flight_class) &
            (self.data['stops'] == stops)
            
        ]
        

        return self.filtered_data
    

    def linear_model(self):
        filter_dataset = Data().filter_data()

# Create an instance of the form and run the GUI


data = Data().filter_data()
print(data.head())
