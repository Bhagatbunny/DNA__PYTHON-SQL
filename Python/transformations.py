import pandas as pd
from datetime import datetime
from utils import FileUtils

logger = FileUtils.set_logger("data_transformer")


class CustomerTransformer:
    """Class to transform customer data."""
    @staticmethod
    def transform(customers: pd.DataFrame) -> pd.DataFrame:
        """Clean and transform customers data."""
        logger.info("Transforming customer data")
        customers = customers.drop_duplicates(subset='customer_id')
        customers['email'] = customers['email'].str.strip()
        customers['name'] = customers['name'].str.strip()
        customers['country'] = customers['country'].str.strip()
        customers['gender'] = customers['gender'].str.strip().str.title()

        customers['join_date'] = pd.to_datetime(customers['join_date'], errors='coerce')
        customers['age'] = customers['age'].apply(lambda x: x if 18 <= x <= 100 else None)
        customers['loyalty_points'] = customers['loyalty_points'].fillna(0)
        customers['is_premium'] = customers['is_premium'].fillna(False)

        today = pd.Timestamp(datetime.today().date())

        # Calculate membership years
        customers['membership_years'] = customers['join_date'].apply(
            lambda x: round((today - x).days / 365, 1) if pd.notnull(x) else None
        )

        def loyalty_level(points):
            if points <= 200:
                return 'Bronze'
            elif points <= 600:
                return 'Silver'
            else:
                return 'Gold'

        # Determine loyalty level
        customers['loyalty_level'] = customers['loyalty_points'].apply(loyalty_level)

        def age_group(age):
            if pd.isnull(age):
                return 'Unknown'
            elif age <= 25:
                return 'Young'
            elif age <= 45:
                return 'Adult'
            elif age <= 60:
                return 'Mid-Age'
            else:
                return 'Senior'

        # Categorize age groups
        customers['age_group'] = customers['age'].apply(age_group)

        # Identify new customers
        customers['new_customer'] = customers['join_date'].apply(
            lambda x: (today - x).days <= 180 if pd.notnull(x) else False
        )

        # Validate email format
        customers['valid_email'] = customers['email'].str.contains(r'^\S+@\S+\.\S+$', regex=True)
        logger.info("customer data cleaned and transformed successfully")
        return customers

class ProductTransformer:
    """Class to transform product data."""
    @staticmethod
    def transform_products(products: pd.DataFrame) -> pd.DataFrame:
        """Clean and transform products data."""
        logger.info("Transforming product data")
        products = products.drop_duplicates(subset='product_id')
        products['category'] = products['category'].str.strip().str.title()
        # products['release_date'] = pd.to_datetime(products['release_date'], errors='coerce')

        products['price'] = products['price'].fillna(products['price'].median())
        products['stock'] = products['in_stock'].fillna(0)

        today = pd.Timestamp(datetime.today().date())

        # products['product_age'] = products['release_date'].apply(
        #     lambda x: round((today - x).days / 365, 1) if pd.notnull(x) else None
        # )

        # products['stock_value'] = products['price'] * products['stock']
        products['is_expensive'] = products['price'] > 1000
        logger.info("Product data cleaned and transformed successfully")
        return products

class OrderTransformer:
    """Class to transform order data."""
    @staticmethod
    def transform_orders(orders: pd.DataFrame) -> pd.DataFrame:
        """Clean and transform orders data."""
        logger.info("Transforming order data")
        orders = orders.drop_duplicates(subset='order_id')
        orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
        orders['quantity'] = orders['quantity'].fillna(1)
        # orders['price'] = orders['price'].fillna(0)

        # orders['order_amount'] = orders['quantity'] * orders['price']
        # orders['high_value_order'] = orders['order_amount'] > 5000
        orders['order_year'] = orders['order_date'].dt.year
        orders['order_month'] = orders['order_date'].dt.month

        today = pd.Timestamp(datetime.today().date())
        orders = orders[orders['order_date'] <= today]

        logger.info("Order data cleaned and transformed successfully")
        return orders

