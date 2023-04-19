"""print size of every python file whose name starts with "m" """

import os

START_DIR = ".."  # start in root of student files  # starting location


def main():
    for currdir, subdirs, files in os.walk(START_DIR):  # walk folder tree
        if '.git' in subdirs:
            subdirs.remove('.git')
        for file in files:  # loop over file names
            if file.endswith('.py') and file.startswith('m'):
                fullpath = os.path.join(currdir, file)  # get file path
                fsize = os.path.getsize(fullpath)
                print("{:8d} {:s}".format(fsize, fullpath))

print(f"os.path.dirname(os.path.abspath(os.getcwd())): {os.path.dirname(os.path.abspath(os.getcwd()))}")


if __name__ == '__main__':
    main()
