
class DataAnalyzer:

    def __init__(self, data):
        self.data = data

    def total_tweets(self):
        return self.data.value_counts(["Biased"])

    def shape(self):
        return self.data.shape

    def average_length(self):
        self.data["count_word"]  = self.data[["Text"]].apply(lambda x : x.str.split().str.len())
        return self.data.groupby(["Biased"])["count_word"].apply(lambda x : x)

    def common_words(self):
        my_dict = {}
        my_list = [self.data[["Text"]].values[i][0] for i in range(len(self.data[["Text"]].values))]
        for x in my_list:
            for i in x.strip(".,'!?#").lower().split():
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1

        data_dict = dict(sorted(my_dict.items(), key= lambda item : item[1], reverse=True)[0:10])
        return data_dict

    def longest_3_tweets(self):
        self.data["len"] = self.data[["Text"]].apply(lambda x : x.str.len())
        data = self.data.groupby(["Biased", "len"])["Text"].apply(lambda x :x)
        return data

    def uppercase_words(self):
        my_dict = {}
        my_list = [self.data[["Text"]].values[i][0] for i in range(len(self.data[["Text"]].values))]
        for x in my_list:
            for i in x.strip(".,'!?#").split():
                if i.isupper():
                    if i in my_dict:
                        my_dict[i] += 1
                    else:
                        my_dict[i] = 1
        return sum(my_dict.values())

    def uppercase_words_antisemitic(self):
        my_dict = {}
        my_list = [self.data[["Text"]][self.data["Biased"]==0].values[i][0] for i in range(len(self.data[["Text"]].values[self.data[["Biased"]]==0]))]
        for x in my_list:
            for i in x.split():
                if i.isupper():
                    if i in my_dict:
                        my_dict[i] += 1
                    else:
                        my_dict[i] = 1
        return sum(my_dict.values())

    def uppercase_words_non_antisemitic(self):
        my_dict = {}
        my_list = [self.data[["Text"]][self.data["Biased"]==1].values[i][0] for i in range(len(self.data[["Text"]].values[self.data[["Biased"]]==1]))]
        for x in my_list:
            for i in x.split():
                if i.isupper():
                    if i in my_dict:
                        my_dict[i] += 1
                    else:
                        my_dict[i] = 1
        return sum(my_dict.values())