import importlib.util,pathlib
from unittest.mock import patch
p=pathlib.Path(__file__).with_name('ruta_tutor_adaptativo_fase2.py')
spec=importlib.util.spec_from_file_location('fase2',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
raw={'nodes':[{'id':'n1','name':'Fuerza neta','outcome':'Resolver F=ma','level':1,'prerequisites':[],'kind':'math','probe':{'prompt':'Explica F=ma','reference':'fuerza neta','kind':'math'}},{'id':'n2','name':'Álgebra','outcome':'Despejar','level':0,'prerequisites':[],'kind':'math','probe':{'prompt':'Despeja','reference':'pasos','kind':'math'}},{'id':'n3','name':'Unidades','outcome':'Usar SI','level':0,'prerequisites':[],'kind':'math','probe':{'prompt':'Unidades','reference':'SI','kind':'math'}},{'id':'n4','name':'Problema integrado','outcome':'Resolver','level':3,'prerequisites':['n1','n2','n3'],'kind':'problem','probe':{'prompt':'Problema','reference':'pasos','kind':'problem'}},{'id':'n5','name':'Transferencia','outcome':'Caso nuevo','level':4,'prerequisites':['n4'],'kind':'transfer','probe':{'prompt':'Caso','reference':'razonamiento','kind':'transfer'}}], 'coverage':[{'id':'n1','name':'Fuerza neta','kind':'math','priority':'blocker','prerequisites':[],'contexts':[], 'dimensions':[{'id':'conceptual','name':'Principio','required':True},{'id':'direct_application','name':'Aplicación','required':True},{'id':'transfer','name':'Transferencia','required':True}]}]}
nodes=m.validated_map(raw);cov=m.validated_coverage(raw,nodes);assert len(cov)==5
with patch.object(m,'gemini',return_value=raw) as g:
 d=m.make_coverage_map({'goal':'Resolver física','context':''});assert g.call_count==1 and len(d['coverage'])==5
# Targeted errors stay local in the evaluator contract; no Gemini for No sé
assert m.evaluate({'question':raw['nodes'][0]['probe'],'answer':'No sé'})['status']=='UNKNOWN'
assert m.map_update({'component_id':'n2','reason':'Fallo de despeje repetido'})['status']=='RECORDED'
print('OK: mapa, dimensiones y reglas de intervención; sin Gemini real.')
