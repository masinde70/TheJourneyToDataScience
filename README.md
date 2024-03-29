# The Journey To DataScience
Data Scientists are expected to build end-to-end solutions to business problems,
which models are a small but important part of it. Data scientist builds data science 
applications.

## Yan 
[Yann LeCun’s Deep Learning Course at CDS](https://cds.nyu.edu/deep-learning/)

## Python Books I am using and for me, they are the best out there
I have used different python books but these three books for me stands out as giants
 1. The Python Apprentice
 2. The Python Journeyman
 3. The Python Master
 4. 

In this python journey I will learn many things, so you can follow along
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

## Dispatch
To dispatch on type means that the code which will be executed depends on some
way on the type of object or objects.

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
8. Effective Data Science Infrastructure (Ville Tuulos)

## What I have to learn
* Apache Spark
*  Databricks
*  Delta Lake 
*  MLFLow
*  Apache Airflow

#### Graphs
1. [Introduction to Graph Neural networks](https://distill.pub/2021/gnn-intro/)
2. [Knowledge Graph](https://innovator.news/the-business-case-for-knowledge-graphs-d6764592028e)
3. [Bayesian Deep Learning for Graphs](https://media-exp1.licdn.com/dms/document/C4D1FAQF0H08wyZ-DkQ/feedshare-document-pdf-analyzed/0/1652694801183?e=1653523200&v=beta&t=Npq_Qw8tmFU1hp21xnxcTtbYcLNvs2tugO2LyQhx3Z8)
4. [Graphs](https://dlg4nlp.github.io/index.html)
5. [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
6. 

#### My wish list
1. [Deep Learning with PyTorch by Eli Stevens, Luca Antiga, and Thomas Viehmann](https://www.manning.com/books/deep-learning-with-pytorch)
2. [MLOPs Deep learning in production by Sergios Karagianakos](https://leanpub.com/DLProd)
3. [Machine learning engineering by Andriy Burkov](https://leanpub.com/MLE)
4. [A Programmer's Guide to Artificial Intelligence by Laurence Moroney](https://theaisummer.com/deep-learning-books-2022/)
5. [Designing Machine Learning Systems](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969)

### Machine Learning Systems Design 
1. [CS 329S: Machine Learning Systems Design](https://stanford-cs329s.github.io/syllabus.html)
2. [The ML booklet by Chip Huyen](https://huyenchip.com/machine-learning-systems-design/toc.html)
3. [Grokking the Machine Learning Interview](https://www.educative.io/courses/grokking-the-machine-learning-interview)
4. [Machine Learning Engineering for Production (MLOps) Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)


#### Interview books
1. [Machine learning Interview by Chip Huyen](https://huyenchip.com/ml-interviews-book/)
2. [Machine Learning Interview questions](https://arxiv.org/abs/2201.00650)
3. [Machine Learning Design Interview: Machine Learning System Design Interviewv](https://www.amazon.com/Machine-Learning-Design-Interview-System-ebook/dp/B09ZKJSKZ1/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=)
4. [medium](https://mlengineer.io/from-google-rejection-to-40-offers-71337a224ebe)


## Blogs which I follow and learn new things
1. [Khuyen Tran's Data Science github](https://github.com/khuyentran1401)
2. [Math data simplified Khuyen Tran](https://mathdatasimplified.com/)
3. [Chip Huyen](https://huyenchip.com/)
4. [Jeff Heaton](https://github.com/jeffheaton)
5. [Tina Huang](https://www.hellotinah.com/)
6. [Ken Jee](https://www.youtube.com/c/KenJee1/about)
7. [Data Professor](https://www.youtube.com/c/DataProfessor/about)
8. [Jacob Amaral](https://www.youtube.com/user/jacobamaral)
9. [Power Analytics](https://analyticshour.io/2021/12/14/182-making-better-decisions-and-being-useful-with-cassie-kozyrkov/?utm_medium=social&utm_source=linkedin)
10. [AI SUMMER](https://theaisummer.com/deep-learning-books-2022/)
11. [Deep VGG16 CNN](https://neurohive.io/en/popular-networks/vgg16/)
12. [Chip Huyen2](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html?utm_content=buffer2111b&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer)
13. [Intro to Proabability for Data Science](https://probability4datascience.com/lecture.html)
14. [Sequantial Decision Analytics](https://castlelab.princeton.edu/sda/)
15. [How Machine Generated Virtual Assistants can 10x Your Productivity in 2022](https://hackernoon.com/how-machine-generated-virtual-assistants-can-10x-your-productivity-in-2022)
16. [The downside of machine learning in health care](https://news.mit.edu/2022/marzyeh-ghassemi-explores-downside-machine-learning-health-care-0201)
17. [CLINICAL EVALUATION OF A MEDICAL DEVICE: CREATING A PROCESS AND ESTABLISHING EQUIVALENCY](https://www.greenlight.guru/blog/clinical-evaluation-process-equivalency)
18. [CT Physics: CT Reconstruction and Helical CT](http://xrayphysics.com/ctsim.html)
19. [AI COMPANIES FOR IMAGES](https://aicentral.acrdsi.org/)
20. [Radiology](https://www.acrdsi.org/Blog/4-Steps-Radiology-Residents)

## Data sources
[Strategy Titan Blog](https://www.strategytitan.com/blog/titanized-real-world-dataset-to-develop-your-analytics-muscle)
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
Short for Numerical Python, is a corner stone of numerical computing in Python.
It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
 * A fast and efficient multidimensional array objects
 * Functions for perfoming element-wise computations with arrays or mathematical operations between arrays
 * Tools for reading and writing array-based dataset to disk
 * Linear algebra operations, Fourier transform and random number generation
 * A mature C API to enable Python extensions and native C or C++ code to access Numpy's data structure and computational facilities 
 ## Advantages of numpy over list
  * Numpy is faster since it occupies small memory compared to built in lists
  * Faster to read less bytes in memory 
# Tensorflow
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

# pandas
derived from panel data
pandas provide high-level data structures and functions designed to make working with structured or tabular data intuitive and flexible. 
 * DataFrame a tabular, column-oriented data structure with both row and column labels
 * Series a one dimensional labelled array object

# matplotlib
is the most popular Python library for producing plots and other two dimensional data visualisations

# SciPy
Is a collection of packages addressing a number of foundational problems in scientific computing.
 * scipy.integrate
 * scipy.linalg
 * scipy.optimize
 
 # scikit-learn
 Scikit-learn is an open source machine learning library that supports supervised and unsupervised learnig.
  * Classification -> Identifying which category an object belongs to
  * Regression -> Predicting a continuous-valued attribute associated with an object
  * Clustering -> Automatic grouping of similar objects into sets
  * Dimensionality reduction -> Reducing the number of random variables to consinder
  * Model selection -> Comparing, validating and choosing parameters and models.
  * Preprocessing -> Feature extraction and normalization
  
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

### Quotes
"Something to do before you get into a big data set, make one of your own!
With a lot of the big data sets, you can produce models. 
But, you don't know what the real model is.
When you make your own data, you can run all the different algorithms you
want and see how well they can find the actual model.
Once you know how well the algorithms work, then you can see how well 
they work on "real" data"

## The infrastructure stack for data science
- Model development
- Feature Engineering
- Model operation
- Versioning
- Job Scheduler
- Compute Resources
- Data warehouse

### The four V's motivation for data science infrastructure
1. Volume  - support large number of data science applications
2. Velocity - easier and quick to prototype and productionize data science applications
3. Validity - the results are supposed to be valid and consistent
4. variety - support many kinds of data science models and applications

### Generalized Infrastructure
#### Benefits
- Allows optimization for volume
- Allows optimization for velocity
- Allows optimization for variety
- Allows optimization for validity

### DAGS
Directed Acyclic Graphs are graphs with no directed cycles.
That consists of vertices (also called nodes) and edges(also called arcs)
with each edge directed from one node to another, such that following those directions will never
form a closed loop
- Introduces common vocabulary -steps and transitions between them which makes it easier to write understand
- Allows to be explicit about the order of operations
- Allows to show the order of operations doesn't matter
#### Schedular
The system that walks through the DAG, sending each step to compute layer
and waiting for their completion before continuing.
##### Types of job schedule
- Static DAG
- Dynamic DAG

**Static branches are suitable for expressing concurrency in code. Dynamic branches
are suitable for expressing concurrency in data**

Job Scheduler is the system that executes a workflow

#### Workflow steps in Metaflow
1. A flow is defined as python class that is derived from the FlowSpec class
2. A step(node or vertices) of the flow is the method of the class
3. Metaflow executes the method bodies as an atomic unit of computation called task
4. The first step(node or vertices) must be called start
5. The edges(arrows) between steps are defined by calling self.next(step_name) on the last line of the method where 
   step_name is the name of the next step to be executed
6. The last step must be called end, since the last step finishes the flow it doesn't need a self.next transition on
   the last line
7. One python file(module) must contain only a single flow. You should
   instantiate the flow class at the bottom of the file inside 
   a 
   ``` 
    if__name__ == '__main__' conditional.
    ```
#### Valid DAG Structure
The step that fans out branches is a split step and the step that fans in branches
is called a join step
* A join step can only join steps that have a common split parent

### Numerical computing loves dynamic branching
The pattern of executing a piece of code for different parts of data in parallel and then collecting the results is 
universal in numerical computing

- Bulk Synchronous Parallel
- Map reduce
- Fork-Join model
- Parallel Map

### Starting new project
1. What is the business problem we are trying to solve?
2. What input data can we use? How and where can we read it?
3. What should be the output data? How and where should we write it?
4. What techniques can we use to produce a better output based on the input

# Learning summary 
1. Set goals and accountability 
2. Break down project into small goals
3. Focus on small goals

## Fine-tuning
The first several layers of filters trained are only going to learn line- and shape-based features because their visual fields are so small. We can reuse or freeze the pre-trained weights of the first few layers and only need to train filter weights to detect higher-order features that are more relevant to your specific use cases. We call this process that only makes adjustment of weights in the last a few layers fine-tuning.

One of the key pieces of fine-tuning is the last layer. We need to adjust the dimension of the last layer to match our specific use cases. We can also add new layers to train from scratch.

This is one of the biggest reasons for ML model failure. Here are 5 top questions we should ask before jumping into model building:

1. Do we have a crystal clear understanding of the business requirements/context?
2.  Do we have enough "quality" data that represent real world cases?
3.  Are we planning to use fancy/complex models only for show-off?
4.  Are we choosing the right metrics for model evaluation?
5.  Are we aware of data drift and model drift that may happen after the model is deployed to production?

What other questions do you ask to avoid model failures?

### Cancer Image Collection for Deep Learning
TCIA is a service which de-identifies and hosts a large archive of medical images of cancer accessible for public download. The data are organized as “collections”; typically patients’ imaging related by a common disease (e.g. lung cancer), image modality or type (MRI, CT, digital histopathology, etc) or research focus. DICOM is the primary file format used by TCIA for radiology imaging. Supporting data related to the images such as patient outcomes, treatment details, genomics and expert analyses are also provided when available.

1. [National Cance Institute](https://www.cancerimagingarchive.net/access-data/)
2. [RED-CNN](https://github.com/SSinyu/RED-CNN)
3. [RED-CNN paper](https://arxiv.org/ftp/arxiv/papers/1702/1702.00288.pdf)

### Medical Imaging Tutorial by DARIEN SCHETTLER 
1. [Multiclass semantic segmentation using DeepLabV3+](https://keras.io/examples/vision/deeplabv3_plus/#building-the-deeplabv3-model)
2. [UWM - GI Tract Image Segmentation - EDA](https://www.kaggle.com/code/dschettler8845/uwm-gi-tract-image-segmentation-eda#create_dataset)
3. [UWMGIT - DeepLabV3+ - End-to-End Pipeline [TF]](https://www.kaggle.com/code/dschettler8845/uwmgit-deeplabv3-end-to-end-pipeline-tf)
