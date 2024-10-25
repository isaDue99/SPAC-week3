# python logfile analysis assignment

### task 1: create a virtual environment (with a requirements.txt) to develop in
# done


### task 2: read a logfile, filter certain messages, sum these up in a new file

# these could be commandline arguments/user input in a real script
log_path = "app_log.txt"
searching_for = ["ERROR", "WARNING"]


def filter2file(filename: str, str: str, helpful=True):
    """
    Searches a file at path (filename) for the string (str) and saves each line that (str) appears in into a new file "{str} - {filename}"

    Also prints count of relevant lines and the latest relevant entry in the log to the terminal. Can be silenced by setting (helpful) to False
    """

    output_path = f"{str} - {filename}"
    output = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if str in line:
                output.append(line)

    if len(output) > 0:
        if helpful:
            print(f"Found {len(output)} lines containing \"{str}\". Saved in file \"{output_path}\".")
            latest = output[-1]
            print(f"Latest entry in log is:\n   {latest}")
        with open(output_path, "w") as f:
            f.writelines(output)
    else:
        if helpful:
            print(f"Found no lines containing \"{str}\".")


try:
    for text in searching_for:
        filter2file(log_path, text)

except FileNotFoundError:
    print(f"couldnt find {log_path} in directory. closing...")
    exit(1)