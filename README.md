# Reddit Mood

![Reddit Mood](https://img.shields.io/badge/Reddit--Mood-v1.0-blue)

**Reddit Mood** is a Python application designed to scrape comments from the Reddit's Tech subreddits, analyze their sentiment, and classify them into various emotional categories. The project uses `praw` for Reddit API interactions and Hugging Face's `transformers` library for emotion detection.

## Installation

To set up and run the project locally, follow these instructions:

### 1. Clone the Repository

```bash
git clone https://github.com/FadlGh/Reddit-Mood.git
cd Reddit-Mood
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate # On Mac use: source venv/bin/activate
```
### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
   
Create a .env file in the root directory and add your Reddit API credentials:

```plaintext
CLIENT_ID=your_client_id
CLIENT_KEY=your_client_key
PASSWORD=your_password
```

## Usage
### Running the Scraper
To scrape comments from the technews subreddit and save them to data/comments.csv, run:

```bash
python src/data_scraper.py
```

To classify the emotions of the comments in data/comments.csv, run:

```bash
python src/emotion_detector.py
```

To train own model, run:

```bash
python src/model.py
```

To graph the data, run:

```bash
python src/graph.py
```
