import json
import requests


organization_id = '70892901'

def read_creds(filename):
    with open(filename) as f:
        credentials = json.load(f)
    return credentials

credentials = read_creds('Li-creds.json')

#scope: w_member_social,r_liteprofile,w_organization_social
access_token = credentials['access_token']
url = "https://api.linkedin.com/v2/ugcPosts"

headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': 'Bearer ' + access_token}


with open('10221jobarts-test.json') as f:
    data = json.load(f)


post_data = {
    "author": "urn:li:organization:"+organization_id,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "📢📢 Importante empresa esta buscando un " + data[0]['job_title'] + " en " + data[0]['city'] + " para una plaza " + data[0]['job_type'] + " . " + "No esperes más y POSTULA en el siguiente enlace 👉 " + data[0]['job_url'] + " 💼👍👍" + " #empleos #oportunidad #oportunidadlaboral #chamba #chambaparacreativos #jobarts"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

print(response)
