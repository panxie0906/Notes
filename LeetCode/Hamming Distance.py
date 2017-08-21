x,y = 1,4
xbin = bin(x)
ybin = bin(y)
output = 0

if x>y:
    biggerbin = xbin
    smallerbin = ybin
else:
    biggerbin = ybin
    smallerbin = xbin

lengthMargin = abs(xbin.__len__()-ybin.__len__())

for i in range(lengthMargin):
    smallerbin = smallerbin[:2]+'0'+smallerbin[2:]

for i in range(len(biggerbin)):
    if biggerbin[i] != smallerbin[i]:
        output = output+1

print(output)