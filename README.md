[![CC BY-NC-ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International][cc-by-nc-nd].

[![CC BY-NC-ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

[cc-by-nc-nd]: https://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY%20NC%20ND%204.0-lightgrey.svg

Build locally with
uv run sphinx-build docs docs/_build

## TODO:
- Affiliate search
- READMEs for repos
- Check force push rules
- Fix links to use intersphinx
- Pre-build devcontainer?
- Lab A make into numbered list
- Update Lab B screenshots to use workspace
- Update early screenshots to use kebab case
- Increase space between items in numbered list
- Add more quantification to the programming motivation.
- Add fetch to git
- Add wrappers/Result<T,E> to data types
- Add structs/enums to data types?
- Extend AI tools section with example prompts
- Check all images for dark mode
- Fix JSON light mode text
- UPdate terminals in Lab A
- Improve object description
- Add common mistakes/hard coding page
- Fix space between k Ohm
- Icons for GUI/CLI tabs in Labs A/B/C
- Fix code syntax in quizdown
- Update Lab B screenshot with Ruff formatted code
- Lab E, get equations aligned
- Move github classroom instructions to single page
- Split dev container settings and course specific settings
- Update theme folders to use kebab case. Same for gradescope docker (in name and folder names). Same for codelens.
- Add logs folder to Lab C
- Add consistent lab setup page at start of each lab.
- Fix tau display for plotly
- Make LaTeX labels in plots work (both plotly and matplotlib)
- Matplotlib and plotly icons in dark mode (lab f)
- Matplotlib fix font size!
- Switch from seaborn to scieceplots?
- Lab F, switch plotly pie chart example to use np.histogram?
- Lab F, add polars time series example with aboslute times
- Add rainbow csv to devcontainer?
- Lab E/F change np.arange to np.linspace
- Lab F add legend to moving average filter graph
- Somewhere: Pathlib, Input arguments
- Part 1: add note on while(1) in operating systems saying can give random delays
- Improve Lab I - presumably can do testing as 1 batch rather than each image seperately in loop
- Lab I make a better model performance vs. training time trade-off
- Lab I split test loop and performance metrics into different functions
- Update theme to allow text as a code block. Current makes text white. Then update assignment J to use text code block
- Assignments A-J remove extra full stop in the part 2 notes.
- Upadte mdbook theme to support v0.5
- Week 7/intro to Part 3. Make TOCs automatic
- mdbook fix figure widths
- mdbook have $ in console not picked up
- mdbook get icons in tabs
- Add signed/unsigned integers in part 1. Common names for then uint8, i8, etc
- Add f64, f32 to floats page in part 1
- mdbook theme: fix aside font when on default
- Part 1: rename environemtn control to be venv and devcontainer
- Add links at the end of each part to go automatically to the next part
- Mdbook fix space above caption when have figure in a tab block
- Mdbook fix markdown inside a markdown hidden box
- Add intellisense for VSCode terminal
- Tidy part 2 headings so everything is like Lab A with just 2
- Update devcontainer file for codespaces to allow it to be re-added as a submodule
- Remove workspace from A-K
- Move getting started to Week 1/2
- Add more on docker/container to getting started
- Labs A-K add "containerEnv": {"localWorkspaceFolder": "${containerWorkspaceFolder}"}, to decontainer and then cd to right folder at start of each lab
- Move gradescope back to git submissions