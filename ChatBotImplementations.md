# Steps to create chatbot 

Backend component: 
1. Data Ingestions: 
    - Load data from different data sources like SQL/PDF/Text files/
2. Extarct data from data sources. 
3.  Create text chunks. 
    - based on context window: 
        - context window input token sizes. how many tokens this model can accept at  at time at input. 
4. Embeddings: each chunks we converting into numbers this is called embeddings. 
5. Build Semantic index: 
    - In vector db there are two types
        1. Knowledge base
        2. Semantic index: identify simpliar clusters. 
6. Knowledge base: will use pinecone/Chroma/FAISS vector db. 


Front End:
1. User input
2. User input request query embeded. 
3. thse query sent to knowledge base. 
4. Knowledge base will provide
    - some ranked results.
    - if ex using LLama 2, looking exact results will from these responses and send it to LLaman2 model. 
    - LLaman 2 will understand the questions and anaswer from DB. both will process it will produce actual responses. 

----------------------------------------------------------------



