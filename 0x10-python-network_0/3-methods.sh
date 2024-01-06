#!/bin/bash
# display all allowed methods of a of a server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
