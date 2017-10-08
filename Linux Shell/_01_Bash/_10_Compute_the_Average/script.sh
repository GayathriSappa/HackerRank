#!/bin/bash
read var1
var2=$var1
var3=0
while [ $var1 -gt 0 ]
do
read var4
var3=$(( $var3 + $var4 ))
var1=$[ $var1 - 1 ]
done
var5=$(echo "scale=4; $var3/$var2" | bc -l)
printf "%.3f" $var5
