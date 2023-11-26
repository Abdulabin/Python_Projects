import os
## Change the path 
os.chdir(r"C:\Users\abdul\Downloads\PROJECTS\Python_Projects\Details_manager")

class UserDetailsManager() :
    def __init__(self):
        os.makedirs(f"{os.getcwd()}/Details", exist_ok=True)
        os.chdir(f"{os.getcwd()}/Details")
        self.user = input("Exixting User Press 'E' OR New User Press 'N' ").upper()
        if self.user == "E" :
            self.__existing_user()
        elif self.user == "N":
            self.__new_registration()
        else:
            print("Invalid Input")
    def __existing_user(self):
        try:
            self.User_name = input("Enter Your User Id ").title()
            if f"{self.User_name}.txt" not in os.listdir(f"{os.getcwd()}"):
                raise Exception
        except Exception:
            print("User Not Found ")
        else:
            self.__password_validate()
    def __password_validate(self):
        for num in range(4):
            try:
                self.__rfile = open(f"{self.User_name}.txt")
                User_Password = input("Enter Your Password ")
                self.__rfile.readline()
                check=self.__rfile.readline().strip()
                if check!=User_Password:
                    raise Exception
            except Exception:
                if num==3:
                    break
                print(f"\nInvalid Password {3 - num} Attempt Left")
            else:
                print("\nLogin Succesfull ")
                print(self.__rfile.read())
                self.__rfile.close()
                break
    def __new_registration(self):
        try:
            NUser_name = input("Set Your User Id ")
            for x in os.listdir(f"{os.getcwd()}"):
                if x.startswith(NUser_name.title()):
                    raise Exception
        except Exception:
            print("User Already Exists ")
        else:
            self.__Nuser_file = open(f"{NUser_name.title()}.txt","w+")
            NUser_Password = input("Set Your Password ")
            self.__Nuser_file.write(f"{NUser_name}\n{NUser_Password}\n")
            self.__Personal()
            self.__Education()
            self.__Professional()
            self.__Nuser_file.close()

    def __Personal(self):
        name=input("Enter Your Full Name ")
        Gender = input("Enter Your Gender ")
        Place = input("Enter Your Home Town ")
        Age = input("Enter Your Age ")
        Dob = input("Enter Your Date Of Birth ")
        self.__Nuser_file.write(f"\nPersonal Details:-\nName :- {name}\nGender :- {Gender}"
                                f"\nHome Town :- {Place}\nAge :- {Age}\nDate Of Birth :- {Dob}\n")
    def __Education(self):
        Collage_name = input("Enter Your Collage Name ")
        Joining_year = input("Enter Your Joining Year ")
        Passout_year = input("Enter Your Passout Year ")
        Cgpa = input("Enter Your Cgpa ")
        Location = input("Enter Your Location ")
        self.__Nuser_file.write(f"\nEducational Details:-\nCollage Name :- {Collage_name}\n"
                                f"Joining Year :- {Joining_year}\nPassout Year :- {Passout_year}"
                                f"\nCgpa :- {Cgpa}\nSalary :- {Location}\n")
    def __Professional(self):
        Company_name = input("Enter Your Company Name ")
        Joining_year = input("Enter Your Joining Year ")
        Experience = input("Enter Your Experience ")
        Salary = input("Enter Your Salary ")
        self.__Nuser_file.write(f"\nProfessional Details:-\nCompany Name :- {Company_name}\n"
                                f"Joining Year :- {Joining_year}\nExperience :- {Experience}\nSalary :- {Salary}\n")

User1=UserDetailsManager()

