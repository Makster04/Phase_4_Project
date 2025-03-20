# Overview
---

# **📌 Unsupervised Interpretability Model for NBA Trade Suggestions**  

## **🧐 Purpose of the Model**  
The goal of this project is to **enhance the interpretability of NBA trade recommendations** using **unsupervised learning techniques**. Instead of relying on predefined labels or target variables, we use **clustering, dimensionality reduction, and feature importance analysis** to:  
1. **Identify player roles and trade value categories**  
2. **Determine team fit based on playing style, impact, and salary**  
3. **Evaluate trade fairness and impact on team performance**  

By leveraging **unsupervised techniques like K-Means, PCA, SHAP, and graph-based modeling**, this approach provides **transparent trade suggestions** that NBA teams, analysts, and fans can better understand.  

---

## **🔹 1. Inputs: Features Considered for Trade Suggestions**  
Our model processes multiple aspects of NBA player and team performance:  

### **A. Player Performance Metrics**  
**Statistical Attributes (Per 36, Per 100, Advanced Stats):**  
- **Scoring**: FG%, 3P%, 2P%, eFG%, TS%, PTS  
- **Playmaking**: AST, AST%, TOV, TOV%  
- **Rebounding**: ORB, DRB, TRB, ORB%, DRB%  
- **Defense**: STL, BLK, STL%, BLK%, DBPM  
- **Usage Rate & Impact**: USG%, BPM, WS/48, VORP  

### **B. Team Fit & Trade Value**  
- **Offensive/Defensive Metrics**: ORtg, DRtg, NRtg, On-Off  
- **Trade Fairness Indicators**:  
  - Change in BPM, WS before/after trade  
  - Net Rating Impact (`NRtg/A`)  
  - Positional Fit (PG%, SG%, SF%, PF%, C%)  

### **C. Salary & Contract Data**  
- Current and future salary (`2024-25`, `2025-26`, `Guaranteed`)  
- Trade flexibility (expiring contracts, cap impact)  

### **D. Playstyle & Clustering Attributes**  
- Turnover tendencies (`BadPass`, `LostBall`)  
- Playstyle variations (`OnCourt`, `On-Off`, `DWS`, `OWS`)  

---

## **🔹 2. Categories: Player Clustering for Trade Interpretation**  
Players are **grouped into clusters based on their playstyle and trade impact**, making trades more interpretable.  

| **Cluster Name**      | **Key Characteristics**                        |  
|----------------------|--------------------------------|  
| **Scoring Guards**   | High PTS, USG%, AST%          |  
| **3&D Wings**       | High 3P%, DBPM, Low USG%      |  
| **Playmakers**      | High AST%, TOV%, BPM          |  
| **Defensive Bigs**  | High BLK%, DRB%, DWS         |  
| **Scoring Bigs**    | High PTS, eFG%, Low AST%     |  
| **Role Players**    | Moderate in all categories, high NRtg impact |  
| **All-Stars/Superstars** | High BPM, WS/48, PTS  |  

### **🔍 How Are These Clusters Formed?**  
- **K-Means Clustering** → Identifies **role-based groups** of players  
- **Hierarchical Clustering** → Detects **similarities in playstyle**  
- **t-SNE/PCA** → Reduces feature dimensions for visualization  

---

## **🔹 3. Outputs: Trade Interpretability Metrics**  
Since this is an **unsupervised model**, we don’t predict specific trade outcomes but instead generate interpretability metrics:  

### **📌 Key Trade Evaluation Scores**  
| **Metric**             | **Purpose** | **Calculation Method** |  
|----------------------|------------|----------------------|  
| **Player Fit Score** | Measures how well a player fits a team’s needs | **Cosine Similarity / Distance Metrics** based on ORtg, DRtg, USG% |  
| **Trade Value Score** | Evaluates fairness of a trade | Change in **BPM, WS, Salary Impact** |  
| **Net Rating Impact** | Measures how trade affects team performance | `NRtg/A` before vs. after trade |  

---

## **🔹 4. Unsupervised Learning Techniques Used**  

| **Method** | **Application** |  
|------------|----------------|  
| **K-Means Clustering** | Groups players into **role-based clusters** |  
| **PCA/t-SNE** | Reduces dimensions, allowing **trade visualization** |  
| **SHAP (SHapley Additive Explanations)** | Explains which stats contribute to a **trade suggestion** |  
| **Graph-Based Trade Network (NetworkX)** | Models how players interact **within team trade scenarios** |  

---

## **📌 Summary: Why This Model Matters?**  
- ✅ **Features:** Captures **player stats, team needs, salary constraints**  
- ✅ **Categories:** Groups players into **role-based clusters** for trade analysis  
- ✅ **Metrics:** Evaluates **Player Fit, Trade Fairness, and Team Impact**  
- ✅ **Techniques Used:** **K-Means, SHAP, PCA, Graph Models** for interpretability  

---

## **🚀 Next Steps**  
Would you like me to:  
1️⃣ **Run K-Means Clustering to categorize NBA players by role?**  
2️⃣ **Use SHAP to explain why a trade suggestion makes sense?**  
3️⃣ **Visualize trade impact using a NetworkX graph?**  

Let me know your next priority! 🚀