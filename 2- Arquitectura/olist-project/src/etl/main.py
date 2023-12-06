from src.etl.customers import *
from src.etl.order_items import *
from src.etl.order_payments import *
from src.etl.order_reviews import *
from src.etl.orders import *
from src.etl.product_category_name import *
from src.etl.products import *
from src.models.apiDto import DwTables

def exec_etl_job(job_key):
    if job_key == DwTables.CUSTOMERS:
        if clean_olist_customers_dataset():
            return load_clean_customers_dataset()
        
    elif job_key == DwTables.ORDER_ITEMS:
        if clean_olist_order_items_dataset():
            return load_clean_order_items_dataset()
        
    elif job_key == DwTables.ORDER_PAYMENTS:
        if clean_olist_order_payments_dataset():
            return load_clean_order_payments_dataset()
        
    elif job_key == DwTables.ORDER_REVIEWS:
        if clean_olist_order_reviews_dataset():
            return load_clean_order_reviews_dataset()
        
    elif job_key == DwTables.ORDERS:
        if clean_olist_orders_dataset():
            return load_clean_orders_dataset()
        
    elif job_key == DwTables.PRODUCT_CATEGORY_NAME_TRANSLATION:
        if clean_product_category_name_translation():
            return load_clean_product_category_name_translation_dataset()
        
    elif job_key == DwTables.PRODUCTS:
        if clean_olist_products_dataset():
            return load_clean_products_dataset()
    
    else:
        raise Exception("La clave solicitada es inválida")
    

def transfer_stg_to_prod(job_key, method):
    if job_key == DwTables.CUSTOMERS:
        return transfer_stg_to_prod_customers(method)
        
    elif job_key == DwTables.ORDER_ITEMS:
        return transfer_stg_to_prod_order_items(method)
        
    elif job_key == DwTables.ORDER_PAYMENTS:
        return transfer_stg_to_prod_order_payments(method)
        
    elif job_key == DwTables.ORDER_REVIEWS:
        return transfer_stg_to_prod_order_reviews(method)
        
    elif job_key == DwTables.ORDERS:
        return transfer_stg_to_prod_orders(method)
        
    elif job_key == DwTables.PRODUCT_CATEGORY_NAME_TRANSLATION:
        return transfer_stg_to_prod_product_category_name_translation(method)
        
    elif job_key == DwTables.PRODUCTS:
        return transfer_stg_to_prod_products(method)
    
    else:
        raise Exception("La clave solicitada es inválida")