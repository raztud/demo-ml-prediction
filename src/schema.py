from typing import Literal
from pydantic import BaseModel


class PingResponse(BaseModel):
    status: Literal['ok'] = 'ok'


class PredictionResponse(BaseModel):
    value: float


class FeaturesData(BaseModel):
    feature: float


class FeedbackData(BaseModel):
    value: float
    label: int
    model_version: str
