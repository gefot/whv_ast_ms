"""
Scripts for testing the get_recordings function
"""
from modules import functions

# Main

record_list = functions.get_recordings("20190522")

for record in record_list:
    print(record)

