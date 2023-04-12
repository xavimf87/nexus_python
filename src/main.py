"""
@author: @xavimf87
"""
import os
import requests

class Nexus:
    """
    A class to Pull, Get items, and Push Files to nexus repository
    """
    def __init__(self, url, username=None, password=None):
        self.url = url
        self.username = username
        self.password = password

    def _make_request(self, url, method='get', data=None):
        """Make a request to the repository.

        Args:
            url (str): The URL to make the request to.
            method (str, optional): The HTTP method to use (get or put). Defaults to 'get'.
            data (str or file-like object, optional): The data to send in the request body. 
                Only used with put method. Defaults to None.

        Returns:
            requests.Response: The response object.
        """
        if self.username is not None and self.password is not None:
            auth = (self.username, self.password)
        else:
            auth = None
        if method.lower() == 'get':
            response = requests.get(url, auth=auth, timeout=30)
        elif method.lower() == 'put':
            response = requests.put(url, data=data, auth=auth, timeout=30)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        return response

    def pull(self, artifact_path: str, destination_path: str):
        """Download an artifact from the repository.

        Args:
            artifact_path (str): The path of the artifact file to download.
            destination_path (str): The local destination folder.
        """
        artifact_url = f"{self.url}/repository/{artifact_path}"
        response = self._make_request(artifact_url)
        
        if response.status_code == 200:
            with open(os.path.join(destination_path, os.path.basename(artifact_path)), 'wb') as file:
                file.write(response.content)
                print(f"Downloaded {artifact_path} to {destination_path}")
        else:
            print(f"Failed to download {artifact_path}. HTTP status code {response.status_code}")

    def get_items(self, repository_name: str) -> dict:
        """Get all items from a repository.

        Args:
            repository_name (str): The name of the repository.

        Returns:
            dict: A JSON object containing all items.
        """
        repository_url = f"{self.url}/service/rest/v1/assets?repository={repository_name}"
        response = self._make_request(repository_url)
        j = response.json()
        items = j['items']
        return items

    def push(self, local_file_path: str, remote_file_path: str):
        """Upload an artifact to the repository.

        Args:
            local_file_path (str): The local filename to upload.
            remote_file_path (str): The remote filename to upload to.
        """
        artifact_path = remote_file_path
        artifact_url = f"{self.url}/{artifact_path}"
        
        with open(local_file_path, 'rb') as file:
            response = self._make_request(artifact_url, method='put', data=file)
            
            if response.status_code == 201:
                print(f"Uploaded {local_file_path} to {artifact_path}")
            else:
                print(f"Failed to upload {local_file_path} to {artifact_path}. "
                      f"HTTP status code {response.status_code}")
