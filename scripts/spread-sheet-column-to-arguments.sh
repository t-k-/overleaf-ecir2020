#!/bin/sh
cat ~/tmp.txt | awk '{printf("\"%s\",", $1)}'
echo ""
cat ~/tmp.txt | awk '{printf("%s,", $1)}'
echo ""
