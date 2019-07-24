# R3CON1Z3R

<span> <a href="https://travis-ci.com/abdulgaphy/r3con1z3r"><img src="https://travis-ci.com/abdulgaphy/r3con1z3r.svg" alt="Build Status" height="18"></a> <a href="https://opensource.org/licenses/GNU"><img src="https://img.shields.io/badge/License-GNU-yellow.svg" alt="License: GNU" height="18"></a> <a href="https://badge.fury.io/py/r3con1z3r"><img src="https://badge.fury.io/py/r3con1z3r.svg" alt="PyPI version" height="18"></a> </span>

R3con1z3r is a lightweight Web information gathering tool with an intuitive features written in python. it provides a powerful environment in which open source intelligence (OSINT) web-based footprinting can be conducted quickly and thoroughly.

Footprinting is the first phase of ethical hacking, its the collection of every possible information regarding the target. R3con1z3r is a passive reconnaissance tool with  built-in functionalities which includes: HTTP header flag, Traceroute, Whois Footprinting, DNS information, Site on same server, Nmap port scanner, Reverse Target and hyperlinks on a webpage. The tool, after being provided with necessary inputs generates an output in HTML format.

## Screenshots

<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/reconizer.png">
<img width="681" alt="r3con1z3r" src="https://raw.githubusercontent.com/abdulgaphy/webshell/master/screenshots/recon.png">

## Installation

r3con1z3r supports **Python 2** and **Python 3**.

```bash
   # install from pypi
   pip install r3con1z3r
```

## Modules

r3con1z3r depends only on the sys and the requests python modules. 

**Python 3:** `$ pip3 install -r requirements.txt`

**For Coloring on Windows:** `pip install win_unicode_console colorama`

## Usage

r3con1z3r installs a command line tool on system path that can be interacted with by using

```bash
r3con1z3r -d domain.com
```

## Examples

- To install on all Operating Systems (Linux, Windows, Mac OS X, Android e.t.c)  i.e Python 2 environment from within the cloned repo:

    `pip install r3con1z3r`

    python3 environment:

    `pip3 install r3con1z3r`

## ToDo

- [x] Include travis setup for automatic testing
- [x] Include automatic deployment of incremented versions to pypi so that `pip install r3con1z3r` can work

## License

r3con1z3r is licensed under the GNU GPL license. take a look at the [LICENSE](/LICENSE) for more information.

## Contribution

This project is open to contributions, Bug reports and pull requests are welcome on GitHub at https://github.com/abdulgaphy/r3con1z3r. Current contributors can be viewed by running `r3con1z3r -a`

## Changelog

1.0 - Release
