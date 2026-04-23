import requests
from .constans import *
import plotly.graph_objects as go
from collections import Counter

def get_user_events(token, user):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }
    
    url = f"{API_BASE_URL}/users/{user["login"]}/events"
    res = requests.get(url, headers=headers)
    print(res.json())
    
    return res.json()


def pushes_per_day(events):
    push_counts = {}
    for event in events:
        if event["type"] == "PushEvent":
            date = event["created_at"][:10]
            if date not in push_counts:
                push_counts[date] = 0
            push_counts[date] += 1

    fig = go.Figure(data=[
        go.Bar(x=list(push_counts.keys()), y=list(push_counts.values()))
    ])
    fig.update_layout(title="Pushes per Day", xaxis_title="Date", yaxis_title="Pushes")
   
    return fig.to_html(full_html=False)


def event_type_breakdown(events):
    type_counts = {}
    for event in events:
        event_type = event["type"]
        if event_type not in type_counts:
            type_counts[event_type] = 0
        type_counts[event_type] += 1

    fig = go.Figure(data=[
        go.Pie(labels=list(type_counts.keys()), values=list(type_counts.values()))
    ])
    fig.update_layout(title="Event Types")
    return fig.to_html(full_html=False)