pipeline {
  agent {
    // Run this job within a Docker container built using Dockerfile
    // contained within your projects repository. This image should include
    // the core runtimes and dependencies required to run the job,
    // for example Python 3.x and NPM.
    dockerfile { filename 'Dockerfile' }
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('build') { // Install any dependencies you need to perform testing
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
