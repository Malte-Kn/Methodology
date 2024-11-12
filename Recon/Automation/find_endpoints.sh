/bash
baseDir="/opt/TARGETS"

if [[ -d "$baseDir" ]]; then
	for dir in "$baseDir"/*/; do
		target=$(basename "$dir")
		if [[ -f "${dir}/liveSubs.txt" ]]; then
			echo "Getting every endpoint for $target:"
			waymore -mode 'U' -i "${dir}/liveSubs.txt" -oU "${dir}/endpoints.txt"
			httpx -l "${dir}/subs.txt" -silent | anew "${dir}/liveSubs.txt"
			echo "--"
			
		else
			echo "No liveSubs found for $target?!"
		fi
	done
else
	echo "Directory $baseDir not found!"
