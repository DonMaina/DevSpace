# Program to read a file and write a modified version to a new file

def modify_content(content):
    """
    Modify the file content in some way.
    For example: convert text to uppercase.
    """
    return content.upper()

try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")
    #notes.txt
    
    # Try opening and reading the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Create a new file name for output
    new_filename = "modified_" + filename

    # Write modified content to new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified content written to '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You do not have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
