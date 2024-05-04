# Use uma imagem base do Python
FROM python:3.8-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 para o exterior
EXPOSE 5000

# Comando para iniciar o servidor Flask quando o contêiner for iniciado
CMD ["python", "run.py"]