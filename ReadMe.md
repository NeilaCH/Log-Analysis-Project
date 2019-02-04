# Logs Analysis Project
 Logs Analysis is a project for the Full Stuck Udacity [Nanodegree program](https://www.udacity.com/nanodegree).
The project consists of creating a reporting tool that prints out reports in text format based on the data in the database of a newspaper site. This database includes three tables (Authors, Articles, Logs).
The reporting tool is a python program based on `psycopg2` module to connect to the database and query the following requests: 
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

# Project Structure
The Logs Analysis project is based on the following files: 
  - `log.py` - is a python program based on `psycopg2` module to connect to the database and query the previously mentioned requests.
  - `result_output.txt` - is a text file that is a copy of the output of the `log.py` program. 

# Installing Requirements
Step 1. Before running The Logs Analysis project you must have the following elements on your machine:
* Python3, you can easily download it [here](https://www.python.org/downloads/).
* Virtual Box,  you can easily download it [here](https://www.virtualbox.org).
* Vagrant, you can easily download it [here] (https://www.vagrantup.com). After Installing vagrant, use your terminal and type `$ vagrant --version` to check if Vagrant is successfully installed.

Step2. Download the Virtual Machine (VM) configuration [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip). After unziping the file, you will get the `fullstack-nanodegree-vm` repository containing the VM files.

Step3. To start your virtual machine (VM), inside your terminal:
* `cd` the `fullstack-nanodegree-vm` repository, then type `ls`.
* `cd`the vagrant/ subdirectory, then type `ls`.
* Run the command `vagrant up` to download and install the Linux operating system.
* Run `vagrant ssh` to log in the virtual machine (VM).

Now your machine is ready to run the Logs Analysis Project.

# Instructions to Run the Project
Step1. Download the Logs Analysis Project and unzip it.
Step2. Copy `log.py` file into `fullstack-nanodegree-vm/vagrant`
Step3. download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it. After that copy the `newsdata.sql` into `fullstack-nanodegree-vm/vagrant`
Step4. In your terminal, run `vagrant@vagrant:~$ cd /vagrant`
Step5. Run `log.py`with this command `vagrant@vagrant:/vagrant$ python log.py` in your terminal.

As result, the terminal will displas the queries defined in the `log.py` file.

### Author
* _Neila CHETTAOUI_

### License

* The [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) used in this porject is provided by [Udacity](https://www.udacity.com).
* The [Virtual Machine (VM) configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) used in this porject is provided by [Udacity](https://www.udacity.com).
