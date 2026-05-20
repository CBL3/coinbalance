from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

bp = Blueprint("hardware", __name__, url_prefix="/api/v1/hardware")

@bp.route("/interface", methods=["POST"])
def interface():
    """
    Hardware Abstraction Layer (HAL) Endpoint.
    Receives agnostic payloads from hardware clients (Xyron, NFC readers, etc.)
    and standardizes them into internal network events.
    """
    data = request.get_json()

    if not data:
        raise BadRequest("Missing JSON payload")

    hardware_id = data.get("hardware_id")
    event_type = data.get("event_type")
    payload = data.get("payload", {})

    if not hardware_id or not event_type:
        raise BadRequest("hardware_id and event_type are required")

    # Future phase: enqueue this event to decouple hardware ingestion from processing.

    # Mocking successful ingestion of the hardware event
    response = {
        "status": "accepted",
        "message": f"Event {event_type} from hardware {hardware_id} accepted by HAL.",
        "processed_payload": payload,
    }

    return jsonify(response), 202
