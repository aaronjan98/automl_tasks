# import os

# path = '../roof-images/'

# files = []
# for  r, d, f in os.walk(path):
#     for file in f:
#         if '.jpeg' in file:
#           print(file)

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
        t = 'needs to be labeled'
        # t = f[:-5] #cut off the .jpeg extension from file, leaving only the name
        
        # if "roof-1" == t:
        #     t = 1
        # if "roof-2" == t:
        #     t = 2
        # if "roof-3" == t:
        #     t = 3
        
        writer.writerow(['TRAINING', 'gs://automl-set-up-task-aj-vcm/roof_segmentation_img/'+f, t, 0, 0, 1, 0, 1, 1, 0, 1]) #write the row to the output csv file