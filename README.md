# Vector-Space-Retrieval-Model
This is the implementation of a Vector Space model using TF-IDF representation for an information retrieval system.

## Required packages
python==3.7

regex==2021.11.10
requests==2.26.0
requests-file==1.5.1
nltk==3.6.5
numpy==1.19.5
beautifulsoup4==4.10.0
certifi==2020.6.20

Please also run the following block to install nltk stopwords list:
```
import nltk
nltk.download('stopwords')
```

## Crawling data
In this repository, you can find a toy sample with rudimentary text files to play with for simplicity sake. 
Beside that, you can also run ```crawl_data.py``` to crawl the content from the websites (the links can be changed manually according to your preference) for making our corpus.

## Retrieving search results

Run the script ```vector_space_model.py``` to train the vector space model


#### List of implementations
- Remove stopwords, punctuations
- Lowercase
- Build a dictionary of words by tokenization
- TF-IDF calculation
- Comparing the query and the corpus by using dot product as the similarity measure

#### List of Arguments accepted
```--k``` Top k retrieval results (Default = 1) <br>
```--data_path``` Path to data folder (Default = "./news_data") <br>
```--query``` Input query for searching <br>

Sample run
```python vector_space_model.py --k 5 --query "wonderful plants"```
