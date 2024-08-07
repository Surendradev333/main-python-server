def main():
    firstname =input("enter firstname:")
    lastname= input("enter lastname:")
    age=int(input("enter age:"))
    full_name(firstname,lastname,age)

def full_name(firstname,lastname,age):
    if age==0:
        print(f"your full name is {firstname} {lastname} and please enter correct age")
    elif age>=18 and age<80:
        print(f"your full name is {firstname} {lastname} and you are major")
    elif age>0 and age<18:
        print(f"your full name is {firstname} {lastname} and you are kid")
    elif age>=80:
        print(f"your full name is {firstname} {lastname} and you are senior citizen")
    elif age<0:
        print(age)
        print(f"your full name is {firstname} {lastname} and you are lucky")
     
if __name__ == "__main__":
    main()
    
