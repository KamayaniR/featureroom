from flask import Flask, Response, abort, request

from reports_app.config import FEATURE_FLAGS
from reports_app.data import ACCOUNTS
from reports_app.exports import export_csv, export_json
from reports_app.reports import build_report

app = Flask(__name__)


def _require_account(account_id: str) -> None:
    if account_id not in ACCOUNTS:
        abort(404)


@app.get("/accounts/<account_id>/report")
def report(account_id: str):
    _require_account(account_id)
    page = int(request.args.get("page", 1))
    return build_report(account_id, page)


@app.get("/accounts/<account_id>/export.json")
def export_report_json(account_id: str):
    _require_account(account_id)
    return Response(export_json(account_id), mimetype="application/json")


@app.get("/accounts/<account_id>/export.csv")
def export_report_csv(account_id: str):
    if not FEATURE_FLAGS["csv_export"]:
        abort(404)
    _require_account(account_id)
    return Response(export_csv(account_id), mimetype="text/csv")
