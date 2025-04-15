# General project setup
project = 'notes-part0'
copyright = 'Alex Casson. <a class="nav-link text-light" href="https://creativecommons.org/licenses/by/4.0/deed.en">Released under CC-BY 4.0 license.</a>'
author = 'Alex Casson'
release = '0.1'
templates_path = ['_templates']
exclude_patterns = []
language = 'en_GB'


# Set extensions
extensions = [
    'sphinx-prompt',
    'sphinx_copybutton',
    'notfound.extension',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    #'sphinx_affiliates', # needs incompatible version of Sphinx. Will re-visit at a later date
    'sphinx_wagtail_theme'
]


# Theme settings
html_theme_path = ['./theme']
html_theme = 'uom_sphinx_wagtail_theme'
html_static_path = ['_static']
html_theme_options = dict(
    project_name = "EEEN11202 course notes",
    searchbox_text = "Search notes part 0",
    breadcrumb_home = "Part 0",
    logo_alt = "University of Manchester logo",
    logo_url = "/",
    logo_width = 88,
    footer_links = ",".join([
        "The University of Manchester|https://www.manchester.ac.uk/",
        "Canvas|https://online.manchester.ac.uk/",
    ]),
    github_url = "https://github.com/UOM-EEE-EEEN11202/uom-eee-eeen11202.github.io/tree/main/docs/",
)
html_show_copyright = True
html_show_sphinx = False


# 404 settings - note this won't display correctly locally, but will on github
notfound_urls_prefix = "/"


# Allow cross-references to other Sphinx sites
#intersphinx_mapping = {
#    'part1': ('https://uom-eee-eeen11202.github.io/notes-part1/', None),
#}

# All external links are set here to ease checking of whether they are still the correct version
# (This isn't checking whether the links are valid, other tools do that. This is for updating, say, policy links to this year's version) 
# Note all need %s on the end to work with the extension correctly
# Link is then :ext_uom_ai_policy:`University's guidance on the use of artificial intelligence. <>` Note <> needed
extlinks = {
  'ext_uom_ai_policy': ('https://documents.manchester.ac.uk/display.aspx?DocID=70286%s',None),
  'ext_uom_malpractice_policy': ('https://documents.manchester.ac.uk/display.aspx?DocID=2870%s',None)
}
