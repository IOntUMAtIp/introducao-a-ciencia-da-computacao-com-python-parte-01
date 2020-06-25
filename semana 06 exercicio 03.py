def incomodam(quant):
    if quant < 1:
        return ""
    else:
        return "incomodam " + str(incomodam(quant - 1))

def elefantes(quant, j = 1):
    if j <= quant:
        if j == 1:
            return ("Um elefante incomoda muita gente\n" + str(elefantes(quant, j + 1)))
        else:
            return str(
                       str(j) + 
                       " elefantes " + 
                       str(incomodam(j)) + 
                       "muito mais\n" + 
                       str(j) +
                       " elefantes incomodam" +
                       " muita gente\n" + 
                       str(elefantes(quant, j + 1)))
                
    return ""
