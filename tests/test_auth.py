from unittest.mock import patch

from app.github.auth import get_access_token, get_auth_url


def test_get_auth_url_uses_configured_client_id(app):
    app.config["GITHUB_CLIENT_ID"] = "client-123"

    with app.app_context():
        assert (
            get_auth_url()
            == "https://github.com/login/oauth/authorize?client_id=client-123&scope=repo"
        )


@patch("app.github.auth.requests.post")
def test_get_access_token_posts_oauth_payload(mock_post, app, fake_response_cls):
    mock_post.return_value = fake_response_cls({"access_token": "token-xyz"})
    app.config["GITHUB_CLIENT_ID"] = "client-123"
    app.config["GITHUB_CLIENT_SECRET"] = "secret-456"

    with app.app_context():
        result = get_access_token("oauth-code")

    assert result == "token-xyz"
    mock_post.assert_called_once_with(
        "https://github.com/login/oauth/access_token",
        data={
            "client_id": "client-123",
            "client_secret": "secret-456",
            "code": "oauth-code",
        },
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "Flask-App",
        },
    )
