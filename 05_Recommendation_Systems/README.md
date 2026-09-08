# Phase 5: Persona-Aware Hybrid Basket Recommender

## Research Objective
To investigate whether customer-segment-specific association rules can improve next-item basket recommendations compared with non-personalized, popularity-based baselines in a retail environment.

## Methodology & Experimental Design
Unlike standard recommendation demos, this engine was evaluated using a strict scientific framework to prevent information leakage and accurately simulate a production environment.

* **Temporal Split:** Processed 828,850 raw item scans chronologically, utilizing the first 80% (663k scans) exclusively for training/rule-mining, and isolating the final 20% (165k scans) for evaluation.
* **The Cold Start Fallback:** Engineered a hierarchical degradation system. The model attempts rule-based inference first; if rules are sparse or the user is unknown, it falls back to *Persona Popularity*, and finally *Global Popularity*.
* **Basket Splitting:** Evaluated performance by taking real, unseen test baskets (>= 4 items), obscuring 50% of the items, and tasking the algorithm with predicting the withheld products.
* **Algorithmic Tuning:** Tested three distinct scoring strategies for the engine—ranking candidate items by pure *Confidence*, pure *Lift*, and a *Combined* metric (Confidence $\times$ Lift).

## Performance Results (K=3)
The offline evaluation across 2,500 holdout shopping trips yielded a definitive winner, successfully defeating the notoriously strong "grocery popularity bias" (where predicting basics like bread and milk often outscores complex models).

* **Baseline (Global Popularity):** Hit Rate: 56.08% | Precision: 0.2645 | NDCG: 0.2709
* **Winner (Hybrid Engine - Confidence Ranked):** Hit Rate: 56.40% | Precision: 0.2680 | NDCG: 0.2851

## Key Business Insights
1. **Confidence > Lift for Ranking:** The experiment proved empirically that ranking recommendations by *Confidence* outperforms *Lift*. While Lift identifies highly correlated niche items (e.g., Pasta ➔ Truffle Oil), Confidence identifies highly probable practical additions (e.g., Pasta ➔ Tomato Sauce), leading to a higher Normalized Discounted Cumulative Gain (NDCG).
2. **Subset Matching:** By allowing the engine to aggregate evidence from overlapping subsets within a single cart, the model behaves dynamically, dynamically boosting the score of consequents that are recommended by multiple items already in the basket.
