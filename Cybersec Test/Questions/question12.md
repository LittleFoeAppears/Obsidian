Write a script which checks for a given file. If the file exists, print "Found {filename}" to stdout, otherwise print "Can't find {filename}".
If no arguments are supplied, print "Nothing to find".

When the life exists:

$ touch file1.txt'
$ ./your_script file.txt
Found file1.txt

When the file exists:

$ rm -f file1.txt'
$ ./your_script file1.txt
Can't find file1.txt

When the script is called with no arguments:

$ ./your_script
Nothing to find

```
#!/bin/bash
# Shebang


# If no argument was submitted when using the script ($0)
if [ $# -eq 0 ]; then
    echo "Nothing to find"

# If argument was submitted use it as var. filename
else
    filename=$1

	# Check if existing file has that name or not
    if [ -e "$filename" ]; then
        echo "Found $filename"
    else
        echo "Can't find $filename"
    fi
fi

```