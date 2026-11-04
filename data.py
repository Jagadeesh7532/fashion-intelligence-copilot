import pandas as pd


# ==================================================
# INVENTORY CLEANING
# ==================================================

def clean_inventory(df):

    df.columns = df.columns.str.strip()

    # Product ID cleanup
    df["product_id"] = (
        df["product_id"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Price cleanup
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["price"] = df["price"].fillna(
        df["price"].median()
    )

    # Stock cleanup
    df["stock_qty"] = pd.to_numeric(
        df["stock_qty"],
        errors="coerce"
    )

    df["stock_qty"] = df["stock_qty"].fillna(0)

    # Reorder cleanup
    df["reorder_level"] = pd.to_numeric(
        df["reorder_level"],
        errors="coerce"
    )

    df["reorder_level"] = df["reorder_level"].fillna(0)

    # Date cleanup
    df["last_restocked"] = pd.to_datetime(
        df["last_restocked"],
        errors="coerce",
        format="mixed"
    )

    return df


# ==================================================
# SALES CLEANING
# ==================================================

def clean_sales(df):

    df.columns = df.columns.str.strip()

    # Product ID cleanup
    df["product_id"] = (
        df["product_id"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    # Mixed date formats:
    # YYYY-MM-DD
    # DD-MM-YYYY

    def parse_date(value):

        if pd.isna(value):
            return pd.NaT

        value = str(value).strip()

        # YYYY-MM-DD
        try:
            if len(value) >= 10 and value[:4].isdigit():
                return pd.to_datetime(
                    value,
                    format="%Y-%m-%d"
                )
        except:
            pass

        # DD-MM-YYYY
        try:
            return pd.to_datetime(
                value,
                format="%d-%m-%Y"
            )
        except:
            pass

        return pd.NaT

    df["date"] = df["date"].apply(parse_date)

    # Unit Price
    df["unit_price"] = (
        df["unit_price"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    # Quantity
    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    # Discount
    df["discount"] = (
        df["discount"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["discount"] = pd.to_numeric(
        df["discount"],
        errors="coerce"
    )

    # Fill missing values
    df["discount"] = df["discount"].fillna(0)

    df["unit_price"] = df["unit_price"].fillna(
        df["unit_price"].median()
    )

    df["quantity"] = df["quantity"].fillna(0)

    return df


# ==================================================
# LOADERS
# ==================================================

def load_inventory():

    inventory = pd.read_csv(
        "data/inventory.csv"
    )

    return clean_inventory(inventory)


def load_sales():

    sales = pd.read_csv(
        "data/sales.csv"
    )

    return clean_sales(sales)


# ==================================================
# TESTING
# ==================================================

if __name__ == "__main__":

    inventory = load_inventory()
    sales = load_sales()

    print("\n=== INVENTORY MISSING VALUES ===")
    print(inventory.isnull().sum())

    print("\n=== SALES MISSING VALUES ===")
    print(sales.isnull().sum())

    print("\n=== INVENTORY SHAPE ===")
    print(inventory.shape)

    print("\n=== SALES SHAPE ===")
    print(sales.shape)

    print("\n=== SAMPLE SALES DATES ===")
    print(sales["date"].head(20))

    print("\n=== DATE RANGE ===")
    print("Min Date:", sales["date"].min())
    print("Max Date:", sales["date"].max())

    print("\n=== TOTAL SALES RECORDS ===")
    print(len(sales))