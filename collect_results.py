#!/usr/bin/python3

import os

"""You will run this script from '.../results/TBX4/F3/xmer/'-like directory"""

# Constants:

PROJ_DIR = '/vol/ek/Home/alisa/Projects/'
RESULTS_DIR = '/vol/ek/Home/alisa/RESULTS/'
COPY = 'cp {what} {to}'
FINAL_10 = 'FINAL_RESULTS'

# if native structure exists:
DECOYS = 'refinement/decoys.silent '
SCORE = 'refinement/score.sc '
CLUSTERING = 'refinement/clustering/cluster_list* '

# no native:
DECOYS_RE = 'refinement/decoys_rescored.silent '
SCORE_RE = 'refinement/rescore.sc '


def collect():
    """Collect top 10 structures, decoys.silent file and score.sc (or rescore.sc),
    and clustering lists"""
    dir_name = RESULTS_DIR + my_path[len(PROJ_DIR):]
    os.system('mkdir -p ' + dir_name)
    if os.path.isfile('refinement/rescore.sc'):
        os.system(COPY.format(what=FINAL_10 + '/*pdb ' + DECOYS_RE + SCORE_RE + CLUSTERING, to=dir_name))
    else:
        os.system(COPY.format(what=FINAL_10 + '/*pdb ' + DECOYS + SCORE + CLUSTERING, to=dir_name))


if __name__ == "__main__":

    my_path = os.getcwd()

    collect()

