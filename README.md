# Minimal graphviz microservice

Based on Alpine Linux 3.4, Python 3 and the hug framework. Exposes a simple REST API for generating Graphviz visualizations from DOT files.

## Running

```bash
docker run -d -p 8000:8000 --name graphviz sseemayer/graphviz
```

## Usage

```bash
$ curl myhost.tld/viz.svg -F dot=@/path/to/a/dotfile.dot
```

```html
<img src="myhost.tld/viz.svg?dot=urlencoded-dot-data>"
<img src="myhost.tld/viz.png?dot=urlencoded-dot-data>"
```
