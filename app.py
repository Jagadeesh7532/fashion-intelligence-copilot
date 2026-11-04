import streamlit as st
import pandas as pd

from tools import (
    inventory_summary,
    find_low_stock,
    get_inventory,
    search_products,
    best_sellers,
    revenue_report,
    october_revenue,
    compare_branch_sales,
    recommend_reorders
)

from agent import route_query

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Fashion Intelligence Copilot",
    page_icon="🛍️",
    layout="wide"
)

# ==================================
# KPI SECTION
# ==================================

summary = inventory_summary()
revenue = revenue_report()

st.title("🛍 Fashion Intelligence Copilot")
st.caption(
    "AI Powered Retail Intelligence Platform"
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Products",
        summary["total_products"]
    )

with c2:
    st.metric(
        "Stock",
        summary["total_stock"]
    )

with c3:
    st.metric(
        "Inventory Value",
        f"₹{summary['inventory_value']:,.0f}"
    )

with c4:
    st.metric(
        "Revenue",
        f"₹{revenue['total_revenue']:,.0f}"
    )

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Low Stock",
        "Inventory",
        "Best Sellers",
        "Revenue",
        "Branch Comparison",
        "Reorder Recommendations",
        "AI Assistant"
    ]
)

# ==================================
# DASHBOARD
# ==================================

if page == "Dashboard":

    st.subheader("📊 Executive Dashboard")

    best = best_sellers().iloc[0]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Low Stock Products",
            summary["low_stock_items"]
        )

    with c2:
        st.metric(
            "October Revenue",
            f"₹{october_revenue():,.0f}"
        )

    with c3:
        st.metric(
            "Top Seller",
            best["product_id"]
        )

    st.divider()

    st.subheader("📈 Executive Insights")

    st.success(
        f"""
Top Selling Product:
{best['product_id']}

Total Revenue:
₹{revenue['total_revenue']:,.0f}

Branch 2 currently leads sales performance.

There are {summary['low_stock_items']} products
below reorder threshold.

Recommendation:
Increase inventory allocation for top selling products
before festive demand peaks.
"""
    )

    st.subheader("🏆 Top Selling Products")

    chart_data = best_sellers()

    st.bar_chart(
        chart_data.set_index("product_id")
    )

    st.subheader("🏬 Branch Performance")

    branch_data = compare_branch_sales()

    st.bar_chart(
        branch_data.set_index("branch")
    )

# ==================================
# LOW STOCK
# ==================================

elif page == "Low Stock":

    st.subheader("⚠️ Low Stock Products")

    st.sidebar.success(
        "Tool: find_low_stock()"
    )

    st.dataframe(
        find_low_stock(),
        use_container_width=True
    )

# ==================================
# INVENTORY
# ==================================

elif page == "Inventory":

    st.subheader("📦 Inventory")

    st.sidebar.success(
        "Tool: get_inventory()"
    )

    st.dataframe(
        get_inventory(),
        use_container_width=True
    )

# ==================================
# BEST SELLERS
# ==================================

elif page == "Best Sellers":

    st.subheader("🏆 Best Sellers")

    data = best_sellers()

    st.sidebar.success(
        "Tool: best_sellers()"
    )

    st.dataframe(
        data,
        use_container_width=True
    )

    st.bar_chart(
        data.set_index("product_id")
    )

# ==================================
# REVENUE
# ==================================

elif page == "Revenue":

    st.subheader("💰 Revenue Analytics")

    report = revenue_report()

    st.metric(
        "Total Revenue",
        f"₹{report['total_revenue']:,.0f}"
    )

    st.metric(
        "Total Orders",
        report["total_orders"]
    )

    st.metric(
        "October Revenue",
        f"₹{october_revenue():,.0f}"
    )

    st.sidebar.success(
        "Tool: revenue_report()"
    )

# ==================================
# BRANCH SALES
# ==================================

elif page == "Branch Comparison":

    st.subheader("🏬 Branch Comparison")

    data = compare_branch_sales()

    st.sidebar.success(
        "Tool: compare_branch_sales()"
    )

    st.dataframe(
        data,
        use_container_width=True
    )

    st.bar_chart(
        data.set_index("branch")
    )

# ==================================
# REORDERS
# ==================================

elif page == "Reorder Recommendations":

    st.subheader(
        "🚚 Diwali Reorder Recommendations"
    )

    st.sidebar.success(
        "Tool: recommend_reorders()"
    )

    data = recommend_reorders()

    st.dataframe(
        data,
        use_container_width=True
    )

    st.info(
        """
Why these products?

✅ High October demand

✅ Low stock

✅ Reorder threshold crossed

✅ Diwali demand expected
"""
    )

# ==================================
# AI ASSISTANT
# ==================================

elif page == "AI Assistant":

    st.subheader(
        "🤖 Fashion Business Assistant"
    )

    query = st.chat_input(
        "Ask a business question..."
    )

    if query:

        st.chat_message("user").write(
            query
        )

        response = route_query(query)

        st.chat_message("assistant").write(
            str(response)
        )

        st.sidebar.success(
            "Agent Executed"
        )

# ==================================
# FOOTER
# ==================================

st.divider()

st.caption(
    "Technizee AI Agent Challenge | Jagadeesh Babu"
)