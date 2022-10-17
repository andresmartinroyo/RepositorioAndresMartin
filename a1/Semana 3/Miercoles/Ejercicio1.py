data = {}
data["Name"]=input("Introduce your name: ")
data["email"]=input("Introduce your email: ")
data["number"]=input("Introduce your number: ")
data["gender"]=input("Introduce your gender: ")
data["age"]=input("Introduce your age: ")
for var, pers in data.items():
    print(f"Your {var} is {pers}.")
    