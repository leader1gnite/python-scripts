#!/usr/bin/env python3

import sys

""" Find the compound percent by using a simple algorithm"""

USAGE = '''
Compound percent

USAGE:
    {script_name} start_money percent years

example: $chmod +x percent.py
$./percent.py 100 10 2
end
'''

USAGE = USAGE.strip()

def compound_percent(args):

    #no arguments provided -- print USAGE and exit with error 
    if len(args) <= 1 or len(args) >=5 :
        print(USAGE)
        exit(-1)


    print(f'Received args: {args}, {len(args)}')
        
    # Separate script name from other args
    script_name = args[0]
    start_money = float(args[1])
    percent = float(args[2])
    years = float(args[3])

    """ So the formula for compound percent is
        result = start_money(1+percent/100)^years
        where result is your final amount of money,
        start_money is your anount of money at the begining
        percent is the rate,
        years is number of years, time that you'll wait
        (bruh, idk the best meaning) 
    """

    result = round(start_money * (pow((1 + percent / 100), years)))

    print(f'And the result is: {result}')
    print(f'Difference between start amount and final: {result-start_money}\n')

if __name__ == '__main__':
    compound_percent(sys.argv)

    


