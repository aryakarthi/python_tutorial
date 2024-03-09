
# # try block

def divide():
    divider = int(input("Enter Divider : "))
    divisor = int(input("Enter Divisor : "))
    try:
        x = divider/divisor
    except Exception as e:
        print("Error : " + str(e))
    else:
        print("Output : " + str(x))
    finally:
        print("Finished!")


divide()
