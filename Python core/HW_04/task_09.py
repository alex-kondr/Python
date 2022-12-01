def is_valid_pin_codes(pin_codes):

    if not pin_codes or len(pin_codes) != len(set(pin_codes)):
        return False

    else:   

        for pin in pin_codes:

            try:

                int(pin)

                if len(pin) != 4:
                    return False
                    
            except ValueError:
                return False            
        
        return True

    
