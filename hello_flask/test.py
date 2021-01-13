def test(num, string):
    counter = 0
    newList = []
    while counter < num:
        counter += 1
        newList.append(string)
    return newList        

print(test(5, 'hello'))