#Done by Carlos Amaral (30/07/2020)


#Adding Clickable Links to Our Graph

"""
Because Plotly allows you to use HTML on text elements, we can easily add
links to a chart. Let’s use the x-axis labels as a way to let the viewer visit any
project’s home page on GitHub. We need to pull the URLs from the data
and use them when generating the x-axis labels:
"""

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")



#Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], [] #Update repo_names to repo_links, to more accurately communicate the kind of info. we want in the chart.
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url'] #Pull the url for project from repo_dict and assign it to temporary variable repo_url.
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>" #Generate a link to the project.
    repo_links.append(repo_link)  #Append the link to the list repo_links.

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


#Make visualization
data = [{
    'type': 'bar',
    'x': repo_links,  #Use the repo_links list for the x-values in the chart.
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,

}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
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
offline.plot(fig, filename = 'python_repos.html')
