BASE64 encode and decode files directly from terminal.
## Usage
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
```
sh-5.2$ ls
sh-5.2$ touch file1
sh-5.2$ echo "any content" > file1
sh-5.2$ cat file1
any content
sh-5.2$ b64ed -e file1
sh-5.2$ ls
file1  file1.b64
sh-5.2$ cat file1.b64 
YW55IGNvbnRlbnQK
sh-5.2$ rm file1
sh-5.2$ ls
file1.b64
sh-5.2$ b64ed -d file1.b64 
sh-5.2$ ls
file1  file1.b64
sh-5.2$ cat file1
any content
sh-5.2$ 
```
