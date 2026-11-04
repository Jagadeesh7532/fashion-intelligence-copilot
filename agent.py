from tools import (
    inventory_summary,
    find_low_stock,
    best_sellers,
    revenue_report,
    compare_branch_sales,
    recommend_reorders
)


def route_query(query):

    query = query.lower().strip()

    # =====================================
    # BEST SELLERS
    # =====================================

    if (
        "best seller" in query
        or "top seller" in query
        or "best sellers" in query
    ):

        data = best_sellers()

        answer = "🏆 Top Selling Products\n\n"

        for idx, row in data.iterrows():

            answer += (
                f"{idx + 1}. {row['product_id']} "
                f"({row['quantity']} units sold)\n"
            )

        answer += (
            "\n📈 Business Insight:\n"
            "These products are generating the highest demand "
            "and should receive inventory priority before festive sales."
        )

        return answer

    # =====================================
    # REVENUE
    # =====================================

    elif "revenue" in query:

        report = revenue_report()

        return f"""
💰 Revenue Analysis

Total Revenue:
₹{report['total_revenue']:,.0f}

Total Orders:
{report['total_orders']}

📈 Business Insight:
Revenue performance is strong. Maintaining inventory
availability for top-selling products will help maximize
future sales and reduce missed opportunities.
"""

    # =====================================
    # LOW STOCK
    # =====================================

    elif (
        "low stock" in query
        or "stock alert" in query
    ):

        data = find_low_stock()

        return f"""
⚠️ Inventory Alert

Products Below Reorder Level:
{len(data)}

📈 Business Insight:
Several products have reached their reorder threshold.
Immediate replenishment is recommended for high-demand
festive items.
"""

    # =====================================
    # BRANCH COMPARISON
    # =====================================

    elif (
        "branch" in query
        or "branch comparison" in query
    ):

        data = compare_branch_sales()

        winner = data.iloc[0]

        return f"""
🏬 Branch Performance Comparison

Top Performing Branch:
{winner['branch']}

Units Sold:
{winner['quantity']}

📈 Business Insight:
This branch currently leads sales performance and may
require increased inventory allocation to avoid shortages.
"""

    # =====================================
    # REORDER RECOMMENDATIONS
    # =====================================

    elif (
        "reorder" in query
        or "diwali" in query
        or "restock" in query
    ):

        data = recommend_reorders().head(5)

        answer = "🚚 Priority Reorder Recommendations\n\n"

        for _, row in data.iterrows():

            answer += (
                f"📦 {row['product_name']}\n"
                f"Suggested Reorder Quantity: "
                f"{int(row['recommended_order'])}\n\n"
            )

        answer += (
            "📈 Business Insight:\n"
            "These products show strong October demand and "
            "require immediate replenishment before festive sales."
        )

        return answer

    # =====================================
    # INVENTORY SUMMARY
    # =====================================

    elif "inventory" in query:

        summary = inventory_summary()

        return f"""
📦 Inventory Summary

Total Products:
{summary['total_products']}

Total Stock Units:
{summary['total_stock']}

Inventory Value:
₹{summary['inventory_value']:,.0f}

Low Stock Products:
{summary['low_stock_items']}

📈 Business Insight:
A significant number of products are close to their
reorder thresholds and should be monitored closely.
"""

    # =====================================
    # HELP
    # =====================================

    else:

        return """
🤖 Fashion Business Assistant

I can help with:

✅ Inventory Summary
✅ Revenue Analysis
✅ Best Sellers
✅ Low Stock Products
✅ Branch Performance
✅ Reorder Recommendations

Try asking:

• best sellers
• revenue
• inventory summary
• low stock
• branch comparison
• reorder recommendations
• diwali recommendations
"""
