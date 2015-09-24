
import re
import sys, getopt


def AvamarParse(argv):
    inputFile = ''

    try:
        # This method returns value consisting of two elements:
        # the first is a list of (option, value) pairs. The second
        # is the list of program arguments left after the option list was stripped.
        # Each option-and-value pair returned has the option as its first element,
        # prefixed with a hyphen for short options (e.g., '-x') or two hyphens for
        # long options (e.g., '--long-option').
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print 'AvamarParse.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'AvamarParse.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg;

    print 'Input file is: ', inputFile


    with open(inputFile, 'r') as f:
        read_data = f.read();
        print read_data
    f.closed

    #print 'Number of arguments: ', len(sys.argv), 'arguments.'
    #print 'Argument List: ', str(sys.argv)




if __name__ == "__main__":
   AvamarParse(sys.argv[1:])
