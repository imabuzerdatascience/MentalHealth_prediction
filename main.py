import joblib 

model = joblib.load('Mental_health_model.pkl') 
from pydantic import BaseModel ,Field
from fastapi import FastAPI 
from typing import Literal
import pandas as pd 

app = FastAPI()

top_countries = ['Other','India','USA','Canada','Australia','UK','Germany','Mexico','Turkey','France']


# first pydantic model 
class StudentData(BaseModel):
    Age: int = Field(... , gt=10 , le=50)
    Gender: Literal['Male' , 'Female' ,'Custom']
    Country: str
    Academic_Level: Literal['Undergraduate', 'Graduate', 'High School']
    Most_Used_Platform: Literal['Facebook', 'LinkedIn', 'Instagram', 'Snapchat', 'Twitter',
       'YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp',
       'WeChat']
    Purpose_Of_Use: Literal['Networking', 'Education', 'Entertainment', 'News'] 
    Avg_Daily_Usage_Hours: float = Field(..., ge=2 , le=20)
    Daily_Unlocks: int = Field(..., ge=0 , le=200 )
    Study_Hours: float = Field(..., ge=0 , le=18)
    Physical_Activity_Hours: float = Field(..., ge=0 , le=8)
    Sleep_Hours_Per_Night: float = Field(..., ge=3 , le=18)
    Stress_Level: Literal['Low', 'Medium', 'High', 'Very High']


# Describe what we send back
class PredictionsResponse(BaseModel) :
    predict_mental_health_score :float

@app.post('/predict' , response_model=PredictionsResponse) 
def get_predict(data : StudentData):
    country_grouped = data.Country if data.Country in top_countries else "Other"
    input_row = pd.DataFrame([{
        "Age": data.Age ,
        "Gender": data.Gender,
        "Country": data.Country,
        "Academic_Level": data.Academic_Level,
        "Most_Used_Platform": data.Most_Used_Platform,
        "Purpose_Of_Use": data.Purpose_Of_Use,
        "Avg_Daily_Usage_Hours": data.Avg_Daily_Usage_Hours,
        "Daily_Unlocks": data.Daily_Unlocks,
        "Study_Hours": data.Study_Hours,
        "Physical_Activity_Hours": data.Physical_Activity_Hours,
        "Sleep_Hours_Per_Night": data.Sleep_Hours_Per_Night,
        "Stress_Level": data.Stress_Level,
        "Grouped_countries": country_grouped ,
    }])

    predictions = model.predict(input_row)[0]
    return PredictionsResponse(predict_mental_health_score = round(float(predictions) , 2))