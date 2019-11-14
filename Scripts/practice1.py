def dupes():
    user_input=list(input("Enter the values: "))
    duplicate=user_input[0]
    for values in user_input:
        if values==duplicate:
            user_input.del(values)
        else:
            return values
        print (user_input)


dupes()


        
