
# **Unsupervised Interpretability Model for NBA Trade Suggestions**  
*(Why This is NOT Even Partially Supervised: The model relies on clustering, dimensionality reduction, and interpretability techniques to generate player role categories and trade evaluation metrics.)*

## **1. Purpose of the Model**  
This project aims to enhance the interpretability of NBA trade recommendations using **unsupervised learning techniques**. Instead of relying on predefined labels or target variables, we apply clustering, dimensionality reduction, and feature importance analysis to:

✅ **Identify player roles and trade value categories**  
✅ **Determine team fit based on playing style, impact, and salary**  
✅ **Evaluate trade fairness and impact on team performance**  

By leveraging techniques like **K-Means, PCA, SHAP, and Graph-based modeling**, this approach provides transparent trade suggestions that NBA teams, analysts, and fans can easily interpret.

---

## **2. INPUTS: Features Considered for Trade Suggestions**  
Our model processes multiple aspects of **NBA player and team performance**, divided into four key input files:

### **A. Player Performance Metrics** *(File: `INPUT_Player_Performance.csv`)*
This dataset captures **statistical attributes** (adjusted per 36 minutes, per 100 possessions, and advanced metrics):

- **Scoring:** FG%, 3P%, 2P%, eFG%, TS%, PTS  
- **Playmaking:** AST, AST%, TOV, TOV%  
- **Rebounding:** ORB, DRB, TRB, ORB%, DRB%  
- **Defense:** STL, BLK, STL%, BLK%, DBPM  
- **Usage & Impact:** USG%, BPM, WS/48, VORP  

### **B. Team Fit & Trade Value** *(File: `INPUT_Player_Trade_Value.csv`)*
Includes team-level metrics that influence trade value:

- **Offensive & Defensive Metrics:** ORtg, DRtg, NRtg, On-Off  
- **Trade Fairness Indicators:**  
  - Change in BPM, WS before/after trade  
  - Net Rating Impact (NRtg/A)  
  - Positional Fit (% of time at PG, SG, SF, PF, C)  

### **C. Salary & Contract Data** *(File: `INPUT_Player_Salary_Contract.csv`)*
- **Current & Future Salary:** 2024-25, 2025-26, Guaranteed Money  
- **Trade Flexibility:** Expiring contracts, cap impact  

### **D. Playstyle & Clustering Attributes** *(File: `INPUT_Playstyle_Clustering.csv`)*
- **Turnover Tendencies:** BadPass, LostBall  
- **Playstyle Variations:** On-Court performance, On-Off impact, DWS, OWS  

---

## **3. Categories: Player Clustering for Trade Interpretation**  
Players are **grouped into clusters** based on their playstyle and trade impact. This step improves **interpretability** of trade suggestions.  

### **A. Determining the Number of Clusters**
We will determine the **optimal number of clusters** using the following methods:  
- **Elbow Method**  
- **Silhouette Score (SS)**  
- **Calinski-Harabasz Index (CHI)**  
- **Davies-Bouldin Index (DBI)**  
- **Gap Statistic** *(Compares WCSS to a null reference distribution.)*  

### **B. Applying Clustering Algorithms**
Once key features are selected, we apply the following clustering methods:  
- **K-Means Clustering** *(Primary Method)*  
- **Hierarchical Clustering** *(Alternative Approach)*  
- **Gaussian Mixture Models (If needed for flexibility in clusters)*  

### **C. Validating and Interpreting Clusters**
To **visualize and interpret** the clusters, we use:  
- **t-SNE / PCA (Dimensionality Reduction & Visualization)**  

### **D. Potential Cluster Categories & Characteristics**
| **Cluster Name**       | **Key Characteristics** |
|------------------------|------------------------|
| **Scoring Guards**     | High PTS, USG%, AST%   |
| **3&D Wings**         | High 3P%, DBPM, Low USG% |
| **Playmakers**        | High AST%, TOV%, BPM   |
| **Defensive Bigs**    | High BLK%, DRB%, DWS   |
| **Scoring Bigs**      | High PTS, eFG%, Low AST% |
| **Role Players**      | Moderate in all categories, high NRtg impact |
| **All-Stars/Superstars** | High BPM, WS/48, PTS |

⚠️ **NOTE:** **SHAP** (SHapley Additive Explanations) will be used throughout the process **not to predict**, but to **explain what features contribute most to trade suggestions**.

---

## **4. OUTPUTS: Trade Interpretability Metrics**  
Since this is an **unsupervised model**, we do **not predict specific trade outcomes**. Instead, we generate **interpretability metrics** to assess trade fairness.

### **Key Trade Evaluation Scores**
| **Metric**            | **Purpose**                                     | **Calculation Method** |
|-----------------------|-----------------------------------------------|------------------------|
| **Player Fit Score**  | Measures how well a player fits a team’s needs | Cosine Similarity / Distance Metrics (ORtg, DRtg, USG%) |
| **Trade Value Score** | Evaluates fairness of a trade | Change in BPM, WS, Salary Impact |
| **Net Rating Impact** | Measures trade impact on team performance | NRtg/A before vs. after trade |

---

## **5. Unsupervised Learning Techniques Used**
| **Method** | **Application** |
|------------|----------------|
| **K-Means Clustering** | Groups players into **role-based clusters** |
| **PCA/t-SNE** | Reduces dimensions, allowing **trade visualization** |
| **SHAP (SHapley Additive Explanations)** | Explains which stats contribute **most to a trade suggestion** |
| **Graph-Based Trade Network (NetworkX)** | Models **how players interact** within team trade scenarios |

---

## **6. Summary: Why This Model Matters?**
✅ **Features:** Captures player stats, team needs, salary constraints  
✅ **Categories:** Groups players into role-based clusters for trade analysis  
✅ **Metrics:** Evaluates Player Fit, Trade Fairness, and Team Impact  
✅ **Techniques Used:** K-Means, SHAP, PCA, Graph Models for interpretability  

---

## **7. Next Steps**
1️⃣ **Run K-Means Clustering** to categorize NBA players by role  
2️⃣ **Use SHAP** to explain why a trade suggestion makes sense  
3️⃣ **Visualize trade impact** using a **NetworkX graph**  

---

### **Final Thoughts**  
This **unsupervised approach** allows for transparent, data-driven trade suggestions without relying on **predefined labels**. By using **clustering, dimensionality reduction, and SHAP explanations**, our model provides NBA analysts and teams with a **clear, interpretable trade evaluation system**.

---

This version improves **clarity, structure, and readability**, while ensuring no key information is missing. Let me know if you need any refinements! 🚀🏀
