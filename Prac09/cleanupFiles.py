"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'


def main():
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    # for filename in os.listdir('.'):
        # ignore directories, just process files
        # if not os.path.isdir(filename):
            # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            # print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)


            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

    for filename in os.listdir('.'):
        fixed_filename = get_fixed_filename(filename)
        print(fixed_filename)


def get_fixed_filename(filename):
    newstring = filename[0] + ''
    for char in filename[1:]:
        if char.isupper():
            newstring += "_" + char
        else:
            newstring += char
    return newstring

# separate variable or enumerate to keep track of char number. Char before cannot be an underscore

main()

# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)
