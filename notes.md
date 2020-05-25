# Notes
> 16 May 2020 20:20
Restructuring the project because of concurrency and Parallelism.
The program will start spawning threads when it hit the git clone phase.
What I need to do is to rewrite the program to do the following:

- Start getting all the repositories from github
- start spawning threads for easy of the repositories that are found
  - each thread will check if it exists locally (done)
  - each thread will start cloning the repo it it's not found locally (done)
  - when a thread is done it should be disposed of automatically