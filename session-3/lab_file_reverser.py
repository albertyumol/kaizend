import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()


# We utilize the try statement to denote that it’s quite possible for an error to happen within the try block
try:
    f = open(args.filename)
    limit = args.limit
# We can handle specific types of errors using the except keyword (we can have more than one).
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
# If there isn’t an error, we want to carry out the code that is in the else block
else:
    with f:
        lines = f.readlines()
        lines.reverse()
    
        if args.limit:
            lines = lines[:args.limit]
        for line in lines:
            print(line.strip()[::-1])

# If we want to execute some code regardless of there being an error or not,
# we can put that in a finally block at the very end of our try/except code
