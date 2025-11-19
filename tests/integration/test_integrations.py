import pytest
import src.order_io as order_io
from src.pricing import format_currency, bulk_total

def test_order_integration(tmp_path):
    csv_file = tmp_path / "order.csv"
    csv_file.write_text(
        "Apple,$1.50\n"
        "Banana,$0.75\n"
        "Orange,$2.00\n"
    )
    items = order_io.load_order(str(csv_file))
   
    assert len(items) == 3
    assert items[0] == ("Apple", 1.50)
    assert items[1] == ("Banana", 0.75)
    assert items[2] == ("Orange", 2.00)
    
    prices = [price for (name, price) in items]
    total = bulk_total(prices, discount_percent=0, tax_rate=0.07)
    receipt_file = tmp_path / "receipt.txt"
    order_io.write_receipt(str(receipt_file), items, discount_percent=0, tax_rate=0.07)
    receipt_content = receipt_file.read_text()
    
    assert "Apple: $1.50" in receipt_content
    assert "Banana: $0.75" in receipt_content
    assert "Orange: $2.00" in receipt_content
 
    expected_total = format_currency(total)
    assert f"TOTAL: {expected_total}" in receipt_content


def test_order_workflow_with_discount(tmp_path):
    csv_file = tmp_path / "order_with_discount.csv"
    csv_file.write_text(
        "Item1,$10.00\n"
        "Item2,$20.00\n"
    )
    items = order_io.load_order(str(csv_file))
   
    assert len(items) == 2
    assert items[0] == ("Item1", 10.00)
    assert items[1] == ("Item2", 20.00)

    receipt_file = tmp_path / "receipt_with_discount.txt"
    order_io.write_receipt(str(receipt_file), items, discount_percent=10, tax_rate=0.07)

    receipt_content = receipt_file.read_text()

    assert "Item1: $10.00" in receipt_content
    assert "Item2: $20.00" in receipt_content

    prices = [price for (name, price) in items]
    total = bulk_total(prices, discount_percent=10, tax_rate=0.07)
    expected_total = format_currency(total)
  
    assert f"TOTAL: {expected_total}" in receipt_content