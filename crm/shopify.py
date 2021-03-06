import requests
from decouple import config

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def run_query(query, customer):
    variables = {
        "input": {
            "firstName": customer.first_name,
            "lastName": customer.last_name,
            "email": customer.email,
            "note": customer.comments,
            "phone": customer.mobile_number,
            "acceptsMarketing": customer.pdpa_agreed
        }
    }
    if customer.gid:
        variables['input']['id'] = customer.gid
    r = requests.post(
        f"https://{config('SHOPIFY_API_KEY')}:{config('SHOPIFY_API_PASSWORD')}@chrysalis-silk"
        "-treasures.myshopify.com/admin/api/2021-04/graphql.json",
        json={
            'query': query,
            'variables': variables,
        },
        headers=headers
    )
    if r.status_code == 200:
        if not customer.gid:
            print(r.json())
            gid = r.json()['data']['customerCreate']['customer']['id']
            customer.gid = gid
            customer.save()
        else:
            pass
        print(r.json())
    else:
        raise Exception('Query failed {}. {}'.format(r.status_code, query))
