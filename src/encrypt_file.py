import argparse
import pyAesCrypt
import os

def encryptFile(input_file, output_file, password, algorithm = "AES"):
        pyAesCrypt.encryptFile(args.input_file, args.output_file, args.password)
        os.remove(args.input_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
    parser.add_argument('-a','--algotihm', type=str,choices=['AES','...'], default='AES', help='The encryption algorithm to use. AES or ...')
    parser.add_argument('input_file', type=str, help='The input file to encrypt or decrypt.')
    parser.add_argument('output_file', type=str, help='The output file to encrypt or decrypt.')
    parser.add_argument('type', type=str, help='Encrypt or decrypt.')
    parser.add_argument('password', type=str, help='Password for encrypt or decrypt.')
    args = parser.parse_args()

    if args.type == "en":
        pyAesCrypt.encryptFile(args.input_file, args.output_file, args.password)
        os.remove(args.input_file)
    elif args.type == "de":
        pyAesCrypt.decryptFile(args.input_file, args.output_file, args.password)
        os.remove(args.input_file)
