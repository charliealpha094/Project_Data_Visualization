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

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")