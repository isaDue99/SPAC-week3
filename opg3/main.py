# python data migration assignment

# task: create a script that reads data from a source file and writes them to a destination file. emphasis on error handling !!


# facts: 
#   we dont know how many rows or columns were working with
#   we dont know if first line will contain headers or actual data
#   we dont know what kinds of data is supposed to go in each column, so cant look for type-correctness
#   this is a data migration tool; dont take data out and dont edit it without being 120% sure we can do it right


source_path = "source_data.csv"
destination_path = "destination_data.csv"

# assignment only requires we migrate the (errorful) data from source to destination without crashing, so I've implemented a few options:
#   header_exists variable, can be used to indicate whether csv file has a header row we can use for (limited) typechecking and stuff
header_exists = True

#   do_corrections variable, tells us if user wants the data to be (conservatively) cleaned up or migrated as-is
do_corrections = True



def process_csv(src: str, dest: str, header=False, correct_data=False) -> None:
    """
    Migrates data from file at path (src) to file at path (dest), writing anything notable into an extra column found in (dest)

    If file has a header in the first row (header=True) then it will be used for more accurate logging.
    If correct_data is set to True, then output will be altered to (conservatively) fix perceived errors. Limited to removing whitespace and empty rows and extra cells.
    """

    # testing that destination is good, before we process all that data
    with open(dest, "w") as f:
        pass

    with open(src, "r") as f:
        input = f.readlines()

    if len(input) == 0:
        print(f"Source file \"{source_path}\" is empty. No data is migrated. Exiting...")
        return

    output = process_data(input, header, correct_data)

    if len(output) > 0:
        with open(dest, "w") as f:
            f.writelines(output)


def process_data(data: list[str], header=False, correct_data=False) -> str:
    """
    Processes the data in the source csv file. 
    If file has a header in the first row (header=True) then it will be used for more accurate logging.
    If correct_data is set to True, then output will be altered to (conservatively) fix perceived errors. Limited to removing whitespace and empty, extra cells.

    BUG: With header=True, correct_data=False, if a row of data both has extra datacells and missing data, 
    then typechecks of the datacells following the empty ones may be incorrect.

    Returns output (csv-formatted string), with extra column noting any weirdness
    """

    output = []

    if header:
        # approach for if we have a header row
        # can log: emptyness, type correctness, row length correctness
        row_len, types = get_header_info(data[0])

        for i in range(len(data)):
            row = data[i].strip().split(",")
            
            # header row comes first and doesnt need to be checked
            if i == 0:
                output.append(to_csv_string(row))
                continue

            if correct_data and "" in row:
                # remove extra empty spaces
                while len(row) > row_len:
                    row.remove("")

            log = ""
            # check the full-row issues first:
            if row == ([""] * row_len):
                if correct_data:
                    # dont add this row to output
                    continue
                else:
                    log = "MISSING ROW;"
            else:
                # now we check each cell of the row
                skips = 0
                for j in range(len(row)):
                    cell = row[j]
                    if cell == "" and len(row) > row_len:
                        log = log + f"{j+1}:EXTRA CELL; "
                        skips += 1
                    elif cell == "":
                        log = log + f"{j+1}:MISSING {types[j-skips]};"
                    elif not type_valid(cell, types[j-skips]):
                        if correct_data and types[j-skips] == "name":
                            cell = cell.strip()
                            row[j] = cell
                            if not type_valid(cell, types[j-skips]):
                                log = log + f"{j+1}:INVALID VALUE FOR TYPE {types[j-skips]}; "
                        else:
                            log = log + f"{j+1}:INVALID VALUE FOR TYPE {types[j-skips]}; "
            row.append(log)
            output.append(to_csv_string(row))

    else:
        # approach for if we dont have a header row
        # can log: emptyness
        for line in data:
            row = line.strip().split(",")
            
            # count empty cells
            empty_cells = 0
            for cell in row:
                if cell == "":
                    empty_cells += 1

            # check how empty row is
            if empty_cells == len(row):
                if correct_data:
                    # dont add this row to output
                    continue
                else:
                    row.append("ROW MISSING")
            elif empty_cells > 0:
                row.append("BAD FORMAT")

            output.append(to_csv_string(row))

    return output

def type_valid(cell: str, type: str) -> bool:
    """
    Checks whether content of a cell is valid for its perceived type. 
    
    Limited the types we know to look for in the header, currently: (positive, rational) number, name, email.
    If type is None then any value in cell is valid.
    """

    if type == "number":
        # is cell a number and positive?
        try:
            num = float(cell)
            if num > 0:
                return True
        except ValueError:
            return False
    elif type == "name":
        # is cell a name (string consisting of two or more words)? and no preceding or trailing whitespace?
        if len(cell.split()) > 1 and len(cell) == len(cell.strip()):
            return True
    elif type == "email":
        # is cell an email? (string formatted like an email. we take the easy way out here)
        if "@" in cell and ".com" in cell:
            return True
    elif type == None:
        return True
    return False


def to_csv_string(row: list[str]) -> str:
    """
    Joins a list of values into a csv-format: ["a", "b", "c", "d"] -> "a,b,c,d\\n"
    """

    return ",".join(row) + "\n"
        

def get_header_info(header: str) -> tuple[int, list[str]]:
    """
    Retrieve info from the header row (string) of a csv file. not perfect!

    Returns length of rows AND list with each column's types where possible, otherwise None
    """

    # if header column contains these words then we have a clue as to what kind of data could be in the rows
    header_field_types = {
        "number" : ["customer_id", "purchase_amount"],
        "name" : ["name"],
        "email": ["email"]
    }

    h = header.strip().split(",")

    types = []
    for label in h:
        if label in header_field_types["number"]:
            types.append("number")
        elif label in header_field_types["name"]:
            types.append("name")
        elif label in header_field_types["email"]:
            types.append("email")
        else:
            types.append(None)
    
    return len(h), types



try:
    process_csv(source_path, destination_path, header_exists, do_corrections)

except FileNotFoundError:
    print(f"Couldn't find source data file \"{source_path}\". Exiting...")
    exit(1)

except PermissionError:
    print(f"Program doesn't have permission to write to \"{destination_path}\". Please obtain permission or choose other destination file. Exiting...")
    exit(1)