import argparse
import zipfile
import glob
import os

def zipInfo(input):
    with zipfile.ZipFile(input, 'r') as file:
        for info in file.infolist():
            print(info.filename)

def compressFile(input, output):
    with zipfile.ZipFile(output, 'w') as zip:
        print("Compressing: {}".format(input))
        for file in glob.glob(input):
            zip.write(file)
        print("Compressed to: {}".format(output))
        

def extractFile(input, output = ""):
    with zipfile.ZipFile(input, 'r') as file:
        print("Extracting: ")
        file.printdir()
        file.extractall(output)
        print('Done!')

def deleteFiles(input):
    for file in glob.glob(input):
        os.remove(file)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Zip files/ directories.')
    parser.add_argument('-i', '--info', action="store_true", help='Info of the zip file.')
    parser.add_argument('-d', '--delete', action="store_true", help='If you don\'t want to save the original files.')
    parser.add_argument('-t', '--type', type=str, choices=['comp', 'ext'], help='Do you want to compress or extract?')
    parser.add_argument('-in', '--input_file', type=str, help='Which file(s) you want to compress. You can add a suffix as well.')
    parser.add_argument('-out','--output_file', type=str, help='Name of the compressed output zip folder.')
    args = parser.parse_args()
    if args.info:
        try:
            zipInfo(args.input_file)
        except:
            print("An error occured. Did you add an input file?")
    else:
        if args.type == 'comp':
            try:
                compressFile(args.input_file, args.output_file)
            except:
                print("An error occured. Check your inputs!")
        elif args.type == 'ext':
            try:
                extractFile(args.input_file, args.output_file)
            except:
                print("Error while extracting a file.")

        if args.delete:
            try:
                deleteFiles(args.input_file)
            except:
                print("Error while removing a file.")

