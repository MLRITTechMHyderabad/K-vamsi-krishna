# #exception handling
# a = int(input("Enter a number "))
# li = [1,2,3,4,5,6]
# try:
#     print(10/a)
#     print(li[20])
# except Exception as e:
# #except (ZeroDivisionError,IndexError) as e:
#     print(e)
# else:
#     print("No Errors")
# finally:
#     print('end')


#Robust calculator

def calculator(a,b, operator):
    try:
        if operator == "+":
            print(a + b)
        elif operator == "-":
            print(a - b)
        elif operator == "*":
            print(a * b)
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError
            print(a / b)
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError
            print(a / b)
        else:
            raise ValueError("Unexpected error")
            # except ZeroDivisionError:
    except ZeroDivisionError as e:
        print("Error: Division by Zero")
    except ValueError as e:
        print("Error: Invalid input")
    except TypeError :
        print("Error:Non-numeric Input")
    except Exception as e:
        print("Error: Unexpected exceptions")

print(calculator(10, 0, "/"))  