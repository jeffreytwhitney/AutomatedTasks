import os

from lib.MicroVuProgram import MicroVuProgram


def _remove_bring_to_metrology_picture(micro_vu: MicroVuProgram) -> None:
    idx = micro_vu.bring_part_to_metrology_index
    if idx == -1:
        return

    del micro_vu.file_lines[idx + 2]
    del micro_vu.file_lines[idx + 1]
    del micro_vu.file_lines[idx]


def _write_file_to_harddrive(micro_vu: MicroVuProgram) -> None:
    try:
        with open(micro_vu.filepath, "w", encoding="utf-16-le", newline="\r\n") as f:
            for line in micro_vu.file_lines:
                f.write(f"{line}")
    except:
        pass


def process_file(filepath: str) -> None:
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
