import requests
import json
from requests.auth import HTTPBasicAuth

# this REST call fetches all user(including inactive users)
url = 'http://3.7.80.11:8080/rest/api/2/user/search?username=.&startAt=0&maxResults=2000&includeInactive=True'

# Basic Authentication
auth = HTTPBasicAuth("admin", "admin")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

try:

    res = requests.get(url=url, headers=headers, auth=auth)

    result = res.json()
    count = 0
    for users in result:

        for key, username in users.items():
            if key == "name":
                if username != 'admin':
                    print(username)
                    url = f'http://3.7.80.11:8080/rest/api/2/user?username=' + username
                    requestData = {
                        "active": True
                    }
                    x = json.dumps(requestData)

                    # PUT request
                    response = requests.request("PUT", url, data=x, headers=headers, auth=auth)
        count += 1
    print(count, " users activated")

except Exception as e:
    print(e)
