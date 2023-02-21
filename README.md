# S3 Keys to Dictionary
AWS S3 can supply a list of keys from an S3 bucket to users. These keys replicate a directory, but are not nested. This repository takes a list of keys as an input and sorts them into a nested dictionary of files and folder.

There must be a root key.

## Requirements
* Only python built in libraries are used.
* Tested on Python 3.9
* There must be a single root directory.

## Output
The output is a nested dictionary. 

Each individual folder is represented by a dictionary with values: 
* "key": A string. The aws object key.
* "name": A string representing the file name or folder name. ie "your/dir/file.jpg" is "file.jpg", or "your/dir/" is "dir".
* "type": A string. Either "file" or "folder"
* "items": A list. containes dictionaries of folders and strings of files.

Files are represented as dictionaries with "key", "name", and "type" values. They are stored in the "items" value of a folder.
```
# For example:
{
    "key": "your/dir/",
    "name": "dir",
    "type": "folder",
    "items": [
        {
            "key": "your/dir/file1.jpg",
            "name": "file1.jpg",
            "type": "file",
        }
    ]
}
```

An entire output might look like this:
```
{
    "key": "root/",
    "name": "root",
    "type": "folder",
    "items": [
        {
            "key": "root/file1.jpg",
            "name": "file1.jpg",
            "type": "file",
        }
        {
            "key": "root/dir",
            "name": "dir",
            "type": "folder",
            "items": [
                {
                    "key": "root/dir/file2.jpg",
                    "name": "file2.jpg",
                    "type": "file",
                }
            ]
        }
    ]
}