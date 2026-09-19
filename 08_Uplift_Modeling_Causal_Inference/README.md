# Phase 8: Causal Inference & Discount Optimization

## Objective
The goal was to prevent margin cannibalization by transitioning from predictive churn modeling to causal inference. Instead of blindly targeting all customers with a retention discount, we sought to isolate the "Persuadables"—customers who will only generate positive net revenue if incentivized.

## Methodology: The T-Learner Architecture
To predict the Individual Treatment Effect (ITE) without conducting a live A/B test, we synthesized a causal dataset from historical campaign records, enforcing a strict chronological split to prevent data leakage:
* **Model C (Control):** A Random Forest Regressor trained on 889 households that received no historical promotions, establishing organic baseline spend.
* **Model T (Treatment):** A Random Forest Regressor trained on 1,558 households that received historical promotions, mapping incentivized spend.

By passing our vulnerable customer segments through both models, we calculated the exact financial **Uplift Score** (Predicted Treatment Spend - Predicted Control Spend) for every individual.

## Scaled Business Impact & ROI
We applied a strict margin-protection rule across our entire "Broad Middle" persona: A $10 retention coupon is only issued if the predicted Uplift strictly exceeds the $10 cost. 

By removing artificial recency/frequency constraints and letting the causal algorithm drive the targeting, the model isolated 204 highly profitable interventions. This targeted strategy requires a minimal marketing investment of $2,040.00 while mathematically projecting a gross uplift of $24,912.84—yielding a net profit of **$22,872.84**. This completely shields baseline profit margins while maximizing Return on Ad Spend (ROAS).
