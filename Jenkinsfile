pipeline {
  agent any
  stages {
    stage('build') {
        agent { docker { image 'python:3.6' } }
        steps {
        sh 'pip install --upgrade pip'  
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
