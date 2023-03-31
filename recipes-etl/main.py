from urllib import request


URL = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
local_file = "data/recipes.json"

request.urlretrieve(URL, local_file)
