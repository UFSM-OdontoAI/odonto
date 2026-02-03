# ODONTO

**ODONTO Does Observation, Not Training Only**

ODONTO é um visualizador web *somente leitura* para bases de dados
de radiografias panorâmicas odontológicas anotadas no formato COCO.

## Funcionalidades
- Separação train / val
- Visualização de imagens
- Bounding boxes e segmentações
- Mostrar / esconder classes
- Zero modificação no dataset

## Execução
```bash
pip install django
python manage.py runserver
```

Coloque seus dados COCO na pasta `data/` (fora do repositório).
