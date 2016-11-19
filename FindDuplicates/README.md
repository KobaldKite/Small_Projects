# 11_duplicates

Prints to the console which files have several instances of them in a given folder. A pair of (name, size) is considered a unique file attribute.   

Path to the folder you want to scan is a positional argument.   

### How to use:   

> python duplicates.py ./folder   
> python duplicates.py /home/dima/Downloads/

### Console output sample:   

> File points.csv size of 345 bytes encountered 3 times:   
> ./folder/points.csv   
> ./folder/folder_2/one_more_folder/points.csv   
> ./folder/folder_1/points.csv   
