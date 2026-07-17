import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"
SCALER_PATH = "models/scaler.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def predict_invoice_flag(input_data):

    model = load_model()
    scaler = load_scaler()

    input_df = pd.DataFrame(input_data)

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    input_df["Predicted_Flag"] = prediction

    input_df["Status"] = input_df["Predicted_Flag"].map({
        0: "Auto Approve",
        1: "Manual Review"
    })

    return input_df


if __name__ == "__main__":

    sample_data = {
        "invoice_quantity": [120],
        "invoice_dollars": [18500],
        "Freight": [450],
        "total_item_quantity": [120],
        "total_item_dollars": [18500]
    }

    print(predict_invoice_flag(sample_data))