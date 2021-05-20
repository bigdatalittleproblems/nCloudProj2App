pipeline {
    
    agent any
    stages {
        stage('EKS Config') {
            steps {
                echo "${env.BUILD_ID}"
                sh "pwd"
                sh "tree"
                sh "aws eks --region us-east-1 update-kubeconfig --name my-cluster"
                
            }
        }
        stage('Build Image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        steps{
        // sh "PACKAGE=ncloud"
        // sh "BUILD_ID=${env.BUILD_ID}"
        // echo "Current Build is: ${BUILD_ID}"
        // echo "docker build -t bigdatalittleproblems/proj2ncloud:${PACKAGE}-${BUILD_ID}"
        sh """
        echo "Build Number: ${env.BUILD_ID}"
        PACKAGE=ncloud
        cd dockerapp
        docker pull bigdatalittleproblems/proj2ncloud
        docker build -t bigdatalittleproblems/proj2ncloud:${env.BUILD_ID} . 
        """
        sh "docker push bigdatalittleproblems/proj2ncloud:${BUILD_ID}"
    }
      
    }
    stage('Deploy Helm') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        steps{
        sh '''
        PACKAGE=ncloud
        DEPLOYED=$(helm list |grep -E "^${PACKAGE}" |grep deployed |wc -l)
        if [ $DEPLOYED = 0 ]
        then
            echo "Helm Chart is installing for the first time"
            helm install "^${PACKAGE}" cramirez-ncloud --set image.tag="^${env.BUILD_ID}"
        else
            echo "Helm Chart is updating"
            helm upgrade ${PACKAGE} cramirez-ncloud --set image.tag=${env.BUILD_ID}
        fi
        echo "Deployed Helm Chart"
        '''}
    }
}
}
