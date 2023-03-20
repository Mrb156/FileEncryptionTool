import argparse
print("ez az encrypt_file.py")

def openFile(file) :
    fajlbe = open(file)
    print(fajlbe.readline())
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
    parser.add_argument('input_file', type=str, help='The input file to encrypt or decrypt.')
    args = parser.parse_args()
    openFile(args.input_file)