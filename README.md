# Welcome to Arman Behnam Finance repository

Here are some courses that I've shared with U to help broaden our knowledge.
Courses are categorized into four parts: [Coursera](https://www.coursera.org/learn/convolutional-neural-networks), [Udemy](https://www.udemy.com/), [Udacity](https://www.udacity.com/), [Interdisciplinary schools](https://github.com/ArmanBehnam/Courses/tree/master/Interdisciplinary%20schools%20-%20Neuroscience)

`Sharing Lnowledge` is a **sacred** job and I'll appreciate this repository will be useful.(Especially in the field of AI and Data science)


- Reach my [Coursera](https://github.com/ArmanBehnam/Courses/tree/master/Coursera) experience
  - Courses:  Hundreds of free courses give you access to on-demand video lectures, homework exercises, and community discussion forums. Paid courses provide additional quizzes and projects as well as a shareable Course Certificate upon completion.
  - Guided Projects: are self-paced, require a smaller time commitment, and provide practice using tools in real-world scenarios, so you can build the job skills you need, right when you need them.
  - Specializations: tackle hands-on projects based on real business challenges, and earn a Specialization Certificate to share with your professional network and potential employers.
- Reach my [Udemy](https://github.com/ArmanBehnam/Courses/tree/master/Udemy) experience
- The leading global marketplace for learning and instruction; by connecting students all over the world to the best instructors, Udemy is helping individuals reach their goals and pursue their dreams.
- Reach my [Udacity](https://github.com/ArmanBehnam/Courses/tree/master/Udacity) experience
  - Learn by doing
  - Practitioner-level skills
  - Job-focused content
  - Real human help
  - Personalized code reviews
  - Real-life projects
- Reach my [Interdisciplinary schools](https://github.com/ArmanBehnam/Courses/tree/master/Interdisciplinary%20schools%20-%20Neuroscience) experience
  - Analysis and discussing [Neuroscience and Cognitive science](http://www.armanbehnam.com/about-me/education/information/neuroscience/) in my website

# THANK YOU
# Finance Repo

Contains all the Jupyter Notebooks used.

All of the research I do in these notebooks is on the full tick history dataset.

I do provide a 2 year sample on tick, volume, and dollar bars to help the community get started. 

## Contributing

Our hope is that the sample data and notebooks will enable the community to build on the research and contribute to the open source community. 

A good place to start for new users is to use the data provided to answer the questions at the back of the chapters in Advances in Financial Machine Learning.

Please review the [Guidelines](https://github.com/ArmanBehnam/Finance/blob/master/Guidelines.md) for research

### Sample Data

The following [folder](https://github.com/ArmanBehnam/Finance/tree/master/Sample-Data) contains 2 years sample data on S&P500 Emini Futures, for the period 2015-01-01 to 2017-01-01.

Specifically the following data structures:
* Dollar Bars: Sampled every $70'000
* Volume Bars: Sampled every 28'000 contracts
* Tick Bars: Sampled every 2'800 ticks

## Installation

Recommended versions:
* Anaconda 3
* Python 3.6

### Installation for Mac OS X and Ubuntu Linux

1. Make sure you install the latest version of the Anaconda 3 distribution. To do this you can follow the install and update instructions found on this link: https://www.anaconda.com/products/individual
2. Launch a terminal
3. Create a New Conda Environment. From terminal: ```conda create -n <env name> python=3.6 anaconda``` accept all the requests to install.
4. Now activate the environment with ```source activate <env name>```.
5. From Terminal: go to the directory where you have saved the file, example: cd Desktop/research/.
6. Install Python requirements, by running the command: ```pip install -r requirements.txt```
7. (Optional) Continue to Chapter-specific Installation 

### Installation for Windows

1. Download and install the latest version of [Anaconda 3](https://www.anaconda.com/products/individual)
2. Launch Anaconda Navigator
3. Click Environments, choose an environment name, select Python 3.6, and click Create
4. Click Home, browse to your new environment, and click Install under Jupyter Notebook
5. Launch Anaconda Prompt and activate the environment: ```conda activate <env name>```
6. From Anaconda Prompt: go to the directory where you have saved the file, example: cd Desktop/research/.
7. Install Python requirements, by running the command: ```pip install -r requirements.txt```
8. (Optional) Continue to Chapter-specific Installation 

### Chapter-specific Installation

We will create a symlink inside each of the Chapters for ease of dataset changes. You may change the symlink of `official_data` to your own dataset rather than using the 2 year sample; the format follows Tick Data LLC.

Create a symbolic link inside the Chapter folder to where you saved the official data:

``` cd Chapter3; ln -s ../Sample-Data official_data ```

## Additional Research Repo
BlackArbsCEO has a great repo based on de Prado's research. It covers many of the questions at the back of every chapter and was the first source on Github to do so. It has also been a good source of inspiration for our research.

* [Adv Fin ML Exercises](https://github.com/BlackArbsCEO/Adv_Fin_ML_Exercises)
