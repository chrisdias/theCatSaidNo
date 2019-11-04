# Deploying a Python Web App from Dev Container in VS Code using GitHub actions

In this lab, you will Visual Studio Code remote development features to work on a Python Flask application in a dockerized development environment. You will then deploy the app to Azure App Service and set up a CI/CD workflow using GitHub Actions


## Requirements

- Python 3.7
- Docker
- Visual Studio Code
- GitHub account

## Open the dev container workspace

1. Fork the following repo: https://github.com/sana-ajani/theCatSaidNo-GHU

1. Open the Windows Terminal, and clone the sample app and open using Visual Studio Code:

    ```cmd
    git clone https://github.com/<yourusername>/theCatSaidNo-GHU

    cd theCatSaidNo

    code . -r
    ```

1. Notice the repo has a `.devcontainer` folder which contains a `Dockerfile` and a `devcontainer.json`. The dev container tells VS Code how to create a development container that has a specific runtime, extensions, and tools. In this case, the dev container is Python specific and tells VS Code to install the Python and Azure App Service extensions. 

1. Click the `Reopen in Container` prompt, or press `F1` and select the `Reopen folder in dev container` command.


## Open the dev container workspace

VS Code is creating the container now. It'll take a few minutes the first time to actually create it, but the next time you reconnect to an existing container is pretty quick. VS Code is also installing a component called "VS Code Server" in the container so you can directly interact with code, the file system, and extensions in the remote workspace.

1. Notice the indicator in the bottom left corner tells us we are inside our dev container

1. Press `F1` and run the command "Open new terminal". Once you are in the new terminal instance, notice we're actually in Bash! Type the command `uname` to see that we're in a Linux environment right now. Run the command `python --version` to check that the version of Python in our remote container is different than the one that is on our local machine. 

1. Press `F5` to run the app inside the container

1. Browse to [`localhost:9000`](http://localhost:9000/) and try out the app! 


## Create an Azure App Service

Instead of running this locally, let's create this as a web app hosted in Azure. 

1. Stop the app running locally. Click on the Azure icon in the sidebar. 

1. Click on the `+` icon to create a new app service under the **VSCode GitHub Universe HOL** subscription.

1. Give your webapp a unique name (we recommend calling it **theCatSaidNo-{your name}**)

1. Select **Linux** as your OS and **Python 3.7** as your runtime. 

1. Browse to your new site! 

## Set up CI/CD with GitHub Actions 

We'll use GitHub actions to automate our deployment workflow for this web app. 

1. Inside the App Service extension, right click on the name of your app service and choose "Open in Portal".

1. From the Overview page, click on "Get publish profile". A publish profile is a kind of deployment credential, useful when you don't own the Azure subscription. Open the downloaded settings file in VS Code and copy the contents of the file.

1. We will now add the publish profile as a secret associated with this repo. On GitHub, click on the "Settings" for your repo and go to "Secrets". 

1. Create a new secret called "WebApp_PublishProfile" and paste the contents from the settings file.

1. Now click on "Actions" in the top bar and create a new workflow. 

1. Select the **Python application** template (not the Python Package one!) and click "Set up this workflow".

1. Add the following lines at the end of the workflow YAML file. This specifies that we want to deploy the web app using the publish profile method. 

    ```
    - uses: azure/webapps-deploy@v1
        with:
        app-name: theCatSaidNo-sana2  # Replace with your app name
        publish-profile: ${{ secrets.WebApp_PublishProfile }}
    ```

1. Once you're done, click on "Start commit". When you commit the file, it will trigger the workflow.

1. You can go back to the Actions tab, click on your workflow, and you can see the deploy taking place. 


## Test our your app!

1. Back in VS Code, go to the App Service extension, and right click on your app service and click on "Browse Website". 

1. Let's test our GitHub Actions workflow we just made. Add the following lines of code to `templates/home.html` in the body class, after we load in the catpaw image:

    ```
    <div>
        <h1 style="text-align:center;"> Press the button!<h1>
    </div>
    ```

1. In the terminal, run the following commands:

    ```
    git add .
    git commit -m "test ci/cd"
    git push
    ```

1. Browse back to your website!