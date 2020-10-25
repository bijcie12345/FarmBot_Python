  pipeline {

  agent any
  
  stages {
    // stage('build') {
    //   steps {
    //     sh 'sudo docker build -t myimage .'     
    //   }
    // }
    stage('run'){
        steps {
          sh 'sudo docker run -d --name mycontainer -p 80:80 myimage'
        }
    }
  }
   post {
        success {
            echo 'I succeeded!'
        }
        failure {
            echo 'I failed :('
        } 
    //   always {
    //      sh "sudo docker-compose down || true"
    //   }
   }   
}