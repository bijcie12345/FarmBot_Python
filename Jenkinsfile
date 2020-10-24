pipeline {

  agent any

  stages {
    stage('build') {
      steps {
        sh 'echo ${USER}'
        sh 'docker-compose build'
        sh 'docker-compose up'
      
      }
    }
  }
   post {
      always {
         sh "docker-compose down || true"
      }
   }   
}