
# coding: utf-8

# In[1]:

def check_prime(number):
    if number == 2 or number == 3:
        return True
    elif number < 2 or number%2 == 0:
        return False
    else:
        for divider in range(3, int(number**0.5) + 1, 2):
            if number%divider == 0:
                return False
    return True


# In[4]:

def get_primes(upto_number):
    primes = [2]
    for num in range(3, upto_number + 1, 2):
        if check_prime(num):
            primes.append(num)
    return primes


# In[9]:

def main():
    # when this module is run, it starts here.
    num = int (input('input a positive integer > 1 : '))
    # validate input
    if num <= 1:
        print( 'input must be an integer greater than 1')
        exit
    else:
        my_primes = get_primes(num)
        print (my_primes)
        print ('There are',len(my_primes),' primes <',num)
# call the main function to get started
main()


# In[ ]:



