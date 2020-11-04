def logo():

    print ("███████████████▀█████████████████████████████████")
    print ("█▄─▄▄─█▄─▄█─▄▄▄▄███▄─▄████▀▄─██─▄─▄─█▄─▄█▄─▀█▄─▄█")
    print ("██─▄▄▄██─██─██▄─████─██▀██─▀─████─████─███─█▄▀─██")
    print ("▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀")
    print (" By. Dylan Dela Cruz.")

logo()

def consonant(word):

    index =0

    while (word[index]not in["a","e","i","o","u","A","E","I","O","U"]):

        index=index+1

    return word[index:]+word[0:index]+"ay"

def vowel(word):

    return word+"way"

def main():

    text = input("Please enter the text you would like to translate:")

    splitText = text.split(" ")

    pigLatinText =""

    for word in splitText:

        if(word[0]in["a","e","i","o","u","A","E","I","O","U"]):

            pigLatinText+=vowel(word)+" "

        else:

            pigLatinText+=consonant(word)+" "

        print(pigLatinText[:-1])

if __name__=="__main__":

    main()
    
restart=input("Would you like to translate another text y/n?:")

if restart=="y":

    main()
    
else:
    exit()

    main()
    
    

