import psycopg2

def conectardb():
    conn = psycopg2.connect(host='dpg-cl5bcnc72pts73ej6m60-a.oregon-postgres.render.com', database='service_wini', user='service_wini_user', password='eKfv4iKaYvxhcMNTpcyqt1EzwFoNFoke')
    return conn

def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from alunos')
    recset = cur.fetchall()
    conexao.close()

    return recset

def inserirDB(login, senha, nome, conexao):
    cur = conexao.cursor()
    exito = False

    try:
        sql = f"insert into alunos values ('{login}', '{senha}', '{nome}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

