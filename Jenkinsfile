pipeline {
    
    agent any
    stages {
        stage('Hello') {
            steps {
                sh "ls"
                // sh "cd dockerapp/Flask"
                // sh "cat dockerapp/Flask/Dockerfile"
                echo 'Hello World'
            }
        }
        stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        steps{
        sh "docker build -t testbuld ."
    }
      
    }
}
}
