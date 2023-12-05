# Credentials file

# MongoDB credentials
# Return:
# Parameters
# dblink - database link
# database_name - name of the database
# collection_name - name of the collection
def mongodb_parameters():

    params = {
        'dblink': 'mongodb://localhost:27017/',
        'database_name': 'e-learning-on-cloud',
        'collection_name': 'User'
    }

    return params
