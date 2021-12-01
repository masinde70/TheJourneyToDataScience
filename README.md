# The Journey To DataScience and ML Engineering

## Python Books I am using and for me they are the best out there
I have used different python books but these three books for me stands out as giants
 1. The Python Apprentice
 2. The Python Journeyman
 3. The Python Master
 4. 

In this journey I will learn many things so can you
- Error handling
- Decorators
- Containers
- Collections
- Files
## Closures and decorators
- Local functions
- Closures and nested scopes
- Functions decorators
- Validating arguments
- Inheritance

## Introspetion
Introspection is the ability of the program to examine its own structure and state.
A process of looking inward to perform self-examinition

## Functions
Functions are known as callable objects
 - Collable instances
    * This is done through implimenting the special __call__() function on our classes
    * Callable instances allow us to define "functions"
 - lambdas
 - Detecting Callable Objects
 - Extended Formal Paramaters Syntax
 - Extended Call Systax
 - Transposing tables
## Context Managers
  - Context manager represents code that runs before and after the with-stament's block
  - Context managers are objects designed to work in with-statements
  - The expression of a with-statement must evaluate to a context-manager
  - Context managers have code that is run before and after with-blocks
  - Context managers are particularly useful for resource management
  - Files objects are a commonly used example of context-managers
  - The context manager protocol involves two methods, __enter__() and __exit__()
  - __enter__() is called before the with-block
  - The return value of __enter__() is bound to name in the optional as-clause of a with-statement
  - contextlib provides some utilities for working with with-statements
  - contextlib.contextmanager is a decorator used for creating context-manager factories out of generator functions
  - A contextmanager generator yields a value which will be bound to name in the optional as-clause
  
  
## Strings and representations
  - Python supports two strings representation
  - __reper__() and __str__()
- Organizing large functions
## How to learn Data Science
   - Plan
      * Setting learning goals
      * create your own personal curriculum
      * Making a schedule
      * Consistency
      * Accountability
   - Learn
      * Learn just enough to start buliding
      * Apply Pomodoro to manage learning time
      * Minimize stuck time
        - get stuck?
        - move on and come back to it later
      * Learning resources
   - Build
      * work on related projects
      * work on weeked projects
      * Use public datasets or compile your own(e.g webscrapping)
      * Compete on Kaggle
   - Explain
     * Explain your model to others
     * Teach others
     * Mentor others
     * Give talks at meetups, conferences and podcasts
     * Draw infographics
     * Write blog posts
     * Build well documented GitHub repository
## Data Science and ML

- Numpy
- Tensorflow
- Visualizations
- NLP
- DeepLearning
## Data Science tools
### Feature engine
 Feature-engine is a Python 3 package
 Can be installed using anaconda
 - $ conda install -c conda-forge feature_engine
 ### Jupyter to medium
 Publish blog posts to medium as Jupyter notebook,
 jupyter_to_medium will automate the process of taking your Jupyter Notebook as is and publishing it as a 
 Medium post in almost no time at all, saving huge amounts of time.
 #### Installtion
 - pip install jupyter_to_medium
 - conda install -c conda-forge jupyter_to_medium
 
 ##### Automatically activated
 You should be able to skip the next step, but if the extension is not showing up in your notebook, run the following command:
 - jupyter bundlerextension enable --py jupyter_to_medium._bundler --sys-prefix
 #### Get an Integration Token from Medium
  - Before using this package, you must request an integration token from Medium
  -  Read the instructions here on how to get your integration token.[Documentation for Medium's OAuth2 API](https://github.com/Medium/medium-api-docs).

 ### Applications of featue engine
  - Missing data imputation
  - Categorical Variable Encoding
  - Variable Transformation
  - Variable Discretisation
  - Outlier Handling
  - Feature Creation
  - Scikit-learn Wrapper
