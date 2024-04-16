#!/usr/bin/env bash

set -e
trap cleanup SIGINT ERR

username="usertraffic"
password="passwordtraffic"
cookie="$(dirname "${0}")/cookies.txt"
host=https://localhost
output="$(dirname "${0}")/output"
useragents=(
	"Mozilla/5.0 (Windows NT 10.0; rv:124.0) Gecko/20100101 Firefox/124.0"
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
endpoints=(
	"/api/users" "/api/media/avatars/default.png"
)
isnumber='^[0-9]?+([.][0-9]+)?$'
if ! [[ "${1}" =~ $isnumber ]]; then
	printf "usage: $(basename "${0}") [delay in seconds]\n"; exit 1;
fi
delay="${1}"

cleanup() {
	printf "\n"
	if [[ -z "${cookie}" ]]; then exit 0; fi
	rm -f "${cookie}"
	printf "removed cookie: ${cookie}\n"
	exit 0
}

printf "host: ${host}\n"
printf "output to: ${output}\n"
mkdir -p "${output}"

if [ ! -f cookies.txt ]; then
	curl --no-progress-meter --insecure --header "Content-Type: application/json" -X POST -d "{\"username\": \"${username}\", \"password\": \"${password}\" }" https://localhost/api/users >"${output}/signup"
	curl --no-progress-meter --insecure --cookie-jar "$cookie" --header "Content-Type: application/json" -X POST -d "{\"username\": \"${username}\", \"password\": \"${password}\" }" https://localhost/api/login >"${output}/login"
	printf "got cookie: ${cookie}\n"
fi

printf "\n"
i=0
while true; do
	printf "\033[1A"
	printf "\033[2K"
	printf "\033[0G"
	i=$((i+1))

	useragent="${useragents[$((${RANDOM} % ${#useragents[@]}))]}"
	endpoint="${endpoints[$((${RANDOM} % ${#endpoints[@]}))]}"
	basename=$(basename ${endpoint})

	printf "request: ${i}, url: ${endpoint}\n"
	curl -s --insecure -H "User-Agent: ${useragent}" -b "$cookie" "${host}${endpoint}" >"${output}/${basename}"
	if [[ "${delay}" ]]; then
		sleep "${delay}"
	fi
done
