pipeline {
  agent none
  stages {
    stage('build') {
        agent { docker { image 'python:3.6.5' } }
        steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python app.py'
      }
    }
  }
}
