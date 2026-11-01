# Reports app (FeatureRoom demo product)

A deliberately small reporting service that FeatureRoom's agents discuss
features against. Accounts have orders; the app serves a paged report and a
JSON export of every row.

```bash
pip install -r requirements.txt
flask --app reports_app.app run
curl localhost:5000/accounts/acme/report
pytest
```

Push this folder as its own repository and give its URL to the template's
`product_repo` input.
