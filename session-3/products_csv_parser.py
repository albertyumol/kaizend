import argparse
import sys
import csv

output_name = input("Name the output file (without the extension) ")

parser = argparse.ArgumentParser(description='Read a file and outputs products with categories')
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()

quotechar='"'
delimiter=","
lineterminator="\n"

fields = {}
rowFields = None
contentRows = []

try:
    f = open(args.filename, newline='')

except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)

else:
    with f as csvfile:
        csvReader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar, lineterminator=lineterminator)
        rowFields = next(csvReader)
        csvReader = list(csvReader)

        for i in range(0, len(rowFields)):
            fields[rowFields[i]] = i
    
        for row in csvReader[:-1]:
            if len(row[fields['Categories']]) != 0:
                contentRows.append(row)
            
        with open(f'{output_name}'+'.csv', 'w') as csvfile:
            csvWriter = csv.writer(csvfile,delimiter=delimiter, quotechar=quotechar,quoting=csv.QUOTE_MINIMAL, lineterminator=lineterminator)
            csvWriter.writerow(rowFields)
            csvWriter.writerows(contentRows)  
