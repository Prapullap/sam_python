value=int(input('Enter the ammount:'))
ten_rs_coin=value//10
temp1=value%10
five_rs_coin=temp1//5
temp2=temp1%5
two_rs_coin=temp2//2
temp3=temp2%2
one_rs_coin=temp3//1

print('It makes')
print(f'''     {ten_rs_coin}: ten rupees coin,
    {five_rs_coin}: five rupees coin,
    {two_rs_coin}: two rupees coin ,
    {one_rs_coin}: one rupee coin'''
                   )
