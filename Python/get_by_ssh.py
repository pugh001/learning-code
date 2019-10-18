import requests
import os
import sys
import io
import getpass

if len(sys.argv) < 3:
    raise SyntaxError('No Git or BitBucket project specified: get_byssh.py: hostPath repoName')

if len(sys.argv) > 3:
    raise SyntaxError('Too many arguments provided: get_byssh.py: hostPath repoName :')

password = getpass.getpass("Please enter your domain password and press [Enter]: ")

url = str(sys.argv[1]) + str(sys.argv[2]) + '/repos?limit=999'

resp = requests.get(url,
    params={'q': 'requests+language:python'},
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'},
    stream=True,
    verify=True,
    auth=(getpass.getuser(), password)
)

if resp.status_code != 200:
    # This means something went wrong.
    raise RuntimeError('GET /projects/ {}'.format(resp.status_code))

for repo in resp.json()["values"]:
    print(repo["slug"])
    dirExists=False
    workingDir = os.getcwd()
    print(workingDir)
    for dir in os.listdir(workingDir):
        if dir == repo["slug"]:
            print("Changing directory")
            dirExists=True
            changeTo = workingDir + "\\" + dir
            os.chdir(changeTo)
            print(os.getcwd())
            os.system('git fetch --all')
            os.system('git reset --hard origin/master')
            os.chdir(workingDir)
            break

    if dirExists==False:
        print("New DIR")
        # We need to check out the new repository
        repoUri = ''

        if str(repo["links"]["clone"][0]['name']) == 'ssh':
            repoUri = str(repo["links"]["clone"][0]['href'])
        else:
            repoUri = str(repo["links"]["clone"][1]['href'])

        clonecmd = 'git clone ' + repoUri + ' ' + repo["slug"]
        os.system(clonecmd)
