#Done by Carlos Amaral (29/07/2020)


#Visualizing Repositories using Plotly

"""
Let’s make a visualization using the data we have now to show the relative
popularity of Python projects on GitHub. We’ll make an interactive bar
chart: the height of each bar will represent the number of stars the project
has acquired, and you can click the bar’s label to go to that project’s home
on GitHub.
"""

import requests

from plotly.graph_objs import Bar #Import Bar class from plotly  
from plotly import offline  #Import offline module from plotly

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process the results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []   #Create 2 empty lists to store the we'll include in the initial chart. 
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make visualization
data = [{   #Define data list. Contains a dictionary.
    'type': 'bar',  #Type of the plot.
    'x': repo_names, #Data for x values.
    'y': stars, #Data for y values.

}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')