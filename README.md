# R3CON1Z3R

[![Build Status](https://travis-ci.org/abdulgaphy/r3con1z3r.svg?branch=master)](https://travis-ci.org/abdulgaphy/r3con1z3r)

R3con1z3r is a lightweight Web information gathering tool with an intuitive features written in python. it provides a powerful environment in which open source intelligence (OSINT) web-based footprinting can be conducted quickly and thoroughly. 

Footprinting is the first phase of ethical hacking, its the collection of every possible information regarding the target. R3con1z3r is a passive reconnaissance tool with  built-in functionalities which includes: HTTP header flag, Traceroute, Whois Footprinting, DNS information, Site on same server, Nmap port scanner, Reverse Target and hyperlinks on a webpage. The tool, after being provided with necessary inputs generates an output in HTML format.

# Screenshots

<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/reconizer.png">
<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/recon.png">


# Installation

r3con1z3r supports **Python 2** and **Python 3**.

```bash
    pip install r3con1z3r

```

# Modules

r3con1z3r depends only on the sys and the requests python modules. 


**For Coloring on Windows:** `pip install win_unicode_console colorama`

# Usage

r3con1z3r [domain.com]

# Examples

- To run on all Operating Systems 

    ```bash
    r3con1z3r google.com
    ```

    ```bash
    r3con1z3r facebook.com
    ```

# ToDo

- [x] Include travis setup
- [x] Include automatic deployment of incremented versions to pypi so that `pip install r3con1z3r` can work
- [x] Test across Python2.7, 3.5 and 3.6
- [x] Test across osx, linux and windows
- [ ] Adjust windows tests to pass

# License

r3con1z3r is licensed under the GNU GPL license. take a look at the [LICENSE](/LICENSE) for more information.

# Contribution
fast_finish: true
This project is open to contributions, Bug reports and pull requests are welcome on GitHub at https://github.com/abdulgaphy/r3con1z3r.



# Changelog

1.0. - Release
1.0.1 - Release
