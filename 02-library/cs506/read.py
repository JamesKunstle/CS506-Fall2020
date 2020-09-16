def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    import csv
    from typing import List 

    matrix: List = []    

    with open(csv_file_path, "rt") as csvfile:

        csv_reader = csv.reader(csvfile) #create a csv_reader object

        for line in csv_reader:
            matrix += [line]
    
    [print(i) for i in matrix]
    return matrix

if __name__ == "__main__":
    read_csv("/Users/jameskunstle/Documents/student/CS506/class_git/CS506-Fall2020/02-library/tests/test_files/dataset_1.csv")