import os
import csv

path = '../images/'

with open('../csv/roof_segmentation.csv', 'w', newline='') as csvfile: #Loop through path and add all files matching *.jpeg to array files
    files = []
    for r,d,f in os.walk(path):
        for _file in f:
            if '.jpeg' in _file:
                files.append(_file)
    
    writer = csv.writer(csvfile, delimiter=',') #Create a writer from csv module
    for f in files: #find type of file
        writer.writerow(['', 'gs://automl-set-up-task-aj-vcm/roof_segmentation_img/'+f, '', 0, 0, 1, 0, 1, 1, 0, 1]) #write the row to the output csv file