import csv
import sys 
import psycopg2


def insert(fname):
 dbconn=psycopg2.connect("dbname=superheronew")
 cur=dbconn.cursor()
 f=open(fname)
 reader=csv.reader(f)
 
 for name,gender in reader:
  print (name,gender)
  
  cur.execute("INSERT INTO heroes (name,gender) values (%s,%s)",(name,gender))
  
 dbconn.commit()
  
def main():
 fname=sys.argv[1]
 insert(fname)
 
main()   
  

