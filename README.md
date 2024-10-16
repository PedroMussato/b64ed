BASE64 encode and decode files directly from terminal.
## Usage
```
b64ed [parameters]

Parameters:
    -e --encode <file path> - encode file
    -d --decode <file path> - decode file
    -o --output <output file> - specify the output file
```

### to encode
```
b64ed -e <input file>
```
optionally you can use `-o <output file>` or `--output <output file>` if output is not specifyed the output file name will be the `<input file>.b64`
### to decode
```
b64ed -d <input file>
```
optionally you can use `-o <output file>` or `--output <output file>`, you have the option to not specify the output name if the input file ends with .b64, if not you must specify an output file name.

(e.g.)
empty dir
```
sh-5.2$ ls
```
creating the file
```
sh-5.2$ touch file1
sh-5.2$ echo "any content" > file1
sh-5.2$ cat file1
any content
```
encrypting file
```
sh-5.2$ b64ed -e file1
sh-5.2$ ls
file1  file1.b64
sh-5.2$ cat file1.b64 
YW55IGNvbnRlbnQK
```
removing original file
```
sh-5.2$ rm file1
sh-5.2$ ls
file1.b64
```
decrypting file and recovering original content
```
sh-5.2$ b64ed -d file1.b64 
sh-5.2$ ls
file1  file1.b64
sh-5.2$ cat file1
any content
sh-5.2$ 
```
