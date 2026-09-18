import h5py
import numpy as np

def main():
#----------

    matrix1 = np.random.random(size = (1000,1000))
    matrix2 = np.random.random(size = (10000,100))

    # create hdf5 file
    f = h5py.File('/scratch/olivie/trial.hdf5', 'w')

    # create data sets
    dataset1 = f.create_dataset('dataset1', data=matrix1)
    dataset2 = f.create_dataset('dataset2', data=matrix2)

    # set attributes
    dataset1.attrs['CLASS'] = 'DATA MATRIX'
    dataset1.attrs['VERSION'] = '1.1'

    f.close()

if __name__ == '__main__':
    main()
