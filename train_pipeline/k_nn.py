
from sklearn.neighbors import KNeighborsClassifier

def train(X_scalar, y_scalar, count=None):
    lista_y_pred =  []
    
    # definisco il numero di "vicini" (n_neighbors) da considerare 
    if count == None:
        vicini = 10
    else:
        vicini = count

    for x in range(0,vicini):
        knn = KNeighborsClassifier(n_neighbors = x)# definisco il modello
        knn.fit(X_scalar, y_scalar) # faccio l'addestramento
        y_pred = knn.predict(X_scalar) # eseguo la predizione
        lista_y_pred.append(y_pred)

    # model , y_pred =random_forest.train(X_train,y_train)

    return (knn, lista_y_pred)