# suman wants to drive a car  and he hears that in planet Zortan  there is no age limit for getting a license.

age: int = 16
planet: str = "earth"

if (age<18  and planet == "earth"):
    print("you are not eligible for a  earth")
elif(age>18 and planet == "earth"):
    print("you can apply for a license on earth")


planet = "march"

if age < 18 and planet == "earth":
    # Evaluation - True and False => False
    print("You are NOT eligible for a license on Earth ")
elif age > 16 and planet == "Earth":
    # Evaluation - False and False => False
    print("You can apply for a license on Earth ")
elif age < 16 or planet == "Zortan":
    # Evaluation - True and True => True
    print("You can apply for a Zortanian  license!!")


# monu wants to drive a car  and wants to know if he can apply for a driving license or not

age = int(input("Enter the age : "))

if(age<18):
    print("You are NOT eligible for a license.")
elif(age==18):
    print("You can apply for a Car  license.")
