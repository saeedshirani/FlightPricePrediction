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
        self.user_input = []


        # Create labels and entry fields for each input


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
        source_city = self.source_city.get()
        destination_city = self.destination_city.get()
        flight_class = self.flight_class.get()
        stops = self.stops_count.get()

        
        self.user_input = [source_city, destination_city, flight_class, stops]
        messagebox.showinfo("Success", f"Registration successful!\n {source_city}, {destination_city}, {flight_class}, {stops}")
        self.root.quit()

        
    def run(self):
        self.root.mainloop()
        return self.user_input
    
        

class Data:

    def __init__(self, user_selection) -> None:
        self.data_path = './Data/Clean_Dataset.csv'
        self.data = pd.read_csv(self.data_path)
        self.user_selection = user_selection
        self.filtered_data = []
    
    def filter_data(self):
        
        source_city, destination_city, flight_class, stops = self.user_selection

        # Placeholder for actual data filtering logic
        self.filtered_data = self.data.loc[
            (self.data['source_city'] == source_city) &
            (self.data['destination_city'] == destination_city) & 
            (self.data['class'] == flight_class) &
            (self.data['stops'] == stops)]
        
        return self.filtered_data
    


class Report():
    def __init__(self, selected_data) -> None:
        self.filtered_data = selected_data

        self.conditional_dict = {}
        self.stat_dict = {}
        

    def reporter(self):
        

        self.unique_airlines = pd.unique(self.filtered_data['airline'])

        
        for single_airline in self.unique_airlines:
            self.stat_dict[single_airline] = {
                                              'mean' : round(self.filtered_data.loc[self.filtered_data['airline'] == single_airline]['price'].mean(),2),
                                              'mode' : round(self.filtered_data.loc[self.filtered_data['airline'] == single_airline]['price'].mode()[0],2),
                                              'median': round(self.filtered_data.loc[self.filtered_data['airline'] == single_airline]['price'].median(),2)
                                                }
            
        

        for airliner in self.stat_dict:


            if self.stat_dict[airliner]['mean'] > self.stat_dict[airliner]['median']:
                self.conditional_dict[airliner] = (self.stat_dict[airliner]['median'], self.stat_dict[airliner]['mean'] )

            elif  self.stat_dict[airliner]['mean'] < self.stat_dict[airliner]['median']:
                self.conditional_dict[airliner] = (self.stat_dict[airliner]['mean'], self.stat_dict[airliner]['median'] )

            else:
                self.conditional_dict[airliner] = (self.stat_dict[airliner]['mode'], self.stat_dict[airliner]['median'] )
        


form = Form().run()
data = Data(form).filter_data()
report = Report(data)
update = report.reporter()
print(report, report.conditional_dict, report.stat_dict)
""")
form = Form().register()
print(form)
print(form.user_input)
data = Data(form.user_input)
report = Report(data.filtered_data)
print(report.conditional_dict)
print(report.stat_dict)
"""

