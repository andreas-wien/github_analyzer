from unittest.mock import patch

from app.github.activity import format_events


@patch("app.github.activity.format_date_string", return_value="Apr 24, 09:15")
def test_format_events_maps_known_and_unknown_types(mock_format_date):
    events = [
        {
            "type": "PushEvent",
            "repo": {"name": "octo/demo"},
            "created_at": "2026-04-24T09:15:00Z",
        },
        {
            "type": "WatchEvent",
            "repo": {"name": "octo/demo"},
            "created_at": "2026-04-24T09:15:00Z",
        },
        {
            "type": "IssueCommentEvent",
            "repo": {"name": "octo/docs"},
            "created_at": "2026-04-24T09:15:00Z",
        },
    ]

    result = format_events(events)

    assert result == [
        {
            "text": "Pushed commits to octo/demo",
            "date": "Apr 24, 09:15",
            "icon": "bi-git",
            "type": "PushEvent",
            "repo": "octo/demo",
            "url": "https://github.com/octo/demo",
        },
        {
            "text": "Starred octo/demo",
            "date": "Apr 24, 09:15",
            "icon": "bi-star",
            "type": "WatchEvent",
            "repo": "octo/demo",
            "url": "https://github.com/octo/demo",
        },
        {
            "text": "IssueCommentEvent in octo/docs",
            "date": "Apr 24, 09:15",
            "icon": "bi-circle",
            "type": "IssueCommentEvent",
            "repo": "octo/docs",
            "url": "https://github.com/octo/docs",
        },
    ]
    assert mock_format_date.call_count == 3
