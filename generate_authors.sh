#!/usr/bin/env bash
set -e


cd "$(/home/vagrant/AirBnB_clone/)"

{
	cat <<- 'EOH'
	# This file lists all individuals having contributed content to the repository.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
