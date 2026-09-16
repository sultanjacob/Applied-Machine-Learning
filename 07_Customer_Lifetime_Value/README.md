# Phase 7: Predicting Silent Attrition & Customer Lifetime Value

## Objective & Methodology
In a non-contractual retail environment, customers do not explicitly cancel their accounts; they simply stop visiting. The objective of this phase was to identify "Silent Attrition" among historically loyal shoppers by analyzing their unique purchasing rhythms.

* **Data Engineering:** Compressed 1.4 million transaction records into a Recency, Frequency, and Monetary (RFM) matrix using daily calibration.
* **Probability Modeling:** Deployed the Buy 'Til You Die (BTYD) framework, specifically fitting a Beta Geometric / Negative Binomial Distribution (BG/NBD) model to calculate $P(Alive)$—the mathematical probability that a customer is still active.
* **Intervention Threshold:** Defined an "At-Risk Loyalist" as any customer with 5+ historical purchases whose $P(Alive)$ dropped below 50%.

## Performance Results & Business Insights
Cross-referencing the probability matrix with our existing Machine Learning clusters revealed a highly concentrated churn problem:
* **Power Shoppers & Premium Shoppers:** Exhibited a 0% silent attrition rate among loyalists, proving high brand stickiness for routine staples and niche specialty items.
* **The Broad Middle:** Accounted for 100% of the identified At-Risk Loyalists, indicating high price-sensitivity and susceptibility to competitor poaching. 

## Strategic Recommendations
The business must pivot from global retention marketing to targeted interventions. Marketing budgets should be explicitly reallocated to intercept Broad Middle shoppers the moment their $P(Alive)$ begins decaying, maximizing return on ad spend (ROAS) and preserving the customer base.
