def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is python week five assignment containing file how to work with files") #line with text only
            file.write("123456789") # line with numbers only
            file.write("This is python week 5 assignment containing file how to work with files") # line with numbers and text
        print("File created successfully.")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        print("File creation process completed.")

# Reading the file
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("File reading process completed.")


# Appending files
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is python assignment from Power Learn Projet(appended)") #line with text only
            file.write("987654321") # line with numbers only
            file.write("This is python assignment from PLP Africa")  # line with numbers and text
        print("Content appended to my_file.txt.")
    except PermissionError as e:
        print(f"Permission error while appending: {e}")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
