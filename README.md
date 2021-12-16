# The Journey To DataScience and ML Engineering

## Python Books I am using and for me, they are the best out there
I have used different python books but these three books for me stands out as giants
 1. The Python Apprentice
 2. The Python Journeyman
 3. The Python Master
 4. 

In this journey I will learn many things, so you can follow along
- Error handling
- Decorators
- Containers
- Collections
- Files

Rule of thumb using "Easier to Ask for Forgiveness than Permission (EAFP) style programming
using exception handlers is considered more Pythonic"

## Closures and decorators
- Local functions
- Closures and nested scopes
- Functions decorators
- Validating arguments
- Inheritance

## Introspection
Introspection is the ability of the program to examine its own structure and state.

A process of looking inward to perform self-examination
A process of looking inward to perform self-examination
```
>>> issubclass(type, object)
True
```
isubclass() performs introspection answers a question about an object in the program

#### Signature
The inspect module contains tools for interrogating individual functions
It is done by retrieving a Signature object function

``` 
>>> init_sig = inspect.signature(sorted_set.SortedSet.__init__)
>>> init_sig
``` 

## Functions
Functions are known as callable objects
 - Callable instances
    * This is done through implementing the special __call__() function on our classes
    * Callable instances allow us to define "functions"
 - lambdas
 - Detecting Callable Objects
 - Extended Formal Parameters Syntax
 - Extended Call Syntax
 - Transposing tables
 - 
## Context Managers
  - Context manager represents code that runs before and after the with-statement's block
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
  - __repr__() and __str__()
  - Organizing large functions

## Advanced FLow Control
  - else clauses on loops
   ```
   while condition:
       flag = excute_condition_is_true()
       if flag:
          break
   else: # nobreak
       excute_condition_is_true()
   ```
  - else clauses on try blocks
  - emulating switch statements
  - dispatching on type

# Data Science and ML
### Books 
1. Graph Algorithms for Data Science (Tomaž Bratanič)
2. The Hundred-Page Machine Learning Book (Andriy Burkov)
3. Introduction to Data Science (Rafael A Irizarry)
4. AI Crash Course (Hadelin de Ponteves)
5. Python Machine Learning (Sebastian Raschka)
6. Machine Learning Algorithms (Giuseppe Bonaccorso)
7. Deep Learning for Natural Language Processing (Jason Brownlee)

## Blogs
1. [Khuyen Tran's Data Science github](https://github.com/khuyentran1401)
2. [Math data simplified Khuyen Tran](https://mathdatasimplified.com/)
3. [Chip Huyen](https://huyenchip.com/)
4. [Jeff Heaton](https://github.com/jeffheaton)
5. [Tina Huang](https://www.hellotinah.com/)
6. [Ken Jee](https://www.youtube.com/c/KenJee1/about)
7. [Data Professor](https://www.youtube.com/c/DataProfessor/about)
8. [Jacob Amaral](https://www.youtube.com/user/jacobamaral)
## How to learn Data Science
   - Plan
      * Setting learning goals
      * create your own personal curriculum
      * Making a schedule
      * Consistency
      * Accountability
   - Learn
      * Learn just enough to start building
      * Apply Pomodoro to manage learning time
      * Minimize stuck time
        - get stuck?
        - move on and come back to it later
      * Learning resources
   - Build
      * work on related projects
      * work on weekend projects
      * Use public datasets or compile your own(e.g. scrapping)
      * Compete on Kaggle
   - Explain
     * Explain your model to others
     * Teach others
     * Mentor others
     * Give talks at meetups, conferences and podcasts
     * Draw infographics
     * Write blog posts
     * Build well documented GitHub repository
# Machine Learning
Machine learning, or ML, is a modern software development technique that enables computers to solve problems by using examples of real-world data.
- In supervised learning, every training sample from the dataset has a corresponding label or output value associated with it.
  As a result, the algorithm learns to predict labels or output values.

- In reinforcement learning, the algorithm figures out which actions to take in a situation to maximize
  a reward (in the form of a number) on the way to reaching a specific goal.

- In unsupervised learning, there are no labels for the training data.
  A machine learning algorithm tries to learn the underlying patterns or distributions that govern the data.
  
# Numpy
It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
# Tensorflow
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

# DeepLearning
When you hear the term deep learning, just think of a large deep neural net. Deep
refers to the number of layers typically and so this kind of the popular term that’s
been adopted in the press. I think of them as deep neural networks generally

## NLP
 Natural language processing (NLP) is a collective term referring to automatic
computational processing of human languages. This includes both algorithms that
take human-produced text as input, and algorithms that produce natural looking
text as outputs.

# Data Science tools
## Feature engine
 Feature-engine is a Python 3 package
 Can be installed using anaconda
 - $ conda install -c conda-forge feature_engine
  #### Applications of feature engine
  - Missing data imputation
  - Categorical Variable Encoding
  - Variable Transformation
  - Variable Discretisation
  - Outlier Handling
  - Feature Creation
  - Scikit-learn Wrapper
  
# Data Visualizations tools
Thanks [Khuyen Tran for great job](https://github.com/khuyentran1401)
 - Graphviz
 - folium
 - dtreeviz
 - HiPlot
 - missingno.dendogram
 - matplotlib-venn
 - UMAP
 - Evidently
 - Mermaid
 - pretty-confusion-matrix
 - 
## Jupyter to medium
 Publish blog posts to medium as Jupyter notebook,
 jupyter_to_medium will automate the process of taking your Jupyter Notebook as is and publishing it as a 
 Medium post in almost no time at all, saving huge amounts of time.
 
 #### Installation
 - pip install jupyter_to_medium
 - conda install -c conda-forge jupyter_to_medium
 
 ##### Automatically activated
 You should be able to skip the next step, but if the extension is not showing up in your notebook, run the following command:
 - jupyter bundlerextension enable --py jupyter_to_medium._bundler --sys-prefix
 
 #### Get an Integration Token from Medium
 
  - Before using this package, you must request an integration token from Medium
  -  Read the instructions here on how to get your integration token.[Documentation for Medium's OAuth2 API](https://github.com/Medium/medium-api-docs).
  -  Save your integration token
  -  Once you have your integration token, create the following folder and file in your home directory.
     *  .jupyter_to_medium/integration_token
     *  If you don't save it to this file, you'll need to access it every time you make a new post.
 
 ## FugueSQL in a Notebook
 
 FugueSQL is designed for heavy SQL users to extend the boundaries of traditional SQL workflows.
 FugueSQL allows the expression of logic for end-to-end distributed computing workflows. 
 It can also be combined with Python code to use custom functions alongside the SQL commands.
 It provides a unified interface, allowing the same SQL code to run on Pandas, Dask, and Spark.
 
 ### Installation
 pip install 'fugue[sql]'


