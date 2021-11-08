# **PY MAN GAME**

You can see the live site [here](https://py-man.herokuapp.com/).

The Py Man application is a hangman style game with Python programming language as its theme. 

It is a simple command line application.

![Mock up image](assets/wireframes/mockup.JPG)

*Please press **Ctrl** in Windows or **Command** on Mac button and click for any links which you would like to open in a new tab when in the README.md file*

## **FEATURES**



## **FUTURE DEVELOPMENT**



## **TESTING**

[wireframes](assets/wireframes/.png)


### **VALIDATOR TESTING**


## **BUGS**

-   I had an issue with the game when word was guessed successfully, the game wouldn't finish until user used all lives available. The issue got resolved upon changing the code which checked the lenght of the guessed letters and the play_word(masked word). However this worked only on words with non-repeating characters. If word, e.g mixin, had two or more repeating character inside, the game wouldn't count it in. The count method and counter need to be implemented. 


## **UNFIXED BUGS**

-   


## **DEPLOYMENT**

The project was deployed using Code Institutes mock terminal for Heroku.

The steps to deploy are as follows:
1. Save all your work and push all changes. Make sure you added \n to all your input code.
2. This project doesn't have any external libraries therefore my requirements.txt file is empty. Otherwise I'd have to follow this step: 
    *type in terminal pip3 freeze > requirements.txt, then save and push the changes into GitHub*
3. Create a new app in Heroku.
4. Select **'New'** and **'Create new app'**.
5. Name the new app and click **'Create new app'**. Name should be something unique, otherwise it won't allow us to continue
6. Go to the settings tab and find the Config Vars section. Click **'Reveal Config Vars'**. Here you should upload content from creds.json file. I don't use it in my project, there are no sensitive data to be protected, therefore I skipped this step.
7. While still in Config Vars, add into KEY: **PORT** and VALUE: **8000**. 
8. After select **'BuildPack'** which is below Config Vars. Select **Python** and save, then select **Nodejs** and save again. It has to be in this specific order. If you have made a mistake, you can drag the Python buildpack and move to the first place. 
9. Click on **'Deploy'** and select your deploy method and repository. You do this by entering the repository name as it is in GitHub then click *'search'*.
10. Click on **'Connect'** button on selected repository.
11. I chose **'Enable Automatic Deploys'** to rebuild my app automatically every time I push any changes in Gitpod.
12. Now deploy by scrolling down and click the **'Deploy Branch'** button. Heroku will notify you that the app was successfully deployed with a button to view the app.
13. The live app address is **https://py-man.herokuapp.com/**.


## **CREDITS**
- Thanks to tutors from Tutor Support - namely Sean Murphy and John Traas.

- **CONTENT**


- **CODE**
- Code from function delete_last_line() was specifically written for my need by a felow coder on stackoverflow.com as I have tried various solutions to what I wanted to achieve and nothing has worked. 
 

- **MEDIA**


*This project is for educational purposes only.*