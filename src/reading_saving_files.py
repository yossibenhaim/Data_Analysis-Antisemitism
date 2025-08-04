import pandas as pd
import json

class ReadAndSaveFile:

    def __init__(self):

        self.dataset_tweets = "../data/tweets_dataset.csv"
        self.tweets_dataset_cleaned = "../results/tweets_dataset_cleaned.csv"
        self.results = "../results/results.json"

    def load_data_csv(self):
        data_csv = pd.read_csv(self.dataset_tweets)
        return data_csv

    def save_tweets_dataset_cleaned(self, tweets_dataset_cleaned):
        tweets_dataset_cleaned.to_csv(self.tweets_dataset_cleaned)

    def save_results_json(self, results_json):
        with open(self.results, "w") as f:
            json.dump(results_json, f)