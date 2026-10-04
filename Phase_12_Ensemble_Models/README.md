# SECOM Predictive Maintenance Pipeline
Objective: Develop a robust, production-ready predictive model to detect manufacturing anomalies and serve as the backend for a real-time mobile application (iOS/Android) on the factory floor.

**Pipeline Execution:**

**Dimensionality Reduction:** Aggressively reduced 590 heavily correlated sensors down to 162 independent Principal Components, preserving 95% of the variance while eliminating the Curse of Dimensionality.

**Distance-Based Modeling (k-NN):** Evaluated geometric separation. Discovered severe class overlap. Applying SMOTE to balance the classes resulted in a 71% detection rate, but triggered 193 false alarms (7% precision). The algorithm reverted to k=1, proving straight-line distance cannot isolate these anomalies.

**Ensemble Modeling (Random Forest):** Deployed 100 non-linear decision trees to navigate the overlap. Even with SMOTE-balanced training data, the model achieved 0% recall.

**Signal Verification (Raw Data Benchmark):** Bypassed PCA entirely to test the full 446-sensor raw matrix. The ensemble model still completely failed to detect failures, mathematically proving PCA did not accidentally compress or delete the predictive signal.

**Sequential Boosting (XGBoost):** Applied extreme Gradient Boosting with a strict 14.10x algorithmic penalty for missing anomalies. The engine caught only 1 out of 21 actual failures, missing 20 entirely.

**Final Business Recommendation:**
Halt the immediate development of the predictive mobile application. Exhaustive algorithmic testing mathematically proves that the existing physical sensors on the factory floor are not capturing the phenomena that cause machine failures. Deploying any model built on this data to an iOS or Android app would result in either a 95%+ miss rate or catastrophic alarm fatigue for the operators. The next phase must focus on a hardware audit to install sensors capable of measuring the actual mechanical root causes of these anomalies.
