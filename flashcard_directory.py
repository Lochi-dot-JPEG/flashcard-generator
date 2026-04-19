#!/bin/python3

import datetime
import os
import sys
import glob

arguments = sys.argv[1:]
flashcard_tag_name = "needs-flashcards"
ignores = ["#wip", "- wip"]

# Ignore syncthing conflict files
filename_ignores = "sync-conflict"


# Search for the flashcard_tag_name in the frontmatter.
def needs_flashcards(file_path: str) -> bool:
    if filename_ignores in file_path:
        print("Ignored conflict " + file_path)
        return False
    with open(file_path, "r") as f:
        frontmatter_split_occurances = 0
        for i in ignores:
            if i in f.read():
                print("Ignored " + file_path)
                return False
            f.seek(0)
        for line in f.readlines():
            if "---" in line:
                frontmatter_split_occurances += 1
            if frontmatter_split_occurances >= 2:
                continue
            if flashcard_tag_name in line:
                return True
                print("This needs falschards")
        return False


def add_flashcards(file_path: str):
    start_time = datetime.datetime.now()
    print("Adding flashcards to " + file_path)
    os.system("sh append_flashcards.sh " + file_path)
    end_time = datetime.datetime.now()
    difference = end_time - start_time
    print("Flashcards took " + str(difference) + " seconds")


pattern = arguments[0] + "/**/*.md"

# Grep all files in directory
files = glob.glob(pattern, recursive=True)

# writes = 0

for file in files:
    if needs_flashcards(file):
        print("adds flashcards to " + str(file))
        add_flashcards(file)
        # writes += 1
        # if writes > 3:
        # print("exits")
        # exit()
