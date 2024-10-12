import base64
import sys

def encode(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as file:
        file_data = file.read()
        encoded_data = base64.b64encode(file_data)

    with open(output_file_path, 'wb') as output_file:
        output_file.write(encoded_data)

def decode(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as encoded_file:
        encoded_data = encoded_file.read()
        decoded_data = base64.b64decode(encoded_data)

    with open(output_file_path, 'wb') as output_file:
        output_file.write(decoded_data)

def main():
    input_file_path = input('Input file > ')
    output_file_path = input('Output file > ')

usage = \
"""\
b64ed [parameters]

Parameters:
    -e --encode <file path> - encode file
    -d --decode <file path> - decode file
    -o --output <output file> - specify the output file
"""

def check_mode_and_file(args):
    """
    return 1 + file for encode
    return 2 + file for decode
    return 0 + None for error
    """

    mode = 0
    file = None

    try:
        i = args.index('-e')
    except:
        pass
    else:
        file = args[i+1]
        mode = 1

    try:
        i = args.index('--encode')
    except:
        pass
    else:
        file = args[i+1]
        mode = 1
        
    try:
        i = args.index('-d')
    except:
        pass
    else:
        file = args[i+1]
        mode = 2

    try:
        i = args.index('--decode')
    except:
        pass
    else:
        file = args[i+1]
        mode = 2
    
    return mode, file

def check_output_file(args):
    """
    return file or None
    """

    file = None

    try:
        i = args.index('-o')
    except:
        pass
    else:
        file = args[i+1]

    try:
        i = args.index('--output')
    except:
        pass
    else:
        file = args[i+1]

    return file        
        
if len(sys.argv) < 3:
    print(usage)
    sys.exit(1)


# check mode and input file
mode, input_file = check_mode_and_file(sys.argv)

# check if there are any output file specifyed
output_file = check_output_file(sys.argv)
if not output_file and mode == 1:
    output_file = f'{input_file}.b64'
else:
    if input_file[-4:] == '.b64':
        output_file = input_file[:-4]
    else:
        print("if the input file does not ends on '.b64' you must specify a output file name.")
        sys.exit(1)

if mode == 1:
    encode(input_file, output_file)

elif mode == 2:
    decode(input_file, output_file)
else:
    print(usage)
