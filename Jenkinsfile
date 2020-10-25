  pipeline {

  agent any
  
  stages {
    stage('build') {
      steps {
        sh 'docker build -t myimage'     
      }
    }
    stage('run'){
        steps {
          sh 'docker run -d --name mycontainer -p 80:80 myimage'
        }
    }
  }
   post {
      always {
         sh "docker-compose down || true"
      }
   }   
}