import requests
import os
import json
import argparse
from git import Repo

parser = argparse.ArgumentParser(description='A github link fetcher')
parser.add_argument("project", help="Uses the following name to fetch all of the repos from github")
parser.add_argument("--token", help="The token of the account that wants to create the repo")
args = parser.parse_args()

TOKEN = ""
project_name = args.project
repo_url = "https://api.github.com/user/repos"

if(args.token == None):
	if os.path.exists("token.ini"):
		with open("token.ini", "r") as token_file:
			TOKEN = token_file.read()
	else:
		print("Please provide a token first with the --token option\n")
else:
	while True:
		temp = input("Do you want to save the current token as the default one? [yn]\n")
		if temp.upper() == "Y":
			with open("token.ini", "w") as token_file:
				token_file.write(args.token)
				TOKEN = args.token
			break
		if temp.upper() == "N":
			TOKEN = args.token
			break
		else:
			print("Please select a valid option\n")

groups = [] 
if os.path.exists("groups.txt"):
	with open("groups.txt", "r") as group_file:
		for g in group_file.readlines():
			line = g.strip()
			print(line)
			groups.append((line.split()[0], line.split()[1]))
else:
	print("Remember to add the group names in the groups.txt file")
	group_file = open("groups.txt", "w")


if(TOKEN != ""):
	folderpath = os.path.join(os.getcwd(), project_name)
	if not os.path.exists(folderpath):
		os.makedirs(folderpath)
		print ('Created:', folderpath)
	for (group, username) in groups:
		if username == "TheTrinity" print("Suca")
		if username != "NULL":
			actual_url = f"https://github.com/{username}/PgAr2021_{group}_{project_name}.git"
			try:
				Repo.clone_from(actual_url, os.path.join(folderpath, group))
				print(f"Repo {actual_url} cloned")
			except:
				print(f"Repo {actual_url} not found")
	headers = {"Authorization": f"token {TOKEN}"}
	data = {"name" : f"{project_name}_WorksArchive"}
	requests.post(repo_url, data=json.dumps(data), headers=headers)

token_file.close()
