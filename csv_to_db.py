import csv

# function which removed all non unicode characters
def convert(filename):
    with open('data/listings_out.csv', "wb") as outfile:
        with open('data/listings.csv') as infile:
            txt = infile.read()
            
            txt = txt.decode('utf-8','ignore').encode("utf-8")
            outfile.write(txt)

if __name__ == '__main__':
    convert('data/listings.csv')