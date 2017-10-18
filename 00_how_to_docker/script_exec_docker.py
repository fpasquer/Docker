#!/usr/bin/python3

import os
import sys

PATH_CURENT_DIR = os.getcwd()
CONTENT_PATH_CURENT_DIR = os.listdir(PATH_CURENT_DIR)
CURENT_FILE_NAME = sys.argv[0].replace("./", "")
LIST_FILE_NAME = []

def execute_shell_cmd(SHELL_COMMAND):
    print ("\033[32m" + SHELL_COMMAND + "\033[0m")
    OUTPUTS = os.popen (SHELL_COMMAND).read()
    ARRAY_OUTPUTS = OUTPUTS.split("\n");
    for OUTPUT in ARRAY_OUTPUTS:
        if len(OUTPUT) > 0:
            print ("\t>\033[31m" + OUTPUT + "\033[0m<")
            os.system (OUTPUT)

#set LIST_FILE_NAME with the content of PATH_CURENT_DIR (without the name of this script)
for FILE_NAME in CONTENT_PATH_CURENT_DIR:
    if FILE_NAME != CURENT_FILE_NAME:
        LIST_FILE_NAME.append(PATH_CURENT_DIR + "/" + FILE_NAME)

#show the content of LIST_FILE_NAME
for LINE_FILE_NAME in LIST_FILE_NAME:
    execute_shell_cmd("cat " + LINE_FILE_NAME)
