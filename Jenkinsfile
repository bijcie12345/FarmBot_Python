pipeline {

  agent any

  stages {
    stage('build') {
      steps {
        sh 'echo ${USER}'
        sh 'sudo docker-compose build'
        sh 'sudo docker-compose up'
      
      }
    }
  }
   post {
      always {
         sh "docker-compose down || true"
      }
   }   
}