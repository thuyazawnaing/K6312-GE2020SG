**Tweets Analysis on Singapore General Election 2020**

Objective: Sentiment Analysis & Topic Modelling

**I. Data scrapping**: Scrap twitter's data using Selenium & Beautiful soup

**II. Data cleaning**: Data cleaning and consolidation

**III. Data annotation**

    *  TextBlob
    *  VaderSentiment
    *  GroundTruth: Both analyzers are used to derive the ground-truth
    
**IV)	Exploratory Data Analysis**

**V)  Topic modeling**  

> Unsupervised Learning 

1. Latent Dirichlet allocation 
2. Singular Value Decomposition + Kmean clustering


**VI)  Model building**

> Supervised Learning 

    1.  MachineLearning (Two-level approach on multi-class classification problem)
            
        Firstly build all the base classifiers.
            * Logistic Regression 
            * Support Vector Machine
            * Decision Tree
            * Naive Bayes
            * Ensemble Learning
                Random Forest
                XGBoost
        Secondly, use all the base classifiers as input to train the Ensemble model 
            *  Ensemble Voting Classifier

    2.  DeepLearning: Keras 
        
        Model Train from scratch
            * Embedding layer
            * Embedding layer + Convolutional Neural Network
            * Embedding layer + Long short-term memory
        Pre-trained Model (https://nlp.stanford.edu/projects/glove/)
        



**How to Run**

1) Clone the git project & follow the same folder structure
```
cd K6312-GE2020SG/
K6312-GE2020SG/

├── data     
├── code      
├── README.md  
├── requirements.txt   </br> 
```

2) Install dependency file list </br>
pip install -r requirements.txt </br>

3) Install the General-purpose pretrained models </br>
!python3 -m spacy download en_core_web_sm 
4) Download the pretrained weights "glove.twitter.27B.100d.txt" from (https://nlp.stanford.edu/projects/glove/) </br>


```
Place the downloaded file in the 
code
└───utli
│   │   glove.twitter.27B.100d.txt
```



**Folder and Files descriptions**

```
data
└───raw_data    : Scrapped data 
│   │   ...
└───clean_data  : Preprocessed data
│   │   ...
code
│   1.data_scrapping.py 
|   2. combine_data.ipynb
|   3. Text_Annotation.ipynb
|   4. Data_Visualization.ipynb
|   5. TopicModelling_EDA.ipynb
|   6. Sentiment_Analysis - Text Classifier.ipynb   
│   │ 
└───util
│   │   custom_stopwords.txt    : use for Topic Modelling
│   │   custom_stopwords1.txt   : use for Text Classification
|   |   glove.twitter.27B.100d.txt: Downloaded weight
└───└───
README.md
requirements.txt
```


