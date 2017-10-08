#!/bin/bash
read var1
var2=$(echo "scale=4; $var1" | bc -l)
printf "%.3f" $var2
