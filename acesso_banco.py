import psycopg2

conexao = psycopg2.connect(host='dpg-cl5bcnc72pts73ej6m60-a.oregon-postgres.render.com', database='service_wini', user='service_wini_user', password='eKfv4iKaYvxhcMNTpcyqt1EzwFoNFoke')

cur = conexao.cursor()

sql = "insert into alunos values ('vitao@gmail.com', '12345', 'Winicius')"
cur.execute(sql)
conexao.commit()