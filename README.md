# R3CON1Z3R

R3con1z3r is a lightweight Web information gathering tool with an intuitive features written in python. it provides a powerful environment in which open source intelligence (OSINT) web-based footprinting can be conducted quickly and thoroughly. 

Footprinting is the first phase of ethical hacking, its the collection of every possible information regarding the target. R3con1z3r is a passive reconnaissance tool with  built-in functionalities which includes: HTTP header flag, Traceroute, Whois Footprinting, DNS information, Site on same server, Nmap port scanner, Reverse Target and hyperlinks on a webpage. The tool, after being provided with necessary inputs generates an output in HTML format.

# Screenshots

<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/reconizer.png">
<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/recon.png">


# Installation

r3con1z3r supports **Python 2** and **Python 3**.

```bash
    git clone https://github.com/abdulgaphy/r3con1z3r.git
    cd r3con1z3r
    # python2 installation
    python setup.py install
    # or python3 installation
    python3 setup.py install
```

# Modules

r3con1z3r depends only on the sys and the requests python modules. 

**Python 3:** `$ pip3 install -r requirements.txt`

**For Coloring on Windows:** `pip install win_unicode_console colorama`

# Usage

python3 r3con1z3r.py [domain.com]

# Examples

- To run on all Operating Systems (Linux, Windows, Mac OS X, Android e.t.c)  i.e Python 2 environment from within the cloned repo:

    `python r3con1z3r/main.py google.com`

    python3 environment:

    `python3 r3con1z3r/main.py facebook.com`

- To run as executable Unix and Windows after installing the library:

    `r3con1z3r google.com`

# ToDo

- [ ] Include travis setup for automatic testing
- [ ] Include automatic deployment of incremented versions to pypi so that `pip install r3con1z3r` can work

# License

r3con1z3r is licensed under the GNU GPL license. take a look at the [LICENSE](/LICENSE) for more information.

# Contribution

This project is open to contributions, Bug reports and pull requests are welcome on GitHub at https://github.com/abdulgaphy/r3con1z3r.



# Changelog

1.0 - Release
