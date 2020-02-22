def smiling_monkey(a_smiling, b_smiling):

    if a_smiling and b_smiling:
        print('both smiling, were are in trouble')
    elif not a_smiling and not b_smiling:
        print('neither is smiling, were are in trouble')

    else:
        print('were are safe')

a_smiling=False
b_smiling =True
smiling_monkey(a_smiling, b_smiling)