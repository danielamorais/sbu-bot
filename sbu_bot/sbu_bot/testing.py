from django.test.runner import DiscoverRunner

#Testes que sobrescrevem o teste default do Django para nao ser criado nenhum banco de dados.
class DatabaselessTestRunner(DiscoverRunner):
    def setup_databases(self):
        pass

    def teardown_databases(self, *args):
        pass
