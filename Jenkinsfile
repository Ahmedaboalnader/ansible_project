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
    // Use both Vault secret and an SSH private key stored in Jenkins credentials
    withCredentials([
      string(credentialsId: 'ansible-vault-pass', variable: 'VAULT_PASS'),
      sshUserPrivateKey(credentialsId: 'vagrantsshkey', keyFileVariable: 'VAGRANT_KEY', usernameVariable: 'VAGRANT_USER')
    ]) {
      sh '''
        set -e
        export ANSIBLE_LOCAL_TEMP=/tmp/ansible_tmp
        export ANSIBLE_REMOTE_TEMP=/tmp/ansible_tmp
        mkdir -p /tmp/ansible_tmp

        # vault file (temporary)
        vaultfile=$(mktemp)
        echo "$VAULT_PASS" > "$vaultfile"
        chmod 600 "$vaultfile"

        # ensure temp key is safe and usable
        chmod 600 "$VAGRANT_KEY" || true
        # also ensure any .vagrant private keys in the workspace are secure (prevents SSH from rejecting them)
        chmod 600 .vagrant/machines/*/virtualbox/private_key || true

        # run ansible using the Jenkins-provided private key (avoids relying on .vagrant paths)
        ansible-playbook "$ANSIBLE_PLAYBOOK" --extra-vars "new_version=$IMAGE_TAG" --vault-password-file="$vaultfile" --private-key "$VAGRANT_KEY"

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