from flask import Flask,request
import requests

app = Flask(__name__)
CLIENT_ID = "0e6e205349ca6060d678"
CLIENT_SECRET = "019286075a13ce0f793996b25dea678e923b6e55"
OAUTH_URL ="https://github.com/login/oauth/access_token"
BASE_URL = "https://api.github.com"

#output = requests.get("https://github.com/login/oauth/authorize?client_key={}".format(CLIENT_ID))

@app.route("/")
def index():
    return '<a href="https://github.com/login/oauth/authorize?client_id={}">Login with Github</a>'.format(CLIENT_ID)

@app.route("/authorize")
def get_githuburl():
    code = request.args.get('code')
    d1 = {'client_id':CLIENT_ID,'code':code,'client_secret':CLIENT_SECRET}
    d2={'Accept':'application/json'}
    post_output = requests.post(OAUTH_URL,data=d1,headers=d2)
    print(post_output.text)
    token = post_output.json()['access_token']
    headers= {'Authorization': 'Bearer {}'.format(token)}
    r2 = requests.get(BASE_URL + '/user/repos',headers=headers)
    print(r2)
    repos = r2.json()
    list_of_repos = []
    for repo in repos:
        list_of_repos.append(repo['name'])
    print(list_of_repos)    
    return '<br>'.join(list_of_repos)
    #return "<h1>SUCCES!! and code is {}</h1>".format(code)
    

if __name__ == "__main__":
    app.run(debug=True)



