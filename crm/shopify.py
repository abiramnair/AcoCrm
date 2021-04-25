import requests

# GraphQL Mutation Query
create_customer_query = """
mutation customerCreate($input: CustomerInput!) {
    customerCreate(input: $input) {
        customer {
        id
    }
    userErrors {
        field
        message
        }
    }
}
"""

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def run_query(query, first_name, last_name, email, phone, accepts_marketing):
    variables = {
        "input": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "phone": phone,
            "acceptsMarketing": accepts_marketing
        }
    }
    r = requests.post(
        "https://07f482e43a73c9a534d365cddd9e7603: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@chrysalis-silk"
        "-treasures.myshopify.com/admin/api/2021-04/graphql.json",
        json={
            'query': query,
            'variables': variables,
        },
        headers=headers
    )
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception('Query failed {}. {}'.format(r.status_code, query))
