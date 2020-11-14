**# Text_Analytic - Lifecycle**

Objective: Sentiment Analysis of Twitter data : SGGE2020

1)	Data scrapping 
        
2)	Annotate the data          
* [ ] Vader
* [ ] Textblob


3)	EDA

* [ ]  Visualization - word cloud  
 
4)	Model building 

* Supervised  

* [ ]  ML FE:(tfidf , countVect)

* [ ]  DL (BERT, LSTM, RNN, etc ) 


* Non-supervised <br>
    

* [ ]   LDA Topic modelling

5) Conclusion - Insights Discovery

How to run
1) Clone the git project & follow the same folder structure
cd text_analytic/
test-project/</br>
├── data     
├── code      
├── README.md  
├── requirements.txt   </br> 

2) Install dependency file list </br>
pip install -r requirements.txt </br>

3) Install the General-purpose pretrained models </br>
!python3 -m spacy download en_core_web_sm 
