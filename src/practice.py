
arun=[5,8,2,10,"arjun"]

arun.append("verma")
print(arun[-1])
arun[4]="ARJUN"
print(arun)
arun.insert(2,"inserted value")
print(arun)

if(len(arun) <5):
    print("Length less than 5")
else:
    print("length more than 5 . Length is " + str(len(arun)))

a = 6
if(a == 1):
    print("1st")
elif(a == 2):
    print("2nd")
else:
    print("3rd")