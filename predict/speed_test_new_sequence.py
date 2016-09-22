import timeit
from random import sample

import numpy as np

from recomb_helper import new_sequence, new_sequence_v2
from diploid import Diploid

possible_starts = tuple(range(10000000))
starts = np.array(sorted(sample(possible_starts, 400)), dtype = np.uint32)
founders = np.array(list(range(400)), dtype = np.uint32)

locations = list(sample(possible_starts, 20))

diploid = Diploid(starts, 10000000, founders)

def speed_new_sequence():
    x = new_sequence(diploid, locations)

def speed_new_sequence_v2():
    x = new_sequence_v2(diploid, locations)

timeit.timeit(speed_new_sequence)

timeit.timeit(speed_new_sequence_v2)