set -e

openssl genpkey -algorithm RSA -out ca-key.pem
openssl req -new -x509 -key ca-key.pem -out cacert.pem -subj $(cat $1 | tr -d "\n")

# Create set of SSL credentials
openssl genpkey -algorithm RSA -out ssl-cert-snakeoil.key
openssl req -new -key ssl-cert-snakeoil.key -out req.pem -subj $(cat $1 | tr -d "\n")
openssl x509 -req -in req.pem -CA cacert.pem -CAkey ca-key.pem -CAcreateserial -out ssl-cert-snakeoil.pem
rm req.pem
