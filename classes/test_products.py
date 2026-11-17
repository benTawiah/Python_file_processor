import pytest
from product import Product, Inventory
from db_inventory import DbInventory
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

def test_duplicate_name():
    shop=Inventory()
    shop.add("Pen",5.5, 8)
    with pytest.raises(ValueError):
        shop.add("Pen", 5.5, 8)
    



""" @pytest.fixture
def shop():
    inventory = DbInventory(":memory:")
    yield inventory
    inventory.close()


def test_add_and_find(shop):
    shop.add("Pen", 6.9, 9)
    assert shop.find("Pen").stock == 9


def test_sale_reduces_stock(shop):
    shop.add("Pen", 6.9, 9)
    shop.sell("Pen", 2)
    assert shop.find("Pen").stock == 7


def test_oversell_refused_and_stock_unchanged(shop):
    shop.add("Pen", 6.9, 9)
    with pytest.raises(ValueError, match="Not enough stock"):
        shop.sell("Pen", 100)
    assert shop.find("Pen").stock == 9


def test_sell_unknown_product(shop):
    with pytest.raises(ValueError, match="Product not found"):
        shop.sell("Banana", 1)


@pytest.mark.parametrize("quantity", [0, -5])
def test_sell_bad_quantity(shop, quantity):
    shop.add("Pen", 6.9, 9)
    with pytest.raises(ValueError):
        shop.sell("Pen", quantity)
    assert shop.find("Pen").stock == 9


def test_duplicate_name_ignores_case(shop):
    shop.add("Pen", 6.9, 9)
    with pytest.raises(ValueError):
        shop.add("pen", 1.0, 1)


def test_empty_name_refused(shop):
    with pytest.raises(ValueError):
        shop.add("   ", 1.0, 1)


def test_remove_missing_product(shop):
    with pytest.raises(ValueError, match="Product not found"):
        shop.remove("Banana") """