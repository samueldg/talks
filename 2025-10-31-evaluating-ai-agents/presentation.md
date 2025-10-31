# Evaluating AI agents 🤖

Samuel Dion-Girardeau  
CTO @ [Tilt](https://tilt.io)

---

## Who am I?

- Background: linguistics, applied NLP
- [Nuance](https://nuance.com) – built NLP developer platforms
- [Delphia](https://delphia.com) – helped people turn their data into an asset
- [Tilt](https://tilt.io) – invest in anything

---

## What you can expect

- *Our* journey from no eval to confidence
- Startup == pragmatic decisions
- Slides available after [samueldg/talks](https://github.com/samueldg/talks)

---

## What I expect

- No financial background
- You're developing an agent (or considering)
- You're already sold on evals

---

## What we do at Tilt

- Tool for pro investors to build stock portfolios
- Specialize in thematics
    * Think "AI data centers" or "International tariffs"
- Thematic research agent 🤖
    * Input: a theme
    * Output: a portfolio of stocks with exposures

---

# End-to-end evaluation

---

## Initial benchmarks

1. Find indexes that:
    * ... publish the list of holdings
    * ... are based on a theme
2. Run the agent on the theme
3. Compare the output to the actual portfolio

---

### Example

🔗 [Morningstar US Exponential Technologies Healthcare](https://indexes.morningstar.com/indexes/details/morningstar-us-exponential-technologies-healthcare-FS0000GLHS)

---

## F-1 Scores

Constituent-based: do we pick the same stocks?

![tilt-v-bench](./_resources/tilt-v-bench.png)

---

### Problem 1: Punished for good picks 😢

- [$TWST - Twist Bioscience Inc](https://www.twistbioscience.com/)
- [$RNA - Avidity Biosciences Inc](https://www.aviditybiosciences.com/)
- Is there a definitive answer?
    * What if you ask 10 analysts?

---

### Problem 2: Exposure scores rarely available

Need to find more continuous approach to inclusion.

---

## Market returns?

- Can we look at the performance of our index?
- Do we outperform the benchmark?

---

### Problem: wrong target

- *Carbon capture*? → $NVDA! 📈
- *GLP-1 drugs*? → $NVDA! 📈
- Thematics ≠ numbers go up

---

## Market returns _correlation_?

- `corr(tilt, benchmark)`
- Can we look at the performance of our index *relative to the benchmark*?
- We should go down when it goes down

---

### Problem: everything is correlated!

![asset-correlation](./_resources/asset-correlation.png)

---

## _Market-neutral_ returns correlation?

```python
corr(
    tilt - market,
    benchmark - market,
)
```

- Closer to tracking a theme
- Not sufficient, but necessary

---

## _PCA-neutral_ returns correlation?

- "The market" isn't everything
- We decide how many we want (PC1 ... PC?)

| Metric                     | Value |
| -------------------------- | ----- |
| Correlation                | 0.67  |
| Market-neutral correlation | 0.41  |
| PCA-neutral correlation    | 0.29  |

---

# Meta-eval

---

## Evaluating the eval

- We have good targets ✅
- How do we know if our metrics are good?
    * Do we want 90% correlation? 60%?
    * Is 0.3 F1-score good?
    * CEO breathing down my neck 😮‍💨

---

### Solution

- Find multiple ETFs with the same theme
- Generate a portfolio with our agent
- One-vs-all for F1 score, market-neutral correlation
- Plot all
- Are we in the pack?

---

### Bad

![meta-eval-bad](./_resources/meta-eval-bad.png)

---

### Good

![meta-eval-good](./_resources/meta-eval-good.png)

---

# Intermediate evals

---

## LLM judge

- _Given a report on a company, how exposed is it?_
- Critique + refinement
- Rubric
    * Add detail + Evolve it over time

---

### Dilemma: eval or product

- Why not add it in the product?
- Reasons:
    * Cost
    * Latency
    * Rate limits
- Idea: Ship your evaluation to prod

---

![stock-defence](./_resources/stock-defence.png)

---

## Industry classification judge

- Used production queries
- Score (theme, industry) pairs for relevance
- Add random pairs too

---

## Citation extraction

- Used production retrieval results
- Input document -> expected citations

---

## Summary

- F1-score for constituent overlap
- PCA-neutral correlation for market tracking
- Groundedness (citations per company)

---

# Takeaways

---

## "Fractal" evals

- Start end-to-end
- Then introduce new evals
- Lower the bar to creating new evals

---

## Meta-evals

- Leaderboard with competition
- Help set realistic targets

---

## Eval vs agent: Arms race

- Improve your eval and agent hand-in-hand

---

## Throw curveballs at it

- E.g. [Pink Chip](https://www.pinkchip.org/)
    * Emerging property of e.g. adding news documents

---

## [Autonomy slider](https://www.latent.space/p/s3)

- Showing some evals to your users, who want to be HitL.

---

## Feedback loop

- Bring prod data in your eval
    * @Nuance, import users' utterances
    * @Tilt, grab user queries and retriever results for intermediate evals

---

## Focus on important metrics

- But go nuts on reporting
- Tracing, etc.
- Artifacts (configs, results, etc.)

---

# Bonus tips

---

## Development

- Keep agent logic thin
    * evals ≠ unit tests
- Use coding tools creatively
    * E.g.: Claude code +  Puppeteer MCP to reconstitute benchmarks.

---

## Tools

- [MLflow](https://mlflow.org/)
- [Langchain](https://www.langchain.com/langchain)/[Langgraph](https://www.langchain.com/langgraph)
- [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [Portkey](https://portkey.ai/)

---

# Thank you!
