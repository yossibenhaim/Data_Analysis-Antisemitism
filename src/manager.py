from reading_saving_files import ReadAndSaveFile
from data_analyzer import DataAnalyzer
from report_builder import ReportBuilder
from data_cleaning import DataCleaning

class Manager:

    def __init__(self):
        self.data = None
        self.analyzer = None
        self.report = ReportBuilder()
        self.connecting_files = ReadAndSaveFile()

    def load_data_csv(self):
        connecting_files = ReadAndSaveFile()
        self.data = connecting_files.load_data_csv()

    def software_flow(self):
        if self.data is None:
            self.load_data_csv()
        if self.analyzer is None:
            self.analyzer = DataAnalyzer(self.data)
        self.send_total_tweets()
        self.send_average_length()
        self.send_common_words()
        self.send_longest_3_tweets()
        self.send_uppercase_words()
        self.save_result()
        self.save_data_cleaning(self.create_cleaning_data())

    def send_total_tweets(self):
        self.report.create_total_tweets(self.create_total_tweets_antisemitic(),
                                   self.create_total_tweets_non_antisemitic(),
                                   self.create_total_tweets(),
                                   self.create_total_tweets_unspecified())
    def send_average_length(self):
        self.report.create_average_length(self.create_average_length_antisemitic(),
                                     self.create_average_length_non_antisemitic(),
                                     self.create_average_length_total())
    def send_common_words(self):
        self.report.create_common_words(self.create_common_words_total())

    def send_longest_3_tweets(self):
        self.report.create_longest_3_tweets(self.create_longest_3_tweets_antisemitic(),
                                       self.create_longest_3_tweets_non_antisemitic())
    def send_uppercase_words(self):
        self.report.create_uppercase_words(self.create_uppercase_words_antisemitic(),
                                      self.create_uppercase_words_non_antisemitic(),
                                      self.create_uppercase_words_total())
    def save_result(self):
        self.connecting_files.save_results_json(self.report.return_report())

    def create_cleaning_data(self):
        cleaning_data = DataCleaning(self.data)
        cleaning_data.remove_columns()
        cleaning_data.deleting_punctuation_marks()
        cleaning_data.replace_word_to_lower_case()
        cleaning_data.remove_row()
        return cleaning_data.return_data_cleaning()

    def save_data_cleaning(self, data_cleaning):
        self.connecting_files.save_tweets_dataset_cleaned(data_cleaning)

    def create_total_tweets(self):
        return self.analyzer.shape()[0]

    def create_total_tweets_antisemitic(self):
        return int(self.analyzer.total_tweets()[1])

    def create_total_tweets_non_antisemitic(self):
        return int(self.analyzer.total_tweets()[0])

    def create_total_tweets_unspecified(self):
        return int(self.analyzer.shape()[0]-(self.analyzer.total_tweets()[0]+self.analyzer.total_tweets()[1]))

    def create_average_length_antisemitic(self):
        return float(self.analyzer.average_length()[1].sum()/(self.analyzer.total_tweets()[1]))

    def create_average_length_non_antisemitic(self):
        return float(self.analyzer.average_length()[0].sum()/(self.analyzer.total_tweets()[0]))

    def create_average_length_total(self):
        return float(self.analyzer.average_length().sum()/(self.analyzer.total_tweets()[0] + self.analyzer.total_tweets()[1]))

    def create_common_words_total(self):
        return self.analyzer.common_words()

    def create_longest_3_tweets_antisemitic(self):
        return list(self.analyzer.longest_3_tweets().tail(3))

    def create_longest_3_tweets_non_antisemitic(self):
        return list(self.analyzer.longest_3_tweets()[[0]].tail(3))

    def create_uppercase_words_antisemitic(self):
        return self.analyzer.uppercase_words_antisemitic()

    def create_uppercase_words_non_antisemitic(self):
        return self.analyzer.uppercase_words_non_antisemitic()

    def create_uppercase_words_total(self):
        return self.analyzer.uppercase_words_total()