# Product Management System
#### Run the app.py file .
```sh
python app.py
```
#### Task Catalog ###
> Adding the product to Catalog:  
Endpoint : /add/product  
payload : {"name": name, "description": description}  
>>

> Getting product/products from Catalog:  
Endpoint : /get/product  
payload : {"name": name}  
**If we don't provide product name then this endpoint will give all products**  

#### Task Geoprice ###
> Adding price and stock for a product  
Endpoint : /add/product/info  
payload : {"product_id": id, "price": price, "stock": stock}  
>>
> Getting price and stock for a product  
Endpoint : /get/product/info  
payload : {"product_id": id}  
**If we don't provide product id then this endpoint will give price and stock of all products**  

