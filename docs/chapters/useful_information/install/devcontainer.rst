.. role:: console(code)
   :language: console

.. _devcontainer:

Using a devcontainer
--------------------

This is our recommended method for accessing the required tools. You can read more about `devcontainers in the Part 1 notes <https://uom-eee-eeen11202.github.io/notes-part1/chapters/software_development_tools/environment_control.html>`_ 

Advantages and disadvantages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advantages:

- Runs locally on your computer. You can thus do coding at home and remotely, at times convenient for you.
- The devcontainer hosts the main tools, so you get the correct version of everything, correctly set up. 

Disadvantages:

- Requires admin permissions on your device.
- Still requires installing quite a few things, which needs to be done correctly for it to work. 
- Installs another operating system in the background, and so may need quite a bit of disk space.
- Uses Docker, which can take quite a lot of computer resources.
- Regardless of what your main operating system is, your programming is actually done in Linux.
- VSCode takes a relatively long time to complete its set up each time you start it (typically about a minute).


Setting up the tools and files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We will use the command line to install the required tools. We'll learn about the command line more `in Lab A <https://uom-eee-eeen11202.github.io/notes-part2/chapters/week2/lab_a.html>`_. If you struggle to follow the steps, bring your personal device to the timetabled lab sessions and we will help you install the tools. 

You only need to follow these steps once. 

#. We have made a range of files that help define the settings used in the course. These are stored in GitHub Classroom

   .. admonition:: GitHub Classroom link

      `<https://classroom.github.com/a/y4CMmA_o>`_


   Click this link.
   

#. Sign in to GitHub. If you don't already have an account, or an account using your University of Manchester email address, create one using the link that gets displayed. Follow the instructions on the website.

   .. figure:: ./images/github_signin1.png
      :width: 300
      :align: center
      :alt: GitHub sign in page

   You can use any username that you would like, it doesn't need to be your University one (and it is probably better if it isn't, so you can keep your University username known only to you). 
   
   **You must enter your University of Manchester provided email address. This is needed for everything to work correctly for the assignments.**
	 

#. After entering your details, GitHub will ask you to "Authorize GitHub Classroom". Do this.
	
   .. figure:: ./images/github_signin2.png
      :width: 300
      :align: center
      :alt: GitHub a authorization page

   It can take a minute or two for everything to set up. You may be shown a waiting page. Wait a minute and then refresh the page in your browser.


#. Click on :console:`Accept assignment`.

   .. figure:: ./images/github_accept_lab.png
      :width: 300
      :align: center
      :alt: GitHub a accept assignment page	

   
#. Once you've accepted the assignment, you'll be taken to a :console:`You're ready to go!` page, as shown below. 

   .. figure:: ./images/github_ready.png
      :width: 800
      :align: center
      :alt: The GitHub ready to go page

   This includes a web address. **Make a note of this, as you'll need it later.** 
   
   The link will be something like `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB`. Your address will be individual to you, depending on what your GitHub username is.


#. Now follow the instructions below for your operating system.

.. tab-set::
    :sync-group: os

    .. tab-item:: :fab:`windows` Windows
        :sync: key1


        #. Use the start menu to open *PowerShell*.

        .. figure:: ./images/start_powershell.png
           :width: 300
           :align: center
           :alt: A Windows start menu search for the PowerShell app

        
        #. Enter the commands below, one at a time. Remember, :console:`>` shows the prompt (i.e. where to enter the commands). It is displayed by PowerShell, you don't need to enter it yourself.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address your address that you noted down above.
           - Replace :console:`C:\Users\alex\OneDrive - The University of Manchester\eeen11202` with the folder where you want to store your code on your computer. We recommend that this is in your University provided OneDrive folder, so that your code is automatically backed up online and available on any University computer where you're signed in to OneDrive. **Make a note of this location, you will need it later.**

           .. prompt::
              :language: powershell

              $env:MY_GITHUB_ADDRESS = 'https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB'
              $env:EEEN11202_FOLDER = 'C:\Users\alex\OneDrive - The University of Manchester\eeen11202'
              winget install -e --id Microsoft.VisualStudioCode
              winget install -e --id Docker.DockerDesktop
              winget install -e --id Git.Git
              New-Item -ItemType Directory -Path $env:EEEN11202_FOLDER -Force
              Set-Location -Path $env:EEEN11202_FOLDER
              git clone --recurse-submodules -j8 $env:MY_GITHUB_ADDRESS



    .. tab-item:: :fab:`apple` macOS
        :sync: key2


        #. Start the :console`Terminal` application. You can find this using Spotlight Search (the magnifying glass icon at the top right of your screen).


        #. Enter the commands below, one at a time. Remember, :console:`$` shows the prompt (i.e. where to enter the commands). It is displayed by the terminal, you don't need to enter it yourself.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address your address that you noted down above.
           - Replace :console:`/Users/alex/OneDrive - The University of Manchester/eeen11202` with the folder where you want to store your code on your computer. We recommend that this is in your University provided OneDrive folder, so that your code is automatically backed up online and available on any University computer where you're signed in to OneDrive. **Make a note of this location, you will need it later.**

           .. prompt::
              :language: bash

              GITHUB_ADDRESS="https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB"
              EEEN11202_FOLDER="/Users/alex/OneDrive - The University of Manchester/eeen11202"
              /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
              brew install --cask visual-studio-code
              brew cask install docker
              brew install git
              mkdir -p $EEEN11202_FOLDER
              cd $EEEN11202_FOLDER
              git clone --recurse-submodules -j8 $GITHUB_ADDRESS


    .. tab-item:: :fab:`linux` Linux
        :sync: key3


        #. Start the :console`Terminal` application.


        #. Enter the commands below, one at a time. Remember, :console:`$` shows the prompt (i.e. where to enter the commands). It is displayed by the terminal, you don't need to enter it yourself.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           - These instructions assume a Debian based Linux distribution such as Ubuntu. 
           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address your address that you noted down above.
           - Replace :console:`/home/alex/OneDrive - The University of Manchester/eeen11202` with the folder where you want to store your code on your computer. We recommend that this is in your University provided OneDrive folder, so that your code is automatically backed up online and available on any University computer where you're signed in to OneDrive. **Make a note of this location, you will need it later.**

           .. prompt::
              :language: bash

              GITHUB_ADDRESS="https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB"
              EEEN11202_FOLDER="/home/alex/OneDrive - The University of Manchester/eeen11202"
              sudo apt update
              sudo apt install software-properties-common apt-transport-https wget
              wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
              sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
              sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
              sudo apt update
              sudo apt install code
              sudo apt install curl ca-certificates
              curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
              echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
              sudo apt update
              sudo apt install docker-ce -y
              sudo usermod -aG docker $USER
              newgrp docker
              sudo apt-get install git-all
              mkdir -p $EEEN11202_FOLDER
              cd $EEEN11202_FOLDER
              git clone --recurse-submodules -j8 $GITHUB_ADDRESS


Starting the programming environment the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You'll need to follow the steps below each time you start programming. 

#. Open VSCode from the Start Menu (Windows) or equivalent on your operating system.

   .. figure:: ./images/start_vscode.png
      :width: 300
      :align: center
      :alt: Starting VSCode from the Windows start menu


#. On the welcome screen, click on :console:`Open folder...`. 

   .. figure:: ./images/vscode_open_folder.png
      :width: 800
      :align: center
      :alt: Opening a folder in VSCode


#. Navigate to the the folder location you chose above (e.g. :console:`C:\Users\alex\OneDrive - The University of Manchester\eeen11202` on Windows). This will contain another folder called :console:`labs-ALEX-CASSON-LAB` (with your GitHub username instead of `ALEX-CASSON-LAB`). Select this folder and click :console:`Select Folder`.

   .. figure:: ./images/vscode_select_folder.png
      :width: 800
      :align: center
      :alt: Selecting a folder in VSCode


#. This will display a :console:`Reopen in Container` prompt. Select :console:`Reopen in Container`. If the prompt disappears (it is only displayed for a few seconds) you can click on the blue arrows in the bottom left corner to bring up the option again.  

   .. figure:: ./images/vscode_reopen_in_container.png
      :width: 800
      :align: center
      :alt: Opening the devcontainer in VSCode

#. This will detect that a :console:`workspace` is present. Select :console:`Open Workspace`. 

   .. figure:: ./images/vscode_open_workspace.png
      :width: 800
      :align: center
      :alt: Opening a workspace in VSCode

   If the prompt disappears (it is only displayed for a few seconds) you can select :console:`File / Open Workspace from File...` and select the eeen11202-labs.code-workspace file that you'll find in your :console:`labs-ALEX-CASSON-LAB` folder equivalent. 

   .. figure:: ./images/vscode_file_open_workspace.png
      :width: 800
      :align: center
      :alt: Opening a workspace in VSCode via the file menu


#. When done your VSCode will look like the below. Note that in the bottom left hand corner it says it's connected to a Dev Container. In the explorer, each lab is listed using upper case letters (e.g. Lab A rather than lab_a) and it says workspace at the top. If you don't have these, you've missed a step. 

   .. figure:: ./images/vscode_final.png
      :width: 800
      :align: center
      :alt: VSCode fully set up


Starting the programming environment subsequent times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are quite a few steps in the above! That is because we've opened both a devcontainer and a workspace. 

Once you've started VSCode correctly once, it will remember the configuration. On the VSCode welcome page you should see an eeen11202 workspace and devcontainer option in the :console:`Recent` list. You can just select this and it will re-load the setup in a single step. 

   .. figure:: ./images/vscode_recents.png
      :width: 800
      :align: center
      :alt: Using the recents list to reload the configuration


.. admonition:: Note

   The above steps actually do two steps:

   #. They set up a programming environment with a range of settings that we've pre-chosen and configured.
   #. They copied the files we'll use in the labs. 

   The lab files are specific to this course, whereas the programming environment and settings may be of use in your own programming projects or other courses. 
   
   To help with this we've made another starting link in GitHub Classroom. If you use the link below, and follow the same steps as above, it will create a blank programming environment for you. You can use this when starting your own projects. 

    `<https://classroom.github.com/a/daa5PxEI>`_