pipeline {

  agent any

  stages {
    stage('build') {
      steps {
        sh 'cd flask'
        sh 'python3 -m venv env'
        sh 'source /env/bin/activate'
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