from unittest.mock import patch

from app.github.utility import format_date_string, get_all_pages


@patch("app.github.utility.requests.get")
def test_get_all_pages_follows_next_links(mock_get, fake_response_cls):
    mock_get.side_effect = [
        fake_response_cls(
            [{"id": 1}],
            headers={
                "Link": '<https://api.github.com/resource?page=2>; rel="next", '
                '<https://api.github.com/resource?page=2>; rel="last"'
            },
        ),
        fake_response_cls([{"id": 2}]),
    ]

    result = get_all_pages("https://api.github.com/resource?page=1", {"A": "B"})

    assert result == [{"id": 1}, {"id": 2}]
    assert mock_get.call_count == 2
    mock_get.assert_any_call("https://api.github.com/resource?page=1", headers={"A": "B"})
    mock_get.assert_any_call("https://api.github.com/resource?page=2", headers={"A": "B"})


def test_format_date_string_formats_iso_timestamp():
    assert format_date_string("2026-04-24T09:15:00Z") == "Apr 24, 09:15"
