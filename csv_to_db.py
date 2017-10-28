
import logging
import io


import csv

def add_data(filename):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if row[28] != 'f' and row[28] != 't':
                print (row)

def convert(filename):
    with open('data/listings_out.csv', "wb") as outfile:
        with open('data/listings.csv') as infile:
            txt = infile.read()
            
            txt = txt.decode('utf-8','ignore').encode("utf-8")
            outfile.write(txt)

if __name__ == '__main__':
    #add_data('data/listings2.csv')
    convert('data/listings.csv')