from unittest.mock import patch

from app.github.repos import get_repo_languages, get_repos


@patch("app.github.repos.get_all_pages")
def test_get_repos_delegates_to_pagination_helper(mock_get_all_pages):
    mock_get_all_pages.return_value = [{"id": 1}]

    result = get_repos("secret-token")

    assert result == [{"id": 1}]
    mock_get_all_pages.assert_called_once_with(
        "https://api.github.com/user/repos",
        {
            "Accept": "application/vnd.github+json",
            "User-Agent": "Flask-App",
            "Authorization": "token secret-token",
        },
    )


@patch("app.github.repos.get_repos")
def test_get_repo_languages_counts_sorts_and_limits(mock_get_repos):
    mock_get_repos.return_value = [
        {"language": "Python"},
        {"language": "Python"},
        {"language": "JavaScript"},
        {"language": "Go"},
        {"language": None},
    ]

    result = get_repo_languages("secret-token", 2)

    assert result == {"Python": 2, "JavaScript": 1}
