import unittest
from unittest.mock import Mock, patch
from azure.quantum import storage
from azure.storage.blob import generate_container_sas, ContainerClient
class TestStorage(unittest.TestCase):
    def setUp(self):
        self.mock_conn_str = "DefaultEndpointsProtocol=https;AccountName=MockStorage;AccountKey=xn5jBJNPX3M+O/j1Uak/1KR5nM7DEqLwDEQMIGgxxb8Ks1HKUYXQ16de+1emxY0h+fgcbIxgorjQLvbTCD1bVw==;EndpointSuffix=core.windows.net"

    @patch('azure.storage.blob.ContainerClient')
    @patch('azure.storage.blob.BlobServiceClient')
    def test_create_container(self, MockBlobServiceClient, MockContainerClient):
        #Arrange
        MockBlobServiceClient.from_connection_string = Mock()
        storage.create_container_using_client = Mock()
        #Act
        container = storage.create_container(self.mock_conn_str, "mock_container_name")
        #Assert
        storage.create_container_using_client.assert_called_once()
        assert container.container_name == "mock_container_name"
    '''
    @patch('azure.storage.blob.ContainerClient')
    def test_create_container_using_client(self, MockContainerClient):
        #Arrage
        mock_client = MockContainerClient()
        #Act
        container = storage.create_container_using_client(mock_client)
        #Assert
        #SMockContainerClient.get_container_properties.assert_called_once()
        mock_client.create_container.assert_called_once()
    '''
    def test_get_container_uri(self):
        #Arrange
        #Act
        uri = storage.get_container_uri(self.mock_conn_str, "mock_container_name")
        print(uri)
        #Assert
        #generate_container_sas_mock.assert_called_once()
        #mock_storage.create_container.assert_called_once()
    
    def test_upload_blob(self):
        #Arrange
        mock_container_client = Mock(spec = ContainerClient)
        mock_data = "\{\"cost_function\": \{ \"\"\}\}"
        #Act
        result = storage.upload_blob(mock_container_client, "mock_blob", "application/json", "gzip", mock_data)
        print(result)

        
        
    


if __name__ == '__main__':
    unittest.main()