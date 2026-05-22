from sklearn.metrics import accuracy_score
'''
prende in input lista di coppie y reale e y predetta
mostra l'accuratezza
'''
def show_accuracy_metric(model_name:str ='',train=None,test=None):
    train_acc, test_acc= None, None
    if train != None :
        train_acc = accuracy_score(y_true=train[:][0],y_pred=train[:][0])
        print(f" train --- {model_name} : accuracy {train_acc}")
        
    if test != None :
        test_acc = accuracy_score(y_true=test[:][0],y_pred=test[:][0])
        print(f" test --- {model_name} : accuracy {test_acc}")


    


    