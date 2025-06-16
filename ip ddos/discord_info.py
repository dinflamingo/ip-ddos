import sys, requests

token = sys.argv[1]
h = {"Authorization": token}
r = requests.get("https://discord.com/api/v9/users/@me", headers=h)
if r.status_code == 200:
    data = r.json()
    print("Username:", data.get("username"))
    print("ID:", data.get("id"))
else:
    print("Fejl: HTTP", r.status_code, r.text)
