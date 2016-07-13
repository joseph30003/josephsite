import csv
import sqlite3
csv.field_size_limit(500 * 1024 * 1024)

class gene:

  def __init__(self,Symbol,Name):
    self.symbol=Symbol
    self.des=Name
    self.synonyms=[]

  def addSynonyms(self,Syns):
    if len(Syns) > 0:
      row = csv.reader([Syns],doublequote = True,skipinitialspace = False)
      for r in row:
        self.synonyms.extend(r)


db = sqlite3.connect('../../db.sqlite3')
db.row_factory = sqlite3.Row
cursor = db.cursor()


lineNum=1
genes = []
with open('genes.tsv') as tsv:
  lines = tsv.readlines()
  for line in lines:
    if lineNum > 1:
      row = csv.reader([line],delimiter='\t',doublequote = True,skipinitialspace = False)
      for r in row:
        genee = gene(r[5],r[4])
        genee.addSynonyms(r[6])
        genee.addSynonyms(r[7])
        genes.append(genee)
    lineNum=lineNum+1
id=1
for g in genes:
  for syn in g.synonyms:
     cursor.execute (" insert into joseph_genesyn(id,gene,synonyms)values(?,?,?)",(id,g.symbol,syn))
     db.commit()
     id=id+1