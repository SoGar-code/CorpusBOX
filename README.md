# Notes about this project

## Main source for the search engine.

https://www.deepset.ai/blog/how-to-build-a-semantic-search-engine-in-python

Disclaimer: installing the repository for the first time requires downloading many packages.

## Using this repository

1. Download the full repository
2. Create a new `.env` file including the following fields:
  ```.env
  COMPOSE_PROJECT_NAME=corpus-box
  NB_USER=jovyan
  JUPYTER_TOKEN=79_my_choice_of_token_256
  ```
3. Using docker compose, create the required Jupyter server with:
```commandline
docker compose up -d
```
4. In your browser, see the contents of the Notebook at:
```commandline
http://localhost:5001/lab/tree/home/jovyan/work/app/search_engine_demo.ipynb
```
To access the Notebook server, provide the Jupyter token defined in the `.env` file.

NB: initialisation of the search engine may take a while!

## Running the script multiple times

* The document store uses both SQL database (saved in the same folder as the notebook) and 
  embeddings, but the saves are done in different places.
* If running the script multiple times, then you need to take this into account.

# Sources of the indexed documents

For information regarding the texts used here, please refer to the CorpusBOX library.
