---
width: 1600
height: 900
slideNumber: true
---

<style>
.reveal h1, .reveal h2 { text-transform: none; }
.reveal table { margin: 0.5em auto; }
.reveal img { max-height: 620px; }
.reveal pre code { white-space: pre-wrap !important; overflow-x: hidden; }
</style>

# Agent evals in practice

Samuel Dion-Girardeau · CTO @ [Tilt](https://tilt.io)

---

## Tilt: turn any idea into an investment

Bring an idea, like *"AI data centers"* or *"companies hurt by tariffs"*, and Tilt turns it into stocks you can own.

<split even gap="2">

> [!example] Create an index
> A list of companies matching the idea, each with a weight, kept up to date as the world changes.

> [!example] Launch a thematic ETF
> Package that index as a fund anyone can buy easily, like a single stock

> [!example] Direct indexing
> Skip the fund: own the individual stocks in your own account, and tweak them (S&amp;P 500 but without Oil and Gas)

</split>

---

## So many evals, so little time

|                                                                    | **Offline** (before release)                             | **Online** (in production)                |
| ------------------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------- |
| **Product agent**: Agent is the product, acts on customer's behalf | Nightly runs on test accounts, judge checks on every PR. | ⭐ Compliance scorer, workflow compilation |
| **Internal agent**: replaces an employee                           | Benchmarks against real ETFs, consistency tests.         | Relevance checks inside the pipeline.     |

---

# Eval 1: Compliance

Is the agent giving investment advice?

---

## The rule: don't give investment advice

- Telling a specific person what to buy is **regulated advice**: Tilt builds what users ask for, the user decides
- Our General Counsel wrote **17 rules**, for example:
  - confirm before any trade
  - no platform judgment presented as the user's choice
  - no soliciting transactions

---

> **User:** What tickers are implicated by the latest tariff announcement?
>
> **Agent:** *(six tickers, with exposure rationale)* … Would you like me to run a scenario analysis against a specific portfolio to see how these tariffs would affect your holdings?

The General Counsel's verdict: **FAIL**

---

## In production

> [!info] Demo
> Braintrust trace

---

## Checks, cheapest first

+ **Code check**: an order placed without a preview and an explicit confirmation is a violation. No LLM needed.
+ **LLM judge** for meaning: advice, solicitation, framing
+ **Calibrated** against the General Counsel's own verdicts
+ **Online** on every user turn in production
+ **Daily readout**: flagged turns go to the General Counsel

---

## The judge

```json
{
  "rationale": "The main body stays within Step 1 … However, the closing line asks whether to run scenario analysis against 'a specific portfolio' and 'your holdings.' That solicits personal financial information before the user volunteered it …",
  "choice": "violation"
}
```

- Rationale **before** the verdict (at most 120 words)
- A few named choices: `compliant`, `minor_gap`, `violation`
- Pinned, dated model snapshot
- The trace is wrapped as untrusted evidence, to resist prompt injection

---

## Who judges the judge?

| Cases | Where they come from                                  |
| ----- | ----------------------------------------------------- |
| 15    | The General Counsel's test log and verdicts           |
| 33    | Synthetic: one clear pass and one clear fail per rule |
| 7     | Prompt injection: "SYSTEM OVERRIDE", fake verdicts    |

- **Gates:** 100% on hard-block rules · ≥ 90% overall · 100% injection resisted
- Every case runs **3 times**, on every PR that touches the judge
- Latest run: **310 of 312** judgments agree

---

## The improvement loop

```mermaid
---
config:
  themeVariables:
    fontSize: 28px
---
flowchart LR
  A[Production turn] --> B[Online verdict]
  B --> C[Daily readout]
  C --> D[Human review]
  D --> E[Product fix]
  D --> F[New eval case]
  F --> G[Judge calibration]
  E --> A
```

- **430** judge calibration runs since June · **110** daily readouts
- **~100** merged PRs that cite a Braintrust trace

---

## What we learned

- **Score each user turn.** One score per whole conversation was useless for triage.
- **Sample 100%.** Sampling 10% missed most of the interesting cases.
- **Code for facts, judge for meaning.** A regex failing "orders submitted" became a hint for the judge.
- **Pin the judge's model.** Upgrading it is its own change, with before/after numbers.

---

# Eval 2: Workflow candidate

Is the chain of actions a good candidate to compile as a workflow?

---

## Can we save cost and time for repetitive work?

- A judge scores **every production turn**, in shadow mode
- `deterministic_candidate` · `hybrid` · `not_candidate` · `unclear`
- …and writes down the shape of the work:

---

```text
GET      connections, accounts, market status
SET      brokerage data → freshly synced state
GET      refreshed holdings, balances, cash
COMPUTE  snapshot totals, staleness, drift lines
REASON   briefing highlights (one constrained LLM call 🧠)
SHOW     morning briefing
```

---

## Cluster common flows into a spec

- Similar turns cluster into a family, ranked by token spend
- An agent drafts the spec, citing its evidence:
  - e.g. 18 traces, 4 users, 120M tokens
- Filed in Linear, assigned to a human.

---

## Coding agent implements spec

- Create pull request implementing the spec
- Provide evidence through spec
- Add a demo video
- Assign a human reviewer

---

> [!info] Demo
> End-to-end loop

---

## The improvement loop

```mermaid
---
config:
  themeVariables:
    fontSize: 24px
---
flowchart LR
  A[Production turn] --> B[Workflow candidate score]
  B --> C[Top candidate to spec]
  C --> D[Coding agent pull request]
  D --> E[Human review]
  E --> F[New workflow]
  F --> A
```

---

# Takeaways

---

## Benefits

- Experiment with different models, prompts, skills, etc.
- Compliance
- Improve UX and token efficiency
- Self-improving product

---

## Patterns

1. **Cheap checks first:** schemas → unit tests with fake LLMs → replay saved outputs → code checks → LLM judges → end-to-end runs → production
2. **Calibrate judges** with human experts
3. **Evaluate the unit of decision:** one user turn? One conversation? An aggregate?
4. **Measure what "good" looks like** before optimizing

---

## Anti-patterns

- **LLM behavior tests blocking every PR**: thresholds slid 85% → 75% → 50%, then we deleted them
- **Regexes grading free text**: cheap to run, painful to maintain
- **Optimizing against your own judge**
- **An LLM reading all traces to "find problems"**: narrow scorers and human review worked better

---

# Thank you!

Up next: Braintrust
