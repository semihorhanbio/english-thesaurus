import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w_forms = [w.lower(), w.title(), w.upper()] 
    for form in w_forms:
        if form in data:
            return data[form]
            
    if len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "Please double check it. The word doesn't exist."
        else:
            return "We didn't understand your entry."
    return "Please double check it. The word doesn't exist."

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)        