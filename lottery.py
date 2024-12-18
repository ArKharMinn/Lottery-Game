import secrets
import sys

secretNumber = secrets.SystemRandom()

while True:
    print('Welcome to our game')
    press1 = int(input("Press 1 to Read Rule or Press 2 to Play Games:>"))
    if press1==1:
        print('>Age must be more than 18')
        print('>Show Money more than 5000')
        print('>You must use more than 1000 each time')
    elif press1==2:
        print("Now, You can play game")
        name=input('Enter your name :')
        age=int(input('Enter your age :'))

        while len(name)>2 and age >17:
            print('Now You can play game')
            print('Welcome :> ',name)

            while True:
                money = int(input("Please Enter your show money :"))
                while money>=5000:
                    while True:
                        print('This is your money $',money)
                        inputMoney=int(input('Place a Bet'))
                        luckyNumber=int(input('Enter your lucky number'))

                        systemNumber = secretNumber.randint(10,99)
                        
                        if systemNumber==luckyNumber:
                            print('You are winner! Lucky number is',systemNumber)
                            money= (inputMoney*10)+money
                            print('This is your money ',money)
                            quit = int(input("Press 0 to play again or Press Any key to exist:"))
                            if quit != 0:
                                sys.exit()
                            else :
                                continue
                            break
                        else :
                            print('Try Again... Lucky Number is' , systemNumber)
                            money=money-inputMoney
                        
                        if money<1000:
                            print('You have not enough Money ',money)
                            break
                        
                print('Your money is lower than 5000')

        print('Please read again the rule')