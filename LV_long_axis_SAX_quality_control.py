# Compute LV long axis after reformatting and check if it's very different to the theoretical one: [0, 0, 1]
# Use uniformly remeshed meshes (different number of points than the ones used in TA view to try to do not
# reproduce same potential errors).

from aux_functions import *

# prefix_path = '/home/marta/Desktop/DATA/Sonny/CHECK_REFORMATS_TO_SAX/0101766215/'   # example of wrong
# prefix_path = '/home/marta/Desktop/DATA/Sonny/CHECK_REFORMATS_TO_SAX/0101766215/correct/'   # example of correct
# prefix_path = '/home/marta/Desktop/DATA/Sonny/CHECK_REFORMATS_TO_SAX/0108029016/'
# prefix_path = '/home/marta/Desktop/DATA/Sonny/CHECK_REFORMATS_TO_SAX/0113214161/'
prefix_path = '/home/marta/Desktop/DATA/Sonny/CHECK_REFORMATS_TO_SAX/QC/0100307131/'
ct_name = 'ct1'

lvendo_filename = prefix_path + ct_name + '-lvendo-sax.mha'
lvwall_filename = prefix_path + ct_name + '-lvwall-sax.mha'
rvepi_filename = prefix_path + ct_name + '-rvepi-sax.mha'

do_lv_lax_qc(prefix_path, lvendo_filename, lvwall_filename, rvepi_filename, tolerance=0.05, npoints_remesh=1500)
# [0 +- tolerance; 0 +- tolerance; 1 - tolerance]
