import logging
import os
import httpx
from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI, Request

from src.schema import PingResponse, PredictionResponse, FeaturesData, FeedbackData

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_model():
    version = os.environ.get("MODEL_VERSION", "")

    model_path = f"{os.getcwd()}/model/model-{version}.pkl"
    if not os.path.isfile(model_path):
        logger.info("Download model...")
        # the base URL should come from a config file
        url = f"https://s3.eu-central-1.amazonaws.com/dropbox.razvantudorica.net/model-{version}.pkl"
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            with open(model_path, "wb") as f:
                f.write(response.content)

    logger.info(f"Loading model {model_path}...")
    return joblib.load(model_path)


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    fastapi_app.model = load_model()
    yield


app = FastAPI(
    title="Demo Service",
    lifespan=lifespan,
)


@app.get("/ping")
async def health() -> PingResponse:
    return PingResponse()


@app.post("/predict")
async def predict(
        request: Request,
        data: FeaturesData
) -> PredictionResponse:
    model = request.app.model
    input_feature = [[data.feature]]
    prediction = model.predict(input_feature).tolist()[0]

    return PredictionResponse(value=prediction)


async def feedback(
    request: Request,
    data: FeedbackData,
) -> None:
    # save to database the feedback data
    # based on this data, we could retrain the model
    pass
