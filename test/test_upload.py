import pytest
from fastapi.testclient import TestClient
from io import BytesIO
import pandas as pd
from app import fastapi_app
from src.models.question import Question

client = TestClient(fastapi_app)


def create_test_excel_file(data : dict):
    df = pd.DataFrame(data)
    output = BytesIO()
    df.to_excel(output , index=False , engine="openpyxl")
    output.seek(0)
    return output

def test_upload_excel_success(db):
    data = {
        "Question": ["What is 2+2?" , "What is the capital of France?"],
        "A": ["3" , "Berlin"],
        "B": ["4" , "Madrid"],
        "C": ["5" , "Paris"],
        "D": ["6" , "Rome"],
    }
    excel_file = create_test_excel_file(data)
    
    response = client.post(
        "/upload",
        files={"file": ("test.xlsx" , excel_file , "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
    )
    
    assert response.status_code == 200
    
    uploaded_questions = response.json()
    assert len(uploaded_questions) == 2
    assert uploaded_questions[0]["question_text"] == "What is 2+2?"
    assert uploaded_questions[1]["question_text"] == "What is the capital of France?"
    
    questions = db.query(Question).all()
    assert len(questions) == 2
    assert questions[0].text == "What is 2+2?"
    assert questions[1].text == "What is the capital of France?"
    
def test_upload_excel_missing_column(db):
    data = {
        "Question": ["What is 2+2?"],
        "A": ["3"],
        "B": ["4"]
        
    }
    
    excel_file = create_test_excel_file(data)
    
    response = client.post(
                "/upload",
        files={"file": ("test.xlsx", excel_file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        )
    
    assert response.status_code == 400
    assert "Missing required columns" in response.json()["detail"]
    
def test_upload_excel_invalid_file_format(db):
    invalid_file = BytesIO(b"Invalid file content")
    response = client.post(
        "/upload",
        files={"file": ("test.txt" , invalid_file, "text/plain")}
    )
    assert response.status_code == 400
    assert "Error processing file" in response.json()["detail"]
    
