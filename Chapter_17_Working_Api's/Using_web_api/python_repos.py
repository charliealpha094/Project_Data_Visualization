#Done by Carlos Amaral (29/07/2020)


#Processing an API response

import requests   #import the requests module.

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #Store the URL of API call in the url variable.
headers = {'Accept': 'application/vnd.github.v3+json'} #Github is on the 3rd verson of  its API. We define headers for API call.
r = requests.get(url, headers=headers) #Use requests to make the call to the API.
print(f"Status code: {r.status_code}") #Print the value of status_code to make sure call went through successfully.

#Store API response in a variable.
response_dict = r.json()  #Store the resulting dictionary in response_dict.

#Process results.
print(response_dict.keys())
