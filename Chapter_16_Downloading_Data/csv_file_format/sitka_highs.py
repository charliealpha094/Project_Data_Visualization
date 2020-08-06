#Done by Carlos Amaral (22/07/2020)


import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:   #Open the file and assign resulting file object to f.
    reader = csv.reader(f)  #Call csv reader() and pass it the file obj. to create a reader object with the file.
    header_row = next (reader) #next() return the next line in the file when passed the reader object. 
    print(header_row)


#Printing the headers and their positions.
    for index, column_header  in enumerate(header_row):
        print(index, column_header)

        