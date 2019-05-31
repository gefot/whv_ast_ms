"""
Scripts for testing the get_recordings function
"""
from modules import functions

# Main

record_list = functions.get_recordings("20190530")

for record in record_list:
    print(record)
    # print(record.path+record.filename)
    print(functions.get_wav_duration(record.path+record.filename))

