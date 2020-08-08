#Done by Carlos Amaral (31/07/2020)


#Try 17.2 - Active Discussions

"""
Using the data from hn_submissions.py, make a bar
chart showing the most active discussions currently happening on Hacker
News. The height of each bar should correspond to the number of comments
each submission has. The label for each bar should include the submission’s
title and should act as a link to the discussion page for that submission.
"""

from operator import itemgetter

import requests

from plotly.graph_objs import bar
from plotly import offline

#Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")


#Process information about each submition.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:20]:
    #Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #Build a dictionary for each article.
    submission_dict ={
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse = True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


#Make lists for all the discussions.
titles, comments, news_links = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    hn_link = submission_dict['hn_link']
    news_link = f"<a href = '{hn_link}'>{title[:20]}</a>"
    
    titles.append(title)
    comments.append(submission_dict['comments'])
    news_links.append(news_link)


#Make visualization
data = [{
    'type': 'bar',
    'x': news_links,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most active discussions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Number of comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'hacker_news_most_active.html')