from pydantic import BaseModel, Field


# ----------------------------------------------------
# Existing Freight Prediction
# ----------------------------------------------------

class FreightPredictionRequest(BaseModel):
    Dollars: float = Field(..., gt=0)


class FreightPredictionResponse(BaseModel):
    predicted_freight: float


# ----------------------------------------------------
# Invoice Analysis Request
# ----------------------------------------------------

class AnalyzeRequest(BaseModel):
    invoice_quantity: float = Field(..., gt=0)

    invoice_dollars: float = Field(..., gt=0)

    total_item_quantity: float = Field(..., gt=0)

    total_item_dollars: float = Field(..., gt=0)


# ----------------------------------------------------
# Invoice Analysis Response
# ----------------------------------------------------

class AnalyzeResponse(BaseModel):

    predicted_freight: float

    freight_ratio: float

    invoice_flag: int

    risk_status: str