## Overview

### Business and Data Understanding

**Business Problem**  
NBA front offices need an objective and interpretable way to assess trade fairness across player performance, fit, and salary impact. Current systems are often subjective, opaque, and prone to bias—leading to broken trades or misaligned acquisitions.

**Primary Stakeholders**  
- **NBA Teams (GMs, Coaches, Scouts):** Gain data-driven insight into trade scenarios, player roles, and salary dynamics.  
- **Data Analysts & Sports Science Teams:** Leverage role-based clustering to refine scouting and development.  
- **Fantasy Sports & Betting Platforms:** Understand value shifts from trades for better predictions and analysis.  
- **Fans & Media Analysts:** Access a clear explanation of trade fairness and player value.

**Objective**  
Use unsupervised machine learning and model interpretability to:
- Categorize players into meaningful archetypes.
- Evaluate trade scenarios across performance, fit, and salary metrics.
- Deliver transparent and accurate recommendations for NBA trades.

---

### Data Understanding

**Data Sources** (via Basketball-Reference):
- Per 36, Per 100, and advanced player statistics
- Play-by-play tendencies
- Team ratings (e.g., ORtg, DRtg, TS%, Net Rating)
- Salary and contract data

**Data Preparation Highlights**
- SQL for data cleaning and extraction
- Imputation of missing values (`SimpleImputer`)
- Over 25 engineered features per player
- Visualizations and scaling (`StandardScaler`)
- Tools/Libraries: `pandas`, `sqlite3`, `sklearn`, `shap`, `matplotlib`, `seaborn`

---

## Modeling

### Unsupervised Player Clustering

**Goal:**  
Cluster NBA players by archetypes to better understand their roles and potential trade fit.

**Methods Used:**
1. Feature Scaling with `StandardScaler`
2. K-Means Clustering
3. Cluster Optimization (Elbow Method, Silhouette Score, Davies-Bouldin, Calinski-Harabasz)
4. Visualization using PCA and t-SNE

**Resulting Archetypes (K=3):**
- **Cluster 0:** Role Players & 3&D Wings  
- **Cluster 1:** Creators & Offensive Engines  
- **Cluster 2:** Rim Protectors & Paint Anchors

---

### Interpretability & Metrics

**Transparency Techniques:**
- Train-test split using Random Forest
- Cross-validation and hyperparameter tuning to improve R²
- SHAP (SHapley Additive exPlanations) for insight into each player's feature contributions

**Model Accuracy:**
- **Player Fit Index:** R² = 0.927  
- **Trade Value Index:** R² = 0.972  
- **Salary Cap Impact:** R² = 0.960  

**SHAP Visuals:**
- Red dots = features that boost trade value (e.g., high BPM)
- Blue dots = features that lower trade value (e.g., high TOV%)

---

### Example Scenarios

**Trade Proposal 1:**  
- *IND sends:* Benedict Mathurin + 2nd Round Pick  
- *DEN sends:* Michael Porter Jr.  
- *Insight:* Balancing youth upside with current value.

**Trade Proposal 2:**  
- *MIN sends:* Naz Reid + Steven Adams  
- *SAS sends:* Jeremy Sochan  
- *Insight:* Young, switchable defender traded for rim protection and depth.

---

## Evaluation

**Strengths:**
- Combines clustering and SHAP for a fully explainable, unsupervised system
- Excellent performance across interpretability and prediction metrics
- Supports real-time trade assessment with context-aware recommendations

**Challenges:**
- Requires ongoing data updates for accuracy
- Potential variance in edge-case player evaluations (e.g., injuries, off-court factors)

---

## Business Recommendations

1. **Subjectivity → Objectivity:**  
   The model introduces consistent standards for trade evaluation through clustering and SHAP insights.

2. **Unpredictable Player Fit → Measurable Fit:**  
   The Player Fit Index quantifies how well a player will mesh with their new team.

3. **Unfair Salaries → Exposed Gaps:**  
   The Trade Value Index reveals overpaid and underpaid contracts relative to production.

4. **Hidden Salary Risks → Clear Indicators:**  
   The Salary Cap Impact metric allows front offices to assess short- and long-term financial implications.

---

## Conclusion

This interpretability-first, unsupervised trade analysis framework empowers NBA decision-makers with transparency and accuracy. By clustering players into archetypes and quantifying value through SHAP-driven metrics, the model transforms how front offices, analysts, and fans understand the fairness and impact of trades. It offers a scalable, data-driven tool that enhances strategy across the league.
