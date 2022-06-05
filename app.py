#Unstructured Supplementary Service Data
from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "b218babfda4a32a3fb3731197f2560cf827db70d795171cda810253d19fdb01f"
africastalking.initialize(username, api_key)
sms = africastalking.SMS
code = False

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
    if code ==False:
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
            response += "For Finicial institutions, contact helpline for an account"
        #FArmer Menu
        elif text == "1*1":
            #farmer menu
            response = "CON Menu\n"
            response += "1. Market Prices\n"
            response += "2. Loan Services & Finicial help  \n"
            response += "3. Farm Equipment Hire & purchase\n"
            response += "4. Verified Buyers\n"
        elif text == "1*1":
            #Buyer  menu
            response = "CON Menu\n"
            response += "1. Market Prices\n"
            response += "2. Loan Services & Finicial help  \n"
            response += "3. Farm Equipment Hire & purchase\n"
            response += "4. Verified Buyers\n"
        elif text == "1*2":
            #farmer menu
            response = "CON Menu\n"
            response += "1. Market Prices\n"
            response += "2. Loan Services & Finicial help  \n"
            response += "3. Farm Equipment Hire & purchase\n"
            response += "4. Back"
        elif text == "1*3":
            #Finicial Institution Data
            response = "CON Menu\n"
            response += "Input Finicial Instition Access code \n"  
        elif text == "2":
        #sub menu English
        response = "CON Smart Farm a'yimi ra?\n"
        response += "kirikisi ipe isele 'dyia\n"
        response += "1. 'Ba amvu yapi vini ori ezo piri "
        response += "2. 'Ba afa jepiri"
        response += "3. ..."
    

    elif text == "2":
        #sub menu 1
        response = "END Your phone number is {}".format(phone_number)
    elif text == "3":
        try:
            #sending the sms
            sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
            print(sms_response)
        except Exception as e:
            #show us what went wrong
            print(f"Houston, we have a problem: {e}")
    elif text == "1*1":
        #ussd menus are split using *
        account_number = "1243324376742"
        response = "END Your account number is {}".format(account_number)
    elif text == "1*2":
        account_balance = "100,000"
        response = "END Your account balance is USD {}".format(account_balance)
   
    else:
        response = "END Invalid input. Try again."

    return response
else:
    code = False
    response = "Test Insitituion 1 /n"
    response += "Users /n"
    response += "Products /n"
    return 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))

