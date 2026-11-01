from reports_app.data import orders_for


def build_report(account_id: str, page: int, page_size: int = 100) -> dict:
    rows = orders_for(account_id)
    start = (page - 1) * page_size
    return {
        "account": account_id,
        "page": page,
        "total_rows": len(rows),
        "rows": rows[start : start + page_size],
    }


def all_rows(account_id: str) -> list[dict]:
    return orders_for(account_id)
