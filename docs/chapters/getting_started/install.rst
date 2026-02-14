Getting access to a programming environment
-------------------------------------------
The tools needed for programming are probably not pre-installed on your computer. You'll need to get access to them before you can carry out the practical aspects of the course. There are a number of different ways in which you can do this, detailed below. You only need to pick **one** of these options.


Approach
^^^^^^^^
In all of the approaches below we try to separate the installation of the tools from the actual computer that you're using. Everybody has a different computer, with different specifications, different operating systems and versions of software. We want our programming environment to be independent of this. This is important when working in larger teams. Again, everyone may have a different physical computer, but everyone working on the same coding project wants to be using the same programming environment. 

We do this by using *containers*. In essence (but this is a simplification) a container is a virtual computer which your actual computer simulates running as if it was a real computer. We can give everyone the same virtual computer for their programming, and it will be the same for everyone, regardless of what physical computer they're using. 

Containers aren't really part of the course, and so you don't need to know anything about them, other than that they'll be used in the background. We mainly us a tool called `Docker <https://www.docker.com/>`_ to run out containers. It just needs to be running in the background, and then we can largely ignore it for the purposes of this course.

We have the option of running our container on your personal computer, in which case we call it a *devcontainer*, or on a computer in the cloud which you access using a web browser, in which case we call it a *codespace*.


Options
^^^^^^^
The options for accessing the tools are:

.. toctree::
   :maxdepth: 1

   install/devcontainer
   install/codespaces
   install/install_locally

Remember, you only need to follow the instructions for one of these. Our recommended approach is to use a :ref:`devcontainer on a personal device <devcontainer>` or a :ref:`codespace on a University cluster computer <codespaces>`.


Using alternative tools
^^^^^^^^^^^^^^^^^^^^^^^
There are lots of different choices for which tools to use for programming. These notes use:

- VSCode to write and debug our programs.
- Git as the version control system to keep track of multiple copies of our program files.
- Python 3.12 or higher, Rust 2024 or newer, Powershell/bash/zsh, clang as a C/C++ compiler.
- Widows as the operating systems (screenshots will be from Windows).

The exact version of each tool should not be critical, but there may be minor differences depending on the exact version you use, and so we provide a route (detailed below) to ensure everyone is using the same versions.

If you choose to use different tools, and there are many different ones to choose from, we'll do our best to support you, but it may be you need to change to using these supported tools. We deliberately use VSCode, for example, because it is open source, cross-platform, and widely used with lots of community support online. Using it on Windows, macOS or Linux should present no problem. Using alternative tools will make it much harder for us to support you - we don't know the intricacies of every possible platform that's out there. 

Remember that tools are very configurable, with lots of different options and customizations available. Don't worry if your set up looks a bit different to the ones in the screenshots used in the teaching materials, as long as it works!

Whichever method you pick, for the in-person exam you should be familiar with how to :ref:`run VSCode on a University computer. <codespaces>` Make sure you take the time to familiarize yourself with this, even if you do most of your coding on a personal device.