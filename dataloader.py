from sklearn.datasets import load_breast_cancer


def get_data():
    dataset= load_breast_cancer()
    return dataset.data,dataset.target