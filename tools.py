import pandas as pd
from data import load_inventory, load_sales


# ==================================================
# INVENTORY TOOLS
# ==================================================

def inventory_summary():

    inventory = load_inventory()

    total_products = len(inventory)

    total_stock = inventory["stock_qty"].sum()

    inventory_value = (
        inventory["price"]
        * inventory["stock_qty"]
    ).sum()

    low_stock_items = len(
        inventory[
            inventory["stock_qty"]
            <= inventory["reorder_level"]
        ]
    )

    return {
        "total_products": total_products,
        "total_stock": int(total_stock),
        "inventory_value": float(
            round(inventory_value, 2)
        ),
        "low_stock_items": low_stock_items
    }


def find_low_stock():

    inventory = load_inventory()

    low_stock = inventory[
        inventory["stock_qty"]
        <= inventory["reorder_level"]
    ]

    return low_stock[
        [
            "product_id",
            "product_name",
            "branch",
            "stock_qty",
            "reorder_level"
        ]
    ]


def get_inventory(branch=None):

    inventory = load_inventory()

    if branch:

        inventory = inventory[
            inventory["branch"]
            .str.lower()
            == branch.lower()
        ]

    return inventory


def search_products(
    category=None,
    min_price=None,
    max_price=None
):

    inventory = load_inventory()

    if category:

        inventory = inventory[
            inventory["category"]
            .str.lower()
            .str.contains(
                category.lower(),
                na=False
            )
        ]

    if min_price is not None:

        inventory = inventory[
            inventory["price"] >= min_price
        ]

    if max_price is not None:

        inventory = inventory[
            inventory["price"] <= max_price
        ]

    return inventory[
        [
            "product_id",
            "product_name",
            "category",
            "price",
            "branch"
        ]
    ]


# ==================================================
# SALES TOOLS
# ==================================================

def best_sellers(
    start_date=None,
    end_date=None,
    top_n=10
):

    sales = load_sales()

    if start_date:

        sales = sales[
            sales["date"]
            >= pd.to_datetime(start_date)
        ]

    if end_date:

        sales = sales[
            sales["date"]
            <= pd.to_datetime(end_date)
        ]

    result = (
        sales.groupby("product_id")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    return result


def revenue_report(
    start_date=None,
    end_date=None
):

    sales = load_sales()

    if start_date:
        sales = sales[
            sales["date"] >= pd.to_datetime(start_date)
        ]

    if end_date:
        sales = sales[
            sales["date"] <= pd.to_datetime(end_date)
        ]

    sales = sales.copy()

    sales["revenue"] = (
        sales["quantity"]
        * sales["unit_price"]
    ) - sales["discount"]

    return {
        "total_revenue": float(
            round(
                sales["revenue"].sum(),
                2
            )
        ),
        "total_orders": len(sales)
    }

def october_revenue():

    sales = load_sales()

    october = sales[
        sales["date"].dt.month == 10
    ].copy()

    october["revenue"] = (
        october["quantity"]
        * october["unit_price"]
    ) - october["discount"]

    return round(
        october["revenue"].sum(),
        2
    )


def compare_branch_sales():

    sales = load_sales()

    result = (
        sales.groupby("branch")["quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="quantity",
            ascending=False
        )
    )

    return result


# ==================================================
# BUSINESS RECOMMENDATION TOOL
# ==================================================

def recommend_reorders():

    inventory = load_inventory()
    sales = load_sales()

    october_sales = sales[
        sales["date"].dt.month == 10
    ]

    sales_summary = (
        october_sales.groupby(
            "product_id"
        )["quantity"]
        .sum()
        .reset_index()
    )

    merged = inventory.merge(
        sales_summary,
        on="product_id",
        how="left"
    )

    merged["quantity"] = (
        merged["quantity"]
        .fillna(0)
    )

    merged["recommended_order"] = (
        merged["quantity"]
        + merged["reorder_level"]
        - merged["stock_qty"]
    )

    recommendations = merged[
        merged["recommended_order"] > 0
    ]

    return recommendations[
        [
            "product_id",
            "product_name",
            "branch",
            "stock_qty",
            "quantity",
            "recommended_order"
        ]
    ].sort_values(
        by="recommended_order",
        ascending=False
    )


# ==================================================
# TESTING
# ==================================================

if __name__ == "__main__":

    print("\n=== INVENTORY SUMMARY ===")
    print(inventory_summary())

    print("\n=== LOW STOCK PRODUCTS ===")
    print(find_low_stock())

    print("\n=== INVENTORY SAMPLE ===")
    print(get_inventory().head())

    print("\n=== SEARCH PRODUCTS ===")
    print(
        search_products(
            category="saree"
        ).head()
    )

    print("\n=== BEST SELLERS ===")
    print(best_sellers())

    print("\n=== REVENUE REPORT ===")
    print(revenue_report())

    print("\n=== OCTOBER REVENUE ===")
    print(october_revenue())

    print("\n=== BRANCH SALES ===")
    print(compare_branch_sales())

    print("\n=== REORDER RECOMMENDATIONS ===")
    print(
        recommend_reorders().head(10)
    )
def festive_readiness_report():

    return {
        "high_priority_reorders":
        len(
            recommend_reorders()
            .head(10)
        ),

        "october_revenue":
        october_revenue(),

        "low_stock_items":
        inventory_summary()["low_stock_items"]
    }
# ==================================================
# QUESTION 2
# DISCOUNT RECOMMENDATIONS
# ==================================================

def recommend_discounts():

    inventory = load_inventory()
    sales = load_sales()

    sales_summary = (
        sales.groupby("product_id")["quantity"]
        .sum()
        .reset_index()
    )

    merged = inventory.merge(
        sales_summary,
        on="product_id",
        how="left"
    )

    merged["quantity"] = merged["quantity"].fillna(0)

    candidates = merged[
        (merged["stock_qty"] >= 10)
        &
        (merged["quantity"] <= 50)
    ].copy()

    candidates["stuck_value"] = (
        candidates["stock_qty"]
        * candidates["price"]
    )

    return candidates[
        [
            "product_id",
            "product_name",
            "branch",
            "stock_qty",
            "quantity",
            "stuck_value"
        ]
    ].sort_values(
        by="stuck_value",
        ascending=False
    )


# ==================================================
# QUESTION 3
# SAREE SALES COMPARISON
# ==================================================

def compare_saree_sales_october():

    inventory = load_inventory()
    sales = load_sales()

    saree_ids = inventory[
        inventory["category"]
        .str.contains(
            "saree",
            case=False,
            na=False
        )
    ]["product_id"].unique()

    october = sales[
        sales["date"].dt.month == 10
    ]

    saree_sales = october[
        october["product_id"]
        .isin(saree_ids)
    ]

    return (
        saree_sales.groupby("branch")["quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="quantity",
            ascending=False
        )
    )


# ==================================================
# QUESTION 4
# OCTOBER CATEGORY ANALYSIS
# ==================================================

def october_category_analysis():

    inventory = load_inventory()
    sales = load_sales()

    october = sales[
        sales["date"].dt.month == 10
    ].copy()

    october["revenue"] = (
        october["quantity"]
        * october["unit_price"]
    ) - october["discount"]

    categories = inventory[
        ["product_id", "category"]
    ].drop_duplicates()

    merged = october.merge(
        categories,
        on="product_id",
        how="left"
    )

    return (
        merged.groupby("category")["revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )


# ==================================================
# QUESTION 5
# PRODUCT EXISTENCE CHECK
# ==================================================

def check_product(product_id):

    inventory = load_inventory()

    result = inventory[
        inventory["product_id"]
        == product_id.upper()
    ]

    if result.empty:

        return (
            f"Product {product_id} "
            f"does not exist in inventory."
        )

    return result
def recommend_discounts():

    inventory = load_inventory()
    sales = load_sales()

    sales_summary = (
        sales.groupby("product_id")["quantity"]
        .sum()
        .reset_index()
    )

    merged = inventory.merge(
        sales_summary,
        on="product_id",
        how="left"
    )

    merged["quantity"] = merged["quantity"].fillna(0)

    candidates = merged[
        (merged["stock_qty"] >= 10)
        &
        (merged["quantity"] <= 50)
    ].copy()

    candidates["stuck_value"] = (
        candidates["stock_qty"]
        * candidates["price"]
    )

    return candidates[
        [
            "product_id",
            "product_name",
            "branch",
            "stock_qty",
            "quantity",
            "stuck_value"
        ]
    ]
def compare_saree_sales_october():

    inventory = load_inventory()
    sales = load_sales()

    sarees = inventory[
        inventory["category"]
        .str.contains(
            "saree",
            case=False,
            na=False
        )
    ]["product_id"].unique()

    october = sales[
        sales["date"].dt.month == 10
    ]

    saree_sales = october[
        october["product_id"]
        .isin(sarees)
    ]

    return (
        saree_sales.groupby("branch")["quantity"]
        .sum()
        .reset_index()
    )
def october_category_analysis():

    inventory = load_inventory()
    sales = load_sales()

    october = sales[
        sales["date"].dt.month == 10
    ].copy()

    october["revenue"] = (
        october["quantity"]
        * october["unit_price"]
    ) - october["discount"]

    categories = inventory[
        ["product_id", "category"]
    ].drop_duplicates()

    merged = october.merge(
        categories,
        on="product_id",
        how="left"
    )

    return (
        merged.groupby("category")["revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )
def check_product(product_id):

    inventory = load_inventory()

    result = inventory[
        inventory["product_id"]
        == product_id.upper()
    ]

    if result.empty:

        return (
            f"Product {product_id} "
            f"does not exist in inventory."
        )

    return result
print("\n=== DISCOUNT RECOMMENDATIONS ===")
print(
    recommend_discounts().head(10)
)

print("\n=== SAREE SALES OCTOBER ===")
print(
    compare_saree_sales_october()
)

print("\n=== OCTOBER CATEGORY ANALYSIS ===")
print(
    october_category_analysis()
)

print("\n=== TZ-999 CHECK ===")
print(
    check_product("TZ-999")
)

print("\n=== FESTIVE READINESS REPORT ===")
print(
    festive_readiness_report()
)