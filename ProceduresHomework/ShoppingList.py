
products = {}
productData = open("products.txt")
for line in productData.readlines():
    row = line.split()
    products[row[0]] = row

print (products)

userWanstToBuy = input("Would you like to buy some fruit? ").lower()
userShoppingList = {}
while userWanstToBuy.startswith("y"):
    productChoice = input("Product code and quantity? ").split()
    if products.get(productChoice[0]):
        userShoppingList[productChoice[0]] = productChoice[1]
    else:
        print("Sorry, we don't have any ", productChoice[0])

    userWanstToBuy = input("Would you like to add another fruit? ").lower()

totalCost = 0

for productCode in userShoppingList.keys():
    product = products.get(productCode)
    productName = product[1]
    unitPrice = float(product[2])
    lineCost = unitPrice * int(userShoppingList.get(productCode))
    print(productCode, "\t", productName, "\t\t\t\t", userShoppingList.get(productCode), "\t\t", unitPrice, "\t\t", lineCost)
    totalCost = totalCost + lineCost


print(" Total cost of order", "\t\t\t", totalCost)
print("Thank you for shopping with us today!")
