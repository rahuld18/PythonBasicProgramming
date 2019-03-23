number={
    "1":"one",
    "2":"two",
    "3":"three"
}

phone= input('phone: ')
output=""
for item in phone:
    output+=number.get(item,"!") + " "

print(output)


