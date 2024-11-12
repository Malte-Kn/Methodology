#!/bin/bash
baseDir="/opt/TARGETS"

if [[ -d "$baseDir" ]]; then
	for dir in "$baseDir"/*/; do
		target=$(basename "$dir")
		if [[ -f "${dir}/maindomains.txt" ]]; then
			echo "Getting every domain for $target:"
			subfinder -dL "${dir}/maindomains.txt" -silent | anew -q "${dir}/subs.txt"
			httpx -l "${dir}/subs.txt" -silent | anew "${dir}/liveSubs.txt"
			echo "--"
			
		else
			echo "No maindomains found for $target?!"
		fi
	done
else
	echo "Directory $baseDir not found!"
fi
