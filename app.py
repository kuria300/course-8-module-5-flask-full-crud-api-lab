from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data=request.get_json()

    if not data or "title" not in data:
        return jsonify({"error":"title missing"}), 400

    title=data.get('title')
    # TODO: Task 3 - Implement the Loop and Process Each Element
    result={
        "id":len(events) + 1,
        "title":f"{title}"
    }
    events.append(result)
    

    return jsonify(result), 201
    # TODO: Task 4 - Return and Handle Results
    

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data=request.get_json()

    if not data or "title" not in data:
        return jsonify({"error":"Data missing"}), 400

    for event in events:
        if event.id == event_id:
            event.title=data.get('title')
            
        return jsonify({"title": event.title}), 200

    return jsonify({"error": "event not found"}), 404

    
# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    deleted_event = None  # (e)
    
    for e in events:
        if e.id == event_id:
            deleted_event = e  # Fixed typo: changed 'a' to 'e'
            break

    if deleted_event is None:
        return jsonify({"error": "event not found"}), 404

    events = [e for e in events if e.id != event_id]

    return "", 204

    

if __name__ == "__main__":
    app.run(debug=True)
