import facebook
import json

#Read credentials
def read_creds(filename):
    with open(filename) as f:
        credentials = json.load(f)
    return credentials

credentials = read_creds('credentials.json')

page_access_token = credentials['page_access_token']
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "101308201907030"

with open('10221jobarts.json') as f:
    data = json.load(f)
    graph.put_object(facebook_page_id, "feed", message="📢📢 Importante empresa esta buscando un " + data[0]['job_title'] + " en " + data[0]['city'] + " para una plaza " + data[0]['job_type'] + " . " + "No esperes más y POSTULA en 👉 " + data[0]['job_url'] + " 💼👍👍" + " #empleos #oportunidad #oportunidadlaboral #chamba #chambaparacreativos #jobarts", link=data[0]['job_url'])

    print("Job Publicado")
