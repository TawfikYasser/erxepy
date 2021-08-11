![erxepy-img](https://github.com/TawfikYasser/erxepy/blob/main/etc/erxepy-img.png)
---

erxepy is a python module, used to make regular expressions more easier.

_**Beta**_ at [PyPi](https://pypi.org/project/erxepym)

### How to install

```shell
python -m pip install erxepym
```

### How to use

```python
# Number Validation
from erxepy import make_regex
import re
numberReg = make_regex() # result from make_regex() => \d{3}\s\d{4}-\d{3}
result = re.search(numberReg,"0111 2497-156")
print(result.group()) # Match result => 0111 2497-156
```
### Output

![](https://github.com/TawfikYasser/erxepy/blob/main/etc/output-erxepy.gif)

---

### How to update the package

```shell
python3 -m pip install --user --upgrade erxepym
```

### Contributing

Hi, Welcome to erxepy, feel free to contribute to this project by (adding/fixing) features.

Just you need to open an Issue and let's discuss it.

---

> More will added soon! Stay tuned. [First stable release will coming soon!]

---

[Visit at PyPi](https://pypi.org/project/erxepym/0.0.7)

[TawfikYasser - LinkedIn](https://www.linkedin.com/in/tawfikyasser)
