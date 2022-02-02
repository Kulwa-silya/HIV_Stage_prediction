from joblib import load

def inference(a, b, c,	d,	e,	f,	g,	h,	i,	j,	k,	l,	m,	n):
    model_inf = load('model/model.joblib')
    return model_inf.predict([[a, b, c,	d,	e,	f,	g,	h,	i,	j,	k,	l,	m,	n]])

# 60.0,3.0,	408.0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	1