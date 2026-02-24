Introduction
============

Welcome to **EEEN11202 Programming and software development**!

This is a first year undergraduate course that introduces students to both general purpose programming for task automation and data analysis (mainly using Python), and higher performance programming (mainly using Rust). We also cover software development processes, such as version control, to help students write secure, maintainable code. 

The course includes some of the theory behind how computers operate, both hardware and software. We go far enough into this for understanding parts of our code which are written a particular way, due to how the hardware and software of a computer works. 

EEEN11202 is an open source in-person course, run at the University of Manchester for students in Electrical and Electronic Engineering. Students enrolled at the University will have a number of timetabled lecture sessions to go over the material, and lab sessions to practice coding and get one-on-one help. 

These course notes are your main guide through the course. They are split into 4 parts.

- `Part 0 (this part) on course administration <https://uom-eee-eeen11202.github.io/>`_. These overview the course administration: the intended learning outcomes and other information needed to work through the course. The notes also provide information on how to install a suitable programming environment for using with the course.

- `Part 1 on underlying theory of how computers operate and how we program them <https://uom-eee-eeen11202.github.io/notes-part1/>`_. Computers work in a particular way, and we need to know some details about the ways in which they work in order to write good programs. We don't need to know everything about how a computer works, but when programming we'll quickly find we can't treat them as a *black box*, and need to know a little about what's going on in order to understand our programs. This includes learning about common programming and software engineering techniques to give some background before you try the techniques in practice.

- `Part 2 on general purpose computing, mainly with Python <https://uom-eee-eeen11202.github.io/notes-part2/>`_. These cover automating tasks on a computer, and using programming to analyze and explore and visualize data. We'll mainly use Python for this, as a very widely used programming language, but will also look briefly at *Shell Scripting* as as a method built in to most operating systems. 

- `Part 3 on higher performance computing, mainly with Rust <https://uom-eee-eeen11202.github.io/notes-part3/>`_. These cover writing programs that can run more quickly. This may be because we're writing a large program which takes a long time to run, or because we only have limited computing resources available, or some other reason. In general, Python is a great tool for writing programs quickly, but they tend to execute relatively slowly. We thus use other languages when high performance computing starts to become more important. Here we're going to look mainly at a language called Rust, but we'll also look briefly at C and C++ as widely used languages.

**To access the links below you will need to signed in to Canvas using your University of Manchester email address.**

For ease of access we've grouped the assignments together into two parts:

- `Assignments A to J <https://canvas.manchester.ac.uk/courses/45995/modules/items/3999270>`_. These assignments relate to the labs in `Part 2 of the course <https://uom-eee-eeen11202.github.io/notes-part2/>`_.

- `Assignments K to T <https://fluffy-adventure-qm5zj92.pages.github.io/>`_. These assignments relate to the labs in `Part 3 of the course <https://uom-eee-eeen11202.github.io/notes-part3/>`_. These will be released later in the course.

The contents of Part 0 of the notes are:

.. toctree::
   :maxdepth: 1
   :numbered:
   :includehidden:

   0. Introduction <self>
   chapters/course_administration
   chapters/course_policies
   chapters/getting_started
   chapters/about
