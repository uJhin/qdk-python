from typing import List, Union, Dict, Optional
from azure.quantum.optimization import Problem
from azure.quantum.storage import ContainerClient, BlobClient
import logging

__all__= ['OnlineProblem']

logger = logging.getLogger(__name__)

class OnlineProblem(Problem):
    def __init__(self, name:str, url:str):
        super(OnlineProblem,self).__init__(name)
        self.uploaded_blob_uri = url
    
    def evaluate(self,configuration: Union[Dict[int, int], Dict[str, int]]) -> float:
        """ An online problem cannot perform this client side operation and should raise an error"""
        raise 'This operation cannot be performed for an OnlineProblem instance. Please download the problem first'

    
    def download(self, workspace:"Workspace") -> Problem:
        logger.warning("This will download the problem to your machine")
        return Problem.download(self)