def common_letter():
    str1 = input('enter a string:')
    str2 = input('enter a string:')

    s1 = set(str1)
    s2 = set(str2)

    lst = s1 & s2

    print(lst)

common_letter()
