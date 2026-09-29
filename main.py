import math

print("\n====== SMART CALCULATOR ======")

while True:
    print("\n1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Unit convertor")
    print("4. Temperature convertor")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")

    # Basic Calculator
    try:
        if choice == "1":

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            operation = input("\nEnter operation: ")

            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))

            if operation == "1":
                print("\nResult =", a + b)
                print("\n=====================================")
                print("=====================================")

            elif operation == "2":
                print("\nResult =", a - b)
                print("\n=====================================")
                print("=====================================")

            elif operation == "3":
                print("\nResult =", a * b)
                print("\n=====================================")
                print("=====================================")

            elif operation == "4":
                if b == 0:
                    print("Cannot divide by zero")
                else:
                    print("\nResult =", a / b)
                    print("\n=====================================")
                    print("=====================================")
                    
            else:
                print("\nInvalid operation")
                print("\n=====================================")
                print("=====================================")
                
                

        # Scientific Calculator
        elif choice == "2":
            print("\n1. Square")
            print("2. Cube")
            print("3. Power")
            print("4. Square Root")
            print("5. Factorial")

            operation = input("\nEnter operation: ")

            if operation == "1":
                num = float(input("\n\nEnter number: "))
                print("Square =", num * num)
                print("\n=====================================")
                print("=====================================")

            elif operation == "2":
                num = float(input("\nEnter number: "))
                print("Cube =", num * num * num)
                print("\n=====================================")
                print("=====================================")

            elif operation == "3":
                num = float(input("\nEnter number: "))
                power = float(input("Enter power: "))
                print("Result =", num ** power)
                print("\n=====================================")
                print("=====================================")

            elif operation == "4":
                num = float(input("\nEnter number: "))

                if num < 0:
                    print("Cannot find square root of a negative number")
                else:
                    print("Square Root =", math.sqrt(num))
                print("\n=====================================")
                print("=====================================")

            elif operation == "5":
                num = int(input("Enter number: "))

                if num < 0:
                    print("Factorial is not possible for negative numbers")
                else:
                    print("Factorial =", math.factorial(num))
                      
                print("\n=====================================")
                print("=====================================")

            else:
                print("\nInvalid operation")
                print("\n=====================================")
                print("=====================================")

        # Unit convertor
        elif choice == "3":

            print("\n====Unit convertor====")
            print("\n1.Kilometer to meter")
            print("2.Meter to kilometer")
            print("3.Kilogram to Gram")
            print("4.Gram to kilogram")
            print("5.Liter to milliliter")
            print("6.Milliliter to liter ")

            operation = input("\nEnter your choice: ")

            if operation == "1":
                km = float(input("\nEnter kilometer: "))
                print("Meter = ", km*1000)
                print("\n=====================================")
                print("=====================================")

            elif operation == "2":
                m = float(input("\nEnter meters: "))
                print("Kilometers =", m / 1000)
                print("\n=====================================")
                print("=====================================")

            elif operation == "3":
                kg = float(input("\nEnter kilograms: "))
                print("Grams =", kg * 1000)
                print("\n=====================================")
                print("=====================================")

            elif operation == "4":
                g = float(input("\nEnter grams: "))
                print("Kilograms =", g / 1000)
                print("\n=====================================")
                print("=====================================")

            elif operation == "5":
                ml = float(input("\nEnter milliliter: "))    
                print("Liter = ",ml/1000)
                print("\n=====================================")
                print("=====================================")

            elif operation == "6":
                l = float(input("\nEnter liter: "))    
                print("milliliter",l*1000)
                print("\n=====================================")
                print("=====================================")

        
            elif operation == "6":
                f = float(input("\nEnter Fahrenheit: "))
                print("Celsius =", (f - 32) * 5 / 9)
                print("\n=====================================")
                print("=====================================")

            else:
                print("\nInvalid choice")
                print("\n=====================================")
                print("=====================================")

        #Temperature convertor
        elif choice =="4":

            print("\n====Temperature convertor====")
            print("\n1.celsius to fahrenheit")
            print("2.Fahrenheit to Celsius")
            print("3.Celsius to kelvin")  
            print("4.kelvin to celsius")
            print("5.Farenheit to kelvin")
            print("6.Kelvin to farenheit")

            operation = input("\nEnter your choice: ")            
            
            if operation == "1":
                c = float(input("\nEnter Celsius: "))
                print("Fahrenheit =", (c * 9 / 5) + 32)
                print("\n=====================================")
                print("=====================================")

            elif operation == "2":
                f = float(input("\nEnter Fahrenheit: "))
                print("Celsius =", (f - 32) * 5 / 9)
                print("\n=====================================")
                print("=====================================")

            elif operation == "3":
                c = float(input("\nEnter celsius:"))    
                print("Kelvin =",c+273.15)
                print("\n=====================================")
                print("=====================================")

            elif operation == "4":
                k = float(input("\nEnter kelvin:"))     
                print("celsius =",k-273.15)
                print("\n=====================================")
                print("=====================================")

            elif operation == "5":
                f = float(input("\nEnter Fahrenheit: "))
                print("Kelvin =",((f - 32) * 5 / 9)+273.15)
                print("\n=====================================")
                print("=====================================")
            
            elif operation == "6":
                k = float(input("\nEnter kelvin:"))
                print("Fahrenheit =", ((k-273.15) * 9 / 5) + 32)  
                print("\n=====================================")
                print("=====================================")   

            else:
                print("\nInvalid choice")
                print("\n=====================================")
                print("=====================================")                             

            # Exit
        elif choice == "5":
             print("\nThank you for using the calculator!")
            
             break

        else:
            print("\nInvalid choice")

    except ValueError:
        print("\nPlease write only numbers!!!")

