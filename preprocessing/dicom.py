from pydicom import dcmread
from pydicom.data import get_testdata_file

import os
import numpy as np

class dicom_properties():
    def __init__(self):
        pass

    def extract_properties_dir(self, data_dir = 'data/anatomy_dicom', save_to_npy_path = None, npy_file_name = None):
        dicom_files = os.listdir(data_dir)
        dicom_properties = {}

        for file in dicom_files:
            file_path = os.path.join(data_dir, file)
            ds = dcmread(file_path)

            print("Adding:", file + " to the dictionary...")
            dicom_properties[file] = ds

        if save_to_npy_path != None:
            print("Saving ", len(dicom_properties), " properties into ", npy_file_name, "...")

            try:
                np.save(os.path.join(save_to_npy_path, npy_file_name + '.npy'), dicom_properties)
                print('done...')
            except:
                print("Could not save to ", npy_file_name)

        
        return dicom_properties


    def extract_properties(self, dicom_file_path = 'data/anatomy_dicom', save_to_npy_path = None, npy_file_name = None):

        dicom_properties = dcmread(dicom_file_path)

        if save_to_npy_path != None:
            print("Saving ", len(dicom_properties), " properties into ", npy_file_name, "...")

            try:
                np.save(os.path.join(save_to_npy_path, npy_file_name + '.npy'), dicom_properties)
                print('done...')
            except:
                print("Could not save to ", npy_file_name)

        
        return dicom_properties



if __name__ == '__main__':
    properties = dicom_properties()
    '''
    out = properties.extract_properties_dir(data_dir='data/anatomy_dicom', 
                                            save_to_npy_path='data', npy_file_name='anatomy_dicom_properties')
    '''
    out = properties.extract_properties(dicom_file_path='data/anatomy_dicom/IM-0002-0001.dcm')
    print(out)