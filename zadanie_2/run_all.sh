#!/bin/bash


for i in {1..6}
do
    echo "running chol_$i"
    make run VERSION="chol_$i"
done
