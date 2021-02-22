pipeline {
  agent any
  stages {
    stage('build') {
        agent { docker { image 'python:3.6' } }
        steps {
        sh 'pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python app.py'
      }
    }
  }
}
