# THE HANGMAN

(Developer: Matej Car)
The Hangman is Python terminal game, which runs in the Code Institute mock terminal on Heroku.
Users can try to guess the word by inputting a letter or whole word until they either guess the word or lose all lives. 
Users have 10 tries to guess the word before they are "hanged".

![The Hangman](/docs/am-i-responsive.png)

[THE HANGMAN >>> Live live website ](https://ci-pp3-the-hangman.herokuapp.com/)

## Table of Contents
- [**How to Play**](#how-to-play)
- [**User Experience**](#user-experience)
- [**Features**](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [**Technical Design**](#technical-design)
    - [Flowchart](#flowchart)
- [**Technologies Used**](#technologies-used)
    - [Frameworks & Tools](#frameworks--tools)
- [**Validation**](#validation)
    - [Testing](#testing)
- [**Bugs**](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Remaining Bugs](#remaining-bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

## How to play

Users play Hangman by inputting commands in terminal. The aim of the game is to guess the hidden word. Hidden word is represented with underscores to indicate how many letters are in word. When user guess the letter correctly, the underscore is replaced with the correct letter. The user has 10 lives to start with and each stage is represented with graphics of a hangman. When the user guesses the word or looses all lives there is a option to play again. 

## User Experience

1. User wants to have an idea of what the program is about
2. User wants to be guided and informed how to make valid inputs
3. User wants to have a clear feedback from inputs
4. User wants to have option to exti the program

[Back to Table Of Contents](#table-of-contents)

# Features

## Existing Features

- Introduction section

    - Once the user runs the program, Hangman graphic is displayed and user is asked to enter the name. In case user enters invalid input, user is instructed to enter a name using letters only. 

![Intro Section](/docs/intro-section.png)
![Invalid Name](/docs/invalid-name.png)

- Welcome and Menu section

    - Once user enters valid name, he is welcomed to Hangman and asked to choose between playing the game or reading the rules. 

![Welcome and Menu](/docs/welcome-and-menu.png)

- Rules 

    - If user choose rules option, rules are printed and user is asked to press 'Enter' when ready to go back on the menu. 

![Rules](/docs/rules.png)

- Play game

    - When user choose play game option, the game is starting. Random word is generated and displayed and the hangman is displayed depending on number of lives left. 
    - User is asked to guess a letter or a word. In case user enter invalid input, user is warned and asked again to guess a letter or a word. 
    - If user guess is correct, the user will get the feedback and letter will be displayed instead of underscore. 
    - If user guess is incorrect, the user will get the feedback. 
    - All user guessess will be displayed on the top of screen. 
    - In case user enter same input two or more times, the message will be displayed and user will be asked for another input.

![Play Game](/docs/start-game.png)

![Invalid Guess](/docs/not-valid-guess.png)

![Correct Guess](/docs/correct-guess.png)

![Wrong Guess](/docs/wrong-guess.png)

![Already Guessed](/docs/already-guessed.png)

- You Win

    - When user guess correctly whole word, user wins and the message is displayed with option to play again.

![You Win](/docs/you-win.png)

- Game Over

    - If user runs out of lives and do not guess the word correctly, user loose and the message is displayed with option to play again. 

![Game Over](/docs/game-over.png)

- Play Again

    - When user wins or loose, user can choose to play again or not. 
    - If user choose to play again, new word is generated and game starts again. 
    - If user choose not to play again, thank you message is displayed and the program exits. 

![Not Play Again](/docs/not-play-again.png)

[Back to Table Of Contents](#table-of-contents)

## Future Features

- Highscore
- Different levels of difficulty

## Technical Design

### Flowchart

 - This Flowchart created using Lucid chart summarises the structure and logic of the application.

![Hangman Lucidchart](/docs/the_hangman_lucid.png)

[Back to Table Of Contents](#table-of-contents)

## Technologies Used

- Languages:
    - Python

- Libraries:
    - Random to select a random word
    - os to clear the terminal

- Other:
    - words.py - A list of words taken from (https://www.randomlists.com/data/words.json)

### Frameworks & Tools

- [Lucidchart](https://www.lucidchart.com/) was used to draw a program flowchart
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create Am I Responsive image and check responsivnes

[Back to Table Of Contents](#table-of-contents)

## Validation

## Testing

The testing approach is as follows:
1. Manual testing correct and incorrect user inputs
2. Automated unit testing using the Python unittest library
3. Tested through CI PEP8 Linter (https://pep8ci.herokuapp.com/). 
    - No errors were returned.

[Back to Table Of Contents](#table-of-contents)

# Bugs

## Solved Bugs

- When game started, under displayed hangman, 'None' was printed. This bug was fixed by adjusting print statement for random word.

![None](/docs/'none'.png)

- On several occasions I was encountering 'line too long' error which was fixed by breaking the code in more lines. 

![Line Too Long](/docs/line-too-long.png)

- When asked if user wants to play again and invalid input was entered, the program extied. This bug was fixed by adjusting the funciton.

![Wrong Input](/docs/wrong_input.png)

[Back to Table Of Contents](#table-of-contents)

## Remaining Bugs

- No bugs remaining

## Deployment

### Heroku
<hr>
The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name and then choose your region
3. Click on create app
4. Go to "Settings"
5. Add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

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
- Code Institute -  "Love Sandwiches - Essentials Project

## Acknowledgements

- Special Thanks to my mentor
- Thanks to my girlfriend, family and friends for support
- Thanks to Code Institute and fellow students on Slack channels 

[Back to Table Of Contents](#table-of-contents)