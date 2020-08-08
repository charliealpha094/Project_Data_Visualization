#Done by Carlos Amaral (31/07/2020)


#Try 17.3.py - Testing python_repos.py

"""
In python_repos.py, we printed the value of
status_code to make sure the API call was successful. Write a program called
test_python_repos.py that uses unittest to assert that the value of status_code
is 200. Figure out some other assertions you can make—for example, that the
number of items returned is expected and that the total number of repositories
is greater than a certain amount.
"""

import requests

from plotly.graph_objs import Bar
from plotly import offline

def get_response():
    """Make an API call and return the response."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r

def get_repo_dicts(r):
    """Return a set of dicts representing the most popular repositories."""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_project_data(repo_dicts):
    """Return data for each repository."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

        return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    """Return visualization of most popular python repositories."""
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

if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)





