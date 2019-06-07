# mockry

A simple but rich mock HTTP server you have searched for. 

* **Easy to start.** Get the docker package and start hacking in a minutes.
* **Easy to use.** Create a simple JSON with your mock data and pass it as param to mockry.
* **Rich.** Parse input CSV, convert it to JSON, send it at some URL and return the combined result? It's just a small things mockry can do for you. No programming required.

# Installation

### Docker

 mockery should be used as a standalone application inside a Docker container. 
 
 Pull the official image from Docker Hub:
 
 ```bash
 $ docker pull glibin/mockry:latest
 $ docker run -p 7777:7777 -it glibin/mockry
 ```

To use your custom schema create and edit `application.json` file and link containing directory to your container:

```bash
$ docker run -p 7777:7777 -v /path/to/application/json/dir:/data -it glibin/mockry
```

Or you can build your own image:

```bash
$ docker build -t mockry .
$ docker run -p 7777:7777 -it mockry
```

### From the source

Python 3.7+ is required to run mockry. You can install it from [python.org](https://www.python.org/) or with your OS package manager.

```bash
$ python3.7 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python -m mockry
```

Possible options:

Option | Description | Default
------ | ----------- | -------
`--host=<host>` | Host to bind the server | `127.0.0.1`
`--port=<port>` | Port to bind the server | `7777`
`--json=<path_to_json>` | Path to application json file | `application.json`
`--debug=<mode>` | Debug mode (if `true` the changes in application json file would be automatically applied) | `true`
`--help` | Show all available options | 
