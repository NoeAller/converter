def eurosToCHF(euros) : 
    return int(euros) * 1.10

euros = input("Enter your value in Euros: ")
chf = eurosToCHF(euros)
print(euros + "€ are " + str(chf) + "CHF")

if(chf >= 100000 ):
    print("This is a lot of money")
