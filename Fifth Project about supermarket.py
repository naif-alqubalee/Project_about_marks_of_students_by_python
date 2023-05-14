# name supermarket  
print("subermarket")
# suppose we have 3 cashiers
num_of_cashiers = 3
countw = 1 # counter for loop
while countw <= num_of_cashiers:
    name = input("Enter your name: ") # name of cashier
    id_person = int(input("Enter your id: ")) # id for cashier
    if id_person == 3: # cashier one
        print(f"welcome {name} ")
        count = 1 # counter for repeat operation
        end = 3 # maximum operations limit for today, let's assume 3 operations
        sum_total1 = 0 # variavle to save the total for the report
        while count < end:
            m = input("Enter product name: ") # product name
            k = int(input("Enter the Quantity: ")) # quantity for product
            cost = float(input("Enter the cost for one product: ")) # select value for one product
            total1 = cost * k # To show the final value of the required product
            sum_total1 = sum_total1 + total1
            print(f"the product: {m}\n the quantity: {k}\n the cost for one product is: {cost}\n the total is: {total1} ")
            item_new = input("add or stop: ") # to add aother product
            if item_new == "add":
                count += 1
            else:
                rep1 = input("if you want report write report: ")
                if rep1 == "report":
                    print(f"information:\n name: naif\n id: 3 \n the total for today is : {sum_total1} ")
                # print(f"the operation for today finshed\n thank you for attend today")
                    break
    elif id_person == 4: # cashier two
        print(f"welcome {name} ")
        count2 = 1 # counter for repeat operation
        end2 = 3 # maximum operations limit for today, let's assume 3 operations
        sum_total2 = 0 # variavle to save the total for the report
        while count2 < end2:
            m2 = input("Enter product name: ") # product name
            k2 = int(input("Enter the quantity: ")) # quantity for product
            cost2 = float(input("Enter the cost for one product: ")) # select value for one product
            total2 = cost2 * k2 # To show the final value of the required product
            sum_total2 = sum_total2 + total2 
            print(f"the montag: {m2}\n the kameah: {k2}\n the cost for one is: {cost2}\n the total is: {total2} ")
            item_new2 = input("Add or stop: ") # to add aother product
            if item_new2 == "add":
                count2 += 1
            else:
                rep2 = input("if you want report write report: ")
                if rep2 == "report":
                    print(f"information:\n name: naif\n id: 3 \n the total for today is : {sum_total1} ")
                # print(f"the operation for today finshed\n thank you for attend today")
                    break
    elif id_person == 5: # cashier three
        print(f"welcome {name} ")
        count3 = 1 # counter for repeat operation
        end3 = 3 # maximum operations limit for today, let's assume 3 operations
        sum_total3 = 0 #variavle to save the total for the report
        while count3 < end3:
            m3 = input("Enter product name: ") # product name
            k3 = int(input("Enter the quantity: "))# quantity for product
            cost3 = float(input("Enter the cost for one product: ")) # select value for one product
            total3 = cost3 * k3 # To show the final value of the required product
            sum_total3 = sum_total3 + total3
            print(f"the montag: {m3}\n the kameah: {k3}\n the cost for one is: {cost3}\n the total is: {total3} ")
            item_new3 = input("Add or stop: ") # to add aother product
            if item_new3 == "add":
                count3 += 1
            else:
                rep3 = input("if you want report write report: ")
                if rep3 == "report":
                    print(f"information:\n name: naif\n id: 3 \n the total for today is : {sum_total3} ")
                # print(f"the operation for today finshed\n thank you for attend today")
                    break
    else: # this for if the user enter the wrong id or name
        print(f"wrong input, please check your id again") 
        break
    countw += 1 # to follow the cashier
# rep1 = input("if you want report write report: ")
# if rep1 == "report":
#     print(f"information:\n name: naif\n id: 3 \n the total for today is : {sum_total1} ")
#         # f"information:\n name: ali\n id: 4 \n the total for today is : {sum_total2} \n"
#         # f"information:\n name: saleh\n id: 5 \n the total for today is : {sum_total3} ")
#     print(f"Finshed")
else:
    print(f"see you soon")

# To request the report, it must that work all cashiers