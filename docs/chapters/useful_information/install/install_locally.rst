
Installing on your personal computer
------------------------------------

Advantages and disadvantages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advantages:

- Runs locally on your computer. You can thus do coding at home and remotely, at times convent for you.
- Compilation tasks will likely be faster than when using an online or devcontainer option. 

Disadvantages:

- Requires admin permissions on your device.
- Requires installing all of the tools. It can be difficult to get everything to work if the instructions are not followed exactly. (Once set up they should then work without issue.)
- The tools are not version controlled, different computers are likely to have slightly different versions of the same tools installed, and may behave slightly differently as a result. This can make software harder to maintain. 


Process
~~~~~~~
We make use of quite a lot of different tools in the course. We won't give step by step instructions for each, as we recommend using either a :ref:`devcontainer on a personal device <devcontainer>` or a :ref:`codespace on a University cluster computer <codespaces>`. 

#. Install VSCode by following the instructions at `https://code.visualstudio.com/docs/setup/setup-overview`.

#. Install git by following the instructions at `https://git-scm.com/book/en/v2/Getting-Started-Installing-Git`.

#. Install uv by following the instructions at `https://docs.astral.sh/uv/#installation`. This will then install Python for you, there is no need to download Python separately from `https://www.python.org/downloads/`.

#. Install Rust by following the instructions at `https://www.rust-lang.org/tools/install`.

#. Install clang by following the instructions at `https://clang.llvm.org/get_started.html`.

#. Install the VScode extensions as listed in `https://github.com/UOM-EEE-EEEN11202/devcontainer/blob/main/devcontainer.json`. This file also contains some suggested settings for VSCode which you might like to apply. Speak to a demonstrator if you need help with this step.