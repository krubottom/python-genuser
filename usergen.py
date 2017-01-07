import json
import urllib2

gen_url = 'https://randomuser.me/api/?nat=us&results=25'

f = urllib2.urlopen(gen_url)
json_string = f.read()
parsed_json = json.loads(json_string)

for user in parsed_json['results']:
    print("First Name: " + user['name']['first'].title())
    print("Last Name: " + user['name']['last'].title())
    print("Username: " + user['login']['username'])
    print("Password: " + user['login']['password']) + "\n"

# print("First Name: " +  parsed_json['results'][0]['name']['first'])
# print("Last Name: " + last_name = parsed_json['results'][0]['name']['last'])
