# Minimal graphviz microservice

Based on Alpine Linux 3.4, Python 3 and the hug framework.

## Usage

```bash
$ curl myhost.tld/viz.svg -F dot=@/path/to/a/dotfile.dot
```

```html
<img src="myhost.tld/viz.svg?dot=urlencoded-dot-data>"
<img src="myhost.tld/viz.png?dot=urlencoded-dot-data>"
```
