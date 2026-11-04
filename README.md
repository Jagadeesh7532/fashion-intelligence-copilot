# 🛍 Fashion Intelligence Copilot

## Live Demo

**Streamlit Application:**  
https://your-app.streamlit.app

**GitHub Repository:**  
https://github.com/yourusername/fashion-intelligence-copilot

---

# Overview

Fashion Intelligence Copilot is an AI-powered retail analytics and decision-support platform designed for fashion retailers.

The platform transforms raw inventory and sales data into actionable business insights through analytics dashboards, recommendation engines, and a conversational AI assistant.

The goal is to help retail managers make informed decisions related to inventory management, revenue optimization, branch performance, and festive season planning.

---

# Key Features

## 📦 Inventory Analytics

- Total Product Tracking
- Stock Quantity Monitoring
- Inventory Valuation
- Low Stock Detection
- Branch-wise Inventory Visibility

## 💰 Revenue Analytics

- Total Revenue Analysis
- October Revenue Analysis
- Order Volume Tracking
- Business Performance Insights

## 🏆 Sales Intelligence

- Best Selling Products
- Product Demand Analysis
- Branch Performance Comparison
- Sales Trend Monitoring

## 🚚 Recommendation Engine

- Diwali Reorder Recommendations
- Inventory Prioritization
- Discount Recommendations
- Inventory Risk Identification

## 🤖 AI Business Assistant

Users can ask:

```text
best sellers

revenue

inventory summary

low stock products

branch comparison

reorder recommendations
```

The assistant converts analytics into business-friendly insights.

---

# Challenge Deliverables

## Part A Features

✅ Retrieve inventory by branch or overall

✅ Low stock detection

✅ Best-selling products

✅ Product search

✅ Inventory summary

## Part B Business Questions

✅ Reorder recommendations before Diwali

✅ Products suitable for discounting

✅ Saree sales comparison between branches

✅ October revenue and top category analysis

✅ Non-existent product validation (TZ-999)

---

# Business Questions Addressed

## 1. Which products should be reordered before Diwali?

The recommendation engine combines:

- Current Stock
- Reorder Threshold
- October Demand

Top recommendations:

| Product | Branch | Suggested Reorder |
|----------|----------|----------:|
| TZ-106 Haldi Special Kota Saree | Branch 1 | 142 |
| TZ-106 Haldi Special Kota Saree | Branch 2 | 143 |
| TZ-112 Classic Cotton Kurta | Branch 1 | 105 |
| TZ-112 Classic Cotton Kurta | Branch 2 | 112 |

---

## 2. Which products should be discounted?

Products with high inventory and low sales:

- Navy Nehru Jacket Set
- Sky Blue Sequin Saree
- Maroon Velvet Kurta Set
- Bandhani Cotton Saree

These products represent inventory with low turnover.

---

## 3. Compare Saree Sales Between Branches

| Branch | Saree Units Sold |
|----------|----------:|
| Branch 1 | 215 |
| Branch 2 | 347 |

Branch 2 outperformed Branch 1 in saree sales during October.

---

## 4. October Revenue Performance

| Metric | Value |
|----------|---------:|
| Total Revenue | ₹87,66,787 |
| October Revenue | ₹37,82,100 |
| Total Orders | 3021 |

### Top Revenue Category

**Saree**

Revenue Contribution:

**₹17,77,831**

---

## 5. Product Validation

Query:

```text
How many pieces of TZ-999 do we have?
```

Response:

```text
Product TZ-999 does not exist in inventory.
```

The system avoids hallucinations and never invents inventory data.

---

# System Architecture

```text
User
│
▼

Streamlit Dashboard
│
▼

AI Business Assistant
│
▼

Tool Router
│
├── Inventory Analytics
│
├── Revenue Analytics
│
├── Sales Intelligence
│
└── Recommendation Engine
│
▼

CSV Data Sources
```

---

# Project Structure

```text
fashion-copilot/
│
├── app.py
├── agent.py
├── tools.py
├── data.py
│
├── data/
│   ├── inventory.csv
│   └── sales.csv
│
├── screenshots/
│   ├── dashboard.png
│   ├── revenue_analytics.png
│   ├── best_sellers.png
│   ├── reorder_recommendations.png
│   ├── ai_total_revenue.png
│   ├── ai_best_sellers.png
│   └── ai_reorder_recommendations.png
│
├── README.md
├── requirements.txt
└── .env
```

---

# Data Cleaning Decisions

## Inventory Dataset

- Standardized Product IDs
- Removed Currency Symbols
- Cleaned Price Fields
- Handled Missing Prices
- Filled Missing Stock Values
- Parsed Restock Dates

## Sales Dataset

- Fixed Mixed Date Formats
- Cleaned Unit Prices
- Filled Missing Discounts
- Converted Numeric Fields
- Standardized Product IDs

---

# Screenshots

## 📊 Executive Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 💰 Revenue Analytics

![Revenue Analytics](screenshots/revenue_analytics.png)

---

## 🏆 Best Sellers Analysis

![Best Sellers](screenshots/best_sellers.png)

---

## 🚚 Diwali Reorder Recommendations

![Reorder Recommendations](screenshots/reorder_recommendations.png)

---

## 🤖 AI Assistant – Revenue Analysis

![AI Revenue](screenshots/ai_total_revenue.png)

---

## 🤖 AI Assistant – Best Sellers

![AI Best Sellers](screenshots/ai_best_sellers.png)

---

## 🤖 AI Assistant – Reorder Recommendations

![AI Reorder Recommendations](screenshots/ai_reorder_recommendations.png)

---

# Technology Stack

## Backend

- Python
- Pandas
- NumPy

## Frontend

- Streamlit

## Analytics

- Business Intelligence Tools
- Recommendation Engine

## AI Components

- Tool Routing Agent
- Conversational Business Assistant

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd fashion-copilot
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Example Queries

```text
best sellers
```

```text
revenue
```

```text
inventory summary
```

```text
branch comparison
```

```text
reorder recommendations
```

---

# AI Usage Disclosure

AI tools were used for:

- Code generation assistance
- Debugging support
- Documentation drafting
- UI improvements

All generated code was manually reviewed, tested, and modified as required.

Business calculations, recommendations, and analytics outputs were verified using the provided inventory and sales datasets.

---

# Future Improvements

- Real Claude Function Calling
- Demand Forecasting
- Inventory Forecasting
- Sales Prediction
- Customer Segmentation
- Multi-Store Support
- Automated Reporting

---

# Author

**Jagadeesh Babu**

B.Tech Information Technology  
Cybersecurity & AI Enthusiast

---

# Conclusion

Fashion Intelligence Copilot combines inventory analytics, sales intelligence, recommendation systems, and conversational AI into a unified retail decision-support platform.

The application helps retailers improve inventory planning, revenue visibility, and operational decision-making through data-driven insights and AI-powered assistance