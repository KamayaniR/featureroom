import random

ACCOUNTS = {
    "acme": {"name": "Acme Corp", "plan": "pro"},
    "globex": {"name": "Globex", "plan": "enterprise"},
}

_ORDERS = {
    "acme": [
        {"id": 1, "customer_email": "jo@example.com", "item": "Widget, large", "amount": 120.0, "date": "2026-09-02"},
        {"id": 2, "customer_email": "sam@example.com", "item": "Gadget", "amount": 45.5, "date": "2026-09-14"},
        {"id": 3, "customer_email": "lee@example.com", "item": 'Cable "USB-C"', "amount": 9.99, "date": "2026-10-01"},
    ],
}


def _large_account(n: int) -> list[dict]:
    rng = random.Random(7)
    return [
        {
            "id": i,
            "customer_email": f"user{i}@example.com",
            "item": rng.choice(["Widget", "Gadget", "Cable"]),
            "amount": round(rng.uniform(1, 500), 2),
            "date": f"2026-{rng.randint(1, 10):02d}-{rng.randint(1, 28):02d}",
        }
        for i in range(1, n + 1)
    ]


def orders_for(account_id: str) -> list[dict]:
    if account_id == "globex":
        return _large_account(250_000)
    return _ORDERS.get(account_id, [])
