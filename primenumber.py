while(True):

    num = int(input("Enter Number!"))
    if num<=1:
        print("Number is not Prime!")
    else:
        is_prime = True
        i = 2
        while i<num:
            if num%i==0:
                is_prime = False
                break
            else:
                i +=1
        if(is_prime):
            print("Number is Prime!" )
        else:
            print("Number is not Prime!")