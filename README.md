# Sentiment Analysis with AWS Glue, PySpark, and S3

This project implements an end-to-end sentiment analysis pipeline using **AWS Glue**, **PySpark**, and **S3**. The pipeline collects data from Twitter using the Twitter API, preprocesses the data, performs sentiment analysis, and stores the results in an **S3 bucket** for further analysis.

## 🛠️ Tech Stack

- **AWS Glue**: For ETL (Extract, Transform, Load) processes using PySpark.
- **PySpark**: Distributed data processing for transformations.
- **Amazon S3**: For storage of raw and processed data.
- **Twitter API**: To collect tweet data.
- **TextBlob**: For sentiment analysis of tweet text.
- **Boto3**: AWS SDK for Python to interact with AWS services like S3 and Glue.
- **AWS Wrangler**: A utility for reading from and writing to S3 using Pandas and Glue.
- **Pandas**: Data manipulation library for preprocessing data.
- **Python 3.x**: Programming language for writing the scripts.
  
## 🚀 Project Overview

This project consists of several modules that perform different tasks:
1. **Data Collection**: Collects tweets from Twitter API using specified keywords.
2. **Preprocessing**: Cleans the collected tweet data, including removing URLs, mentions, and special characters.
3. **Sentiment Analysis**: Analyzes the sentiment of the cleaned tweets using **TextBlob**.
4. **ETL with AWS Glue**: Transforms the data using **AWS Glue** PySpark transformations and loads it back into **S3**.

## 🚀 Setup Instructions

1. Clone the Repository
    Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis-twitter.git
    cd sentiment-analysis-twitter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your **Twitter API keys** in `src/config.py`.

## 🚀 Running the Pipeline
  
  Run the Python scripts:
    - **Collect Twitter Data**:
      ```bash
      python src/collect_data.py
      ```
    - **Preprocess Data**:
      ```bash
      python src/preprocess.py
      ```
    - **Perform Sentiment Analysis**:
      ```bash
      python src/analyze_sentiment.py
      ```
    - **Transform Data with AWS Glue**:
      ```bash
      python src/glue_transform.py
      ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.