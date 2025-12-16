pipeline {
  agent any

  environment {
    DOCKER_REGISTRY = 'ahmedmostafa22'
    APP_NAME = 'ansible_project'     
    IMAGE_TAG = "v${env.BUILD_ID}"
    ANSIBLE_PLAYBOOK = "playbooks/rolling_update.yml"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Image') {
      steps {
        sh """
          docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG} roles/app_deploy/files/app/
        """
      }
    }

    stage('Login to Registry & Push') {
  steps {
    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
      sh '''
        set -e
        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
        docker push "$DOCKER_REGISTRY/$APP_NAME:$IMAGE_TAG"
      '''
    }
  }
}

stage('Deploy via Ansible') {
  steps {
    withCredentials([string(credentialsId: 'ansible-vault-pass', variable: 'VAULT_PASS')]) {
      sh '''
        set -e
        export ANSIBLE_LOCAL_TEMP=/tmp/ansible_tmp
        export ANSIBLE_REMOTE_TEMP=/tmp/ansible_tmp
        mkdir -p /tmp/ansible_tmp
        vaultfile=$(mktemp)
        echo "$VAULT_PASS" > "$vaultfile"
        chmod 600 "$vaultfile"
        ansible-playbook "$ANSIBLE_PLAYBOOK" --extra-vars "new_version=$IMAGE_TAG" --vault-password-file="$vaultfile"
        rm -f "$vaultfile"
      '''
    }
  }
}
  }

//   post {
//   failure {
//     echo "Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
//   }
// }
}