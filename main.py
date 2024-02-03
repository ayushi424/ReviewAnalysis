import pandas as pd 
from ydata_profiling import ProfileReport

#loading reviews data
with open('customer_booking.csv', 'r', encoding='utf-8', errors='replace') as file:
    data = pd.read_csv(file)

#generating report
profile=ProfileReport(data)
profile.to_file(output_file="booking.html")