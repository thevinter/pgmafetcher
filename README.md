# A simple GitHub repo fetcher to use inside the Arnaldo Program of the IEEE Student Branch of the University Of Brescia

# Usage
* Clone the file into an empty repository
* Generate the dependencies using ```pip install -r requirements.txt```
* Modify the groups.txt file using a line for each group using the format "GROUPNAME ADMINNAME" (Use NULL if the admin name is unknown)
* Create an OAuth Personal token with Repo permissions 

```
1. Login to your Github account.
2. Go to Settings -> Developer Settings ->Personal Access Tokens
3. Click on Generate new token. Confirm your password to continue.
4. Give any description to your token.
5. Under scopes check the "Repo" box
6. Click Generate new token.
```

* The first time the program is run it has to be run with the --token option specifying your token

**General Usage:**
```python3 fetcher.py [ProjectName]```