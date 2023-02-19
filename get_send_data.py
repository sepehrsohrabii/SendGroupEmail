import re


def get_data():
    # Replace file_path with the path to your text file
    file_path = "outline.txt"

    # Open the file and read its contents
    with open(file_path, "r") as file:
        data = file.read()

    # Define a regular expression pattern to match entire lines starting with "ss://"
    pattern = r"ss://.*$"

    # Use the findall method to extract all lines matching the pattern from the data
    links_list = re.findall(pattern, data, re.MULTILINE)

    # Print the extracted lines
    print(links_list)
    
    return links_list
