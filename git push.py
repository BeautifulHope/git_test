import os,datetime
import subprocess
n = os.system("ls")
a = n >> 8
print(a)

date = datetime.datetime.today().isoformat()[0:10]

status = subprocess.run(["git", "status"],shell=True)
print(status)

print('**********start git add.**********')
gadd = subprocess.run(["git", "add", "."])
print('**********git add done.**********')
print('**********start git commit.**********')
gcom = subprocess.run(["git", "commit", "-m" + date])
print('**********git commit done.**********')
print('**********start git push.**********')
gpush = subprocess.run(["git", "push", "origin", "master"])
print('**********git push done.**********')