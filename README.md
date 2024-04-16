# NLP-Powered-YouTube-Analytics

This project aims to make it easier to evaluate YouTube videos by using advanced NLP techniques. The system will give short summaries of videos and their comments, automatically analyze sentiments and emotions, and identify key themes. This helps users make well-informed decisions about the quality and relevance of the video content.

## Project Requirements

```
pip install -r requirements.txt
```

You need to start the NLTK Downloader and download all the data you need.
Open a Python console and do the following:

```
>>> import nltk
>>> nltk.download()
showing info http://nltk.github.com/nltk_data/
```

Install spaCy **en_core_web_sm** model

```bash
python -m spacy download en_core_web_sm
```
## Run the Project

Start the Flask based server
```bash
python server.py
```

Start the Reactjs Server
```bash
cd frontend
npm i
npm start
```


## Dataset

[Link](https://docs.google.com/spreadsheets/d/19Ovg-9q9wAAQVc9SHOT6oYHjEuG4deT_lI7yojaJajQ/edit?usp=sharing)
