# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

datasets = []
DS_OPTION = 0 # select witch table provided to use

# prints formatted matrix
def print_m(matrix):
    for line in matrix:
        print(line)

with open('data.txt', 'r') as f:
    line = f.readline()
    
    matrix = []
    while line:
        # removes headers
        try:
            x = int(line[0])
        except:
            line = f.readline()
            datasets.append(matrix)
            matrix = []
        
        line = line.strip()         #removes \n
        values = line.split(',')
        values.pop(0)               # remove y coordinates indicator
        values = [float(x) for x in values]
        matrix.append(values)

        line = f.readline()
    datasets.append(matrix)
    datasets.pop(0)
            
    print_m(datasets[DS_OPTION])
    
# what datasets[0] should look like for base experiment setup
# x2 = [5.3, 5.3, 5.5, 5.5, 5.6, 5.6, 5.6]
# x1 = [3.0, 3.4, 3.5, 3.5, 3.6, 3.5, 3.6]
# x3 = [7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5]
# x4 = [9.3, 9.3, 9.3, 9.4, 9.4, 9.4, 9.4]
# x5 = [11.5, 11.5, 11.4, 11.4, 11.3, 11.2, 11.1]
# x6 = [13.6, 13.4, 13.4, 13.5, 13.3, 13.2, 13.2]
# x7 = [16.4, 16.0, 15.6, 15.5, 15.2, 15.1, 15.0]
# X = np.transpose([x1, x2, x3, x4, x5, x6, x7])

X = datasets[DS_OPTION]

Y = [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
     [ 2.,  2.,  2.,  2.,  2.,  2.,  2.,],
     [ 4.,  4.,  4.,  4.,  4.,  4.,  4.],
     [ 6.,  6.,  6.,  6.,  6.,  6.,  6.],
     [ 8.,  8.,  8.,  8.,  8.,  8.,  8.],
     [10., 10., 10., 10., 10., 10., 10.],
     [12., 12., 12., 12., 12., 12., 12.]]

# plt.plot(X, Y, marker='o', color='k', linestyle='none')
# plt.show()

z = np.linspace(0.5, 2, 7)
Z = [z] * 7
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)

plt.savefig("graph.pdf", format='pdf', bbox_inches='tight')
