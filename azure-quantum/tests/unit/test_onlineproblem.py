from azure.quantum.optimization import Problem, OnlineProblem, Term
from azure.quantum import Workspace
from unittest.mock import Mock, patch
import unittest

class TestOnlineProblem(unittest.TestCase):
    def setUp(self):
        self.mockWs = Mock(spec = Workspace)
        self.mockUrl = "https://mock.blob.core.windows.net/mck461d9-9cb0-11eb-991b-1860247f69ed/mck461d9-9cb0-11eb-991b-1860247f69ed"
    def test_evaluate_oproblem(self):
        # Arrange
        o_problem = OnlineProblem('test_prob', self.mockUrl)
        config = {
            1:1,
            0:-1
        }
        # Act
        # Assert
        self.assertRaises(Exception, o_problem.evaluate, config)

    @patch('azure.quantum.optimization.online_problem.logger')
    @patch('azure.quantum.optimization.online_problem.Problem', spec = Problem)
    def test_download_problem(self, MockProb, Mocklog):
        #Arrange
        o_prob = OnlineProblem('test_prob', self.mockUrl)
        self.mockWs._get_linked_storage_sas_uri = Mock(return_value = self.mock_conn_str)
        MockProb.download = Mock(return_value = "")
        #Act
        o_prob.download(self.mockWs)
        #Assert 
        MockProb.download.assert_called_once()
        Mocklog.warning.assert_called_with('This will download the problem to your machine')
        


    