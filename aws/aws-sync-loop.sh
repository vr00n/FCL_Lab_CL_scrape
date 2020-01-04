#!/bin/bash
#run in a tmux session
for i in  `seq 1 1000000`
do
        aws s3 sync /home/ubuntu/ s3://fcl-zapier/ --exclude "/home/ubuntu/*" --include "/home/ubuntu/cl-results.txt" --acl public-read
        sleep 3600
done
