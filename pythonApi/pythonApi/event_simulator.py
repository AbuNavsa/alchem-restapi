# event_simulator.py

import sqlite3
import random
import time

DATABASE = 'events.db'

# Performance states
PERFORMANCE_STATES = [
    'Idle', 'Processing', 'High Load', 'Overloaded', 'Degraded Performance', 'Normal Operation'
]

# Corresponding error logs
ERROR_LOGS = {
    'Idle': [
        {'type': 'info', 'message': 'System is idle.'},
        {'type': 'info', 'message': 'No active tasks or processes.'}
    ],
    'Processing': [
        {'type': 'error', 'message': 'Task {task_id} failed to complete.'},
        {'type': 'error', 'message': 'Processing timeout for task {task_id}.'}
    ],
    'High Load': [
        {'type': 'warning', 'message': 'High CPU usage detected.'},
        {'type': 'warning', 'message': 'Memory usage exceeds 80%.'},
        {'type': 'error', 'message': 'Task {task_id} exceeded maximum execution time.'}
    ],
    'Overloaded': [
        {'type': 'critical', 'message': 'CPU usage at 100%.'},
        {'type': 'critical', 'message': 'Memory allocation failed.'},
        {'type': 'error', 'message': 'System unable to handle additional tasks.'},
        {'type': 'error', 'message': 'Task {task_id} dropped due to overload.'}
    ],
    'Degraded Performance': [
        {'type': 'warning', 'message': 'Task {task_id} is taking longer than expected.'},
        {'type': 'error', 'message': 'Performance degradation detected in component {component_name}.'},
        {'type': 'error', 'message': 'Service response time exceeded acceptable limits.'}
    ],
    'Normal Operation': [
        {'type': 'info', 'message': 'Routine maintenance task {task_id} completed.'},
        {'type': 'warning', 'message': 'Minor latency detected in service {service_name}.'},
        {'type': 'error', 'message': 'Non-critical error in task {task_id}, retrying...'}
    ]
}

def simulate_events():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    performance_state = random.choice(PERFORMANCE_STATES)
    error_log_entry = random.choice(ERROR_LOGS[performance_state])
    error_log_message = error_log_entry['message'].format(
        task_id=random.randint(1, 1000),
        component_name=random.choice(['Database', 'API', 'Service']),
        service_name=random.choice(['AuthService', 'PaymentService', 'UserService'])
    )
    
    # Use 'event_type' to specify the type of error
    try:
        cursor.execute("""
            INSERT INTO events (event_type, status, message, timestamp)
            VALUES
            (?, ?, ?, CURRENT_TIMESTAMP)
        """, (
            error_log_entry['type'].capitalize(),  # Event type as error type
            performance_state,
            error_log_message
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

# Main loop to simulate events continuously
if __name__ == "__main__":
    while True:
        simulate_events()
        time.sleep(5)  # Simulate event every 5 seconds
        print("Status logged")
