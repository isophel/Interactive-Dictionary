import json
from difflib import get_close_matches

#loading data from a json file
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))> 0:
        yn  =input( "Did you mean %s Instead? Enter Y if yes or N if no: " %get_close_matches(w,data.keys())[0]) #checking for similarity 
        yn2  = yn.lower() 
        if yn2=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn2=="n":
            return "The word doesn't exist. Please double check it."
        else:
            return " Sorry We didn't understand your Entry"
            
        
    else:
        return "This word doesn't exist in the dictionary"

word =  input('Enter a word:') 

output  = translate(word)

#checking whether to print a list
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
