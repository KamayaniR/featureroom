# FeatureRoom workflow

The workflow, phase by phase, and what happens when things do not go to plan.
The agents' instructions in `featureroom.template.yaml` implement it.

## Who is involved

| | Role |
|---|---|
| `feature-host` | Intake, opening rooms, invitations, outcomes, nudges. Owns the **Feature index** in `#feature-ideas`. |
| `feature-eng` | Reads the product's code. It does discovery, answers "what if" questions, re-checks the code after approval and breaks the spec into tasks. |
| `feature-risk` | Asks the questions people forget: permissions, personal data, scale, migration, failure, abuse, accessibility. |
| `feature-scribe` | Owns each room's **Decision board** and writes the **Spec**. |
| Proposer | Brings the idea. |
| Approver | The one person who can approve, reject or park a feature. The default comes from the template, and the proposer can name someone else. |

## Rules in every phase

1. Agents act only when addressed, because Switch delivers an agent only the messages that mention it. People mention `@feature-scribe` when they decide something. Each time the scribe is mentioned, it reads the room history since its last update and records anything said without a mention. One reply per message, and never a reply to another agent's acknowledgement. This keeps agents from talking to each other in a loop.
2. Cite or say "unknown". The engineer and the risk reviewer give file paths, and say what they did not check.
3. People decide. Agents propose and record. Status changes come only from the approver.
4. The documents are the memory. Agents re-read the index or board before acting, so a restart or a long thread loses nothing.
5. Failures are posted where people see them: a room that could not be created, a person who could not be added, an agent that is offline.
6. One room per feature.

## Phase 1: Intake in `#feature-ideas`

The host restates the idea, checks the index, asks at most three questions (the problem, who it is for, why now), and proposes a room with its people and approver. It waits for the proposer's yes.

| Edge case | What happens |
|---|---|
| The idea is vague | The host keeps asking. No room opens without a problem and a target user. |
| It duplicates an open feature | The host points to that room and asks what is different. |
| It was rejected before | The host quotes the reason and asks what has changed. |
| It was parked | The host offers to reopen that room. |
| It is a bug | The host says so. No feature room opens. |
| The message holds several features | The host lists them, numbered, and each gets its own room. |
| The proposer goes quiet | Nothing happens until someone addresses the host again. There is no timer. |
| It is a sensitive feature | A private room. Agents only see rooms they are in. |

## Phase 2: Room setup

The host:
1. creates `#feat-<slug>`;
2. adds the people and the approver;
3. invites the three agents;
4. links the room from `#feature-ideas`;
5. posts the kickoff;
6. adds a row to the index.

The scribe then creates the board.

| Edge case | What happens |
|---|---|
| The room name is taken | The host proposes `feat-<slug>-2`. |
| A person cannot be added | The host names them and gives the reason, and does not claim they joined. |
| Room creation fails | The exact error is posted in `#feature-ideas`. |
| The proposer is also the approver | Allowed, and visible on the board. |

## Phase 3: Discovery

The engineer reports:
- the affected files;
- the code that can be reused;
- whether the feature already exists;
- an estimate with its confidence;
- unknowns;
- what it searched.

The risk reviewer posts up to five risks that apply, as questions with owners. The scribe adds both as open questions and sets the status to Discussion.

| Edge case | What happens |
|---|---|
| The feature already partly exists | The engineer says so first, with the file and line. |
| The code cannot be found | The engineer says where it looked and asks to be pointed to the right place. |
| A person disagrees with the estimate | Both estimates go on the board. |
| The engineer and the risk reviewer disagree | Each states its view once, and the people decide. |
| An agent is offline | `!agents-status` shows it. People carry on, and the agent catches up from the room history. |

## Phase 4: Discussion

The scribe records:
- decisions, marked Decided when the approver makes them and Proposed otherwise;
- questions;
- risks;
- assumptions;
- scope.

It posts one line per change. Anyone can ask the scribe for a `summary`. `@feature-host nudge` addresses every owner of an open question.

| Edge case | What happens |
|---|---|
| A decision reverses an earlier one | It is flagged and the approver is asked to confirm. The old decision stays, struck through. |
| Someone without authority decides something | It is recorded as Proposed until the approver confirms it. |
| Scope creep | The idea moves to Out of scope, and the host can start it as its own idea. |
| A decision was made in a meeting or DM | The scribe asks for it to be stated in the room, so it has a source. |
| An earlier message was edited | The scribe asks for a new message, because edits may not reach the agents. |
| Someone joins late | They ask for a `summary` or read the board. |
| Two features depend on each other | The rooms are linked both ways, and each board records the dependency. |

## Phase 5: Readiness and approval

When every question is resolved or deferred and every risk is acknowledged, the scribe sets the status to Ready and asks the approver. The approver answers with one of:
- `approve`
- `approve with changes: …`
- `reject: reason`
- `park until <date>`

| Edge case | What happens |
|---|---|
| Approval is asked for too early | The scribe lists what blocks it, by owner. The approver may override, and the override is recorded. |
| Someone other than the approver approves | It is recorded as a comment and the status does not change. |
| "Mark it approved", from anyone but the approver | Refused. |
| Approve with changes | Each change becomes an open question. Only those changes need approval again. |
| Rejected | The reason goes on the board and the index, the outcome is posted in `#feature-ideas`, and the room is archived. |
| Parked | The status shows the date. `@feature-host reopen` brings it back. |
| The approver hands over the role | The change is recorded, with who made it. |

## Phase 6: Handoff

The scribe writes the spec:
- the problem and the users;
- scope and out of scope;
- decisions, with their sources;
- acceptance criteria;
- risks and how each is handled;
- the estimate.

The engineer pulls the latest code, reports what changed since discovery, and adds tasks with the files each touches. The host posts the outcome in `#feature-ideas`.

| Edge case | What happens |
|---|---|
| The code changed during the discussion | The engineer reports what changed and updates the estimate. |
| The work is more than about three days | The engineer proposes v1 and v2, and the approver picks. |
| A change is requested after approval | The scribe writes Spec v2 with what differs, and only that difference needs approval. |
