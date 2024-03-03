# Inference Demo

This is a simple example of how to use FastAPI to serve a model for inference. The model is a simple linear regression model trained on the `iris` dataset. The model is trained using `scikit-learn` and is saved to disk using `joblib`. The model is then loaded into memory when the FastAPI app starts and is used to make predictions on new data.

## Running the app

To run the app, you can use the following command:

```bash 
MODEL_VERSION=0.0.1 uvicorn src.main:app --reload
```

or using docker-compose:
```bash
docker-compose up
```

For convenience, we are using uvicorn in `docker-compose`, while in the real-world Dockerfile we would use `gunicorn` to run the app.


This will start the FastAPI app and you can access the app at `http://localhost:8000`. 
You can open http://localhost:8000/docs to see the API documentation generated in Swagger UI.
And also you can make a request to the API using Swagger UI.

## Other files in the project

- `Dockerfile`: This is the Dockerfile used to build the Docker image for the app.
- `docker-compose.yml`: This is the docker-compose file used to run the app using `docker-compose`.
- `requirements.txt`: This file contains the Python packages required to run the app.
- `requirements_dev.txt`: This file contains the Python packages required to run the app in development mode. Eg: testing, linting, etc.
- `training-pipeline`: In this folder are the files mentioned in the Document provided separately about the architecture of Argo Workflows pipeline.
- `model/train_model.py`: It is a very simple model training script which will generate the .pkl file used as model. 
  - This model should be uploaded to S3, and the path should be provided in the `src/main.py` file. For convenience, I used a public link for the model. 
  - In the real world, the model can be downloaded from the private S3 bucket using boto3 library.
