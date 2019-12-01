#print ("start")
#
#import sys
#
#print ("This is the name of the script: ", sys.argv[0])
#print ("First argument: ", sys.argv[1])



import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--bars', '-b', help="Number of bars", type= int, default= 1)

args = parser.parse_args()
print(args)  

# Namespace
print(args.bars)