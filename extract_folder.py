# Et program jeg, tro det eller ei, faktisk ble ganske ferdig med.
# Sikkert fortsatt mange ting som kan forbedres, f. eks. lett installasjon,
# men det kan jo fikses senere en gang, om jeg føler meg inspirert.

import os
import sys
import ctypes

# This functions ensure that files with conlicting names still will be extracted
def move_file(old, new):
    try:
        os.rename(old, new)
    except FileExistsError:
        print(f"File {i} already exists in {target_dir}")
        move_file(old, new+" (1)")

# First argument is the directory that the files will be extracted from
if os.path.exists(sys.argv[0]):
    directory = os.path.abspath(sys.argv[1]) 
    target_dir = os.path.split(directory)[0]

    content = os.listdir(directory)
    result = ctypes.windll.user32.MessageBoxW(0, f"Are you sure you want to extract {len(content)} item(s) from \"{directory}\"?",
                                              "Extract Items from Folder", 52)
    print(int(result))
    if int(result) == 6:
        for i in content:
            old_path = os.path.join(directory, i)
            new_path = os.path.join(target_dir, i)
            move_file(old_path, new_path)
        os.rmdir(directory)

