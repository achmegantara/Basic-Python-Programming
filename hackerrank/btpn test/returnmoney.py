def returnMoney(price, pay):
    # validation input
    if price % 1000 == 0 and pay % 100000 == 0 and pay > price:
        returnPayments = pay - price
        nomPayments = []
        nominal = [100000, 20000, 5000, 2000, 1000]
        i = 0
        #divide nominal into several money
        while(i < len(nominal)):
            if returnPayments >= nominal[i]:
                nomPayments.append(nominal[i])
                returnPayments = returnPayments - nominal[i]
            else:
                i = i + 1

        print(nomPayments)
    else:
        print("Invalid input")


price = int(input("Input total price: "))
pay = int(input("Input total payments: "))
returnMoney(price, pay)
#
