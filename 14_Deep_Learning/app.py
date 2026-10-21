import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app_full = FastAPI(title="Multi-Modal Climate Inference API")

def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# Load ALL models via the lightweight TFLite runtime
mlp_interpreter = load_tflite_model('models/mlp_carbon_flux_quantized.tflite')
cnn_interpreter = load_tflite_model('models/cnn_spatial_quantized.tflite')
lstm_interpreter = load_tflite_model('models/lstm_temporal_quantized.tflite')

# Schemas
class TabularInput(BaseModel):
    features: list[float]

class SpatialInput(BaseModel):
    image_matrix: list[list[list[float]]]

class TemporalInput(BaseModel):
    time_series: list[list[float]]

# Endpoints
@app_full.post("/predict/tabular")
def predict_tabular(data: TabularInput):
    if len(data.features) != 8:
        raise HTTPException(status_code=400, detail="Must provide exactly 8 features.")
    input_data = np.array([data.features], dtype=np.float32)
    mlp_interpreter.set_tensor(mlp_interpreter.get_input_details()[0]['index'], input_data)
    mlp_interpreter.invoke()
    prediction = mlp_interpreter.get_tensor(mlp_interpreter.get_output_details()[0]['index'])[0][0]
    return {"anomaly_probability": float(prediction)}

@app_full.post("/predict/spatial")
def predict_spatial(data: SpatialInput):
    input_data = np.array([data.image_matrix], dtype=np.float32)
    cnn_interpreter.set_tensor(cnn_interpreter.get_input_details()[0]['index'], input_data)
    cnn_interpreter.invoke()
    prediction = cnn_interpreter.get_tensor(cnn_interpreter.get_output_details()[0]['index'])[0][0]
    return {"deforestation_detected": bool(prediction > 0.5), "confidence": float(prediction)}

@app_full.post("/predict/temporal")
def predict_temporal(data: TemporalInput):
    input_data = np.array([data.time_series], dtype=np.float32)
    lstm_interpreter.set_tensor(lstm_interpreter.get_input_details()[0]['index'], input_data)
    lstm_interpreter.invoke()
    prediction = lstm_interpreter.get_tensor(lstm_interpreter.get_output_details()[0]['index'])[0][0]
    return {"forecasted_stress_index": float(prediction)}

@app_full.get("/")
def health_check():
    return {"status": "Hybrid API Online"}
