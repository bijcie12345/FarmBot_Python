pipeline {

  agent any
  
  stages {
    stage('build') {
      steps{
        sh 'sudo docker-compose build'
      }
    }
    stage('deploy') {
      steps {
        sh 'sudo docker-compose up -d'
      }
    }
  }
}