# AG-News-Classification (Text Classification)

## Introduction:
* The objective of this task is to build a text classification model using the state-of-art method to classify a dataset of text into one of multiple categories.  
* AG News dataset which consists of news articles labelled as [1-World, 2-Sports, 3-Business, 4-Sci/Tech].
* Each class contains 30,000 training samples and 1,900 testing samples.
* Dataset Link - https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset
* I have used three different models for text classification: 1. N-grams, 2. LSTM, 3. BERT
  
## Data Pre-processing:
I have performed the following pre-processing steps on the dataset:

* Merged the "Title" and "Description" columns into a single column named "Text."
* Converted all text to lowercase.
* Eliminated all punctuation, numbers, and special characters.
* Excluded all stop words using the NLTK library, specifically in the context of n-grams.
* Tokenized the text using the tokenizer provided by the pre-trained model.
  
### Note - 1:
* Please be aware that the size of the BERT model associated with this project exceeds the 25MB limit imposed by GitHub for individual files. If needed i will upload the models on my google drive
* Before running the code, please follow the instructions below to ensure all necessary dependencies or packages are installed. Please note that you may need to restart the Jupyter Notebook kernel after downloading the dependencies.
   #### !pip install transformers nltk datasets numpy seaborn pandas scikit-learn matplotlib
   #### !pip install torch
   #### !pip install accelerate>=0.20.1
   #### !pip install mlxtend
   #### !pip install tensorflow

## Note - 2:
To run the FastAPI implementation of the LSTM model API stored in the "main.py" file within the "LSTM" folder, follow these steps:
# 1. Install FastAPI:
   !pip install fastapi
# 2. Install Uvicorn with standard dependencies:
   !pip install "uvicorn[standard]" or !pip install uvicorn[standard]
# 3. Run the "main.py" file using Uvicorn:
   uvicorn main:app --reload

