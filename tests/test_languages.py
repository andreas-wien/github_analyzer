from unittest.mock import patch

from app.github.languages import get_language_usage_sum


@patch("app.github.languages.requests.get")
@patch("app.github.languages.get_repos")
def test_get_language_usage_sum_aggregates_language_bytes(mock_get_repos, mock_get, fake_response_cls):
    mock_get_repos.return_value = [
        {"languages_url": "https://api.github.com/repos/1/languages"},
        {"languages_url": "https://api.github.com/repos/2/languages"},
    ]
    mock_get.side_effect = [
        fake_response_cls({"Python": 100, "JavaScript": 25, "": 99}),
        fake_response_cls({"Python": 40, "Go": 60}),
    ]

    result = get_language_usage_sum("secret-token")

    assert result == {"Python": 140, "JavaScript": 25, "Go": 60}
    assert mock_get.call_count == 2
