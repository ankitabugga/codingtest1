#Write a Python program to read a CSV file and display its contents.

import csv

# Function to read and display the contents of a CSV file
def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# Specify the path to your CSV file
#csv_file_path = r"C:\Users\Acer\Desktop\PY1\anudip data anlytics\testactivity\Book1.csv"
csv_file_path = "C:\\Users\\Acer\\Desktop\\PY1\\anudip data anlytics\\testactivity\\Book1.csv"



# Call the function to read and display the CSV file contents
read_csv(csv_file_path)



#output
"""['ï»¿Product', 'Region', 'Sales Amount', 'Date']
['Product A', 'North', '1200', '01-01-2024']
['Product B', 'South', '1500', '02-01-2024']
['Product C', 'East', '800', '03-01-2024']
['Product D', 'West', '700', '04-01-2024']
['Product A', 'North', '1100', '05-01-2024']
['Product B', 'South', '1400', '06-01-2024']
['Product C', 'East', '900', '07-01-2024']
['Product D', 'West', '850', '08-01-2024']
['Product A', 'North', '1300', '09-01-2024']
['Product B', 'South', '1600', '10-01-2024']"""
