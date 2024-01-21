# AG-News-Classification

## Introduction:
* The objective of this task is to build a text classification model using the state-of-art method to classify a dataset of text into one of multiple categories.  
* AG News dataset which consists of news articles labelled as [1-World, 2-Sports, 3-Business, 4-Sci/Tech].
* Each class contains 30,000 training samples and 1,900 testing samples.
* Dataset Link - https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset

### Note:
* Please be aware that the size of the BERT model associated with this project exceeds the 25MB limit imposed by GitHub for individual files.
* Before running the code, please follow the instructions below to ensure all necessary dependencies or packages are installed. Please note that you may need to restart the Jupyter Notebook kernel after downloading the dependencies.
   #### !pip install transformers nltk datasets numpy seaborn pandas scikit-learn matplotlib
   #### !pip install torch
   #### !pip install accelerate>=0.20.1
   #### !pip install mlxtend
   #### !pip install tensorflow
