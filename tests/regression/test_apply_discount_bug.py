from src.pricing import apply_discount

def test_apply_discount_regression():
    result = apply_discount(100.0, 10)
    assert result == 90.0, f"Expected 90.0 but got {result}"


def test_apply_discount_various_percentages():
    assert apply_discount(50.0, 20) == 40.0
    assert apply_discount(100.0, 100) == 0.0
    assert apply_discount(100.0, 50) == 50.0
    assert apply_discount(100.0, 1) == 99.0

