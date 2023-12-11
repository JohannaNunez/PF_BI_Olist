from enum import Enum
 
class DwTables(Enum):
    CUSTOMERS = "customers"
    ORDER_ITEMS = "order_items"
    ORDER_PAYMENTS = "order_payments"
    ORDER_REVIEWS = "order_reviews"
    ORDERS = "orders"
    PRODUCT_CATEGORY_NAME_TRANSLATION = "product_category_name_translation"
    PRODUCTS = "products"
    GEOLOCATION = "geolocation"

class TransferMethod(Enum):
    SP = "sp"
    ORM = "orm"