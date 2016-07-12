def dotProduct(listA, listB):
    total = 0
    for i in range(len(listA)):
        total += listA[i] * listB[i]
    return total


print dotProduct([-12, -19, -42, -79, 25, -81], [-80, -31, -37, -22, 92, 5])
print dotProduct([10, -49, -75, -60, -81, 73, -89, -64], [-62, 100, -79, -97, 9, 74, 22, 90])
