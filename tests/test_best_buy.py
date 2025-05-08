# tests/test_best_buy.py
import pytest
from product import Product
from store import Store

# --- Product Tests ---
def test_product_init_invalid():
    with pytest.raises(ValueError):
        Product("", 10, 5)
    with pytest.raises(ValueError):
        Product("Test", -1, 5)
    with pytest.raises(ValueError):
        Product("Test", 10, -5)


def test_product_activation_and_quantity():
    p = Product("Test", 10, 0)
    # Initial inactive when quantity is zero
    assert not p.is_active()
    # Activate / deactivate explicitly
    p.activate()
    assert p.is_active()
    p.deactivate()
    assert not p.is_active()

    # Setting quantity
    p.set_quantity(5)
    assert p.get_quantity() == 5
    assert p.is_active()
    with pytest.raises(ValueError):
        p.set_quantity(-1)


def test_product_buy_errors_and_stock_update():
    p = Product("Test", 10, 5)
    # Invalid purchase quantities
    with pytest.raises(ValueError):
        p.buy(0)
    with pytest.raises(ValueError):
        p.buy(-1)
    # Over-purchase
    with pytest.raises(ValueError):
        p.buy(10)
    # Inactive product
    p.deactivate()
    with pytest.raises(Exception):
        p.buy(1)
    # Valid purchase leads to deactivation at zero stock
    p.activate()
    cost = p.buy(5)
    assert cost == 50
    assert p.get_quantity() == 0
    assert not p.is_active()

# --- Store Tests ---
def test_store_operations_and_errors():
    p1 = Product("A", 5, 10)
    p2 = Product("B", 2, 0)
    store = Store([p1, p2])
    # Total quantity sums correctly
    assert store.get_total_quantity() == 10
    # Only active products returned
    assert store.get_all_products() == [p1]
    # Adding a new product
    p3 = Product("C", 1, 3)
    store.add_product(p3)
    assert store.get_total_quantity() == 13
    # Removing a product not in active list should still remove
    store.remove_product(p2)
    # Removing non-existent product raises
    with pytest.raises(ValueError):
        store.remove_product(p2)
    # Invalid order item types
    with pytest.raises(TypeError):
        store.order([("not a product", 1)])
    # Valid order updates quantities and returns total
    total = store.order([(p1, 2), (p3, 3)])
    assert total == (2 * 5 + 3 * 1)
    assert p1.get_quantity() == 8
    assert p3.get_quantity() == 0
    # After p3 depletes, it should be inactive
    assert p3 not in store.get_all_products()
