# !calc performs basic math operations, for example:  2*2*2=8.0

import re, sys
from errbot import BotPlugin, botcmd, arg_botcmd

class calc(BotPlugin):

    @arg_botcmd('tokens', type=str)  # flags a command
    def calc(self, msg, tokens=None):

        # remove whitespace
        tokens = re.sub('\s+', '', tokens)

        # split by addition/subtraction operators
        tokens = re.split('(-|\+)', tokens)

        # takes in a string of numbers, *s, and /s. returns the result
        def solve_term(tokens):
            try:
                tokens = re.split('(/|\*)', tokens)
                ret = float(tokens[0])
                for op, num in zip(tokens[1::2], tokens[2::2]):
                    num = float(num)
                    if op == '*':
                        ret *= num
                    else:
                        ret /= num
                return ret
            except:
                return("Error, please check your input and try again.")
                exit()

        # initialize final result to the first term's value
        result = solve_term(tokens[0])

        # calculate the final result by adding/subtracting terms
        for op, num in zip(tokens[1::2], tokens[2::2]):
            result +=  solve_term(num) * (1 if op == '+' else -1)

        return result

