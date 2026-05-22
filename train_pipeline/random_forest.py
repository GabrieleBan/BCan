
from sklearn.ensemble import RandomForestClassifier

def train(x_train,y_train):
    tree_cls = RandomForestClassifier(n_estimators=10, max_depth=5)
    tree_cls =  tree_cls.fit(X=x_train,y=y_train)

    return tree_cls, tree_cls.predict(X=x_train)


