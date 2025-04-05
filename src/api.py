from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Database connection
conn = psycopg2.connect(
    dbname="traffic_data",
    user="mohammedwasifahmed",  # use `whoami` if unsure
    host="localhost",
    port="5432"
)

@app.get("/")
def root():
    return {"message": "🛣️ Adaptive Traffic Signal API is running"}

@app.get("/traffic/recent")
def get_recent_traffic(limit: int = 10):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM traffic ORDER BY datetime DESC LIMIT %s", (limit,))
    results = cursor.fetchall()
    return results


@app.get("/traffic/stats/daily")
def get_daily_stats():
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT DATE(datetime) as date, SUM(vehicles) as total_vehicles
        FROM traffic
        GROUP BY DATE(datetime)
        ORDER BY DATE(datetime) ASC;
    """)
    return cursor.fetchall()
