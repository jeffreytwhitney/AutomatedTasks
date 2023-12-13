import subprocess


def run_powershell_script(script_path, *params):
    commandline_options = [
        "powershell.exe",
        "-ExecutionPolicy",
        "Unrestricted",
        script_path,
    ]
    for param in params:
        commandline_options.append("'" + param + "'")

    process_result = subprocess.run(
        commandline_options,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    print(process_result.returncode)
    print(process_result.stdout)
    print(process_result.stderr)

    if process_result.returncode == 0:
        Message = "Success !"
    else:
        Message = "Error Occurred !"

    return Message
