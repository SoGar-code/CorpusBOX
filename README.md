# CorpusBOX

*Multilingual semantic search engine* for a corpus of diaries and ego-documents regarding the Boxer rebellion and the Eight-Nation alliance (1900-1901), including multiple languages.

## Main source for the search engine.

https://www.deepset.ai/blog/how-to-build-a-semantic-search-engine-in-python

Disclaimer: installing the repository for the first time requires downloading many packages and could take some time!

## Using this repository

### Prerequisite

The installation of this repository requires Docker (and Docker compose). Moreover, the embedding model used requires significant computation power and available space on the hard drive.

### Installation steps

1. Download the full repository
2. Create a new `.env` file including the following fields:
  ```.env
  COMPOSE_PROJECT_NAME=corpus-box
  NB_USER=jovyan
  JUPYTER_TOKEN=791_my_choice_of_token_256
  ```
  Please choose your own Jupyter Token and note it for use when accessing the Jupyter server (see step 4. below).
  
3. Using docker compose, create the required Jupyter server with:
  ```commandline
  docker compose up -d --build
  ```
  Depending on your configuration, you may need:
  * to use `sudo docker compose up -d --build`
  * and/or to replace `docker compose` by `docker-compose` in the previous expression.
4. In your browser, see the contents of the Notebook at:
  ```commandline
  http://localhost:5001/lab/tree/home/jovyan/work/app/search_engine_demo.ipynb
  ```
  To access the Notebook server, copy-paste the Jupyter token defined in the `.env` file.

NB: initialisation of the search engine may take a while!

### Shutdown

To save resources, it is possible to shutdown the system using the command line:
  ```commandline
  docker compose down
  ```
This command line has to be run in the terminal, from the project root folder 
(typically folder `CorpusBOX`).

### Search engine start

If the search engine has been shutdown following the instructions of the previous section,
it is possible to start it again using the following command line in the terminal, 
from the project root folder:
  ```commandline
  docker compose up -d
  ```
and then see the contents of the Notebook in a browser at:
  ```commandline
  http://localhost:5001/lab/tree/home/jovyan/work/app/search_engine_demo.ipynb
  ```
NB: see above the installation steps for more details/alternative docker commands.   

# Sources of the indexed documents

For information regarding the texts used here, please refer to the [CorpusBOX Zotero library](https://www.zotero.org/groups/4808612/corpusbox).

# Contributing to this project

Feel free to contribute to this project, by creating a pull request to merge on the main branch!
