from flask import Blueprint, request, jsonify, current_app
from .utils import validate_tc_number, send_email


bp = Blueprint("api", __name__, url_prefix="/api")




@bp.route("/health", methods=["GET"])
def health():
return jsonify({"status": "ok"}), 200




@bp.route("/tc-validate", methods=["POST"])
def tc_validate():
data = request.get_json() or {}
tc = data.get("tc")
if not tc:
return jsonify({"error": "tc alanı gerekli"}), 400
ok = validate_tc_number(str(tc))
return jsonify({"tc": tc, "valid": ok}), 200




@bp.route("/send-email", methods=["POST"])
def route_send_email():
data = request.get_json() or {}
to = data.get("to")
subject = data.get("subject", "Bildirim")
body = data.get("body", "")
if not to:
return jsonify({"error": "to alanı gerekli"}), 400


try:
send_email(
smtp_host=current_app.config.get("SMTP_HOST"),
smtp_port=current_app.config.get("SMTP_PORT"),
smtp_user=current_app.config.get("SMTP_USER"),
smtp_pass=current_app.config.get("SMTP_PASS"),
subject=subject,
body=body,
to=to,
)
return jsonify({"sent": True}), 200
except Exception as e:
current_app.logger.exception("Email gönderme hatası")
return jsonify({"sent": False, "error": str(e)}), 500
