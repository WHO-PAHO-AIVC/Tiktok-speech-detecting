import csv
import glob

column_names = ['a','b','c'] # or whatever


with open("convert_sample.csv", 'w', newline='') as target:
    writer = csv.DictWriter(target, fieldnames=column_names)
    writer.writeheader() # if you want a header
    for path in glob.glob("C:/Users/david/Desktop/CHI Research Project.text_files/*.txt"):
        with open(path, newline='') as source:
            reader = csv.DictReader(source, delimiter='/', fieldnames=column_names)
            writer.writerows(reader)
        
