# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023

# prints formatted matrix
print_m = lambda matrix: [print(line) for line in matrix]

# converts Hexcoded color string to rgba tuple   
hex_to_rgba = lambda hex, a: (int(hex[1:3], 16)/255, int(hex[3:5], 16)/255, int(hex[5:7], 16)/255, a)