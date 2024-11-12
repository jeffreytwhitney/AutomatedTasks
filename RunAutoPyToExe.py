import subprocess
import sys


def main():
    # Access command-line arguments
    script_path = sys.argv[1]  # Path to the script you want to convert
    output_name = sys.argv[2]  # Desired name for the executable

    # Construct the command for auto-py-to-exe
    command = [
        "auto-py-to-exe",
        "--pyinstaller-options",
        f"--name={output_name}",
        "--onefile",
        "--noconsole",
        script_path
    ]

    # Run auto-py-to-exe with the specified arguments
    subprocess.run(command)


if __name__ == "__main__":
    main()
