import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)


def translate():
    cursor = con.cursor()

    word = input("Enter the word: ")
    w_forms = [word.lower(), word.title(), word.upper()] 

    for form in w_forms:
        results = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % form).fetchall()
        if results:
            for result in results:
                print(result[0])
        elif len(get_close_matches(word, results)) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, results)[0])
            if yn == 'Y':
                print(results[get_close_matches(word, results)[0]])
            elif yn == 'N':
                print("Please double check it. The word doesn't exist.")
            else:
                print("We didn't understand your entry.")
        else:
            print("Please double check it. The word doesn't exist.")

if __name__ == '__main__':
    translate()               