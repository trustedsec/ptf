# Docker support for PTF

To be able to use the principle Security-in-a-box and run constantly penetration testing and vulnerability assessment against our applications and infrastructure, I developed a quick hack to be able to run PTF framework inside a Docker container.


First of all, build and compile all the tools and the image itself (~2 hours).
Inside this folder run the following:
```
docker build --rm -t spinfoo/ptf:1.1 .
```


After, you can run PTF anytime with:
```
docker run -it spinfoo/ptf:1.1 /bin/bash
```


# TODO
* Run install checks after modules update/install (go through /usr/local/bin and check successful execution)
* Check automatically for dependencies, improve efficiency


# Credits
David Kennedy/Trustedsec PTF project and Jacobo Avariento (spinfoo) for the docker support.
