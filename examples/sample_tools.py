"""
Sample tool functions for testing the schema generator
"""

from typing import List, Optional, Dict, Union
import json


def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> Dict[str, any]:
    """
    Get current weather information for a location
    
    Args:
        location (str): The city or location to get weather for
        units (str): Temperature units - celsius or fahrenheit
        include_forecast (bool): Whether to include 5-day forecast
        
    Returns:
        Dict[str, any]: Weather information including temperature, conditions, etc.
    """
    return {
        "location": location,
        "temperature": 22,
        "condition": "sunny",
        "units": units
    }


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float, 
                      unit: str = "km") -> float:
    """
    Calculate distance between two geographic coordinates
    
    Parameters
    ----------
    lat1 : float
        Latitude of first point
    lon1 : float  
        Longitude of first point
    lat2 : float
        Latitude of second point
    lon2 : float
        Longitude of second point
    unit : str
        Unit for distance (km, miles, nautical)
        
    Returns
    -------
    float
        Distance between the two points
    """
    # Simplified calculation for demo
    return 100.5


def send_notification(message: str, recipients: List[str], 
                     priority: str = "normal", 
                     channels: Optional[List[str]] = None) -> bool:
    """
    Send notification to specified recipients
    
    :param message: The notification message to send
    :param recipients: List of recipient identifiers
    :param priority: Notification priority level (low, normal, high, urgent)
    :param channels: Optional list of channels to use (email, sms, push)
    :return: True if notification was sent successfully
    """
    return True


def process_data(data: Dict[str, any], 
                operations: List[str],
                output_format: str = "json",
                validate: bool = True) -> Union[Dict, str]:
    """
    Process data with specified operations
    
    A comprehensive data processing function that can apply multiple
    operations to input data and return results in various formats.
    
    Args:
        data: Input data as dictionary
        operations: List of operations to apply (filter, transform, aggregate)
        output_format: Format for output data (json, csv, xml)
        validate: Whether to validate data before processing
        
    Returns:
        Processed data in requested format
    """
    if output_format == "json":
        return {"processed": True, "operations": operations}
    else:
        return "processed_data_string"


def search_files(pattern: str, 
                directory: str = ".", 
                recursive: bool = True,
                file_types: Optional[List[str]] = None,
                max_results: int = 100) -> List[Dict[str, str]]:
    """
    Search for files matching a pattern
    
    Args:
        pattern (str): Search pattern or regex
        directory (str): Directory to search in
        recursive (bool): Whether to search subdirectories
        file_types (List[str], optional): File extensions to include
        max_results (int): Maximum number of results to return
        
    Returns:
        List[Dict[str, str]]: List of matching files with metadata
    """
    return [
        {"path": "/example/file.txt", "size": "1024", "modified": "2024-01-01"}
    ]