import sys
import argparse

# this program allows users to create json files from the command line
# for the FRB rate calculator

# sample command:
# python auto-json.py -N <name> -Y <year> -n <nFRBs> -S <FWHM_2> 
# -R <radius> -b <beams> -t <tpb> -f <flux>

parser = argparse.ArgumentParser(description="Makes a json file to house the data for FRB rate calculation.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-N', '--name', help='name of main author in the paper', action='store', type=str, required=True)
parser.add_argument('-Y', '--year', help='year of discovery', action='store', type=str, required=True)
parser.add_argument('-n', '--nFRBs', help='number of FRBs', action='store', type=float, required=True)
parser.add_argument('-S', '--FWHM_2', help='Sensitivity at FWHM divided by 2', action='store', type=float, required=True)
parser.add_argument('-R', '--radius', help='FWHM diameter in arcminutes divided by 2 to get radius divide by 60 to get degrees', action='store', type=float, required=True)
parser.add_argument('-b', '--beams', help='number of beams', action='store', type=float, required=True)
parser.add_argument('-t', '--tpb', help='time per beam', action='store', type=float, required=True)
parser.add_argument('-f', '--flux', help='flux, do not seperate values with commas - only spaces are needed', action='store', nargs='+', type=float, default=[], required=True)
args = parser.parse_args()

# define the name of the file
filename = args.name+"_"+args.year+"_Rate-Data.json"
# ex. filename - Name_Year_Rate-Data.json
    
# print that information into a file with the filename that was supplied
with open(filename, "w") as fobj:
    fobj.write("{ \"properties\": [{\n")
    fobj.write("\t\"surveys\": \"{} {}\",\n".format(args.name, args.year))
    fobj.write("\t\"nFRBs\": {0},\n".format(args.nFRBs))
    fobj.write("\t\"FWHM_2\": {0},\n".format(args.FWHM_2))
    fobj.write("\t\"R\": {0},\n".format(args.radius))
    fobj.write("\t\"beams\": {0},\n".format(args.beams))
    fobj.write("\t\"tpb\": {0},\n".format(args.tpb))
    fobj.write("\t\"flux\": {0}\n".format(args.flux))
    fobj.write("\t}\n")
    fobj.write("]}")
