# FeatureRoom

**Feature discussions where the agents check the code, track every decision, and hand the team a spec — while the people make the calls.**

Built on [Switch](https://github.com/sandbox-quantum/switch) for the Flip the Switch Hackathon (Track 1: Best Business Workflow).

## The problem

Every feature starts as a team discussion, and those discussions go wrong in the same ways:

- They are scattered across Slack threads, meetings and DMs.
- Decisions get lost, and nobody remembers why something was decided.
- Open questions stay open, because nobody owns them.
- Effort is argued about without anyone looking at the code. Sometimes the feature already half exists.
- Security, privacy and scale come up after building has started.
- After all the talk, someone still writes the spec and tickets by hand.

Meeting summarizers and AI notes summarize *after* the discussion. In FeatureRoom the agents take part *during* it.

## How it works

```
 #feature-ideas                      #feat-csv-export  (one room per feature)
 ┌───────────────────────┐  link     ┌─────────────────────────────────────────┐
 │ people                │ ────────► │ proposer · teammates · approver         │
 │ @feature-host         │           │ @feature-host   opens, invites, nudges  │
 │ 📄 Feature index      │ ◄──────── │ @feature-eng    reads the real code     │
 └───────────────────────┘  outcome  │ @feature-risk   asks what people forget │
                                     │ @feature-scribe 📄 Decision board, Spec │
                                     └─────────────────────────────────────────┘
```

1. **Intake.** Someone tells `@feature-host` an idea in `#feature-ideas`. The host checks the feature index for duplicates and earlier rejections, asks for what is missing (the problem, the users, why now), and proposes a room. Once the proposer agrees, it opens the room.
2. **Discovery.** `@feature-eng` searches the product's code. It reports the affected files, the code that can be reused, an estimate with its confidence, and whether the feature already partly exists. `@feature-risk` raises the permission, privacy, scale and migration questions that apply.
3. **Discussion.** People discuss. `@feature-scribe` keeps a **decision board**, a room document listing:
   - decisions, with who made each one and the message it came from;
   - open questions, each with an owner;
   - risks;
   - what is out of scope.

   It flags when a decision reverses an earlier one.
4. **Approval.** When nothing is left open, the scribe asks the approver for a decision. Only the approver named on the board can approve, reject or park the feature. Anyone else who asks is refused.
5. **Handoff.** The scribe writes the spec. The engineer re-checks the code, in case it changed during the discussion, and breaks the spec into tasks. The host reports the outcome in `#feature-ideas`.

The full workflow, with every edge case, is in [docs/workflow.md](docs/workflow.md).

## Why Switch

FeatureRoom is a workflow on top of Switch, and it would not work without it:

| Switch feature | Used for |
|---|---|
| Rooms bridged to Slack | Every feature room is a Slack channel where the people and the agents are members |
| Agents creating rooms, inviting people and agents | The host opens `#feat-<name>` and brings in the right people and the three agents |
| Linked rooms | `#feature-ideas` links to every feature room, and outcomes flow back |
| Room documents | The feature index and each decision board and spec live in their room, visible to everyone |
| Addressing | Agents only act when addressed, which keeps them out of the way of people talking |
| Membership | An agent sees only the rooms it is in, so a private feature room stays private |
| Any provider | Each agent can run on a different coding agent: Claude Code, Codex, OpenCode |
| Templates | One YAML file creates the whole team: [featureroom.template.yaml](featureroom.template.yaml) |

## Setup

You need:
- **Switch Console**, from the [Switch releases](https://github.com/sandbox-quantum/switch/releases/latest);
- **a Slack workspace** where you can install apps;
- **one coding agent** installed and signed in (Claude Code, Codex or OpenCode).

1. **Pick the product repository.** For the demo, use [featureroom-sample-app](https://github.com/KamayaniR/featureroom-sample-app), a small reports service. Or use your own product's repository.
2. **Connect Slack in Switch Console.** switch-buddy can walk you through it.
3. **Run the template.** In Console, open Templates and paste [featureroom.template.yaml](featureroom.template.yaml). Then fill in:
   - **Product repository:** `https://github.com/KamayaniR/featureroom-sample-app`, or your own.
   - **Default approver:** the Slack username of whoever approves features.
4. **Open the room.** Console creates the four agents and `#feature-ideas`, and the host introduces itself.
5. **Bring an idea:** `@feature-host customers keep asking to export their reports as CSV`.

## Demo

[Demo video](#) · [Demo script](docs/demo-script.md)

## Repository layout

The demo product lives in its own repository,
[featureroom-sample-app](https://github.com/KamayaniR/featureroom-sample-app), so the agents read only the product's code and not these notes.

| Path | What it is |
|---|---|
| `featureroom.template.yaml` | The Switch template: four agents, the ideas room, and the instructions that hold the rules |
| `docs/workflow.md` | The workflow and its edge cases |
| `docs/demo-script.md` | The scripted demo |

## Limits

- Switch delivers an agent only the messages that mention it. People mention `@feature-scribe` when they decide something, and whenever the scribe is mentioned it catches up on the rest of the room from its history. A decision nobody mentions the scribe about reaches the board the next time someone does.
- Agents act only when a message addresses them. Nudging quiet owners and reopening a parked feature happen when someone asks (`@feature-host nudge`, `@feature-host reopen`), not on a timer.
- Edits to old Slack messages may not reach the agents. The scribe asks people to post corrections as new messages.
- The approver check compares the sender's name with the approver on the board. It is a workflow rule the agents follow, not a permission Switch enforces.
