

# ** Project Report – Phishing URL Detection**

## **Project Overview**

This project focuses on detecting phishing websites using machine learning classification techniques. By analyzing URL-based and domain-based features, the model classifies websites as **phishing** or **legitimate**, helping to enhance cybersecurity and protect users from malicious online threats. The final solution is deployed as an interactive **Streamlit web application**.

---

## **Objectives**

* Analyze phishing and legitimate URL characteristics
* Perform exploratory data analysis (EDA) to understand feature behavior
* Build and compare multiple classification models
* Evaluate models using appropriate classification metrics
* Deploy the best-performing model as a web application

---

## **Methodology**

1. **Data Loading and Understanding**
2. **Exploratory Data Analysis (EDA)**
3. **Data Preprocessing**
4. **Model Building and Training**
5. **Model Evaluation**
6. **Model Saving**
7. **Deployment using Streamlit**

---

## **Data Preparation**

* Dataset contains **30 URL-based and domain-based features**
* Target variable:

  * `1` → Phishing
  * `-1` → Legitimate
* Feature values include **{-1, 0, 1}**, representing suspicious, neutral, and legitimate indicators

### Preprocessing Steps:

* Verified no missing or duplicate values
* Converted target labels where required for model compatibility
* Split data into training and testing sets using **stratified sampling** to preserve class distribution

---

## **Exploratory Data Analysis (EDA)**

Key insights from EDA and correlation analysis:

* Several features such as **UsingIP, ShortURL, HTTPSDomainURL, RequestURL, and AbnormalURL** show strong correlation with phishing behavior
* Heatmap analysis revealed **no severe multicollinearity**, making tree-based and linear models suitable
* Phishing URLs tend to:

  * Use IP addresses instead of domain names
  * Contain abnormal URL structures
  * Lack HTTPS or have misleading HTTPS usage
* Class distribution is reasonably balanced, reducing bias risk

---

## **Model Building and Training**

The following classification models were implemented and compared:

### **1. Logistic Regression**

* Used as a baseline linear classifier
* Provides strong interpretability and fast training

**Performance:**

* Accuracy (Test): **94.0%**
* Precision: **94.1%**
* Recall: **95.2%**
* F1-score: **94.7%**

---

### **2. Random Forest Classifier**

* Ensemble-based model capturing nonlinear feature interactions
* Robust to noise and feature correlations

**Performance:**

* Improved generalization over Logistic Regression
* Better handling of complex phishing patterns
* Reduced false negatives (critical for security applications)

---

## **Model Evaluation**

Evaluation was performed using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Confusion Matrix Interpretation (Logistic Regression Example):

* **True Positives**: Correctly identified phishing URLs
* **True Negatives**: Correctly identified legitimate URLs
* **False Positives**: Legitimate URLs flagged as phishing
* **False Negatives**: Phishing URLs missed by the model (most critical)

The models demonstrated **strong recall**, ensuring phishing sites are rarely missed.

---

## **Model Saving**

* Final trained models were saved using `joblib`
* Ensures fast loading and compatibility during deployment

```python
joblib.dump(model, "phishing_model.pkl")
```

---

## **Deployment**

### **Deployment Stack**

* Frontend: **Streamlit**
* Model Storage: `.pkl` file
* Hosting: **Streamlit Cloud**

### Application Features:

* User inputs URL feature values via UI
* Real-time prediction:

  * **Phishing Website**
  * **Legitimate Website**
* Clean and user-friendly interface
* Fast inference performance

🔗 **Live App**:
[https://phishing-url-detection-project-cj7tpltrmzqb96n6rwcopq.streamlit.app/](https://phishing-url-detection-project-cj7tpltrmzqb96n6rwcopq.streamlit.app/)

---

## **Results & Conclusion**

* Machine learning models effectively detect phishing URLs with **high accuracy and recall**
* Random Forest and Logistic Regression both performed well, with Random Forest capturing more complex patterns
* Feature-based URL analysis proves to be a reliable approach for phishing detection
* Successful deployment enables real-time phishing classification for end users

---

## **Future Enhancements**

* Integrate real-time URL feature extraction
* Add Gradient Boosting / XGBoost for performance comparison
* Deploy using Docker and AWS for production scalability
* Implement logging and monitoring for predictions
* Extend model to detect zero-day phishing URLs

---


