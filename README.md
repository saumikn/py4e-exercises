# Intro
Hello! My name is [Saumik](https://saumikn.com), and I'm a PhD student at Washington University, studying Computer Science with a focus in AI.

I created this project as an interactive companion to the course [Python for Everybody (PY4E)](https://www.py4e.com/), created by [Dr. Charles Severance](http://www.dr-chuck.com/), a professor at the University of Michigan. PY4E is hand's down the best course for teaching programming I've found - it's practical with an emphasis on getting going quickly, but without any expectation of prior coding experience. And it's free!

As part of the course, Dr. Severance provides a complete textbook which he wrote, video lectures covering the whole book, PowerPoint slides for each unit, quizzes at the end of each unit, and interactive exercises for students to solve. This last part is extermely important. There are a ton of other courses out there which consist of just videos or text. However, unless you're actively engaged with the material, writing and running your own code, passively watching videos is a complete waste of time in my opinion.

While the PY4E exercises are great, there are two main drawbacks. First, not all of the exercises have autograders available. In the first 10 chapters, the book provides 46 exercises, but only 12 of the exercises are autograded. Second, PY4E uses a custom, web-based autograding environment which doesn't provide offline access for students.

This project solves both of these problems. Out of the 46 exercises, I've created autograders for 39 of these exercises (the remaining 7 are free-response questions which autograders are generally [very bad](https://www.vice.com/en/article/pa7dj9/flawed-algorithms-are-grading-millions-of-students-essays) at grading). Additionally, my code runs in something called Jupyter Notebook, which allows for both online and offline access.

At the moment, I have only written autograders for the first 10 chapters. I could finish writing autograders for the rest of the chapters, but if people want to continue going through the book, I think it would be better at that point for students to start writing the programs on the own, as the book starts to go into more creative and unstructured types of problems.

# Running the Notebooks

For this project, I've decided to put all of my exercises into an environment called Jupyter Notebook. Jupyter Notebooks are essentially a combination of traditonal Python programs and the interactive Python interpreter/shell. If you've never programmed before or if you've only worked in traditional programming environments before, Jupyter Notebooks will be a unfamiliar at first, but you will get used to it quickly. The opposite is also true, if you can write code in Jupyter Notebooks, writing code in regular programs will also be easy.

I chose to use Jupyter Notebook for a few reasons. The first is that it allows me to combine exercises together much more cleanly than I would have been able to with individual files. The second is that I personally feel that Jupyter is a good environment to learn programming in, due to it's very interactive nature. The last is that practice with the Jupyter environment is very valuable, especially in the rising fields of Data Science, Machine Learning, and AI, areas where Jupyter is the standard way to work.

There are two ways of running the Jupyter Notebooks in this project - online and offline.

### Online

Using the free services provided by the Binder Project, students can access this entire project online for free, without needing to download Python, Jupyter, or any of the code. No registration necessary!

**Running Jupyter Notebooks Online:**
1. Go to https://mybinder.org/v2/gh/saumikn/py4e-exercises/HEAD. It may take about a minute or two before your interactive environment is ready to use.
2. Click on one of the notebooks to start solving exercises.
3. When you are finished, click the Download button at the top bar to save your work. 

Note that Binder has a relatively short timeout (providing computing resources is expensive). If you leave your computer for even 10 minutes, you will likely come back to an error message saying `"Connection Failed"`. As long as you don't close your tab, you can follow these [steps](https://discourse.jupyter.org/t/getting-your-notebook-after-your-binder-has-stopped/3268) to restart your notebook without losing any of your changes. 

### Offline

This is what I would reccomend most people do.

**Setting up your Offline Environment:**
1. Download [Anaconda](https://www.anaconda.com/products/individual), a program which installs Python and Jupyter for you.
2. Download the exercises and autograder by going to https://github.com/saumikn/py4e-exercises, and clicking Code → Download Zip. Unzip this file.

**Running Jupyter Notebooks Offline:**
1. Open the [Anaconda Prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt), type `jupyter notebook`, and press enter. This should automatically open Jupyter Notebook in your browser.
2. Find the folder where you saved the unzipped file in Jupyter Notebook.
3. Click on one of the notebooks to start solving exercises.
4. When you are finished, save your notebook using File → Save.

# Getting the most out of PY4E

The list of all lessons in the course can be found at https://www.py4e.com/lessons. You can skip the first lesson (Installing Python), since we will be using Jupyter Notebook for these exercises.

Here's my recomendation for how to go through each unit in the course:
1. Watch the videos where Dr. Severance goes over all the material. Each unit will generally have 30-60 minutes of lecture videos. The full video playlist is available on [Youtube](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p), and I will link the relevant videos for each unit at the top of each notebook. Some units will also have videos titled "Worked Exercise", but you should skip these for now.
2. Read the textbook chapter. The full textbook is available online as a [PDF](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf). Each chapter is also available as a website, and I will link the relevant chapter at the top of each notebook. The textbook has been translated into a few other [languages](https://www.py4e.com/book).
3. Take the quiz for each unit. You will need to sign into the website using a Google account in order to take the quiz.
4. If you found the quiz difficult, or if you're still uncomfortable with the some of the content, rewatch the videos or reread the textbook.
5. Solve the exercises in Jupyter Notebook! Each exercise will have a problem statement, a space for you to fill in your answer, and a space for the autograder to check your answer. Your goal should be to correctly solve each of the exercises in the unit, and (more importantly) understand why your solution works.
6. If you're feeling stuck on the exercises, check if Dr. Severance goes over it in one of the "Worked Exercise" videos.
7. Once you've finished everything in one unit, you can move onto the next one!

# How to use Jupyter

Here, I'll just provide a quick overview of how to get started working on the exercises. If you're interested in learning more about how Jupyter works, check out the [Documentation](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

**For this section, I reccomend that you actually open [00-readme.ipynb](https://github.com/saumikn/py4e-exercises/blob/main/00-readme.ipynb) in a Jupyter Notebook session, and follow along so you start to get practice with Jupyter.**

Each excercise is written in a Markdown cell. [Markdown](https://www.markdownguide.org/basic-syntax/) is a special formatting language which allows people to display formatted text (things like bullet points, headers, or code blocks). Markdown has two views - read and edit. By default, Jupyter should display the read mode. However, if you double-click on a Markdown cell, it may switch to edit mode. To go back to view mode, just click on the cell and press shift and enter at the same time. Try double-clicking on this cell to switch to edit mode, and press shift-enter to switch back to view mode.

In the PY4E course, there are three types of exercises - free response, multiple choice, and coding. 

Free response exercises ask the student to just answer a question or explain a topic in their own words. These questions don't have an autograder built in, but you should still complete these questions the best you can! Try answering the next question:

**Exercise 1: Why do you want to learn coding?**

Answer: I want to learn coding because ...

The next two types of exercises - multiple choice and coding - both have autograder capabilities. At the top of each notebook, there will be a code cell which looks like this:


```python
from grader import check_exercise
```

In order to enable the autograder, you must run the above code cell. You can run code cells by clicking on the cell and then pressing shift-enter. Try running the above cell. Once you've done this, there should be a number on the left side of the cell, which will look something like `[1]`. This means the autograder was loaded correctly. To verify this, try running the next cell.


```python
check_exercise
```

If the autograder was loaded correctly, you should see an output which looks something like `[2]: <function grader.check_exercise(exercise)>`. If you got an error which looks like `NameError: name 'check_exercise' is not defined`, this means you forgot to load the autograder. Once the autograder is loaded, you are all good to go, you don't need to run it each time you check a new problem.

Multiple choice exercises will consist of two cells - a Markdown problem cell, and a code cell where you put your answer. The answer cell will start of with a line that looks something like `exercise = 'Exercise 0.2'`. This line tells the autograder which problem you're trying to solve.

Next, there are a pair of lines that look like `### Begin Answer Here ###` and `###  End Answer Here  ###`. Not surprisingly, in between these lines is where your answer goes. When you put your answer down, the letter should be surrounded by single quotes, so it will look like `answer = 'a'`, `answer = 'b'`, `answer = 'c'`, or `answer = 'd'`.

Finally, the cell will print out the answer you put, so the autograder can grade your solution.

Try solving the next exercise:

**Exercise 2: What is 2 + 2?**

a\) 2

b) 3

c) 4

d) 5


```python
exercise = 'Exercise 0.2'

### Begin Answer Here ###
answer = 
###  End Answer Here  ###

print(repr(answer))
```

Once you've solved the exercise, you can check your answer by running the following cell. Make sure to save the notebook before checking your answer, otherwise the autograder won't see your most recent changes. You can save your notebook by running File → Save.


```python
# Make sure to save your notebook before checking!
check_exercise('Exercise 0.2')
```

Did you get the answer correct?
* If you got it correct, you will get a message that says `'All tests passed!'`
* If you got it wrong, you will get a message that says `Error: Wrong answer`
* If you didn't answer the question at all (or you forgot to save before checking your answer), you will get a message that says `SyntaxError: invalid syntax`

Coding exercises are very similar to multiple-choice exercises. The cell will start with a line which looks like `exercise = 'Exercise 0.3'`, and have two lines that say `### Start Code Here ###` and `###  End Code Here  ###`

The only difference is that instead of writing a single letter between those lines, you'll have to write your own Python program! Sometimes I will start you off with some code for you to modify, and sometimes you will have to write the entire answer from scratch. Try running the next code block (without fixing the typo), and checking the exercise.

**Exercise 3: Fix the typo in the following Python program (instead of printing `Hellow orld!`, you should print `Hello World!`). You'll find out what how this Python program actually works next lesson.**


```python
exercise = 'Exercise 0.3'

### Begin Answer Here ###
print('Hellow orld!')
###  End Answer Here  ###
```


```python
# Make sure to save your notebook before checking!
check_exercise('Exercise 0.3')
```

You should have gotten a few lines which say that your code printed the wrong value, show the value that the autograder expected your code to print (`'Hello World!\n'`), and what your code actually printed (`'Hellow orld!\n'`). Note that `\n` represents the [newline](https://en.wikipedia.org/wiki/Newline) character, which you can just ignore.


After you've run the program and seen the error, try solving the exercise by fixing the typo in the program. Once you know how to solve this exercise, you're ready to get started with the rest of the course! Good luck with the exercises and happy Pythoning!

If you have any questions or comments, feel free to email me at saumik.narayanan@outlook.com. I'd love to hear back from people who found these exercises useful!