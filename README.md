# PF_BI_Olist

**Proyecto Final Curso Henry Consultor BI**

Propuesta - E-Commerce Public Dataset by Olist

Una empresa de E-Commerce de Argentina, esta evaluando la posibilidad de expandirse al Brasil, y para ello necesita entender como es el mercado de E-Commerce de alla. Para ello, se consiguio data de 100k de ordenes desde el 2016 hasta el 2018, de distintos puntos de venta en BRasil. Esto se puede ver desde distintas dimensiones, status de las ordenes, precios, pagos y perfomance de envios hacia los usuarios, productos e incluso reviws de los mismos escritos por diversos clientes. Asi mismo, se podra encontrar un archivo de geolocalizacion con todos los codigos postales de Brasil, junto con tu lat y long

El proceso es el siguiente, una vez que el cliente realiza una compra en Olist, un vendedor es notificado para comenzar a armar la orden Luego, cuando el cliente recibe el producto o se agoto el tiempo en el cual debia recibirlo, el cliente recibe una encuesta de satisfaccion por mail, donde puede hacer una review sobre su experiencia

Consideraciones Una order puede tener mas de un producto. Cada producto puede ser despachado por distintos puestos de venta. Todos los nombres de las tiendas y empleados fueron remplazados por nombres de Games of Thrones

Data Schema Los datos estan divididos en distintos datasets para ser comprendidos de una manera mas eficiente

La informacion clasificada fue removida.

# Dataset

El dataset con el que se trabaja en este proyecto fue proveido por Olist. Se cuenta con 11 dataset que refieren a datos sobre las órdenes, productos, categorías de productos, pagos de órdenes, datos de clientes, datos de vendedores, zonas geográficas, entre otras. 
En base a esos conjuntos se ha iniciado el análisis del proyecto.

# EDA

Se ha realizado un análisis exploratorio de datos sobre cada uno de los dataset del proyecto.

El análisis exploratorio de datos se encuentra disponible en el siguiente espacio:
https://colab.research.google.com/drive/1tZtxGP1B0gFNLiAVnFNEmIUKr1y2J4Ta?usp=sharing

## Análisis del EDA

Del análisis se entiende lo siguiente:

1.	**Olist_seller_dataset**

- **Resumen**: Este dataset contiene datos de los vendedores en Brasil. El conjunto de datos tiene 3095 registros y 4 columnas.
- **Variables**: Las variables del dataset son: ['seller_id', 'seller_zip_code_prefix', 'seller_city', '*seller_state*'].
- Variables categóricas: ['seller_id', 'seller_city', 'seller_state']. Tipo de datos : object
- Variables numéricas: ['seller_zip_code_prefix']. Tipo de dato: int64
- **Nulos**: Las mismas no presentan valores nulos.
- **Posible PK**: seller_id
- **Posible FK**:  NA
- **Información encontrada**:
Existen 3095 vendedores ya que se encuentran 3095 valores únicos en la variable seller_id.
Existen 23 regiones de Brasil que contienen 611 ciudades. Se puede mencionar que existe una mayor representación del Estado SP en la variable seller_state con 1849  apariciones dentro de la variable. Esto significa que hay 1849 vendedores que se encuentran dentro del estado SP. Le sigue el estado PR con alrededor de 349 apariciones.
Existe un registro que corresponde a una ciudad, dentro del estado PR que se debe limpiar dado que corresponde a una dirección de e-mail (@)

**2.	product_category_name_translation**

- **Resumen**: Este dataset tiene información únicamente del nombre de las categorías de productos (en portugués e inglés). El conjunto de datos tiene 71 registros y 2 columnas.
- **Variables**: Las variables del dataset son: ['product_category_name', 'product_category_name_english']
- Variables categóricas: ['product_category_name', 'product_category_name_english'] Tipo de datos : object
- Variables numéricas: No aplica.  Tipo de dato: int64
- **Posible PK**: No tiene un ID producto category.
- **Posible FK**:  NA
- **Nulos**: Las mismas no presentan valores nulos.
- **Información encontrada**:
Hay 71 categorías de productos las cuales son: ['health_beauty' 'computers_accessories' 'auto' 'bed_bath_table'
 'furniture_decor' 'sports_leisure' 'perfumery' 'housewares' 'telephony'
 'watches_gifts' 'food_drink' 'baby' 'stationery' 'tablets_printing_image'
 'toys' 'fixed_telephony' 'garden_tools' 'fashion_bags_accessories'
 'small_appliances' 'consoles_games' 'audio' 'fashion_shoes' 'cool_stuff'
 'luggage_accessories' 'air_conditioning'
 'construction_tools_construction'
 'kitchen_dining_laundry_garden_furniture' 'costruction_tools_garden'
 'fashion_male_clothing' 'pet_shop' 'office_furniture' 'market_place'
 'electronics' 'home_appliances' 'party_supplies' 'home_confort'
 'costruction_tools_tools' 'agro_industry_and_commerce'
 'furniture_mattress_and_upholstery' 'books_technical' 'home_construction'
 'musical_instruments' 'furniture_living_room' 'construction_tools_lights'
 'industry_commerce_and_business' 'food' 'art' 'furniture_bedroom'
 'books_general_interest' 'construction_tools_safety'
 'fashion_underwear_beach' 'fashion_sport' 'signaling_and_security'
 'computers' 'christmas_supplies' 'fashio_female_clothing'
 'home_appliances_2' 'books_imported' 'drinks' 'cine_photo' 'la_cuisine'
 'music' 'home_comfort_2' 'small_appliances_home_oven_and_coffee'
 'cds_dvds_musicals' 'dvds_blu_ray' 'flowers' 'arts_and_craftmanship'
 'diapers_and_hygiene' 'fashion_childrens_clothes' 'security_and_services']

**3.	olist_products_dataset**

- **Resumen**: Este dataset tiene información de los productos ofrecidos, como el id, categoría, descripción, photos, y medidas del producto. El conjunto de datos tiene 32951 registros y 9 columnas.
- **Variables**: Las variables del dataset son: ['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
- Variables categóricas: ['product_id', 'product_category_name'] Tipo de datos : object
- Variables numéricas: 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']. Tipo de dato: float64
- **Posible PK**: product_id
- **Posible FK**:  No tiene el id_category_name porque no está definido en la tabla de categorías pero debería tenerlo, ya que tiene la variable producto_category_name.
- **Nulos**: Existen 610 registros que tienen valores faltantes en las siguientes variables: category_name, name_lenght, description_lenght, photos_qty. 610 representa 1.85% del total de registros del dataset.
Existen 2 registros que tienen valores faltantes en weight, lenght, height, width. Representan el  0.006070% del total de registros.
- **Información encontrada:** Existen 32951 productos dado que la variable producto_id contiene esa cantidad de valores únicos.
Hay 73 categorías en la variable producto_category_name en este dataset. En cambio, en el dataset producto_category_name_translation se encuentra 71 categorías. La diferencia está dada por dos categorías extras que se suman en el dataset olist_products_dataset: 'moveis_sala' y 'pc_gamer’.
A su vez, no hay productos (0) de la categoría 'portateis_cozinha_e_preparadores_de_alimentos’ en el dataset olist_products_dataset.
Las categorías con mayor cantidad de productos son cama_mesa_banho con 3029 productos, esporte_lazer con 2867, moveis_decoracao con 2657 productos, beleza_saude con 2444 productos, utilidades_domesticas con 2335 productos.
Las categorías con menor cantidad de productos son: fashion_roupa_infanto_juvenil con 5 productos, casa_conforto_2 con 5 productos, pc_gamer con 3 productos, seguros_e_servicos con           2 productos y cds_dvds_musicais con 1 producto.

**4.	olist_order_reviews_dataset**

- **Resumen**: Este dataset tiene información sobre las reviews de los productos. El conjunto de datos tiene 99224 registros y 7 columnas.
- **Variables**: Las variables del dataset son: 'review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp'
- Variables categóricas: 'review_id', 'order_id', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp' - - Tipo de datos : object
- Variables numéricas: 'review_score', Tipo de dato: int64
- **Posible PK**: review_id
- **Posible FK**:  order_id
- **Nulos**: Existen en la variable review_comment_title 87656 registros vacíos (88,34% del total). Y en la variable review_comment_message: 58247 registros (58,70%) del total. Estas columnas no aportan más información al dataset, dado que se cuenta en su defecto con la variable review_score que no posee nulos.  
- **Información encontrada**: Existen 98410 órdenes en la base. Las ordenes fueron catalogadas mayormente por satisfactorias dado que 57328 tiene puntaje 5 y 19142 tienen puntaje 4, haciendo un total de 76470 lo que representa un 77,70% del total de órdenes.


5.	olist_orders_dataset

- Resumen: Este dataset tiene información de las órdenes. El conjunto de datos tiene 99441 registros y 8 columnas.
Variables: Las variables del dataset son: - order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'
- Variables categóricas: Todas las variables son categóricas. Tipo de datos : object
Variables numéricas: NA. Tipo de dato: int64
- Posible PK: order_id
- Posible FK:  customer_id
- Nulos: Existen en la variable order_approved_at 160 registros vacíos (0,16% del total). En la variable order_delivered_carrier_date: 1783 registros (1,79%) del total y en la variable order_delivered_customer_date: 2965 registros (2,98%) del total Estas columnas no aportan más información al dataset, dado que se cuenta en su defecto con la order_status que no posee nulos.  
- Información encontrada: Existen 99441 órdenes en el dataset. Un 96478 órdenes tienen un estado “delivered” y tan solo 625 han sido canceladas.

6.	olist_orders_payments_ dataset

- Resumen: Este dataset muestra información de los pagos: el id de la orden a la que corresponde, forma de pago, valor del pago. El conjunto de datos tiene 103886 registros y 5 columnas
- Variables: Las variables del dataset son: 'order_id', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value'
- Variables categóricas: 'order_id', 'payment_type'. Tipo de datos : object
- Variables numéricas: 'payment_sequential', 'payment_type', 'payment_installments'. Tipo de dato: int64.
'payment_value'. Tipo de dato: float64
- Posible PK: order_id
- Posible FK:  NA
- Nulos: No hay nulos.  
- Información encontrada: Existen 99440 órdenes en el dataset.

Método de pago: 76795 órdenes fueron pagadas con credit card, 19784 con boleto, 5775 con voucher, 1529 con debit card y 3 no tienen definida su forma de pago.

Valor de pago: Respecto al valor pagado por cada compra (payment_value):

-	La mayoría de las ventas ronda entre los 56.79 y 171.83 pesos. Esto corresponde a 51649 órdenes o su equivalente a 51,94% de las ordenes sobre el total.

-	Un 25% de las órdenes (21643) están por encima de 171, entre ellas:
De 171 a 500 pesos: 21860
De 500 a 1000 pesos: 3105
De 1000 a 10000 pesos: 1148
De más de 10000: 1.

-	Un 25 % de las órdenes (23254) está por debajo de 56 pesos.

7. olist_order_items_dataset

- Resumen: Este dataset tiene información sobre los items de las compras. Usa como referencia el id de la orden, el id del producto y el id del vendedor. El conjunto de datos tiene 112650 registros y 7 columnas.
- Variables: Las variables del dataset son: 'order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value’.
- Variables categóricas: 'order_id', 'payment_type'. Tipo de datos : object
- Variables numéricas: 'order_item_id'. Tipo de dato: int64.
'price', 'freight_value’.Tipo de dato: float64
- Posible PK: order_id
- Posible FK:  product_id, seller_id
- Nulos: No hay nulos.  
- Información encontrada:
Hay 98666 órdenes con 32951 productos involucrados.
La variable order_item_id muestra el número de items que un producto representa en la orden en cuestión. El número de orden de item va desde 1 a 21. Por ejemplo, hay una sola orden que tiene hasta 21 items.

El precio de los productos varía entre 0.85 y 6735 pesos. El promedio del valor es 74.99. La mayoría de los productos (el 50% central de ellos) tiene un valor entre 39.90 y 134.90. Un total 820 productos tienen un valor por arriba de 1000, y 25 productos tienen valor mayor a 3000.

8.	olist_geolocation_dataset

- Resumen: Este dataset contiene información sobre los estados, ciudades, code, lat y lon en Brasil. El conjunto de datos tiene 1000163 registros y 5 columnas.
- Variables: Las variables del dataset son: 'geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state'.
- Variables categóricas: 'geolocation_city', 'geolocation_state'.. Tipo de datos : object
- Variables numéricas: 'geolocation_zip_code_prefix'. Tipo de dato: int64.
'geolocation_lat', 'geolocation_lng'. Tipo de dato: float64
- Posible PK: 'geolocation_zip_code_prefix' posiblemente se puede unir con otras variables que son zip_code en otras tablas, pero tienen diferente prefijo en el nombre de la variable.
- Posible FK:  NA
- Nulos: No hay nulos.  
- Información encontrada: Existen 27 estados y 8011 ciudades.

9. olist_customers_dataset

- Resumen: El dataset muestra información sobre los clientes con su id, un unique id, ciudad, estado. El conjunto de datos tiene 99441 registros y 5 columnas.
- Variables: Las variables del dataset son: 'geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state'.
- Variables categóricas: 'geolocation_city', 'geolocation_state'.. Tipo de datos : object
- Variables numéricas: 'geolocation_zip_code_prefix'. Tipo de dato: int64.
'geolocation_lat', 'geolocation_lng'. Tipo de dato: float64
- Posible PK: 'geolocation_zip_code_prefix' posiblemente se puede unir con otras variables que son zip_code en otras tablas, pero tienen diferente prefijo en el nombre de la variable.
- Posible FK:  customer_id o customer_unique_id / customer_zip_code_prefix
- Nulos: No hay nulos.  
- Información encontrada: Existen 99441 clientes en la base de datos. La mayoría de los clientes  (41746) pertenece al estado de SP.


10.	olist_closed_deals_dataset

- Resumen: El dataset muestra información sobre los tratos comerciales realizados con diferentes tipos de negocios. El conjunto de datos tiene 842 registros y 14 columnas.
- Variables: Las variables del dataset son: 'mql_id', 'seller_id', 'sdr_id', 'sr_id', 'won_date', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'average_stock', 'business_type', 'declared_product_catalog_size', 'declared_monthly_revenue'
- Variables categóricas: 'mql_id', 'seller_id', 'sdr_id', 'sr_id', 'won_date', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'average_stock', 'business_type', Tipo de datos : object
- Variables numéricas: 'declared_product_catalog_size', 'declared_monthly_revenue' Tipo de dato: float64
- Posible PK: mql_id
- Posible FK:  seller_id
- Nulos: business_segment: 1 , lead_type :6, lead_behaviour_profile :177, has_company: has_gtin:                      778, average_stock : 776, business_type : 10, declared_product_catalog_size :773.
- Información encontrada: Existen 587 acuerdo comerciales con reseller, 242 con manufacturer, 3 con othres y 10 que no se puede determinar por tener valor vacío. El tipo de acuerdo podía ser: ‘online_medium', 'industry', 'online_big', 'online_small', 'offline', 'online_top', 'online_beginner', 'other', nan

11. olist_marketing_qualified_leads_dataset

- Resumen: Este dataset refiere a los clientes potenciales obtenidos, con su primer fecha de contacto y origen del contacto. El conjunto de datos tiene 8000 registros y 4 columnas.
- Variables: Las variables del dataset son: ['mql_id', 'first_contact_date', 'landing_page_id', 'origin']
- Variables categóricas: ['mql_id', 'first_contact_date', 'landing_page_id', 'origin']- Tipo de datos : object
- Variables numéricas: NA.
- Posible PK: mql_id
- Posible FK:  NA.
- Nulos: Origin tiene 60 registros vacíos.  
- Información encontrada: Existen 8000 clientes potenciales originados de diferentes formas de marketing como organic search, paid search, social, direct traffic, email, referral, etc. Organic search tiene un total de 2256 registros, paid search 1586 y social 1350.

# Análisis del valor las órdenes en los dataset

En la tabla de ordenes y pagos, (olist_order_payments_dataset) se puede ver tanta cantidad valores de pago como payment_sequential. Es decir, que una orden de pago está dividida en varias secuencias de pago. Esto quiere decir, que cada secuencia de pago tiene un valor de pago asociado y la suma de cada uno de ellos será el total monetario de la orden. 

Asimismo, en la tabla de ordenes y productos, olist_order_items_dataset, se puede entender que una orden tiene asociada varios productos . El valor de cada producto mas su valor de envio, da el mismo total que la orden. 

Al poder ver esto, se puede entender que:
- existen varios registros con el mismo order_id, no solo por la cantidad de diferentes productos asociados a la orden, si no tambien por las distintas "payment_sequential" con la que cuenta la orden. Cada una de ellas tiene un valor distinto en el pago (payment_installments) pero si se suman, va a dar el total de lo que se pago por producto y la suma de productos, dara el total del pago de la orden.

Por lo tanto se decide:

Realizar una agrupamiento por orden y dejar el valor total unificado en una nueva variable para poder utilizarla en la predicción de ventas.


Las tablas a utilizar para el modelo de ventas serán:

Tabla (5): olist_orders_dataset
- Variables a utilizar:
 * order_id
 * order_status: se tomarán aquellas con valor delivered y se excluirán aquellas canceled.
 *order purchase timestamp (para saber la fecha de la orden)

Tablas y variables a utilizar en el modelado de machine learning

Tabla (6): olist_order_payments_dataset.
- Variables a utilizar:
 * order_id
 * payment sequential (para agrupar la orden y calcular el monto total)
 * payment value (será la base del monto total de la orden)

Existe dos tablas que aportan información de las ventas, pero a priori se descartan del análisis. Una de ellas contiene información de cuantos productos existen por orden y cuales productos son los comprados. La otra tiene información de las categorías de los productos.

Tabla (3): olist_products_dataset
- Variables:
 * product_id
 * product_category_name

Tabla (7): olist_order_items_dataset
- Variables:
 * order_id
 * order_item_id
 * product_id



# Análisis de serie de tiempo - Predicción ARIMA

Se ha decidido implementar un modelo ARIMA para predecir en base al tiempo, los valores de órdenes que se tendrán de aquí a 3 años.

Los pasos que se han tomado son los siguientes:

Resumen: 

1. Preparación de los datos:
- Carga de datos: Cargar los conjuntos de datos en Python utilizando bibliotecas como Pandas para manipular los datos.
 - Procesamiento: Se crearán los dataframes necesarios para llegar al dataframe final que se procesará con ARIMA. Se aclara que se ha creado una variables llamado pago_orden que contiene el valor de ventas por orden y valor promedio por mes y año. Esta variable es la variable a predecir..
2. Aplicación de modelo de series de tiempos:

- Arima:
Preparación de los Datos: Los datos se agrupan por mes (con el objetivo de obtener una serie temporal más manejable y para ayudar a revelar patrones estacionales o tendencias)

Revisión de la Estacionariedad: Se realizan pruebas de estacionariedad, como la prueba de Dickey-Fuller aumentada, para determinar si es necesario diferenciar los datos para hacerlos estacionarios. Los datos no eran estacionarios, por lo que se aplicó la técnica para convertirlos en estacionarios y poder aplicarles ARIMA.

Identificación de los Parámetros ARIMA: Se utilizaron las funciones de autocorrelación (ACF) y autocorrelación parcial (PACF) para identificar los parámetros p, d, y q del modelo ARIMA.

Ajuste del Modelo ARIMA: Se ajusto el modelo ARIMA con los parámetros identificados a los datos. Y adicionalmente se optimizaron los parámetros con Optuna.

Predicciones: Se realizaron las predicciones para los próximos años.


# PRESENTACIÓN

Sprint 1 - Disponible en: https://docs.google.com/presentation/d/1wFD95IvHmxr3oWKwislMtzi_sooNNYs-CMHx7Rlzb7k/edit?usp=sharing
Sprint 2 - Disponible en: https://docs.google.com/presentation/d/1aA-qDT_98h2zXOgji52HPClorW7Ov_iAyRxW8jGSVfw/edit?usp=sharing

# CICLO DE VIDA DEL DATO

![Ciclo de vida del dato](https://github.com/C0A0A/PF_BI_Olist/blob/main/diagrama-flujo-datos.jpg)

# Código de EDA y Predicciones en Arima.

Ver documentos del proyecto.

Actualización: 11.12.2023
