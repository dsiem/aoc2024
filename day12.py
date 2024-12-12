import numpy as np
import scipy.signal
import skimage.measure

input = np.vectorize(ord)(np.genfromtxt(open(0), delimiter=1, dtype=str))
plots, num = skimage.measure.label(input, connectivity=1, return_num=True)
areas = np.bincount(plots.ravel())[1:]
split = (plots[:, :, None] == np.arange(1, num + 1)).astype(np.uint8).transpose(2, 0, 1)
edges = np.abs(scipy.signal.convolve(split, np.array([[[2, -1], [-1, 0]]]))).sum((1, 2))
sides = np.abs(scipy.signal.convolve(split, np.array([[[1, -1], [-1, 1]]]))).sum((1, 2))
print(*(areas * [edges, sides]).sum(1))
