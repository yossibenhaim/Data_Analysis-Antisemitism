from reading_saving_files import ReadAndSaveFile
from data_analyzer import DataAnalyzer

class Manager:

    def __init__(self):
        self.data = None

    def load_data_csv(self):
        connecting_files = ReadAndSaveFile()
        self.data = connecting_files.load_data_csv()

    def check(self):
        if self.data is None:
            self.load_data_csv()
        analyzer = DataAnalyzer(self.data)
        # print(analyzer.total_tweets())
        print("total_tweets", analyzer.shape()[0])
        print("antisemitic", analyzer.total_tweets()[0])
        print("non antisemitic", analyzer.total_tweets()[1])
        print("unspecific", analyzer.shape()[0]-(analyzer.total_tweets()[0]+analyzer.total_tweets()[1]))
        print()
        print("tutel average = ",analyzer.average_length().sum()/(analyzer.total_tweets()[0] + analyzer.total_tweets()[1]))
        print("average 0 = ", analyzer.average_length()[0].sum()/(analyzer.total_tweets()[0]))
        print("average 1 = ",analyzer.average_length()[1].sum()/(analyzer.total_tweets()[1]))
        print()
        print("total", analyzer.common_words())
        print()
        print("longest_3_tweets")
        print("antisemitic", analyzer.longest_3_tweets()[[0]].tail(3))
        print("non antisemitic", analyzer.longest_3_tweets().tail(3))
        print()
        print("uppercase_words")
        print("antisemitic", analyzer.uppercase_words_antisemitic())
        print("non_antisemitic", analyzer.uppercase_words_non_antisemitic())
        print("count all upper", analyzer.uppercase_words())

