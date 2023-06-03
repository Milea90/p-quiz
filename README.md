# P-quiz 

This Python quiz is for those who likes cats. The quiz is simple and contains three questions about cats. The quiz is meant to be fun and easy and at the same time informative.
It is easy to play. Just hit the letter that represents the answer, and then hit enter to get to the next question.
Link to deployed site: https://p-quiz.herokuapp.com/

![alt text](/readme-images/am-i-resp.png)

## How to play
It is easy to play this game. All you have to do is click the letter for your answer on your keyboard, then hit enter. The next question will then pop up and run until all the answers has been answered. And then a score will tell you how well you did.

## Features 
First, a welcome message is shown, telling you what kind of quiz it is and starting with the first question. 
![alt text](/readme-images/quiz-welcome.png)


Then, you will have to answer, using the letter for the answer you chose. 

Lastly, after you have answered the last question, your score will automatically show up on the screen. 
![alt text](/readme-images/score.png)

## Features left to implement
Add more questions and be able to make the user type in both the letter and/or the correct answer using words.

## Data model
I have used a class for the questions in or
der to run the answers and the questions as well as keeping score. 

## Testing
I have used the terminal to make sure the program works as expected. I also used PEP8 linter to check the code (see picture). The results were complaining about white spaces, but that made the code easier to read, so I chose not to change that. 
![alt text](/readme-images/pep8.png)

## Bugs - solved and unsolved 
* I was trying to add AND, OR to the possible answers so that the user could answer with both letters and/or type in the words. But I found many bugs while doing so. For example, the score was not giving the correct answer no matter if I used AND or OR. So I decided just to leave it as it is. 

* I am not sure how this project will work as the deployed version, since I got a message in the terminal saying that pyenv 3.8.12 was not installed. But as you can see in the image below, at the bottom left, it seems to be installed and working just fine. So hopefully it will work just fine. 
![alt text](/readme-images/term-error.png)

* I had a problem/bug with my questions and could not figure out why. Turned out they were missing a comma. Tutor helped me with that.

## Credits
The code for this quiz was made thanks to this tutorial on YouTube: https://www.youtube.com/watch?v=SgQhwtIoQ7o 
Thanks to tutor, I resolved some bugs with my code. 

## Deployment
To deploy this project: 
Clone this repository and then create a new app on Heroku. Make sure to set build backs to Python and NodeJS in that order. 
Link the Heroku app with Github and click deploy. 

