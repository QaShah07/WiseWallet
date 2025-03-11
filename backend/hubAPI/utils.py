from typing import Union
from django.http import JsonResponse

# custom exception for custom status code
class InvalidStatusCodeError(Exception):
    def __ini__(self,function_name,status_code):
        self.message =f"Invalid Status code {status_code} for function {function_name}."
        super().__init__(self.message)


def custom_server_error_response(error_message: str = "An unexpected error occured. Please try again later.", status_code: int=500)-> JsonResponse:
    """
    Returns a JSON response for server errors (500-599 status codes).

    Args:
        error_message (str): The error message to include in the response. Defaults to a generic server error message.
        status_code (int): The HTTP status code (must be between 500 and 599). Defaults to 500.

    Returns:
        JsonResponse: A JSON response with 'success': False and the error message.

    Raises:
        InvalidStatusCodeError: If the status_code is not between 500 and 599.
    """
    if 500 <= status_code < 600:
        return JsonResponse({'success': False, 'message': error_message}, status=status_code)
    raise InvalidStatusCodeError("custom_server_error_response",status_code)

def custom_user_error_response(error_message: str = "Invalid request. Please check your input.", status_code:int=400)-> JsonResponse:
    """
    Returns a JSON response for user errors (400-499 status codes).

    Args:
        error_message (str): The error message to include in the response. Defaults to a generic user error message.
        status_code (int): The HTTP status code (must be between 400 and 499). Defaults to 400.

    Returns:
        JsonResponse: A JSON response with 'success': False and the error message.

    Raises:
        InvalidStatusCodeError: If the status_code is not between 400 and 499.
    """
    if 400 <= status_code < 500:
        return JsonResponse({'success': False, 'message': error_message}, status=status_code)
    raise InvalidStatusCodeError("custom_user_error_response",status_code)


def custom_success_response(success_message: Union[str, dict] = "Operation completed successfully.", status_code:int=200)->JsonResponse:
    """
    Returns a JSON response for successful operations (200-299 status codes).

    Args:
        success_message (str or dict): The success message or data to include in the response. Defaults to a generic success message.
        status_code (int): The HTTP status code (must be between 200 and 299). Defaults to 200.

    Returns:
        JsonResponse: A JSON response with 'success': True and the success message or data.

    Raises:
        InvalidStatusCodeError: If the status_code is not between 200 and 299.
    """
    if 200 <= status_code < 300:
        response = {'success': True, 'message': success_message}
        return JsonResponse(response, status=status_code)

    raise InvalidStatusCodeError("custom_success_response",status_code)