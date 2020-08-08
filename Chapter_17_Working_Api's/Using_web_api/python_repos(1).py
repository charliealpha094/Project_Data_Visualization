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
print(f"Total repositories: {response_dict['total_count']}") #Print the total_count- total number of Python repositories on GitHub.

#Explore the information about the repositories.
repo_dicts = response_dict['items']  #Store a list of dictionaries in repo_dicts
print(f"Repositories returned: {len(repo_dicts)}") #Print the length of the repo_dicts to see how many repositories we have info of.

#Examine the first repository.
repo_dict = repo_dicts[0]  #Pull out the 1st item from repo_dicts and and store it in repo_dict, to look closer at info from each repository.
print(f"\nKeys: {len(repo_dict)}") #Print the no. of keys in dictionary to see how much info. we have.
for key in sorted (repo_dict.keys()): #Print all dictionary's keys to see what kind of info is included.
    print(key)