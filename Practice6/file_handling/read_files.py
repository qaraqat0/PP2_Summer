
def create_sample_file():
    with open("sample.txt", "w") as file: 

        file.write("Hello, My name is Karakat.\n")
        file.write("I am studying Python.\n")
        file.write("I am learning to work with files.\n")
        file.write("That's it.\n")
        file.write("Bye.\n")
    
create_sample_file()


def read_file_contents():

    #Read file at once
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
    
    #Read line by line
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
    
    #Read all lines into a list
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"  Line {i}: {line.strip()}")

read_file_contents()