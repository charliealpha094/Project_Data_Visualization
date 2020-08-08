#Done by Carlos Amaral (29/07/2020)


#Refining Plotly Charts

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process the results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repositoty'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

"""The marker settings shown here affect the design of the bars. We set a
custom blue color for the bars and specify that they’ll be outlined with a
dark gray line that’s 1.5 pixels wide. We also set the opacity of the bars to
0.6 to soften the appearance of the chart a little.
"""