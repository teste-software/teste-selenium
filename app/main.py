import unittest
from webphone import ManagerWebphone
from realtime import ManagerRealtime


class RegressiveTestWebphone(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manager_webphone = ManagerWebphone()
        cls.manager_realtime = ManagerRealtime()

        cls.manager_webphone.login('davi.andrade@55pbx.com.br', 'qwpozxmn1029', 'Desenvolvimento Teste')
        print('LOGIN WEBPHONE FINALIZADO')

        cls.manager_realtime.register('davi.andrade@55pbx.com.br', 'qwpozxmn1029', 'Desenvolvimento Teste')
        print('LOGIN REALTIME FINALIZADO')

    def test_login_webphone(self):
        status = self.manager_realtime.get_status_ramal('davi andrade')
        print('STATUS: ', status)
        self.assertEqual(status, 'LIVRE')

    def test_disk_webphone(self):
        self.manager_webphone.diskPhone('11964205989')
        status = self.manager_realtime.get_status_ramal('davi andrade')
        print('STATUS: ', status)
        self.assertEqual(status, 'OCUPADO')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.manager_webphone.close()
        cls.manager_realtime.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegressiveTestWebphone('test_login_webphone'))
    suite.addTest(RegressiveTestWebphone('test_disk_webphone'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite())
