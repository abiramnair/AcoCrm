# GraphQL Mutation Queries CRUD
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

update_customer_query = """
mutation customerUpdate($input: CustomerInput!) {
    customerUpdate(input: $input) {
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