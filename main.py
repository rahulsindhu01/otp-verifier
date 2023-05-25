#importing the required modules in our file
import random
from twilio.rest import Client

# generating a random 6 digit number 
otp = int(random.randint(100000, 999999))

# essential credentials required for the working of twilio api that we used to send the otp
account_sid = "{your account sid here}"

auth_token = "{your account auth token here}"

client = Client(account_sid, auth_token)

user_mobile_number = input("Enter your mobile number:")
#sending the otp to client
msg = client.messages.create(
  
  
      body=f"Your OTP is{otp}",
      from_= "+15672352207",
      to= user_mobile_number 

    )

#getting the otp from user
otp_by_user = int(input("Enter your OTP:"))

# verifying if the otp is correct or not as entered by the user
if otp == otp_by_user:
  print("OTP verified")
else:
  print("Incorrect OTP") 
