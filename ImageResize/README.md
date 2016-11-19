# 12_image_resize

The program looks at an image file and creates a new one with the same picture but of a different size. Image proportions can be changed, if yser so desires.

## Arguments:

**Positional argument:** path to the file you want to resize.

**--output_path** - path to the resized file. If not specified, it's set to name\_\_AxB.ext, where   
name - original file's name (wihout extension)   
A, B - width and height of the resized file   
ext - original file's extension   
**Important!** The new filename should have a file extention!

**--width, --height** - desired width and height. If only one is given, the other one is set to keep the image's proportions. If both are set, the proportions might be distorted.   

**--scale** - multiplies both width and height by scale. If width and/or heights are also set, they are ignored, and scale is prioritised.

## Usage examples:

> python image_resize.py kittens.png --scale=0.5   

Creates file kittens\_\_120x100.png, providing the original file was 240x200.   

> python image_resize.py kittens.png --width=360   

Creates file kittens\_\_360x300.png   

> python image_resize.py kittens.png --width=100 --height=100 --output_path = "cats.png"   

Creates 100x100 file cats.png   
