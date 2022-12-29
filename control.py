import const
import calculator
import loging

def parse(text):
    try:
        if text == "/help":
            result = const.help_mess
            loging.log(text)
        else:
            result=calculator.calc(text)
    except:
        result=const.error_mess
        loging.log("Error: \t" + text)
    return result    
 
#print(parse(input()))