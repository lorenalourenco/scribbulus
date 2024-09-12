# Use uma imagem base com Python
FROM python:3.9-slim

# Crie um diretório para a aplicação
WORKDIR /app

# Copie o arquivo de requisitos para instalar dependências
COPY requirements.txt ./

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação
COPY . .

# Exponha a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["gunicorn", "scribbulus.wsgi:application", "--bind", "0.0.0.0:8000"]