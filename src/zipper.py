#!/usr/bin/env python3

import argparse
import zipfile
import glob
import os
import maskpass
import shutil
from datetime import datetime

from packages.encrypt_file_package import encryptFile


def zipInfo(input):
    with zipfile.ZipFile(input, 'r') as file:
        for info in file.infolist():
            print("{}\t {}\t {} bytes".format(info.filename, datetime(*info.date_time), info.compress_size))


def compressFile(input, output):
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
        if(os.path.isdir(input)):
            print("Compressing: {}".format(input))
            for path, directories, files in os.walk(input):
                for file in files:
                    file_name = os.path.join(path, file)
                    zip.write(file_name)
            print("Compressed to: {}".format(output))
        else:
            for file in glob.glob(input):
                if(os.path.isdir(file)):
                    for path, directories, files in os.walk(file):
                        for file in files:
                            file_name = os.path.join(path, file)
                            zip.write(file_name)
                zip.write(file)
                print("{} compressed".format(file))
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
        for file in glob.glob(input):
            os.remove(file)


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
            if not args.input_file:
                print("Add an input file!")
    else:
        default_output_path = args.output_file
        if args.type == 'comp':
            if not args.output_file:
                default_output_path= os.path.dirname(
                    os.path.realpath(__name__)) + '/' + args.input_file + ".zip"
            elif args.output_file and not args.output_file.__contains__('.zip'):
                if os.path.isdir(args.output_file):
                    default_output_path = args.output_file + '/' + args.input_file + '.zip'
                else:
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
                        print("Unable to encrypt.")
            except:
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
            
                print("Error while extracting a file.")
