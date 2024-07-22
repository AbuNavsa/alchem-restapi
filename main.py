from fastapi import FastAPI
import sqlite3

app = FastAPI()

DATABASE = 'events.db'

def get_status():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Correct SQL query to fetch status, event_type, and timestamp
    cursor.execute("SELECT status, event_type, message, timestamp FROM events ORDER BY timestamp DESC LIMIT 1")
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        status, event_type, message, timestamp = result
        return {
            "status": status,
            "event_type": event_type,
            "message": message,
            "timestamp": timestamp
        }
    else:
        return {
            "status": "No status available",
            "event_type": "N/A",
            "message": "N/A",
            "timestamp": "N/A"
        }

@app.get("/api/status")
def read_status():
    return get_status()

# To run the FastAPI app, use the following command:
# uvicorn main:app --reload
