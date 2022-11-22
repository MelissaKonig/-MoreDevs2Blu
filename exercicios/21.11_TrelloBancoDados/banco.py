import psycopg2

try:
    conn = psycopg2.connect(host = "localhost", port = "5450", database = "postgres", user="mel", password = "123456")
    print('Você foi conectado com sucesso!')
except:
    print('Erro na conexão!')
    

if conn is not None:
    print('Sua conexão está estável!')
    
    cursor = conn.cursor()
    #E faça a criação de uma tabela com id nome sobre nome
    cursor.execute("CREATE TABLE pessoa(id INTEGER PRIMARY KEY, nome VARCHAR(20), sobrenome VARCHAR(30))")
    conn.commit()
    cursor.close()
    conn.close()