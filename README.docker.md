# Docker support for PTF



First of all, build and compile all the tools and the image itself (~1hour):
```
docker -t spinfoo/ptf:1.0 build .
```


After, you can run PTF anytime with:
```
docker run -it spinfoo/ptf:1.0 /bin/bash
```

