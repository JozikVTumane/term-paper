import pymysql
connection = pymysql.connect(host='localhost', user='MY_USER', passwd='12345', database='learner_corpus')
cursor = connection.cursor()
cursor.execute("USE learner_corpus")
cursor.execute("SHOW TABLES")
for (table_name,) in cursor:
    print(table_name)

print("lex:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%lex%')")
print(cursor.fetchall())

print("word:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%word%')")
print(cursor.fetchall())

print("phrase:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%phrase%')")
print(cursor.fetchall())

print("meton:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%meton%')")
print(cursor.fetchall())

print("intens:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%intens%')")
print(cursor.fetchall())

print("deriv:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%deriv%')")
print(cursor.fetchall())

print("paron:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%paron%')")
print(cursor.fetchall())

print("asp:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%asp%')")
print(cursor.fetchall())

print("nmz:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%nmz%')")
print(cursor.fetchall())

print("aux:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%aux%')")
print(cursor.fetchall())

print("styl:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%styl%')")
print(cursor.fetchall())

print("official:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%official%')")
print(cursor.fetchall())

print("colloq:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%colloq%')")
print(cursor.fetchall())

print("agr:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%agr%')")
print(cursor.fetchall())

print("gov:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%gov%')")
print(cursor.fetchall())

print("compar:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%compar%')")
print(cursor.fetchall())

print("complex:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%complex%')")
print(cursor.fetchall())

print("rel_clause:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%rel_clause%')")
print(cursor.fetchall())

print("sent_arg:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%sent_arg%')")
print(cursor.fetchall())

print("conn:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%conn%')")
print(cursor.fetchall())

print("coord:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%coord%')")
print(cursor.fetchall())

print("discoord:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%discoord%')")
print(cursor.fetchall())

print("ref:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%ref%')")
print(cursor.fetchall())

print("converb:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%converb%')")
print(cursor.fetchall())

print("pron:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%pron%')")
print(cursor.fetchall())

print("voice:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%voice%')")
print(cursor.fetchall())

print("lack:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%lack%')")
print(cursor.fetchall())

print("constr:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%constr%')")
print(cursor.fetchall())

print("discourse:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%discourse%')")
print(cursor.fetchall())

print("parc:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%parc%')")
print(cursor.fetchall())

print("logic:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%logic%')")
print(cursor.fetchall())

print("link:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%link%')")
print(cursor.fetchall())

print("WO:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%WO%')")
print(cursor.fetchall())

print("tauto:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%tauto%')")
print(cursor.fetchall())

print("top:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%top%')")
print(cursor.fetchall())

print("cause:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%cause%')")
print(cursor.fetchall())

print("typo:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%typo%')")
print(cursor.fetchall())

print("contam:")
cursor.execute("SELECT count(*) FROM annotator_sentence WHERE id IN (SELECT document_id FROM annotator_annotation WHERE tag LIKE '%contam%')")
print(cursor.fetchall())