import json

from reports_app.exports import export_json
from reports_app.reports import build_report


def test_report_pages():
    report = build_report("acme", page=1, page_size=2)
    assert report["total_rows"] == 3
    assert len(report["rows"]) == 2


def test_export_json_has_every_row():
    assert len(json.loads(export_json("acme"))) == 3
