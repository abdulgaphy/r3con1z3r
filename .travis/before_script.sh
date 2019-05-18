set -e
set -v

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then brew update; fi
if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then 
    if [[ "$TRAVIS_PYTHON_VERSION" == "27" ]]; then
        ln -s pip=pip2;
    elif [[ "$TRAVIS_PYTHON_VERSION" == "35" ]]; then
        brew install sashkab/python/python35;
        echo 'export PATH="/usr/local/opt/python35/bin:$PATH"' >> ~/.bash_profile;
        ln -s pip=pip3.5;
    elif [[ "$TRAVIS_PYTHON_VERSION" == "36" ]]; then
        :
    fi
fi


if [[ "$TRAVIS_OS_NAME" = "windows" ]]; then 
    if [[ "$TRAVIS_PYTHON_VERSION" == "27" ]]; then
        choco install python2;
        export PATH="/c/Python27:/c/Python27/Scripts:$PATH";
    elif [[ "$TRAVIS_PYTHON_VERSION" == "35" ]]; then
            choco install python3 --version 3.5.2;
            export PATH="/c/Python35:/c/Python35/Scripts:$PATH";
    elif [[ "$TRAVIS_PYTHON_VERSION" == "36" ]]; then
            choco install python --version 3.6.5;
            export PATH="/c/Python36:/c/Python36/Scripts:$PATH";
    fi
    python -m pip install --upgrade pip wheel
    # install unicode and colorama
    pip install win_unicode_console colorama;
fi
