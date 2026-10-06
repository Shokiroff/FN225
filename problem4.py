import json
from os import system

def check_admin_exists(admin: list[dict],admin_id: int)-> str:
	for admin in admins:
		if admin["admin_id"] == admin_id:
			return admin["admin_name"]

if __name__ =="__main__":
	with open("users.json","rt",encoding = "utf-8") as file:
		admins = json.load(file)
		admin = check_admin_exists(admins,4)
		print(f"Admin topildi: {admin}")
