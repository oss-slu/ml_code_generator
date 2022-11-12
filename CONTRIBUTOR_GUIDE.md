# A Guide for new contributors
Welcome to ML Code Generator! You are probably looking at this page because you are interested in
contributing to this project. We want your contributions. Here, you will find instructions on how
to get started running this code in your development environment.

## Install pre-requisite tools
To take advantage of the development environment defined in this project, you will need two tools:
1. <a href="https://code.visualstudio.com/">Visual Studio Code</a>
2. <a href="https://www.docker.com/products/docker-desktop/">Docker Desktop</a>

Make sure to install these tools on your development system. Don't worry, they are free!

## Clone the repository
Clone this git repository to your computer either way you like:
* You can use git command line tool
* You can clone the repo via Visual Studio code

## Start Docker
The development environment will use a Docker container. All the dependencies will be installed
in a Docker container and the code will run in Docker. In order to make this happen, Docker must be
running on your computer. Make sure to start Docker Desktop.

## Open the project in VS Code
Start Visual Studio code and open your clone of this git repository. 

## Install Dev Containers extensions
In Visual Studio code, click on the <a href="https://code.visualstudio.com/docs/editor/extension-marketplace">Extensions</a> icon and search for "Dev Containers". Install the the remote containers extension.

## Build and run the container
In Visual Studio code, open the <a href="https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette">Command Palette (Ctrl+Shift+p)</a> (you can also find the command palette by clicking on the gear icon at the bottom left corner). Type in: Dev Containers: Reopen in Container, and select the option that matches what you typed. This will build a container and run your code in it. 

## Run the code
Once the container is ready, open a terminal from VS code and run the application with:
<code>
python flask_app/flask_main.py
</code>
