import pytest
import src.pricing as pricing

@pytest.mark.parametrize("price, expected_price", [("$1,234.50", 1234.50), ("$12.5", 12.5), ("$.99", 0.99)])
def test_parse_price_valid(price, expected_price):
    assert pricing.parse_price(price) == expected_price

@pytest.mark.parametrize("invalid_price", ["abc", "$12,34,56", "invalid"])
def test_parse_price_invalid(invalid_price):
    result = pricing.parse_price("$12,34,56")
    assert result == 121234.56
    with pytest.raises(ValueError):
        pricing.parse_price(invalid_price)

@pytest.mark.parametrize("value, expected", [
    (1234.5, "$1234.50"),      
    (12.5, "$12.50"),          
    (0.99, "$0.99"),           
])
def test_format_currency(value, expected):
    assert pricing.format_currency(value) == expected

@pytest.mark.parametrize("price, percent, expected", [
    (100, 50, 50),          
    (100, 100, 0),          
])
def test_apply_discount_valid(price, percent, expected):
    assert pricing.apply_discount(price, percent) == expected

@pytest.mark.parametrize("price, percent", [
    (100, -10),             
    (50, -1),
    (100, 0),
    (100, 101),
])
def test_apply_discount_negative_or_over(price, percent):
    if percent <= 0 or percent > 100:
        with pytest.raises(ValueError):
            pricing.apply_discount(price, percent)

@pytest.mark.parametrize("price, discount_percent, tax_rate, expected", [([1,2,3,4,5], 0, 0.07, 16.05)])
def test_bulk_total(price, discount_percent, tax_rate, expected):
    assert pricing.bulk_total(price, discount_percent,tax_rate ) == expected