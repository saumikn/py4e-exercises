# What is PY4E-Exercises?
Hello! My name is [Saumik](https://saumikn.com), and I'm a PhD student at Washington University, studying Computer Science with a focus in AI.

I created this project as an interactive companion to the course [Python for Everybody (PY4E)](https://www.py4e.com/), created by [Dr. Charles Severance](http://www.dr-chuck.com/), a professor at the University of Michigan. PY4E is hands down the best course for teaching programming I've found - it's practical with an emphasis on getting going quickly, even for beginners without any coding experience. And it's free!

As part of the course, Dr. Severance provides a complete textbook which he wrote, video lectures covering the whole book, PowerPoint slides for each unit, quizzes at the end of each unit, and interactive exercises for students to solve. This last part is extremely important. There are a ton of other courses out there which consist of just videos or text. However, unless you're actively engaged with the material, writing and running your own code, passively watching videos is a complete waste of time in my opinion.

While the PY4E exercises are great, there are two main drawbacks. First, not all of the exercises have autograders available. In the first 10 chapters, the book provides 46 exercises, but only 12 of the exercises are autograded. Second, PY4E uses a custom, web-based autograding environment which doesn't provide offline access for students.

This project solves both of these problems. Out of the 46 exercises, I've created autograders for 39 of these exercises (the remaining 7 are free-response questions which autograders are generally [very bad](https://www.vice.com/en/article/pa7dj9/flawed-algorithms-are-grading-millions-of-students-essays) at grading). Additionally, my code runs in something called Jupyter Notebook, which allows for both online and offline access.

At the moment, I have only written autograders for the first 10 chapters. I could finish writing autograders for the rest of the chapters, but if people want to continue going through the book, I think it would be better at that point for students to start writing the programs on the own, as the book starts to go into more creative and unstructured types of problems.

# Getting the most out of PY4E

The list of all lessons in the course can be found at https://www.py4e.com/lessons. You can skip the first lesson (Installing Python), since we will be using Jupyter Notebook for these exercises.

Here's my recommendation for how to go through each unit in the course:
1. Watch the videos where Dr. Severance goes over all the material. Each unit will generally have 30-60 minutes of lecture videos. The full video playlist is available on [Youtube](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p), and I will link the relevant videos for each unit at the top of each notebook. Some units will also have videos titled "Worked Exercise", but you should skip these for now.
2. Read the textbook chapter. The full textbook is available online as a [PDF](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf). Each chapter is also available as a website, and I will link the relevant chapter at the top of each notebook.
3. Take the quiz for each unit. You will need to sign into the PY4E website using a Google account before you can take the quiz.
4. If you found the quiz difficult, or if you're still uncomfortable with the some of the content, rewatch the videos or reread the textbook.
5. Solve the exercises in Jupyter Notebook! Each exercise will have a problem statement, a space for you to fill in your answer, and a space for the autograder to check your answer. Your goal should be to correctly solve each of the exercises in the unit, and (more importantly) understand why your solutions work.
6. If you're feeling stuck on the exercises, check if Dr. Severance goes over it in one of the "Worked Exercise" videos.
7. Once you've finished everything in one unit, you can move on to the next unit!


# Running the Notebooks

For this project, I've decided to put all of my exercises into an environment called Jupyter Notebook. Jupyter Notebooks are essentially a combination of traditional Python programs and the interactive Python interpreter/shell. If you've never programmed before or if you've only worked in traditional programming environments before, Jupyter Notebooks will be unfamiliar at first, but you will get used to it quickly. The opposite is also true, if you can write code in Jupyter Notebooks, writing code in regular programs will also be easy.

I chose to use Jupyter Notebook for a few reasons. The biggest reason is that Jupyter allows me to combine exercises together much more cleanly than I would have been able to with individual Python files. Additionally, I believe feel that Jupyter is a good environment to learn programming in because of its interactive nature. Finally, practice working with the Jupyter environment is very valuable, especially for students interested in the rising fields of Data Science, Machine Learning, and AI, areas where Jupyter is very commonly used.

There are two ways of running the Jupyter Notebooks in this project - online and offline.

### Online

Using the free services provided by the Binder Project, students can work on all of exercises and access the autograder online, for free! No downloads or registration required.

This is ideal for students who don't have access to a personal computer they can work on, or for students using computers that don't support Python (e.g. Chromebooks, iPads).

**Running Jupyter Notebooks Online:**
1. Go to https://mybinder.org/v2/gh/saumikn/py4e-exercises/HEAD. It may take about a minute or two before your interactive environment is ready to use.
2. Click on one of the notebooks to start solving exercises.
3. When you are finished, click the Download button at the top bar to save your work. 

Note that Binder has a relatively short timeout (providing computing resources is expensive). If you leave your computer for even 10 minutes, you will likely come back to an error message saying `"Connection Failed"`. As long as you don't close your tab, you can follow these [steps](https://discourse.jupyter.org/t/getting-your-notebook-after-your-binder-has-stopped/3268) to restart your notebook without losing any of your changes. 

### Offline

This is what I would recommend most people do.

**Setting up your Offline Environment:**
1. Download [Anaconda](https://www.anaconda.com/products/individual), a program which installs Python and Jupyter for you.
2. Download the exercises and autograder by going to https://github.com/saumikn/py4e-exercises, and clicking Code → Download Zip. Unzip this file.

**Running Jupyter Notebooks Offline:**
1. Open the [Anaconda Prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt), type `jupyter notebook`, and press enter. This should automatically open Jupyter Notebook in your browser.
2. Find the folder where you saved the unzipped file in Jupyter Notebook.
3. Click on one of the notebooks to start solving exercises.
4. When you are finished, save your notebook using File → Save.

# How to use Jupyter

I've created a guide to Jupyter Notebook and solving the exercises at [00-getting-started.ipynb](https://github.com/saumikn/py4e-exercises/blob/main/00-getting-started.ipynb). If you've never used Jupyter before, please open this file in an interactive Jupyter session and follow along so you can start to get comfortable with the tools you'll be using.

# Contact
If you have any questions or comments, feel free to email me at saumik.narayanan@outlook.com. I'd love to hear back from people who found these exercises useful!