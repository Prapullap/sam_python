def sum_oddeven(num):
    sum=0
    for i in range(len(num)):
        if i%2==0 and num[i]%2==0:
            sum+=num[i]
    return sum
num=[int(i) for i in input('Enter a number to find its sum of odd placed even digits:')] 
print('sum:',sum_oddeven(num))
