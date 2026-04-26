from unittest.mock import patch


def test_home_renders_index_for_logged_out_users(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"GitHub Analyzer" in response.data


def test_home_redirects_logged_in_users_to_dashboard(client):
    with client.session_transaction() as session:
        session["github_token"] = "token"

    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"] == "/dashboard"


def test_dashboard_redirects_without_token(client):
    response = client.get("/dashboard")

    assert response.status_code == 302
    assert response.headers["Location"] == "/"


def test_languages_load_redirects_without_token(client):
    response = client.get("/languages/load")

    assert response.status_code == 302
    assert response.headers["Location"] == "/"


@patch("app.routes.languages_routes.get_language_usage_sum", return_value={"Python": 10})
def test_languages_load_returns_json_for_authenticated_user(mock_get_language_usage_sum, client):
    with client.session_transaction() as session:
        session["github_token"] = "token"

    response = client.get("/languages/load")

    assert response.status_code == 200
    assert response.get_json() == {"Python": 10}
    mock_get_language_usage_sum.assert_called_once_with("token")


@patch(
    "app.routes.auth_routes.get_auth_url",
    return_value="https://github.com/login/oauth/authorize?client_id=abc",
)
def test_login_redirects_to_github_auth_url(mock_get_auth_url, client):
    response = client.get("/login")

    assert response.status_code == 302
    assert response.headers["Location"] == "https://github.com/login/oauth/authorize?client_id=abc"
    mock_get_auth_url.assert_called_once_with()


@patch("app.routes.auth_routes.get_access_token", return_value="oauth-token")
def test_callback_stores_token_in_session(mock_get_access_token, client):
    response = client.get("/callback?code=oauth-code")

    assert response.status_code == 302
    assert response.headers["Location"] == "/dashboard"
    mock_get_access_token.assert_called_once_with("oauth-code")
    with client.session_transaction() as session:
        assert session["github_token"] == "oauth-token"


def test_logoff_clears_session(client):
    with client.session_transaction() as session:
        session["github_token"] = "token"
        session["extra"] = "value"

    response = client.get("/logoff")

    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    with client.session_transaction() as session:
        assert dict(session) == {}


def test_context_processor_hides_back_button_on_home_and_dashboard(app):
    with app.test_request_context("/"):
        context = {}
        app.update_template_context(context)
        assert context["show_back_button"] is False

    with app.test_request_context("/dashboard"):
        context = {}
        app.update_template_context(context)
        assert context["show_back_button"] is False

    with app.test_request_context("/profile"):
        context = {}
        app.update_template_context(context)
        assert context["show_back_button"] is True
