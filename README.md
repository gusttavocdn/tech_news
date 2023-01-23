# Tech News :newspaper:

![cover](./cover.png)

## :page_with_curl: About/Sobre

<details>
  <summary markdown="span"><strong>:us: English</strong></summary><br />

Python data science project developed by [Gustavo da Silva](https://www.linkedin.com/in/gustavocdn/) at the end of Section 2 and Computer Science Module of Trybe's Web Development course.

The project goal was develop a Web Crawler to scrape data directly from [Trybe's blog](https://blog.betrybe.com/). Storing the data in a MongoDB database and capable of doing some simple analysis with them.
<br />

</details>
<details>
  <summary markdown="span"><strong>:brazil: Português</strong></summary><br />

Projeto de Python e ciência de dados desenvolvido por [Gustavo da Silva](https://www.linkedin.com/in/gustavocdn/) ao final da Seção 2 do Módulo de Ciências de Computação do curso de Desenvolvimento Web da Trybe.

O objetivo do projeto foi desenvolver um Web Crawler para rapasgem de dados diretamente do [blog da Trybe](https://blog.betrybe.com/). Guardando os dandos em um banco de dados MongoDB e capaz de fazer algumas analises simples com eles.
<br />

</details>

## :man_technologist: Developed Skills/Habilidades Desenvolvidas

<details>
  <summary markdown="span"><strong>:us: English</strong></summary><br />

-   Use scraping techniques and tools.
-   Develop algorithms with Python.
-   I/O with Python.
-   Reading and writing tests with Pytest.
<br />
</details>

<details>
  <summary markdown="span"><strong>:brazil: Português</strong></summary><br />

-   Utilizar técnicas e ferramentas de raspagem de dados.
-   Desenvolver algoritmos com Python.
-   I/O com Python.
-   Leitura e escrita de testes com Pytest.

<br />
</details>

## :hammer_and_wrench: Tools/Ferramentas

-   Python
-   Pytest
-   MongoDB
-   BeautifulSoup
-   Docker

## :rocket: How to run/Como rodar

<details>
  <summary markdown="span"><strong>:us: English</strong></summary><br />
    
<details open>
<summary markdown="span"><strong>:computer: Local</strong></summary><br />
            
**1 - Clone the repository and enter the project folder**
            
```bash
git clone git@github.com:gusttavocdn/tech_news.git && cd tech_news
```
**2 - Start a virtual environment and install dependencies**
            
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r dev.requirements.txt
```
**3 - Start a container with the MongoDB database to store data**
            
```bash
docker run -d -p 27017:27017 --name tech-news-mongo mongo
```
            
**4 - Run the main script**
            
```bash
tech-news-analyzer
```

</details>

<details>
<summary markdown="span"><strong>:whale: Docker</strong></summary><br />
            
**1 - Clone the repository and enter the project folder**
            
```bash
git clone git@github.com:gusttavocdn/tech_news.git && cd tech_news
```

**2 - Start the containers**

```bash
docker-compose up -d
```

**3 - Run the main script**

```bash
docker exec -it tech-news-analyzer tech-news-analyzer
```

</details>
<br>
</details>

<details>
  <summary markdown="span"><strong>:brazil: Português</strong></summary><br />

  <details open>
   <summary markdown="span"><strong>:computer: Local</strong></summary><br />
    
   **1 - Clone o repositório e entre na pasta do projeto**
    
   ```bash
    git clone git@github.com:gusttavocdn/tech_news.git && cd tech_news
   ```
   **2 - Inicie um ambiente virtual e faça instalação das dependencias**
        
   ```bash
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r dev.requirements.txt
   ```
   **3 - Inicie um container com o banco de dados MongoDB para guardar dados**
        
   ```bash
    docker run -d -p 27017:27017 --name tech-news-mongo mongo
   ```

**4 - Execute o script principal**

```bash
 tech-news-analyzer
```

  </details>
  <details>
   <summary markdown="span"><strong>:whale: Docker</strong></summary><br />
        
   **1 - Clone o repositório e entre na pasta do projeto**
        
   ```bash
    git clone git@github.com:gusttavocdn/tech_news.git && cd tech_news
   ```

**2 - Inicie os containers**

```bash
 docker-compose up -d
```

**3 - Execute o script principal**

```bash
  docker exec -it tech-news-analyzer tech-news-analyzer
```

  </details>

</details>

<!-- ## :trophy: Grade/Nota -->
