import os
import csv
import pandas as pd

class CSVWriter():

    filename = None
    fp = None
    writer = None

    def __init__(self):
        self.filename = 'Company.csv'
        

        if os.path.isfile(self.filename):
            print("file exist at this time")
            self.fp = open(self.filename, 'a+', encoding='utf8')
            self.writer = csv.writer(self.fp, delimiter=',', lineterminator='\n')
        else:
            print("file not exists at this time")
            self.fp = open(self.filename, 'a+', encoding='utf8')
            self.writer = csv.writer(self.fp, delimiter=',', lineterminator='\n')
            self.writer.writerow(['Company_id','Name','Address','Countory','State','Pincode','Phone_No','Mobile_No','FAX_No','Email_ID','Website','Financial_Year_Date','Booking_Date'])

    def close(self):
        self.fp.close()

    def write(self, elems, len_data):
        for i in range(len_data):
            self.writer.writerow(elems[i])

        df = pd.read_csv(self.filename)
        df = df.dropna(how='any')       
        df.dropna(how='any', inplace=True)
        

    def size(self):
        return os.path.getsize(self.filename)

    def fname(self):
        return self.filename
