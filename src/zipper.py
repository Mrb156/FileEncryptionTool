#!/usr/bin/env python3

import argparse
import zipfile
import glob
import os
import maskpass
import shutil

from packages.encrypt_file_package import encryptFile


def zipInfo(input):
    with zipfile.ZipFile(input, 'r') as file:
        for info in file.infolist():
            print(info.filename)


def compressFile(input, output):
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
        if(os.path.isdir(input)):
            input = input+"/*"
            print("Compressing: {}".format(input))
            for file in glob.glob(input):
                zip.write(file)
            print("Compressed to: {}".format(output))
        else:
            for file in glob.glob(input):
                zip.write(file)
            print("Compressed to: {}".format(output))


def extractFile(input, output):
    with zipfile.ZipFile(input, 'r') as file:
        print("Extracting: ")
        file.printdir()
        file.extractall(output)
        print('Done!')


def deleteFiles(input):
    if(os.path.isdir(input)):
        shutil.rmtree(input)
    else:
        os.remove(input)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Zip files/ directories.')
    parser.add_argument('-i', '--info', action="store_true",
                        help='Info of the zip file.')
    parser.add_argument('-d', '--delete', action="store_true",
                        help='If you don\'t want to save the original files.')
    parser.add_argument('-t', '--type', type=str,
                        choices=['comp', 'ext'], help='Do you want to compress or extract?')
    parser.add_argument('-in', '--input_file', type=str,
                        help='Which file(s) you want to compress. You can add a suffix as well.')
    parser.add_argument('-out', '--output_file', type=str,
                        help='Name of the compressed output zip folder.')
    parser.add_argument('-e', '--encrypt', action="store_true",
                        help='Encrypt the folder.')
    args = parser.parse_args()
    if args.info:
        try:
            zipInfo(args.input_file)
        except:
            print("An error occured. Did you add an input file?")
    else:
        error = False
        default_output_path = args.output_file
        if args.type == 'comp':
            if not args.output_file:
                default_output_path= os.path.dirname(
                    os.path.realpath(__name__)) + ".zip"
            elif args.output_file and args.output_file.find('.zip') == -1:    
                default_output_path = args.output_file + '.zip'
            try:
                compressFile(args.input_file, default_output_path)
                if args.delete:
                    try:
                        deleteFiles(args.input_file)
                    except:
                        print("Error while removing a file.")
                if args.encrypt:
                    output_file = input('The encrypted file path/ name: ')
                    password = maskpass.askpass(
                        prompt='Password: ', mask="")
                    try:
                        encryptFile(args.output_file,
                                    output_file, password)
                        deleteFiles(args.output_file)
                        print(
                            'Successfully encrypted. You can decrypt this file with the decrypt method.')
                    except:
                        error = True
                        print("Unable to encrypt.")
            except:
                error = True
                print("An error occured. Check your inputs!")
        elif args.type == 'ext':
            if not args.output_file:
                default_output_path= os.path.dirname(
                    os.path.realpath(__name__))
            try:
                extractFile(args.input_file, default_output_path)
                if args.delete:
                    try:
                        deleteFiles(args.input_file)
                    except:
                        print("Error while removing a file.")
            except:
                error = True
                print("Error while extracting a file.")

        if error:
            print("An error occured.")
