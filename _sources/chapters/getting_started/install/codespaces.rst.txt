.. role:: console(code)
   :language: console

.. _codespaces:

Using VSCode online with codespaces
-----------------------------------

Advantages and disadvantages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advantages:

- Runs online. You thus don't need to install anything, and can do coding at home and remotely, at times convenient for you.

Disadvantages:

- Requires you to be online, and may be relatively slow compared to a local install. 
- Uses `GitHub codespaces <https://classroom.github.com/>`_, which by default allows 60 hours per month of free use. This should be sufficient to complete the course, but you may find limiting. If you verify your student status with GitHub they will increase your limit to 180 free hours per month. Full details are `here <https://education.github.com/discount_requests/application>`_.
- VSCode takes a relatively long time to complete its set up each time you start it (typically about a minute).


Setting up the tools and files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You only need to follow these steps once. 

#. We have made a range of files that help define the settings used in the course. These are stored in GitHub Classroom. The GitHub Classroom link is on `Canvas <https://canvas.manchester.ac.uk/>`_ in the Week 2 module. Click on this link.

   .. admonition:: Note

      We recommend using GitHub classroom via the link provided in Canvas for the best experience. You only need to access this once to do the initial setup. If you can't access Canvas, you can follow the :ref:`instructions instructions <git_clone_codespaces>` to clone the required files from GitHub directly. You can then skip to :ref:`Starting the programming environment the first time <starting_codespace_subsequent_times>`.


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


   This includes a web address. **Make a note of this, as you'll need it to return to your files later.**

   The link will be something like `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB`. Your address will be individual to you, depending on what your GitHub username is.


Starting the programming environment the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click on :console:`Open with Codespaces`

   .. figure:: ./images/github_start_codespace.png
      :width: 800
      :align: center
      :alt: Starting a new codespace from GitHub

      Screenshot of GitHub, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. Click on :console:`Open Workspace`

   .. figure:: ./images/github_open_workspace.png
      :width: 800
      :align: center
      :alt: Opening the workspace in GitHub

      Screenshot of GitHub Codespace, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. Wait while the setup completes. It can take a minute. When done your codespace will look like the below. Note that in the bottom left hand corner it says Codespace. In the explorer, each lab is listed using upper case letters (e.g. Lab A rather than lab-a) and it says workspace at the top. If you don't have these, you've missed a step. 

   .. figure:: ./images/github_codespace_final.png
      :width: 800
      :align: center
      :alt: The Codespace setup in GitHub

      Screenshot of GitHub Codespace, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


Stopping a Codespace
~~~~~~~~~~~~~~~~~~~~

.. danger::

    A :console:`Codespace` is a virtual computer that runs on the Internet. GitHub give you 60 hours per month for free of using this online computer. This is enough for this course. The course is expected to take approximately 200 hours in total, and is spread over several months.

    **Make sure you close your Codespace when you're not using it!** Otherwise you may run out of free time.
    
    Optionally you can verify your student status with GitHub they will increase your limit to 180 free hours per month. There is no need to verify with GitHub, but if you would like to `follow the instructions online <https://education.github.com/discount_requests/application>`_. 

    If you run out of time with GitHub Codespaces, speak to a demonstrator before taking any other actions.

To pause or stop a Codespace when you reach the end of a coding session:


#. In the top left of the VSCode window click on the :console:`hamburger` icon and select :console:`My Codespaces`.

   .. figure:: ./images/github_stop_codespace.png
      :width: 800
      :align: center
      :alt: Stopping a Codespace from the VSCode menu

      Screenshot of GitHub Codespace, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


#. In the web page that appears, click on your repository and find your Codespace. In the figure below it is :console:`Redesigned pancake`. Yours will have a different randomly assigned name. Click on the :console:`...` menu next to it and select :console:`Stop codespace`. 

   .. figure:: ./images/github_stop_codespace2.png
      :width: 800
      :align: center
      :alt: Stopping a Codespace

      Screenshot of GitHub Codespace, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


.. danger::

    If you just close your web browser or tab, the Codespace will keep running in the background, and will continue to use up your free hours. Make sure you explicitly stop it as above. 
    
    The Codespace will automatically stop after a period of inactivity, with the default set at 4 hours. We suggest that you follow `these GitHub instructions <https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces>`_ to reduce the timeout to a smaller value.


.. _starting_codespace_subsequent_times:

Starting the programming environment subsequent times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Earlier you made note of a web address. This was something like, `https://github.com/UOM-EEE-EEEN11202-LABS/labs-ALEX-CASSON-LAB` with the ending different depending on your GitHub username. 

   Return to this address in the browser. 


#. You'll see your files stored on the cloud. 

   Click on :console:`Code` and then :console:`Codespaces` then the name of your Codespace. In the figure below it is :console:`Redesigned pancake`. Yours will have a different randomly assigned name.

   .. figure:: ./images/github_start_codespace_from_repo.png
      :width: 800
      :align: center
      :alt: Starting a Codespace from a GitHub repository

      Screenshot of GitHub Codespace, software from `Microsoft <https://github.com/>`_. See `course copyright statement <https://uom-eee-eeen11202.github.io/chapters/about/copyright>`_.


.. _git_clone_codespaces:

.. admonition:: Note

   The above steps actually do two steps:

   #. They set up a programming environment with a range of settings that we've pre-chosen and configured.
   #. They copied the files we'll use in the labs. 

   The lab files are specific to this course, whereas the programming environment and settings may be of use in your own programming projects or other courses. 
   
   To help with this we've also made a blanks starting repository, which has the settings we use but not the files. You can use the command below when starting your own projects to keep using the programming environment and settings that we use in this course. 

   .. tab-set::
      :sync-group: os

      .. tab-item:: :fab:`windows` Windows
         :sync: key1

         Make a new repository on GitHub and make a note of the address. Then enter:

         .. prompt::
            :language: powershell

            git clone --recurse-submodules -j8 https://github.com/UOM-EEE-EEEN11202/blank-development-folder my_project_name
            git remote set-url origin <NEW_GIT_URL_HERE>

      .. tab-item:: :fab:`apple` macOS
         :sync: key2

         Make a new repository on GitHub and make a note of the address. Then enter:

         .. prompt::
            :language: bash

            git clone --recurse-submodules -j8 https://github.com/UOM-EEE-EEEN11202/blank-development-folder my_project_name
            git remote set-url origin <NEW_GIT_URL_HERE>

      .. tab-item:: :fab:`linux` Linux
         :sync: key3

         Make a new repository on GitHub and make a note of the address. Then enter:

         .. prompt::
            :language: bash

            git clone --recurse-submodules -j8 https://github.com/UOM-EEE-EEEN11202/blank-development-folder my_project_name
            git remote set-url origin <NEW_GIT_URL_HERE>