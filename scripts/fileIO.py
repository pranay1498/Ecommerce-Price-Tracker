#functions for reading and writing to the files
import csv

filename = 'info.csv'
def fileRead():
    info = {}
    with open(filename, "r") as fo:
        csv_reader = csv.DictReader(fo)
        for line in csv_reader:
            info = line.copy()
        fo.close()
    return info


def fileWrite(website, link, price, mail, time):
    with open(filename, "w") as fo:
        csv_writer = csv.DictWriter(fo, fieldnames={'website', 'link', 'price', 'mail', 'time'})
        csv_writer.writeheader()
        csv_writer.writerow({'website': website, 'link': link, 'price': price, 'mail': mail, 'time': time})
        fo.close()
