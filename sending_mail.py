import smtplib
import requests
    
try:
    to = input("ENTER RECIVER EMAIL ADDRESS :- ")
    url = "https://mailcheck.p.rapidapi.com/"

    querystring = {"domain":to}

    headers = {
        "X-RapidAPI-Key": "923a211b74msh68f1693f786b3ebp1492b4jsnf8576e78851c",
        "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    if response.json()['valid'] == True:
        sub = input('Subject :-')
        mess  = input('Message :-')
        print('connecting to smtplib')
        mail = smtplib.SMTP('smtp.gmail.com',587)
        print('connecting to email address')
        mail.starttls()
        mail.login('dhairyaajwani2002@gmail.com','ehajvqnlttrfwuvi')
        print('sending email')
        mail.sendmail('dhairyaajwani2002@gmail.com',to,'Subject : '+sub+ '\n\n'+mess )
        print("Sended successfully")
    else:
        print('invalid email address')
except Exception as e:
    print(e)
