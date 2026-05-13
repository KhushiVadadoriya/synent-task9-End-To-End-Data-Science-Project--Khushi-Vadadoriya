import os
import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
	directory = os.path.dirname(file_path)
	if directory:
		os.makedirs(directory, exist_ok=True)

	with open(file_path, "wb") as file_obj:
		pickle.dump(obj, file_obj)


def load_object(file_path):
	with open(file_path, "rb") as file_obj:
		return pickle.load(file_obj)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
	model_report = {}
	for model_name, model in models.items():
		model_params = param.get(model_name, {})
		if model_params:
			grid_search = GridSearchCV(model, model_params, cv=3, scoring="r2", n_jobs=-1)
			grid_search.fit(X_train, y_train)
			best_model = grid_search.best_estimator_
			models[model_name] = best_model
		else:
			model.fit(X_train, y_train)
			best_model = model
			models[model_name] = best_model

		predictions = best_model.predict(X_test)
		model_report[model_name] = r2_score(y_test, predictions)

	return model_report
