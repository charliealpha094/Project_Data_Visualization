#Done by Carlos Amaral (30/07/2020)


#Adding custom tooltips

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process the results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []  #Define empty list to hold text we want to display to each project.
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login'] 
    description = repo_dict['description']
    label = f"{owner}<br />{description}" #Plotly allows for HTML code.
    labels.append(label)


#Make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,

}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},  #'titlefont' key to define the font size of the overall chart title. 
    'xaxis': { #Settings to control the font-size of x-axis title (titlefont) and tick labels (tickfont).
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},

    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
