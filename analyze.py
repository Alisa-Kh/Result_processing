#!/usr/bin/python3

import os

"""You will run this script from '.../results/TBX4/F3/xmer/'-like directory"""

# Constants go here:

INT_ANALYZER_DIR = 'interface_analyzer'
ALA_DIR = 'ala_scan'
RUN_INT_ANALYZER = '/vol/ek/Home/alisa/rosetta/Rosetta/main/source/bin/InterfaceAnalyzer.default.linuxgccrelease ' \
                   '-in:file:s {pdb} -add_regular_scores_to_scorefile -compute_packstat -out:file:score_only {sc}'
RUN_ALA_SCAN = '/vol/ek/share/bin/ALASCAN_ROBETTA/run_ROBETTA.sh {} A B'
BUILD_PLOT = 'Rscript plot.R'

ALA_RESULTS = 'PROTONATED_{}.alascan.results'
DDG_CUT = 1
DG_CUT = 0.9


def run_interface_analyzer():
    if not os.path.exists(INT_ANALYZER_DIR):
        os.mkdir(INT_ANALYZER_DIR)
    os.chdir(INT_ANALYZER_DIR)
    for model in os.listdir('../FINAL_RESULTS'):
        os.system(RUN_INT_ANALYZER.format(pdb=model, sc=(os.path.basename(model) + '.sc')))
    os.chdir(my_path)


def run_ala_scan():
    if not os.path.exists(ALA_DIR):
        os.mkdir(ALA_DIR)
    os.chdir(ALA_DIR)
    for model in os.listdir('../FINAL_RESULTS'):
        os.system(RUN_ALA_SCAN.format(model))

        # fullname_results = ALA_RESULTS.format(model)
        # with open(fullname_results, 'r') as res:
        #     all_lines = res.readlines()
        #     headers = all_lines[1:3]
        #     only_res = all_lines[3:]
        # with open('filtered_results' + model, 'w') as new:
        #     for line in headers:
        #         new.write(line)
        #     for line in only_res:
        #         if float(line.split()[5]) >= float(DDG_CUT) and float(line.split()[7]) <= float(DG_CUT):
        #             new.write(line)
    os.chdir(my_path)


def build_a_plot():
    os.system(BUILD_PLOT)


if __name__ == "__main__":

    my_path = os.getcwd()

    run_interface_analyzer()

    run_ala_scan()

    build_a_plot()




