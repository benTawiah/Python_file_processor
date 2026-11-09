import pytest
from product import Product, Inventory
def test_valid_sale():
    product = Product("Pen", 2, 5)    # arrange: a product with stock 5
    product.sell(2)                   # act: sell 2 units
    assert product.stock == 3         # assert: 5 - 2 should leave 3
    
def test_sale_larger_than_stock():
    product = Product("Clock", 7.9, 5)
    product.sell(100)
    assert product.stock == 5
    
    
def test_negative_price():
    with pytest.raises(ValueError):
        Product("Pen", -5, 3)
        
        
def test_length():
    shop = Inventory()
    shop.add("computer", 100.99,6)
    assert len(shop.product_collect) == 1

def test_missing():
    shop = Inventory()
    result = shop.find("Cup")
    assert result is None
    
def test_remove():
    shop = Inventory()
    shop.add("Shirt", 2, 5)
    shop.remove("Shirt")
    assert len(shop.product_collect) == 0
    assert shop.find("Shirt") is None
    