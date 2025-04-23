def main():
    # Create and write to a file
    with open("example.txt", "w+") as file:
        file.write("This is a test file.\nLet's try some file operations.\nAnother line here.")

    # Reopen the file to demonstrate seek, tell, and truncate
    with open("example.txt", "r+") as file:
        # Move to the 10th byte
        file.seek(10)
        print("Pointer after seek(10):", file.tell())

        # Read from that point
        data = file.read(20)
        print("Data read from position 10:", repr(data))

        # Go back to the beginning
        file.seek(0)
        print("Pointer after seek(0):", file.tell())
        # Truncate the file at 25 bytes
        file.truncate(25)

    # Read final contents
    with open("example.txt", "r") as file:
        print("\nFinal file content after truncate:")
        print(file.read())

        if __name__ == "__main__":
            main()
