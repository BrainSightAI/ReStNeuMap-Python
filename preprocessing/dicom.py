from pydicom import dcmread
from pydicom.data import get_testdata_file

import os
import numpy as np

anatomy_dicom_files = os.listdir('data/anatomy_dicom/')

anatomy_dicom_properties = {}

for file in anatomy_dicom_files:
    path = os.path.join('data/anatomy_dicom', file)
    ds = dcmread(path)

    print("Adding :", file + " to the dictionary...")
    anatomy_dicom_properties[file] = ds


print("Saving ", len(anatomy_dicom_properties), " properties into 'anatomy_dicom_properties.npy'...")

try:
    np.save('anatomy_dicom_properties.npy', anatomy_dicom_properties)
    print('done...')
except:
    print("Could not save to 'anatomy_dicom_properties.npy'")