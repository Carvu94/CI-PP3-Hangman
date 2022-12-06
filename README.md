# THE HANGMAN

(Developer: Matej Car)

[THE HANGMAN >>> Live live website ]()


## About


## Table of Contents

## Project Goals
<hr>

- 

### User Goals


### Site Owner Goals



## User Experience

### Target Audience




### User Requirements and Expectations


### User Manual
<hr>

#### Overview

[Back to Table Of Contents](#table-of-contents)

## User Stories
<hr>

### Users

1. I want to have an idea of what the program is about

### Site Owner
 
1. I want user to easily and intuitively navigate troughout program
2. I want user to be guided and informed how to make valid inputs
3. I want user to have clear feedback from  inputs
4. I want user to have the option to exit the program


[Back to Table Of Contents](#table-of-contents)

## Technical Design
<hr>

### Flowchart

 - This Flowchart created using Lucid chart summarises the structure and logic of the application.


### Data models
<hr>

## Technologies Used
<hr>

### Languages


- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Lucidchart](https://www.lucidchart.com/) was used to draw a program flowchart

- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment
- [Font Awesome](https://fontawesome.com/) - icons from Font Awesome were used in the footer below the program terminal

### Libraries

#### Python Libraries
- random - used to generate random player values inside given parameters

#### Third Party Libraries

[Back to Table Of Contents](#table-of-contents)

## Features
<hr>

[Back to Table Of Contents](#table-of-contents)

## Future features to implement

<hr>


## Validation
<hr>

## Testing

The testing approach is as follows:
1. Manual testing of user stories
2. Automated unit testing using the Python unittest library

### Manual Testing
<hr>

### Automated Testing
<hr>

## Bugs

## Deployment

### Heroku
<hr>
The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-login.png">
    </details>

2. Create a new app, add a unique app name ( for example PP3_The_Coach) and then choose your region
3. Click on create app
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-new-app.png">
    </details>

4. Go to "Settings"
5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-conf-var.png">
    </details>

6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-buildpack.png">
    </details>

7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-deploy.png">
    </details>

9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-branch-deploy.png">
    </details>

11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.
    <details><summary>Screenshot</summary>
    <img src="docs/deployment/heroku-end.png">
    </details>

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on the Fork button in the top right corner
3. Copy of the repository will be in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files (next to 'Add file') and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Code

- [ASCII Art Generator](http://patorjk.com/software/taag/) was used to create program title

- Code Institute -  "Love Sandwiches - Essentials Project" walkthrough helped me to connect  Google Spreadsheet to my project.


## Acknowledgements