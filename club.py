#check empty()
import csv

#Custom error #1
class PassError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Unrecognizable pass token for {self.name}."
    
def main():
    add_members()
    show_members()

def show_members():
    print("\n\nMembers-")

    #reading from file(members.csv)
    with open("members.csv") as file:
        reader = csv.DictReader(file)

        for line in reader:
            print(f"Name: {line['name']}\nAge: {line['age']}\nPass: {line['pass']}\n")


def add_members():
    with open("members.csv", 'a', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "pass"])

        #writing to file(members.csv)
        for person in entrees():
            try:
                _ = int(person["age"])
                
                if person["pass"] != "True" and person["pass"] != "False":
                    raise PassError(person["name"])
            except ValueError:
                print(f"Invalid age for {person['name']}.")
            except PassError as e:
                print(e)
            else:
                if int(person["age"]) >= 21 and person["pass"] == "True":
                    if not no_repeat(person):
                        writer.writerow(person)

                        print(f"{person['name']} accepted.")
                    else:
                        print(f"{person['name']} is already a member.")
                else:
                    print(f"{person['name']} is not allowed to enter.")

def entrees(): #helper method to add_members()
    people = []

    #adding entrees to an object
    with open("entrees.csv") as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            people.append(line)
        
    #empty()

    return people

def empty(): #helper method to entrees()
    #deleting information from file(entrees.csv)
    with open("entrees.csv", 'w') as file:
        writer = csv.writer(file, fieldnames=["name", "age", "pass"])

        writer.writerow(["name", "age", "pass"])  

def no_repeat(person): #helper method to add_members()
    repeat = False

    #checking for duplicity
    with open("members.csv") as file:
        reader = csv.DictReader(file)

        for line in reader:
            if line == person:
                repeat = True
                break
            else:
                repeat = False
        
    return repeat

if __name__ == "__main__":
    main()