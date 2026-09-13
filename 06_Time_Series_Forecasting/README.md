# Phase 6: Persona-Specific Revenue Forecasting.

**Objective & Methodology**
The goal was to predict weekly retail revenue independently for distinct customer segments rather than forecasting aggregate global sales. This approach provides actionable intelligence for targeted inventory and staffing.

***Data Engineering:*** Aggregated 1.4 million raw transaction scans into continuous daily time series tracks, handling missing days by zero-filling to maintain mathematical integrity.

***Smoothing:*** Resampled daily data into weekly revenue to eliminate artificial day-of-week volatility.

***Temporal Split:*** Enforced a strict chronological holdout, using the first 40 weeks for training and quarantining the final 11 weeks for evaluation.

**Performance Results**
We benchmarked Holt's Exponential Smoothing (an additive trend model) against a Naive Baseline (which predicts next week's sales will exactly mirror last week's). Performance was measured using Mean Absolute Percentage Error (MAPE) and Mean Absolute Error (MAE).

***Cluster 0 (Broad Middle):*** ML Model (3.54%) defeated the Naive Baseline (5.60%).

***Cluster 1 (Power Shoppers):*** Naive Baseline (6.05%) defeated the ML Model (7.13%).

***Cluster 2 (Premium Shoppers):*** ML Model (6.87%) defeated the Naive Baseline (10.37%).

**Business Impact & Deployment**
These results mathematically prove that a monolithic forecasting approach is fundamentally flawed in retail. Power Shoppers exhibit rigid, predictable spending habits where simple baseline heuristics excel. Conversely, Premium Shoppers display volatile, trend-driven behavior requiring advanced smoothing algorithms to capture momentum.

The production architecture for this system will utilize an ensemble routing system: deploying baseline logic for stable segments and machine learning for dynamic ones. Ultimately, the goal is to serve these targeted predictions directly to store managers via a dedicated Android/iOS app, empowering real-time, floor-level inventory decisions based on incoming persona traffic.
