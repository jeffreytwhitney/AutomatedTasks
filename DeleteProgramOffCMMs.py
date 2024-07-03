import os
import shutil
import sys
from tkinter import simpledialog


def delete_cmm_program(cmm_location: str, cmm_program_name: str):
    for root, dirs, files in os.walk(cmm_location):
        for dir in dirs:
            found_it = dir.find(cmm_program_name)
            if found_it > -1:
                shutil.rmtree(dir, ignore_errors=True)
    return


def call_delete(cmm_program_name: str):
    delete_cmm_program("\\\\Rms-cmmx006\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\rms-cmmx007\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\rms-cmmx008\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx010\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx012\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx014\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx019\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx020\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx021\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx022\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx024\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx025\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx028\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx030\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx031\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx032\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx033\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx036\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx037\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx038\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx039\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx040\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx041\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx042\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx043\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx048\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx050\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx051\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx052\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx053\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx054\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx056\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx057\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx058\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx059\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx060\\cmm\\", cmm_program_name)
    delete_cmm_program("\\\\Rms-cmmx061\\cmm\\", cmm_program_name)


def trim_program_name(cmm_program_name: str):
    space_loc = cmm_program_name.rfind(" ")
    space_slash = cmm_program_name.rfind("\\")
    return cmm_program_name[space_slash + 1:space_loc] if space_loc else cmm_program_name


n = len(sys.argv)

if n == 1:
    program_name = simpledialog.askstring("Program Name", "Enter Program Name:")
    call_delete(program_name)
else:
    for i in range(1, n):
        new_file = trim_program_name(sys.argv[i])
        call_delete(new_file)
