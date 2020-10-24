pipeline {

  agent none

  stages {
    stage("Fix the permission issue") {

      agent any

      steps {
        sh "sudo chown root:jenkins /run/docker.sock"
      }
      
    stage('build') {
      steps {
        sh 'cd flask'
        sh 'python3 -m venv env'
        sh 'pip install flask uwsgi'
        sh 'cd ..'
        sh 'export FLASK_APP=run.py'
        sh 'export FLASK_ENV=development'
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