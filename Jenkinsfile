node {
   stage "Build"
   checkout scm
   sh "rm -rf .venv"
   sh "pipenv install --deploy --dev"

   stage "Test"
   sh "pipenv run nosetests"
   step $class: 'JUnitResultArchiver', testResults: 'nosetests.xml'
}
