# Structure for the cli app
"""
options for the cli :
1. --file : to_input file (.csv, .xls, .xlsx) only.
2. --operation : 
    1. analyze : give summary about the file with all the rows and column counts,
                mean, median, mode of each column and overall data.
    2. analyzewithgraph : performs the analysis(like the above operation), and outputs
                            the result in a visual graph.
"""
# import pandas


class DataAnalyzerCli:
    def __init__(self, *csv_file, excel_file):
        self.csv_files = csv_file
        self.excel_files = excel_file

    def csv_analyzer(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
