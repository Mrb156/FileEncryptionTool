#!/usr/bin/env python3

import argparse
import pyAesCrypt
import os

def encryptFile(input_file, output_file, password):
    pyAesCrypt.encryptFile(input_file, output_file, password)
    
def decryptFile(input_file, output_file, password):
    pyAesCrypt.decryptFile(input_file, output_file, password)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
    parser.add_argument('type', type=str, help='Encrypt or decrypt.')
    parser.add_argument('input_file', type=str, help='The input file to encrypt or decrypt.')
    parser.add_argument('output_file', type=str, help='The output file to encrypt or decrypt.')
    #parser.add_argument('-a','--algorithm', type=str,choices=['AES','blowfish'], default='AES', help='The encryption algorithm to use. AES or blowfish')
    parser.add_argument('password', type=str, help='Password for encrypt or decrypt.')
    args = parser.parse_args()

    if args.type == "en":
        encryptFile(args.input_file, args.output_file, args.password)
    elif args.type == "de":
        decryptFile(args.input_file, args.output_file, args.password)

