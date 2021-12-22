import gzip
import json
import ast
from typing import final


def parse_rank(path):
  with open(path,"r") as myfile:
     
      for l in myfile:
        rank_string=eval(l)['rank']
        rank_1=[s for s in rank_string if s.isdigit()] 
        if len(rank_1)>=1:
            final_rank= int("".join(rank_1))

        yield json.dumps(final_rank)
      



def parse_lowrank_nodes(path):
  with open(path,"r") as myfile:
     
     for l in myfile:
        rank_string=eval(l)['rank']
        rank_1=[s for s in rank_string if s.isdigit()] 
        if len(rank_1)>=1:
            final_rank= int("".join(rank_1))

        else:
          continue

        if final_rank >=59 and final_rank <=10524:
            a=[]
            k=eval(l)['also_buy']
            if len(k)>=1:
               new_list=[eval(l)["asin"]]*len(k)
               a.append(tuple(zip(new_list,k)))
               yield json.dumps(a)
        else:
          continue



def parse_mediumrank_nodes(path):
  with open(path,"r") as myfile2:
     
     for l in myfile2:
        rank_string=eval(l)['rank']
        rank_1=[s for s in rank_string if s.isdigit()] 
        if len(rank_1)>=1:
            final_rank= int("".join(rank_1))
            
        else:
          continue

        a=[]
        if final_rank >=20830 and final_rank<33855:
            k=eval(l)['also_buy']
            if len(k)>=1:
               new_list=[eval(l)["asin"]]*len(k)
               a.append(tuple(zip(new_list,k)))
               yield json.dumps(a)
        else:
          continue



def parse_highrank_nodes(path):
  with open(path,"r") as myfile3:
     
     for l in myfile3:
        rank_string=eval(l)['rank']
        rank_1=[s for s in rank_string if s.isdigit()] 
        if len(rank_1)>=1:
            final_rank= int("".join(rank_1))
            
        else:
          continue

        a=[]
        if final_rank >=48460 and final_rank<65624:
            k=eval(l)['also_buy']
            if len(k)>=1:
               new_list=[eval(l)["asin"]]*len(k)
               a.append(tuple(zip(new_list,k)))
               yield json.dumps(a)
        else:
          continue


f1 = open("../data/Low_rank_nodes", 'w')
for l in parse_lowrank_nodes("../data/original_data.json.gz"):
  f1.write(l + '\n')



f2 = open("../data/medium_rank_nodes", 'w')
for l in parse_mediumrank_nodes("../data/original_data.json.gz"):
  f2.write(l + '\n')


f3 = open("../data/high_rank_nodes", 'w')
for l in parse_highrank_nodes("../data/original_data.json.gz"):
  f3.write(l + '\n')


f4=open("../data/rank.csv","w")
for l in parse_rank("../data/original_data.json.gz"):
  f4.write(l+"\n")



