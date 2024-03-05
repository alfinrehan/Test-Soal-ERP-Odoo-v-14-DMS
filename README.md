# Test-Soal-ERP-Odoo-v14

1.
- Endpoints untuk Create: /api/product
  Request Body:
  { 
    "jsonrpc": "2.0",
    "params": {
      "name": "product_name",
      "price": product_price,
      "description": "product_description",
      "qty_available": "product_qty_available"
    }
  }
  
- Endpoints untuk Read: /api/get_product
  
- Endpoints untuk Update: /api/update_product/<int:id>
  Request Body:
  { 
    "name": "new_product_name",
    "price": "new_product_price",
    "description": "new_product_description",
    "qty_available": "new_product_qty_available"
  }
  
- Endpoints untuk Delete: /api/delete_product/<int:id>
  