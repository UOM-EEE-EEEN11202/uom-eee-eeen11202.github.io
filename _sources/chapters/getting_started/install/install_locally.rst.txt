
Installing tools one by one
---------------------------

.. important::

   This isn't our recommended approach for setting up your programming environment. We recommend using a :ref:`devcontainer on a personal device <devcontainer>` or a :ref:`codespace on a University cluster computer <codespaces>`. It can be used as a backup option. 


Advantages and disadvantages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advantages:

- Runs locally on your computer. You can thus do coding at home and remotely, at times convent for you.

Disadvantages:

- Requires admin permissions on your device.
- Requires installing all of the tools. It can be difficult to get everything to work if the instructions are not followed exactly. (Once set up they should then work without issue.)
- The tools are not version controlled, different computers are likely to have slightly different versions of the same tools installed, and may behave slightly differently as a result. This can make software harder to maintain. 


Process
~~~~~~~
We make use of quite a lot of different tools in the course. We won't give step by step instructions for each, as we recommend using either a :ref:`devcontainer on a personal device <devcontainer>` or a :ref:`codespace on a University cluster computer <codespaces>`. 

#. Install VSCode by following the instructions at `<https://code.visualstudio.com/docs/setup/setup-overview>`_.

#. Install git by following the instructions at `<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.

#. Install uv by following the instructions at `<https://docs.astral.sh/uv/#installation>`_. Uv will install Python for you, there is no need to download Python separately from `<https://www.python.org/downloads/>`_.

#. Install Rust by following the instructions at `<https://www.rust-lang.org/tools/install>`_.

#. Install clang by following the instructions at `<https://clang.llvm.org/get_started.html>`_.

#. Install the VScode extensions as listed in `<https://github.com/UOM-EEE-EEEN11202/devcontainer/blob/main/devcontainer.json>`_. This file also contains some suggested settings for VSCode which you might like to apply. Speak to a demonstrator if you need help with this step.

#. Follow the instructions in the GitHub Classroom link to set up your repository at `<https://classroom.github.com/a/y4CMmA_o>`_