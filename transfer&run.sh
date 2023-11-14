#!/bin/bash

# Define variables for the remote server
remote_username="root"
remote_server="65.1.116.216"
remote_directory="/home/ubuntu/Workspace/KanakResume/"

# Define the name of the shell script to run on the remote server
remote_script="rundocker.sh"

# Copy only changed files to the remote server using rsync
echo "Copying files to remote server..."
rsync -r --update --delete * "${remote_username}@${remote_server}:${remote_directory}"

# Check if the rsync command was successful
if [ $? -eq 0 ]; then
    echo "File transfer successful."

    # SSH into the remote server and run the shell script
    ssh "${remote_username}@${remote_server}" "cd ${remote_directory} && chmod +x ${remote_script} && ./${remote_script}"

    # Check if the remote command was successful
    if [ $? -eq 0 ]; then
        echo "Remote script execution successful."
    else
        echo "Failed to execute the remote script."
    fi
else
    echo "Failed to copy files to the remote server."
fi