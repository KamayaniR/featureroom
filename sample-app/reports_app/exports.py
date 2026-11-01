import json

from reports_app.reports import all_rows


def export_json(account_id: str) -> str:
    return json.dumps(all_rows(account_id))


# TODO: started for the CSV export request, never finished or tested.
def export_csv(account_id: str) -> str:
    rows = all_rows(account_id)
    if not rows:
        return ""
    header = ",".join(rows[0].keys())
    lines = [",".join(str(v) for v in row.values()) for row in rows]
    return "\n".join([header, *lines])
