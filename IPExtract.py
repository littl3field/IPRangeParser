import re
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Grab all IP address ranges from a file", usage="use -f to specify filename",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", dest="filename",
                        help="File to be crawled")
    args = parser.parse_args()

    if args.filename is not None:
        for line in open(args.filename, 'r'):
            # Grab the full host information for an IP
            findall = re.findall(r'\b25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.25[0-5]|2[0-4][0-9]|[/]|[01]?[0-9][0-9]?\b',
                line)
            result = ".".join(str(x) for x in findall)
            rme = re.sub('\.\/.', "/", result)
            filename = 'test.txt'
            with open(filename, 'a') as f:
                f.write(rme + '\n')
            if not os.path.isfile(filename):
                print("{} does note exist ".format(filename))
                return
            with open(filename) as filehandle:
                lines = filehandle.readlines()
            with open(filename, 'w') as filehandle:
                lines = filter(lambda x: x.strip(), lines)
                filehandle.writelines(lines)
    else:
        print("Please specify a filename, use -H for help")

if __name__ == "__main__":
    main()
