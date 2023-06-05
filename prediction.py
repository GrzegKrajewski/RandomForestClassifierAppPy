def make_pred(X,model):
    answer=model.predict(X)
    chance=model.predict_proba(X)

    return answer, chance