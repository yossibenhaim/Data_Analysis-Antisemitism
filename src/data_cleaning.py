
class DataCleaning:

    def __init__(self, data_csv):
        self.data = data_csv

    def remove_columns(self):
        self.data = self.data[["Text","Biased"]]

    def deleting_punctuation_marks(self):
        self.data["Text"] = self.data["Text"].str.strip(".,'!?#")

    def replace_word_to_lower_case(self):
        self.data["Text"] = self.data["Text"].str.lower()

    def remove_row(self):
        self.data = self.data.dropna(subset=["Biased"])

    def return_data_cleaning(self):
        return self.data
