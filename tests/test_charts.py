from app.github.charts import event_type_breakdown, pushes_per_day


def test_pushes_per_day_renders_bar_chart_html():
    html = pushes_per_day(
        [
            {"type": "PushEvent", "created_at": "2026-04-24T09:15:00Z"},
            {"type": "PushEvent", "created_at": "2026-04-24T12:30:00Z"},
            {"type": "WatchEvent", "created_at": "2026-04-25T08:00:00Z"},
        ]
    )

    assert "Pushes per Day" in html
    assert "2026-04-24" in html
    assert "2" in html


def test_event_type_breakdown_renders_pie_chart_html():
    html = event_type_breakdown(
        [
            {"type": "PushEvent"},
            {"type": "WatchEvent"},
            {"type": "WatchEvent"},
        ]
    )

    assert "Event Types" in html
    assert "PushEvent" in html
    assert "WatchEvent" in html
