import re

_regex = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
file_lines = []


def get_file_lines():
    global file_lines
    if not file_lines:
        log_file = r"\\RMS-1Fact-mvu\MicroVu\bin\log.txt"
        with open(log_file, 'r') as file_handle:
            file_lines = file_handle.readlines()

    return file_lines


def extract_date(text):
    return match.group() if (match := _regex.search(text)) else None


def get_most_recent_date_for_machine(machine_name):
    _file_lines = get_file_lines()
    matching_lines = [line for line in _file_lines if line.find(machine_name) > 0]
    return extract_date(matching_lines[-1]) if matching_lines else 'No Data'


earliest_date = extract_date(get_file_lines()[0])
machines = ["rms-microvuy006", "rms-microvuy008", "rms-microvuy011", "rms-microvuy012", "rms-microvuy020",
            "rms-microvuy021", "rms-microvuy024", "rms-microvuy026", "rms-microvuy028", "rms-microvuy029",
            "rms-microvuy031", "rms-microvuy032", "rms-microvuy033", "rms-microvuy035", "rms-microvuy036",
            "rms-microvuy037", "rms-microvuy045", "rms-microvuy046", "rms-microvuy047", "rms-microvuy048",
            "rms-microvuy050", "rms-microvuy051", "rms-microvuy054", "rms-microvuy055", "rms-microvuy057",
            "rms-microvuy058", "rms-microvuy059", "rms-microvuy060", "rms-microvuy061", "rms-microvuy062"]

print(f"Oldest Date in log file: {earliest_date} ")
for machine in machines:
    machine_date = get_most_recent_date_for_machine(machine)
    print(f"Last Run Date for machine: {machine} {machine_date}")
