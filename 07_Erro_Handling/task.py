num=input()
num2=input()
try:
    avg=(int(num)+int(num2))/2
except Exception as err:
    print(err)
finally:
    print(avg)
    print("final statement")