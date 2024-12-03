from asyncore import write
import os


def chapter_62():
    print()
    print('Thursday 25th August 2022')
    print("Python - Chapter 62: Data files")
    print('===============================================')
    print()

    print("If we put all the things we've done on a computer, when it turns off, it would all be deleted.")
    print("This is how to begin to save data processed by python")
    # with open("whatever.txt", "w") as file_to_work_with:
    with open("greet01.txt", "r") as file_to_work_with01:
        text_of_file01 = file_to_work_with01.read()

    print(text_of_file01)

    print("This line opens the text file whatever.txt if it exists.")
    print("If it doesnt exist, Python creates it.")

    print("You could open the file without the initial with, opting to close the file yourself.")
    with open("greet02.txt", "r") as file_to_work_with02:
        text_of_file02 = file_to_work_with02.read()

    print(text_of_file02)

    print("The designation 'whatever.txt' assumes that the file is in the same folder as the Python program.")
    print("If it isnt in the same folder, e.g if its in the data subfolder of the Python folder on Windows, you write:")
    with open("data/greet03.txt", "r") as file_to_work_with03:
            text_of_file03 = file_to_work_with03.read()
    print(text_of_file03)
    print()

    print("On OS(Apple) and Linux, you use a forward slash:")
    # with open("data/whatever.txt", "w") as file_to_work_with:

    print("The variable file_to_work_with can be anything, as long as its legal.")

    return

def chapter_63():

    print()
    print('Thursday 26th August 2022')
    print("Python - Chapter 63: Storing data")
    print('===============================================')
    print()

    print("This second line stores the string in that file (greet.txt)")
    with open("greet01.txt", "w") as file01:
        file01.write("Hello, world! - Greet01")
    print(file01)
    with open("greet02.txt", "w") as file02:
        file02.write("Hello, world!- Greet02")
    print(file02)
    data = 'data'
    os.makedirs(data, exist_ok=True)
    with open("data/greet03.txt", "w") as file03:
        file03.write("Hello, world!- Greet03")
    print(file03)
    return


while(1 == 1):

    print("James's Python app")
    print()

    num = int(input("Enter a number - 1,2 or 3: "))

    if num == 1:
        print("Hello World!")
    elif num == 2:
        print("My name is James")
    elif num == 62:
        chapter_62()
    elif num == 63:
        chapter_63()
    else:
        print("Goodbye World!")

