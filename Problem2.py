result = [1, 2]
sum = 0
for item in range(10000):
    sum = result[item] + result[item+1]
    if sum > 4000000:
        break
    else:
        result.append(sum)
    
print result

calculation = 0
for item in range(len(result)):
    if result[item] % 2 == 0:
        calculation += result[item]
print calculation
