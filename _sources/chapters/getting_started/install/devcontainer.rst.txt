.. role:: console(code)
   :language: console

.. _devcontainer:

Using a devcontainer
--------------------

This is our recommended method for accessing the required tools. You can read more about `devcontainers in the Part 1 notes <https://uom-eee-eeen11202.github.io/notes-part1/chapters/software_development_tools/environment_control.html>`_. 

.. admonition:: Key points

   - You need to install the required software.
   - You need to download the pre-made files for this course from GitHub.
   - In VSCode you need to attach to the devcontainer.
   - In VSCode you need to open the workspace file.
   - The container runs Linux. You should follow the Linux instructions in the labs, even if your main operating system is Windows or macOS.


Setting up the tools and files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We will use the command line to install the required tools. We'll learn about the command line more `in Lab A <https://uom-eee-eeen11202.github.io/notes-part2/chapters/week2/lab_a.html>`_. If you struggle to follow the steps, bring your personal device to the timetabled lab sessions and we will help you install the tools. 

You only need to follow these steps once. 

#. We have made a range of files that help define the settings used in the course. These are stored in GitHub Classroom. The GitHub Classroom link is on `Canvas <https://canvas.manchester.ac.uk/>`_ in the Week 2 module. Click on this link.

#. Sign in to GitHub. If you don't already have an account, or an account using your University of Manchester email address, create one using the link that gets displayed. Follow the instructions on the website.

   .. figure:: ./images/github_signin1.png
      :width: 300
      :align: center
      :alt: GitHub sign in page

      Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.

   You can use any username that you would like, it doesn't need to be your University one (and it is probably better if it isn't, so you can keep your University username known only to you). 
   
   **You must enter your University of Manchester provided email address. This is needed for everything to work correctly for the assignments.**
	 

#. After entering your details, GitHub will ask you to "Authorize GitHub Classroom". Do this.
	
   .. figure:: ./images/github_signin2.png
     :width: 300
     :align: center
     :alt: GitHub a authorization page
     
     Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


   It can take a minute or two for everything to set up. You may be shown a waiting page. Wait a minute and then refresh the page in your browser.


   .. admonition:: Bug

      Some people are presented with a :console:`Repository Access Issue` page due to a bug in GitHub classroom. 

      .. figure:: ./images/github_access_issue.jpg
         :width: 800
         :align: center
         :alt: GitHub a accept assignment page	

         Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.

      If you get this: Do one of:
         
      - View `this video <https://office.kingma.ch/s/5WxeNMf2EJxfay4?dir=/&editing=false&openfile=true>`_ which shows you how to fix it. Select the EEEN11202 organization. 
      - Go directly to your repositories page on GitHub: https://github.com/UOM-EEE-EEEN11202-LABS/labs-a-j-USERNAME where you replace USERNAME with your GitHub username. 


#. Click on :console:`Accept assignment`.

   .. figure:: ./images/github_accept_lab.png
      :width: 800
      :align: center
      :alt: GitHub a accept assignment page	

      Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.

   
#. Once you've accepted the assignment, you'll be taken to a :console:`You're ready to go!` page, as shown below. 

   .. figure:: ./images/github_ready.png
      :width: 800
      :align: center
      :alt: The GitHub ready to go page

      Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.

   This includes a web address. **Make a note of this, as you'll need it later.** 
   
   The link will be something like `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB`. Your address will be individual to you, depending on what your GitHub username is.

.. _download_files:

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

           Screenshot of Windows start menu, software from `Microsoft <https://www.microsoft.com/en-gb/windows>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.

        
        #. Enter the commands below, one at a time. Remember, :console:`>` shows the prompt (i.e. where to enter the commands). It is displayed by PowerShell, you don't need to enter it yourself. These commands install the software we'll use.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           
           .. prompt::
              :language: powershell

              winget install -e --id Microsoft.VisualStudioCode
              winget install -e --id Docker.DockerDesktop
              winget install -e --id Git.Git
              wsl --install

        #. You will be asked to reboot the computer. Do this.

           .. admonition:: Aside
              :class: dropdown

              This uses the `Windows Subsystem for Linux (WSL) <https://docs.microsoft.com/en-us/windows/wsl/about>`_ backend, which is available on Windows Home and Windows Pro. If you are running Windows Pro, you can also use the `Hyper-V <https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/>`_ backend. Both work equally well for this course.

        #. Start Docker using the Start Menu. This will display a set of terms and agreemtns. Read, and then if happy accept the terms and agreements. 
        
        #. You may be asked to sign in to Docker Hub. You can skip this step by clicking :console:`Skip`.

        #. Enter the commands below, one at a time. These commands download the pre-made files we've made for the course, and install an extension in VSCode.

           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address that you noted down above.
           - Replace :console:`C:\\Users\\alex\\OneDrive - The University of Manchester\\eeen11202` with the folder where you want to store your code on your computer. We recommend that this is in your University provided OneDrive folder, so that your code is automatically backed up online and available on any University computer where you're signed in to OneDrive. **Make a note of this location, you will need it later.**

           .. prompt::
              :language: powershell

              code --install-extension ms-vscode-remote.remote-containers
              $env:MY_GITHUB_ADDRESS = 'https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB'
              $env:EEEN11202_FOLDER = 'C:\Users\alex\OneDrive - The University of Manchester\eeen11202'
              New-Item -ItemType Directory -Path $env:EEEN11202_FOLDER -Force
              Set-Location -Path $env:EEEN11202_FOLDER
              git clone --recurse-submodules -j8 $env:MY_GITHUB_ADDRESS



    .. tab-item:: :fab:`apple` macOS
        :sync: key2


        #. Start the :console:`Terminal` application. You can find this using Spotlight Search (the magnifying glass icon at the top right of your screen).

        #. Install :console:`Homebrew` by entering the command below. This is a package manager that makes it easy to install software on macOS.

           .. prompt::

              /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

           When the installation completes the terminal will display some instructions. Follow these instructions to complete the installation before moving on to the next step.

        #. Generate a :console:`Personal Access Token` on GitHub. 
           
           #. Go to GitHub. Click on your profile picture in the top right and then :console:`Settings`.

           #. Click on :console:`Developer settings` in the left hand menu, at the very bottom. 
           
           #. Click on :console:`Personal access tokens` and then :console:`Tokens (classic)`.

           #. Click on :console:`Generate new token` and then :console:`Generate new token (classic)`.

           #. Add a name for your token in the :console:`Note` box.
           
           #. Set the expiration to a date after the end of the course.

           #. Tick the :console:`repo` box to give the token permissions to access your repositories. This will tick all of the boxes under :console:`repo`. You can leave all other categories unticked.

           #. Click :console:`Generate token` at the bottom of the page.

           #. This will generate a password, around 40 characters long. **You will need this later.** 

        #. Enter the commands below, one at a time. Remember, :console:`$` shows the prompt (i.e. where to enter the commands). It is displayed by the terminal, you don't need to enter it yourself.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address that you noted down above.
           - Replace :console:`/Users/alex/OneDrive - The University of Manchester/eeen11202` with the folder where you want to store your code on your computer. We recommend that this is in your University provided OneDrive folder, so that your code is automatically backed up online and available on any University computer where you're signed in to OneDrive. **Make a note of this location, you will need it later.**
           - When you run the :console:`git clone` command, it will ask you for your GitHub username and password. For the username, enter your GitHub username. For the password, enter the Personal Access Token that you generated in the previous step.

           .. prompt::
              :language: bash

              GITHUB_ADDRESS="https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB"
              EEEN11202_FOLDER="/Users/alex/OneDrive - The University of Manchester/eeen11202"
              brew install --cask visual-studio-code
              code --install-extension ms-vscode-remote.remote-containers
              brew install --cask docker
              brew install git
              mkdir -p $EEEN11202_FOLDER
              cd $EEEN11202_FOLDER
              git clone --recurse-submodules -j8 $GITHUB_ADDRESS
              sed -i '' 's/\/\///' `basename $GITHUB_ADDRESS`/.devcontainer/devcontainer.json

        #. Start Docker. This will display a set of terms and agreemtns. Read, and then if happy accept the terms and agreements. 
        
        #. You may be asked to sign in to Docker Hub. You can skip this step by clicking :console:`Skip`.

    .. tab-item:: :fab:`linux` Linux
        :sync: key3


        #. Start the :console:`Terminal` application.


        #. Enter the commands below, one at a time. Remember, :console:`$` shows the prompt (i.e. where to enter the commands). It is displayed by the terminal, you don't need to enter it yourself.
        
           - You may be asked to enter some information during the installation, and some graphical items may be displayed. Enter any needed information and press Enter to proceed.
           - Let each command complete before moving on to the next.
           - These instructions assume a Debian based Linux distribution such as Ubuntu. 
           - Replace `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the web address that you noted down above.
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
              code --install-extension ms-vscode-remote.remote-containers
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

#. Start Docker using the Start Menu (Windows) or equivalent on your operating system.. You can close the main window, Docker just needs to be running in the background. 

#. Open VSCode from the Start Menu (Windows) or equivalent on your operating system.

   .. figure:: ./images/start_vscode.png
      :width: 300
      :align: center
      :alt: Starting VSCode from the Windows start menu

      Screenshot of Windows start menu, software from `Microsoft <https://www.microsoft.com/en-gb/windows>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.
      

#. The first time you open VSCode it will let you change some of the default settings. We suggest that you turn on GitHub Copilot, and otherwise choose whichever settings you prefer. You can always change these later. 

#. On the welcome screen, click on :console:`Open folder...`. 

   .. figure:: ./images/vscode_open_folder.png
      :width: 800
      :align: center
      :alt: Opening a folder in VSCode

      Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. Navigate to the the folder location you chose above (e.g. :console:`C:\\Users\\alex\\OneDrive - The University of Manchester\\eeen11202` on Windows). This will contain another folder called :console:`labs-ALEX-CASSON-LAB` which has been downloaded automatically from GitHub for you (with your GitHub username instead of `ALEX-CASSON-LAB`). It contains a number of pre-made files and settings that we'll use in the labs.

   Select this folder and click :console:`Select Folder`.

   .. figure:: ./images/vscode_select_folder.png
      :width: 800
      :align: center
      :alt: Selecting a folder in VSCode

      Screenshot of Windows file dialog, software from `Microsoft <https://www.microsoft.com/en-gb/windows>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. This will display a :console:`Reopen in Container` prompt. Select :console:`Reopen in Container`. If the prompt disappears (it is only displayed for a few seconds) you can click on the blue arrows in the bottom left corner to bring up the option again.  

   .. figure:: ./images/vscode_reopen_in_container.png
      :width: 800
      :align: center
      :alt: Opening the devcontainer in VSCode

      Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. This will detect that a :console:`workspace` is present. Select :console:`Open Workspace`. 

   .. figure:: ./images/vscode_open_workspace.png
      :width: 800
      :align: center
      :alt: Opening a workspace in VSCode

      Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


   If the prompt disappears (it is only displayed for a few seconds) you can select :console:`File / Open Workspace from File...` and select the :console:`eeen11202-labs.code-workspace` file that you'll find in your :console:`labs-ALEX-CASSON-LAB` folder equivalent. 

   .. figure:: ./images/vscode_file_open_workspace.png
      :width: 800
      :align: center
      :alt: Opening a workspace in VSCode via the file menu

      Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. When done your VSCode will look like the below. Note that in the bottom left hand corner it says it's connected to a Dev Container. In the explorer, each lab is listed using upper case letters (e.g. Lab A rather than lab-a) and it says workspace at the top. If you don't have these, you've missed a step. 

   .. figure:: ./images/vscode_final.png
      :width: 800
      :align: center
      :alt: VSCode fully set up

      Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


Starting the programming environment subsequent times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are quite a few steps in the above! That is because we've opened both a devcontainer and a workspace. 

#. Start Docker using the Start Menu. You can close the main window, Docker just needs to be running in the background. 

#. Once you've started VSCode correctly once, it will remember the configuration. On the VSCode welcome page you should see an eeen11202 workspace and devcontainer option in the :console:`Recent` list. You can just select this and it will re-load the setup in a single step.

.. figure:: ./images/vscode_recents.png
   :width: 800
   :align: center
   :alt: Using the recents list to reload the configuration

   Screenshot of VSCode, software from `Microsoft <https://code.visualstudio.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.