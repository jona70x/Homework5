The test coverage report shows 42 statements with 3 missed, with a 93% coverage. The file src/order_io.py achieved 90% coverage with two uncovered lines (12 and 15), while src/pricing.py reached 95% coverage, missing one line (25). 
The uncovered lines in order_io.py show an I/O or exception-handling where there are some paths that are not triggered during execution. The missed line in pricing.py is part of the main pricing logic tied to discount validation or formula handling—and and I am going to test it again. Since pricing has the less coverage, I am adding additional tests and confirm correct behavior for all the input. 

# After improvements

- To improve my coverage, I added the following tests to tests/unit/test_my_functions.py:

- test_add_tax_valid: checks valids rates

- test_add_tax_negative_rate: checks negatives

- test_add_tax_default_rate: checks that the default rate is correct

- test_bulk_total_comprehensive: checks for multiple discounts and combinations

By adding these tests, I closed the main coverage in pricing.py. The previously missed line 25—related to negative tax rate validation—is now covered by test_add_tax_negative_rate. 