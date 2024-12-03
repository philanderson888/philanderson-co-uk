print("all projects")
print("============")

def chapter_53():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name

    import json

    pid4343 = '{"last_name": "Taleb"}'
    x = json.loads(pid4343)
    pid4344 = {"last_name": "Anand"}
    pid4345 = {"last_name": "Lin"}
    pid1298 = {"last_name": "Nilsson"}

    print("Patient 4343's last name is " + str(x["last_name"]))
    print("Patient 4344's last name is " + pid4344["last_name"])
    print("Patient 4345's last name is " + pid4345["last_name"])
    print("Patient 1298's last name is " + pid1298["last_name"])
    print(" ")

#============================================================================================

def chapter_57():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")
    class Patient():
        def __init__(self, last_name, first_name, age):
            self.last_name = last_name
            self.first_name = first_name
            self.age = age

    pid4343 = Patient("Taleb", "Sue", 61)
    pid4344 = Patient("Anand", "Punya", 29)
    pid4345 = Patient("Lin", "Lilly", 48)
    pid1298 = Patient("Nilsson", "Rhonda", 33)

    # To get Sue Taleb's age:
    age_of_patient = pid4343.age
    # To display it:
    print("age of patient is " + str(age_of_patient))

    print(f"First patient - {pid4343.first_name} {pid4343.last_name}, age {pid4343.age}") 
    print(f"Second patient - {pid4344.first_name} {pid4344.last_name}, age {pid4344.age}")
    print(f"Third patient - {pid4345.first_name} {pid4345.last_name}, age {pid4345.age}")
    print(f"Fourth patient - {pid1298.first_name} {pid1298.last_name}, age {pid1298.age}")
    print(" ")

#=======================================================================================================

def chapter_59():
    print("")
    print("Friday 02/09/22")
    print("Using methods for functions")
    print("====================================")
    print("")

    # Methods
    class Patient:
      def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    # function to check if patients are over 21:
      def age_check(self):
        if self.age > 21:
            print(self.first_name + " " + self.last_name + " is not a minor, she is over 21.")
        else:
         print(self.first_name + " " + self.last_name + " is a minor, they are younger than 21.")

    pid4343 = Patient("Taleb", "Sue", 61)

    # This is a method:
    pid4343.age_check()

#=============================================================================================================================================================================================================================================


user_input = ""
while user_input != "q":
  user_input = input("Enter a chapter, or q to quit:")
  print(f"chapter {user_input}:")

  if user_input != "q":

    if user_input == "53":
        chapter_53()
    
    elif user_input == "54":
        chapter_53()

    elif user_input == "55":
        chapter_53()
    
    elif user_input == "56":
        chapter_53()

    elif user_input == "57":
        chapter_57()

    elif user_input == "58":
        chapter_57()

    elif user_input == "59":
        chapter_59()

    elif user_input == "60":
        chapter_59()