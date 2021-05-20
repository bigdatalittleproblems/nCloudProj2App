#!/bin/sh
DEPLOYED=$(helm list | grep deployed | wc -l)
BUILD_ID=105
PACKAGE=ncloud
if [ $DEPLOYED = 0 ]
then
    echo "Helm Chart is installing for the first time"
    echo "helm install $PACKAGE cramirez-ncloud --set image.tag=${env.BUILD_ID}"
else
    echo "Helm Chart is updating to version ${env.BUILD_ID}"
    echo "helm upgrade $PACKAGE cramirez-ncloud --set image.tag=${env.BUILD_ID}"
fi
echo "Deployed Helm Chart"
