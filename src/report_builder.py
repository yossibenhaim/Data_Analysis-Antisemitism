class ReportBuilder:

    def __init__(self):
        self.report = {}

    def create_total_tweets(self, antisemitic, non_antisemitic, total, unspecified):
        self.report["total_tweets"] = \
            {"antisemitic" : antisemitic,
            "non_antisemitic" : non_antisemitic,
            "total": total,
            "unspecified": unspecified}

    def create_average_length(self,  antisemitic, non_antisemitic, total):
        self.report["average_length"] = \
            {"antisemitic" : antisemitic,
            "non_antisemitic" : non_antisemitic,
            "total": total}

    def create_common_words(self, total):
        self.report["common_words"] = \
            {"total": total}

    def create_longest_3_tweets(self, antisemitic, non_antisemitic):
        self.report["longest_3_tweets"] = \
            {"antisemitic" : antisemitic,
            "non_antisemitic" : non_antisemitic}

    def create_uppercase_words(self, antisemitic, non_antisemitic, total):
        self.report["uppercase_words"] = \
            {"antisemitic" : antisemitic,
            "non_antisemitic" : non_antisemitic,
            "total": total}

    def return_report(self):
        return self.report