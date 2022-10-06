# error codes
DEFAULT_HTTP_ERROR_CODE = 500
DEFAULT_ERROR_CODE = 5000
BAD_REQUEST_CODE = 400
SUCCESS_CODE = 200
DEFAULT_HTTP_ERROR_MESSAGE = "Internal Server Error"
DEFAULT_AUDIT_ERROR_MESSAGE = "Audit Service Error"
DEFAULT_DSAR_ERROR_MESSAGE = "DSAR Request Error"
DEFAULT_RABBITMQ_ERROR_MESSAGE = "RabbitMQ Error"
CONFLICT_HTTP_ERROR_CODE = 409
NO_CONTENT_CODE = 204
NOT_FOUND = 404
FORBIDDEN_CODE = 403
ALREADY_REPORTED = 208
ENTITY_CREATED = 201

# custom status codes
UNAUTHORISED = 4001

# form data messages
INVALID_FORM_MESSAGE = "Invalid form fields. Please check again the data you have entered."
USER_DOES_NOT_EXIST = "User does not exist"
NO_INVITATION = "No invitation"
CODE_VERIFIED_SUCCESSFULLY = "Code Verified Successfully"
INVALID_JWT_TOKEN = "Invalid JWT Token"

# encodings
UTF_ENCODING = "utf-8"

JWT_ENCRYPTION_ALGO = "HS256"

TEMPORARY_JWT_EXP_TIME_MINS = 60
MFA_TIME_INTERVAL = 600
MFA_EXP_TIME_IN_SECONDS = 600
