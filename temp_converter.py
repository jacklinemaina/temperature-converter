temp=input("input temperatute to convert):")
degree=int(temp[:-1])
i_convention=temp[-1]
if i_convention.upper()=="c":
    results=int(round((9*degree)/5+32))
    o_convention="fahrenheit"
elif i_convention.upper()=="F":
    results=int(round((degree-32)*5/9))
    o_convention="celsius"
else:
    print("input proper convention.")
    quit()
    print("the temperature in",o_convention,"is",result,"degree.")