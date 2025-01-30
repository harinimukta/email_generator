import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="app/resource/Portfolio.csv"):
        """
        Initializes the Portfolio class with a file path for the CSV and sets up a ChromaDB collection.
        
        :param file_path: Path to the CSV file containing tech stack and links.
        """
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        """
        Loads data from the CSV file into the ChromaDB collection, if not already loaded.
        """
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        """
        Queries the ChromaDB collection for relevant links based on at least one matching skill.
        
        :param skills: List of skills to query.
        :return: List of relevant links based on matching skills.
        """
        relevant_links = set()  # Use a set to avoid duplicate links

        # Query the portfolio collection for each skill
        for skill in skills:
            query_result = self.collection.query(query_texts=[skill], n_results=5)  # Adjust `n_results` as needed
            for metadata in query_result.get('metadatas', []):
                if 'links' in metadata:
                    relevant_links.add(metadata['links'])  # Add to set to ensure uniqueness

        return list(relevant_links)  # Return only matching links
