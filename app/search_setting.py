"""
Module including the setup of the search pipeline
"""
from pathlib import Path
from haystack import Pipeline
from haystack.nodes import EmbeddingRetriever
from haystack.utils import convert_files_to_docs

from haystack.document_stores.faiss import FAISSDocumentStore

FAISS_INDEX_PATH = Path('.')/"faiss_document_store.svg"


def initialize_document_store():
    """
    Initialize document store with data from sources
    """
    land_boxer_file = Path("../data") / "land_of_the_boxer.txt"
    souvenirs_silbermann_file = Path("../data") / "souvenirs_silbermann_chine.txt"

    all_docs = convert_files_to_docs(file_paths=[land_boxer_file, souvenirs_silbermann_file],
                                     split_paragraphs="True")

    document_store = FAISSDocumentStore(faiss_index_factory_str="Flat",
                                        similarity="cosine",
                                        embedding_dim=768
                                        )
    document_store.write_documents(all_docs)

    return document_store


def get_document_store():
    """
    Load data from suitable folder and return document store
    """
    if check_index_exists():
        return FAISSDocumentStore.load(FAISS_INDEX_PATH)

    return initialize_document_store()


def check_index_exists():
    """
    Check if the document store index already exists
    """
    return FAISS_INDEX_PATH.exists()


def get_initialize_search_engine():
    """
    Initialize and return search engine with loaded data

    Create and save index if need be - this is performed with the update_embeddings command
    """
    document_store = get_document_store()

    model = 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
    retriever = EmbeddingRetriever(document_store=document_store, use_gpu=True,
                                   embedding_model=model, top_k=20)

    if not check_index_exists():
        document_store.update_embeddings(retriever)
        document_store.save(FAISS_INDEX_PATH)

    pipeline = Pipeline()
    pipeline.add_node(component=retriever, name='Retriever', inputs=['Query'])

    return pipeline


def get_answers(engine, question, nbr_answers=5):
    """
    Given a question and a search engine, print associated answers

    Args:
        * engine: search engine to use
        * question: string containing the question to anwser
        * nbr_answers (int, optional): maximum number of answers to print (max=20)
    """
    prediction = engine.run(query=question)

    for i, pred in enumerate(prediction['documents'][:nbr_answers]):
        print(i, pred.content + '\n')
