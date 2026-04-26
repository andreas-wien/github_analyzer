from unittest.mock import patch

from app.github.user import get_followers, get_user


@patch("app.github.user.requests.get")
def test_get_user_fetches_current_user(mock_get, fake_response_cls):
    mock_get.return_value = fake_response_cls({"login": "octocat"})

    result = get_user("secret-token")

    assert result == {"login": "octocat"}
    mock_get.assert_called_once_with(
        "https://api.github.com/user",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "Flask-App",
            "Authorization": "token secret-token",
        },
    )


@patch("app.github.user.get_all_pages")
def test_get_followers_uses_followers_url(mock_get_all_pages):
    mock_get_all_pages.return_value = [{"login": "follower"}]

    result = get_followers(
        "secret-token",
        {"followers_url": "https://api.github.com/users/octocat/followers"},
    )

    assert result == [{"login": "follower"}]
    mock_get_all_pages.assert_called_once()
