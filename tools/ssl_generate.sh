set -e

# Check input
if [[ -z "$1" ]]; then
    echo "Usage: $0 <subject file>"
    exit 1
fi

if [ -z "$(ls -A)" ]; then
    echo "Generating ssl certificate"
else
    echo "SSL directory already has files in it -> skipping creation of new ssl certificate"
    exit 0
fi

SUBJECT_FILE=$1

if [[ ! -r "$SUBJECT_FILE" ]]; then
    echo "Error: can't read subject file: $SUBJECT_FILE"
    exit 1
fi

SUBJECT=$(cat "$SUBJECT_FILE" | tr -d "\n")

# Generate CA private key
openssl genpkey -algorithm RSA -out ca-key.pem

# Create self-signed CA certificate
openssl req -new -x509 -key ca-key.pem -out cacert.pem -subj "$SUBJECT"

# Generate server private key
openssl genpkey -algorithm RSA -out ssl-cert-snakeoil.key

# Create server certificate request
openssl req -new -key ssl-cert-snakeoil.key -out req.pem -subj "$SUBJECT"

# Sign server certificate with CA certificate
openssl x509 -req -in req.pem -CA cacert.pem -CAkey ca-key.pem -CAcreateserial -out ssl-cert-snakeoil.pem

# Cleanup
rm req.pem
