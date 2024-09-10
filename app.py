from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

# Define the path to your CSV file
CSV_FILE_PATH = 'health_data_continuous_sleep_all.csv'

@app.get("/get-csv-data/")
async def get_csv_data():
    if not os.path.exists(CSV_FILE_PATH):
        raise HTTPException(status_code=404, detail="CSV file not found.")
    
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(CSV_FILE_PATH)
        
        # Convert the DataFrame to JSON
        data = df.to_dict(orient='records')
        
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Home endpoint for testing
@app.get("/")
def read_root():
    return {"Hello": "World"}

# starting code
# uvicorn app:app --reload