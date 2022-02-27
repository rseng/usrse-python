#!/bin/bash

echo
echo "************** START: test_client.sh **********************"

# Create temporary testing directory
echo "Creating temporary directory to work in."
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
shpc_root="$( dirname "${here}" )"

. $here/helpers.sh

# Create temporary testing directory
tmpdir=$(mktemp -d)
output=$(mktemp ${tmpdir:-/tmp}/usrse_test.XXXXXX)
printf "Created temporary directory to work in. ${tmpdir}\n"

# Make sure it's installed
if ! command -v usrse &> /dev/null
then
    printf "usrse is not installed\n"
    exit 1
else
    printf "usrse is installed\n"
fi

echo
echo "#### Testing base client "
runTest 0 $output usrse --version

echo
echo "#### Testing list "
runTest 0 $output usrse list --help
runTest 0 $output usrse list


echo
echo "#### Testing get "
runTest 0 $output usrse get --help
for endpoint in $(usrse list); do
    runTest 0 $output usrse get $endpoint
    runTest 0 $output usrse get $endpoint --live
done   

rm -rf ${tmpdir}
