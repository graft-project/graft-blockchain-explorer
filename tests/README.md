## Python selenium testing of the explorer

As the explorer grows, monero keep changing, it is increasingly time consuming
to keep testing the explorer manually. Thus, with the help of selenium, python and nose
it is hope that at least part of this process can be automated.

```bash
sudo pacman -S python-selenium python-nose
```

```
nosetests main.py
```