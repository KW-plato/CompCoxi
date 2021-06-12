"""
Script reads all the raw data files, adds subject id and condition to every line.
Finally a master raw data file is created.
"""
import pandas as pd
from os import listdir

files_loc = "/home/sabi/Techspace/CompCoxi/CompCoxi/Dataset/MPIIDPEye/Eye_Tracking_Data"

files = listdir(files_loc)
print("no. of files {}".format(len(files)))
listofdf = []
for filename in files:
    df = pd.read_csv(files_loc+'/'+filename,
                     delimiter=';',
                     names= ['pupil_position_x','pupil_position_y','timestamp','confidence','pupil_diameter']
                     )
    elements = filename.replace('.csv', '').split('_')
    df['subject_id'] = elements[1]
    df['condition'] = elements[2]
    listofdf.append(df)

finaldf = pd.concat(listofdf)
finaldf.to_csv(files_loc +'/master_raw_data.csv',
               header=['pupil_position_x','pupil_position_y','timestamp','confidence','pupil_diameter','subject_id','condition']
               )