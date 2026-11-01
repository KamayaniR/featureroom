# Demo script

About 3–4 minutes, recorded in Slack.

Cast:
- **Priya**, the proposer;
- **Sam**, a backend engineer;
- **Lead**, the approver.

Two or three Slack accounts are enough.

The sample app sets up three moments:
- the CSV export already half exists behind a flag;
- the export includes customer emails;
- one account has 250,000 rows.

## 1. Intake (30s)

In `#feature-ideas`, **Priya**:
> @feature-host customers keep asking to export their reports as CSV so they can open them in Excel

**The host** restates the idea, asks who it is for and why now, then proposes `#feat-csv-export` with Priya, Sam and Lead as approver. **Priya**: `yes`.

## 2. Discovery (45s)

The room opens, and the three agents get the kickoff.
- **The engineer** says first that the CSV export already exists behind the `csv_export` flag in `reports_app/exports.py`. It is untested, and it doesn't quote commas or quotes (`Widget, large` and `Cable "USB-C"` would break rows). It points to `export_json` as code to reuse, and gives an estimate of about half a day, with medium confidence.
- **The risk reviewer** points out that exports include `customer_email`, which is personal data, and that the endpoint has no permission check. It also notes the `globex` account has 250,000 rows, which is built in memory in one request.
- **The scribe** creates the decision board with these as open questions, each with an owner.

## 3. Discussion (60s)

- **Sam**: `@feature-scribe decided: use Python's csv module, stream the response`. Recorded as Proposed, since Sam isn't the approver.
- **Lead**: `@feature-scribe confirmed. Admins only can export.` Both become Decided.
- **Priya**: `@feature-scribe while we're at it, can we add PDF export too?` The scribe moves it to Out of scope and suggests starting it as its own idea.
- **Priya**: `@feature-scribe mark it approved`. **Refused**: only Lead can approve.
- **Lead**: `@feature-scribe actually, let's not remove emails, customers need them`. The scribe flags that this reverses an earlier decision and asks Lead to confirm.

Agents only receive messages that mention them. Every line meant for the board names `@feature-scribe`. When the scribe is mentioned, it also catches up on anything said in the room without a mention.

## 4. Approval and handoff (45s)

- The scribe sets the status to Ready and addresses Lead with a five-line summary.
- **Lead**: `@feature-scribe approve`.
- The scribe writes the Spec. The engineer re-checks the code and adds tasks:
  - fix the quoting;
  - stream rows;
  - add the admin check;
  - add tests;
  - turn on the flag.
- In `#feature-ideas`, the host posts: *Approved: feat-csv-export, spec in the room.*

## 5. Close (15s)

Show:
- the decision board;
- the spec;
- the link from `#feature-ideas` to the feature room.

End with the line: **"From an idea in Slack to an approved, code-checked spec — and every decision has an owner and a source."**

## Before recording

- Run the whole script once beforehand. Agents' wording varies between runs. If a step goes off-script, keep the run whose output reads best.
- Restart from a fresh template run, so the feature index is empty. Otherwise the second run's intake reports a duplicate.
