while True:
    name = input("Please enter your name:\n>")
    if name:
        print(f"Hello {name}")
        break
    else:
        print("Please enter your name!")
