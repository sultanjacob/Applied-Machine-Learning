# Customer Segmentation: Unsupervised Learning Pipeline

## Overview
This repository contains a rigorous, end-to-end unsupervised machine learning pipeline designed to extract behavioral business intelligence from raw retail data. Using the Dunnhumby "Complete Journey" dataset (comprising over 1.4 million grocery transactions), this project evaluates multiple clustering algorithms to segment households based on their purchasing habits, lifetime spend, and store visit frequency.

## Project Architecture
* **Phase 1: Data Engineering:** Aggregated raw transactional data into distinct household profiles, engineered behavioral features (e.g., average basket value), and applied standard scaling.
* **Phase 2: K-Means Clustering:** Utilized the Elbow Method and Silhouette Score to isolate an optimal K=3, mathematically dividing the user base into distinct marketing personas (Budget, Bulk, and Power Shoppers).
* **Phase 3: DBSCAN:** Deployed density-based clustering with a K-Distance graph to test K-Means assumptions, proving the core customer base operates on a continuous spectrum and successfully isolating 22 extreme statistical anomalies.
* **Phase 4: Hierarchical Clustering:** Generated a dendrogram using Ward's linkage to evaluate bottom-up variance, organically discovering optimal data splits without relying on pre-defined centroids.

## Key Insights
* K-Means is highly effective for forced segmentation when clear marketing boundaries are required.
* DBSCAN excels at anomaly detection within retail data, preventing high-spending outliers from skewing the averages of core segments.
* Hierarchical Clustering mathematically validated the "Power Shopper" cohort, proving that top-tier loyalists remain an undeniable distinct persona regardless of the algorithm used.

## Technologies Used
* **Languages:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (K-Means, DBSCAN, AgglomerativeClustering), SciPy (Dendrograms)
* **Visualization:** Matplotlib, Seaborn
