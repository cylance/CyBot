# !cc validates a credit card number

import re, sys
from errbot import BotPlugin, botcmd, arg_botcmd

class cc(BotPlugin):

    @arg_botcmd('pan', type=str)  # flags a command
    def cc(self, msg, pan=None):

        # Test the number for validity
        try:
            r = [int(ch) for ch in str(pan)][::-1]
            validity = (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0
            # Returns true if the algorithm checks out
        except ValueError:
            validity = 0
        
        if validity==0:
            return("The number did not pass the Luhn Check.")
        
        """The function wiki_brand_compare(pan) in this module checks BIN numbers (first 6 digits of pan) against
        data from the Wikipedia page https://en.wikipedia.org/wiki/Payment_card_number."""
        
        #Accuracy is not guaranteed!!!
        # Matching performed in order of most accurate digit groupings
        
        bin_number = pan[:6]
        
        pan_first_1 = int(bin_number[:1])
        pan_first_2 = int(bin_number[:2])
        pan_first_3 = int(bin_number[:3])
        pan_first_4 = int(bin_number[:4])
        pan_first_5 = int(bin_number[:5])
        pan_first_6 = int(bin_number[:6])
        
        # If Wikipedia has a 6 digit match
        if pan_first_6 in range(560221, 560225+1):
            return("The number passed the Luhn Check.  The brand is: BANKCARD")
        
        elif pan_first_6 in range(622126, 622925+1):
            return("The number passed the Luhn Check.  The brand is: DISCOVER")
        
        elif pan_first_6 in [564182, 633110]:
            return("The number passed the Luhn Check.  The brand is: SWITCH")
        
        elif pan_first_6 in range(506099, 506198+1) or pan_first_6 in range(650002, 650027+1):
            return("The number passed the Luhn Check.  The brand is: VERVE")
        
        elif pan_first_6 in range(979200, 979289+1):
            return("The number passed the Luhn Check.  The brand is: TROY")
        
        
        # If Wikipedia has a 5 digit match
        # none as of June 2017
        
        # If Wikipedia has a 4 digit match
        elif pan_first_4 == 5610:
            return("The number passed the Luhn Check.  The brand is: BANKCARD")
        
        elif pan_first_4 in [2014, 2149]:
            return("The number passed the Luhn Check.  The brand is: DINERSCLUB")
        
        elif pan_first_4 == 6011:
            return("The number passed the Luhn Check.  The brand is: DISCOVER")
        
        elif pan_first_4 in range(3528, 3589+1):
            return("The number passed the Luhn Check.  The brand is: JCB")
        
        elif pan_first_4 in [6304, 6706, 6771, 6709]:
            return("The number passed the Luhn Check.  The brand is: LASER")
        
        elif pan_first_4 in [5019, 4175, 4571]:
            return("The number passed the Luhn Check.  The brand is: DANKORT")
        
        elif pan_first_4 in range(2200, 2204+1):
            return("The number passed the Luhn Check.  The brand is: MIR")
        
        elif pan_first_4 in range(2221, 2720+1):
            return("The number passed the Luhn Check.  The brand is: MASTERCARD")
        
        elif pan_first_4 in [6334, 6767]:
            return("The number passed the Luhn Check.  The brand is: SOLO")
        
        elif pan_first_4 in [4903, 4905, 4911, 4936, 6333, 6759]:
            return("The number passed the Luhn Check.  The brand is: SWITCH")
        
        elif pan_first_4 == 5392:
            return("The number passed the Luhn Check.  The brand is: CARDGUARD")
        
        
        # If Wikipedia has a 3 digit match
        elif pan_first_3 in [300, 301, 302, 303, 304, 305, 309]:
            return("The number passed the Luhn Check.  The brand is: DINERSCLUB")
        
        elif pan_first_3 in range(644, 649+1):
            return("The number passed the Luhn Check.  The brand is: DISCOVER")
        
        elif pan_first_3 == 636:
            return("The number passed the Luhn Check.  The brand is: INTERPAYMENT")
        
        elif pan_first_3 in [637, 638, 639]:
            return("The number passed the Luhn Check.  The brand is: INSTAPAYMENT")
        
        
        # If Wikipedia has a 2 digit match
        elif pan_first_2 in [34, 37]:
            return("The number passed the Luhn Check.  The brand is: AMEX")
        
        elif pan_first_2 == 62:
            return("The number passed the Luhn Check.  The brand is: CHINAUNIONPAY")
        
        elif pan_first_2 in [36, 38, 39]:
            return("The number passed the Luhn Check.  The brand is: DINERSCLUB")
        
        elif pan_first_2 == 65:
            return("The number passed the Luhn Check.  The brand is: DISCOVER")
        
        elif pan_first_2 in [50, 56, 57, 58]:
            return("The number passed the Luhn Check.  The brand is: MAESTRO")
        
        elif pan_first_2 in [51, 52, 53, 54, 55]:
            return("The number passed the Luhn Check.  The brand is: MASTERCARD")
        
        
        # If Wikipedia has a 1 digit match
        elif pan_first_1 == 6:
            return("The number passed the Luhn Check.  The brand is: MAESTRO")
        
        elif pan_first_1 == 4:
            return("The number passed the Luhn Check.  The brand is: VISA")
        
        elif pan_first_1 == 1:
            return("The number passed the Luhn Check.  The brand is: UATP")
        
        else:
            return("The number passed the Luhn Check.  The brand is: UNKNOWN")
        
