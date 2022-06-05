#Unstructured Supplementary Service Data
from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "7fbdf43c5e1adb10199703e845f5c6197917bce4e86a865cf39f2959429fd129"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd logic
    if text == "":
        #main menu
        response = "CON Welcome To Smart Farm Market\n"
        response += "Please select A Language\n"
        response += "1. English\n"
        response += "2. Lugubara \n"
        response += "3. Kiswahili \n"
    elif text == "1":
        #sub menu English
        response = "CON Smart Farm Welcomes You?\n"
        response += "Please choose a category.\n"
        response += "1. Farmer \n"
        response += "2. Buyers \n"
        response += "3. Finicial Institution \n"
        response += "4. Help \n"
    #FArmer Menu
    elif text == "1*1":
        #farmer menu
        response = "CON Menu\n"
        response += "1. Market Prices\n"
        response += "2. Loan leed  \n"
        response += "3. Farm Equipment Hire & Purchase\n"
        response += "4. Verified Buyers\n"
        response += "5. My Account \n"
        response += "0. Back to home\n"
    elif text == "1*1*2":
        response = "CON Categories\n"
        response += "1. Seed Loan\n"
        response += "2. Equipment Loan\n"
        response += "0. Back to home\n"
    elif text == "1*1*2*1":
        response = "CON Available Sources\n"
        response += "1. Centenary Bank\n"
        response += "2.Tellego Development Farmer\n"
        response += "2. Equity Bank\n"
        response += "0. Back to home\n"
    elif text == "1*1*2*1*1":
        response = "CON Loaning Rates\n"
        response += "1.Seed Loan 2% per Month\n"
        response += "0. Back to home\n"
    elif text == "1*2":
        #Buyer  menu
        response = "CON Menu\n"
        response += "1. Market Prices\n"
        response += "2. Available Products \n"
        response += "3. My Account \n"
    elif text in ["1*1*1" , "1*2*1"]:
        #market Prices
        response = "CON Day: Sunday 05/06/2022 \n"
        response += "1. Arua Main Market \n Cassava 1kg @ Ugsh 3000 || Maize 1kg @ 3500\n"
        response += "2. Yumbe Main Market \n Cassava 1kg @ Ugsh 3100 || Maize 1kg @ 3400\n"
        response += "3. Arua Casava Proccessing Industry \n Cassava 1kg @ Ugsh 3550 || Maize 1kg @ ...\n"
        response += "00. More"
    elif text == "1*3":
        #Finicial Institution Data
        response = "CON Menu\n"
        response += "Input Finicial Instition Access Code \n" 
    elif text == "2":
    #sub menu English
        response = "CON Smart Farm ai'mi ra?\n"
        response += "kirikisi ipe isele 'diyi alea\n"
        response += "1. 'Ba amvu yapi vini ori ezo piri \n "
        response += "2. 'Ba afa jepiri \n"
        response += "3.  Mari esuta \n "
    elif text == "0":
        text  = ""
        #sub menu English
        response = "CON Smart Farm Welcomes You?\n"
        response += "Please choose a category.\n"
        response += "1. Farmer \n"
        response += "2. Buyers \n"
        response += "3. Finicial Institution \n"
        response += "For Finicial institutions, contact helpline for an account"
        return response
    else:
        if "1*3*" in text:
            response = "CON Innovations Uganda "
            response += "1. Add a service\n"
            response += "2. Clients\n"
            response += "2. Request for Finicial Data \n"
        else:
            response = "END Feature Unavailable. Try again later."
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))

