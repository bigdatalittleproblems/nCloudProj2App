pipeline {
    
    agent any
    stages {
        stage('eks config') {
            steps {
                sh "aws eks --region us-east-1 update-kubeconfig --name my-cluster"
                echo 'Hello World'
            }
        }
        stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        steps{
        sh "docker build -t bigdatalittleproblems/proj2ncloud:latest ."
        sh "docker push bigdatalittleproblems/proj2ncloud"
    }
      
    }
    stage('deploy helm') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        steps{
        sh "helm upgrade ncloud cramirez-ncloud"
        }
      
    }
}
}
