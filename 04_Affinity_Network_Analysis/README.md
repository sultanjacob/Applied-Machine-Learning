# Phase 4: Persona-Isolated Affinity Network Analysis

## Overview
Standard Market Basket Analysis often yields high-frequency but low-value insights (e.g., "bread and milk"). This project elevates traditional association rule mining by introducing **Persona-Isolated Affinity Mining**. By segmenting 1.4 million retail transactions using Agglomerative Hierarchical Clustering prior to running the Apriori algorithm, this analysis extracts highly targeted, demographic-specific cross-selling strategies.

## Methodology
1. **Macro-Micro Integration:** Mapped demographic cluster labels (Power Shoppers, Premium Shoppers) directly onto 828,000 individual transactional records.
2. **Matrix Engineering:** Pivoted raw transaction data into segment-specific, one-hot encoded bipartite matrices.
3. **Association Rule Mining:** Deployed the Apriori algorithm to discover frequent itemsets (min_support = 3%) and filtered the results mathematically using **Lift** to identify combinations with the highest gravitational pull.
4. **Business Translation:** Replaced academic network graphs with "Business Impact Bar Charts," translating mathematical lift into plain-English merchandising directives.

## Key Business Insights
By isolating the data, the algorithm proved that purchasing physics vary drastically across customer segments:
* **The Power Shopper (Cluster 1):** Exhibits a massive "Household Restock" phenomenon. High-confidence rules center around bundled staples (Buy: Milk & Cheese ➔ Buy: Eggs [Lift: 5.10x]). 
* **The Premium Shopper (Cluster 2):** Exhibits an "Experiential Meal" phenomenon. Rules indicate complex, high-margin dinner solutions (Buy: Specialty Cheese ➔ Buy: Deli Meats [Lift: 8.74x]).

## Technologies Used
* **Algorithms:** Apriori, Association Rules (MLxtend)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Seaborn, Matplotlib
