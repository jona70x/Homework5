# Homework
- Name: Jonathan Carpio Arellano

## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit Test: Tests that verify the functionality of small blocks of code or components that make up a bigger block of code. I would use it to test functions or classes right after I creat them. 
- Integration Test: They test how well code blocks or components work with other units. I would use these tests if I create different classes that need to interact with each other. Also, I'd use them if I install a framework and I need to make sure that works well with my components. 
- Regression Test: These are testss that make sure that there is still compatibility with previous code. Basically, they test that the new changes still work with the previous units and do not break anything. I'd use them if I implement a patch or update an existing framework that is used in my code and I want to make that everything still works. 

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.

- Answer: Pytest discovery is the automatic process where pytest locates test files in a project. When we run pytest in our terminals, it searches the current directory and its subdirectories for test items based on specific naming conventions. Pytest will search for files that start with test_*.py or end with *_test.py 

- A fixture is a function in the pytest framework that provides the initial enviroment for tests. Basically, it sets up all the preconditions, such as data and resources that our tests require. Fixtures are constituted in for steps:

1. Arrange: where we prepara the test with functions, classes, objects, databases, etc.

2. Act: Where the actions test the behavior of our code. 

3. Assert: Where we look at the result of what we are testing. 

4. Cleanup: The tests cleans after running, so other tests are not picking up on previous results. 