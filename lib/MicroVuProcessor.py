import os
import pathlib
from datetime import datetime

import pymsgbox

from lib.MicroVuProgram import MicroVuProgram


def _remove_bring_to_metrology_picture(micro_vu: MicroVuProgram) -> None:
    idx = micro_vu.bring_part_to_metrology_index
    if idx == -1:
        return

    del micro_vu.file_lines[idx + 2]
    del micro_vu.file_lines[idx + 1]
    del micro_vu.file_lines[idx]


def _remove_dontmeasure_statements(micro_vu: MicroVuProgram) -> None:
    for idx, line in enumerate(micro_vu.file_lines):
        if " (DontMeasure)\n" in line:
            new_line = line.replace(" (DontMeasure)", "")
            micro_vu.file_lines[idx] = new_line


def _write_file_to_harddrive(micro_vu: MicroVuProgram) -> None:
    try:
        with open(micro_vu.filepath, "w", encoding="utf-16-le", newline="\r\n") as f:
            for line in micro_vu.file_lines:
                f.write(f"{line}")
    except:
        pass


def _rename_filepath(dir_path: str, old_rev: str, new_rev: str) -> str:
    dir_path = dir_path.upper()
    current_directory_name: str = pathlib.Path(dir_path).parts[-1].upper()
    if new_directory_name := _replace_rev_name(current_directory_name, old_rev, new_rev):
        return (
            current_directory_name
            if current_directory_name == new_directory_name
            else dir_path.replace(current_directory_name, new_directory_name)
        )
    else:
        return ""


def _replace_rev_name(current_rev_name, old_rev, new_rev):
    new_rev_name = ""
    if "REV" not in current_rev_name:
        return current_rev_name
    if current_rev_name.count("REV") > 1:
        pymsgbox.alert("Value has the letters 'REV' in it more than once, so I don't know what to change.")
        return ""
    search_string = f"REV{old_rev.upper()}"
    if search_string in current_rev_name:
        new_rev_name = current_rev_name.replace(search_string, f"REV_{new_rev}")
        return new_rev_name
    search_string = f"REV {old_rev.upper()}"
    if search_string in current_rev_name:
        new_rev_name = current_rev_name.replace(search_string, f"REV_{new_rev}")
        return new_rev_name
    search_string = f"REV_{old_rev.upper()}"
    if search_string in current_rev_name:
        new_rev_name = current_rev_name.replace(search_string, f"REV_{new_rev}")
        return new_rev_name


def _update_comments(micro_vu: MicroVuProgram, new_rev_letter: str) -> None:
    date_text = datetime.now().strftime("%m/%d/%Y")
    new_comment = f"\\r\\nUprevved to MFG Rev {new_rev_letter.upper()}, no changes. JTW {date_text}."
    current_comment = micro_vu.comment
    current_comment += new_comment
    micro_vu.comment = current_comment


def uprev_microvu(filepath: str, old_rev: str, new_rev: str) -> None:
    if not filepath.upper().endswith(".IWP"):
        return
    if not os.path.exists(filepath):
        return
    micro_vu = MicroVuProgram(filepath)

    if not micro_vu.is_smartprofile:
        old_report_path = micro_vu.report_filepath
        if old_report_path:
            if new_report_path := _rename_filepath(old_report_path, old_rev, new_rev):
                micro_vu.report_filepath = new_report_path

    if micro_vu.is_converted:
        micro_vu.rev_letter_field = new_rev.upper()
        old_export_path = micro_vu.export_filepath
        if new_export_path := _rename_filepath(old_export_path, old_rev, new_rev):
            micro_vu.export_filepath = new_export_path
    else:
        old_partnumber_field = micro_vu.part_number_field
        if new_partnumber_field := _replace_rev_name(old_partnumber_field, old_rev, new_rev):
            micro_vu.part_number_field = new_partnumber_field

    _update_comments(micro_vu, new_rev)
    micro_vu.update_instruction_count()
    _write_file_to_harddrive(micro_vu)


def remove_dont_measure_statements(filepath: str) -> None:
    if not filepath.upper().endswith(".IWP"):
        return
    if not os.path.exists(filepath):
        return

    micro_vu = MicroVuProgram(filepath)
    _remove_dontmeasure_statements(micro_vu)
    micro_vu.update_instruction_count()
    _write_file_to_harddrive(micro_vu)


def remove_metrology_picture(filepath: str) -> None:
    if not filepath.upper().endswith(".IWP"):
        return
    if not os.path.exists(filepath):
        return

    micro_vu = MicroVuProgram(filepath)
    if not micro_vu.has_bring_to_metrology_picture:
        return

    _remove_bring_to_metrology_picture(micro_vu)
    micro_vu.update_instruction_count()
    _write_file_to_harddrive(micro_vu)
