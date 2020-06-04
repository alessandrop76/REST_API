from flask_restful import Resource

lista_habilidades = ['Python', 'Django', 'C++', 'Java']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades