#!/usr/bin/env python3

import argparse
import pyAesCrypt
import os
import maskpass

def encryptFile(input_file, output_file):
    password = maskpass.askpass(prompt = 'Password: ', mask="*")
    pyAesCrypt.encryptFile(input_file, output_file, password)
    os.remove(input_file)
    
def decryptFile(input_file, output_file):
    password = maskpass.askpass(prompt = 'Password: ', mask="*")
    pyAesCrypt.decryptFile(input_file, output_file, password)
    os.remove(input_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
    parser.add_argument('-t','--type', type=str,choices=['en','de'], help='Encrypt or decrypt.')
    parser.add_argument('-in','--input_file', type=str, help='The input file to encrypt or decrypt.')
    parser.add_argument('-out', '--output_file', type=str, help='The output file to encrypt or decrypt.')

    args = parser.parse_args()
    try:
        if args.type == "en":
            encryptFile(args.input_file, args.output_file)
        elif args.type == "de":
            decryptFile(args.input_file, args.output_file)
    except:
        print('An error occured!')

