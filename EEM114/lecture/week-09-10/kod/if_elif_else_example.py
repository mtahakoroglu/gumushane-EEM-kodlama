flag1, flag2 = False, True
if flag1:
    print("Merhaba!")
elif flag1 and True:
    print("Hola!")
elif flag1 or not flag2:
    print("Hello!")
elif not flag2:
    print("Güle güle dostum.")
elif not flag1 and flag2:
    print("Adios amigo.")
else:
    print("Good bye dude.")