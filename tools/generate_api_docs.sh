set -e

echo "Generating API docs..."

echo "Generating HTTP API docs..."
python3 generate_http_api_docs.py ../backend/transc/api/constants_endpoint_structure.py \
		> ../docs/api-http/README.md